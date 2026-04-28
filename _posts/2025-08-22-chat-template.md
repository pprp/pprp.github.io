---
layout: post
title: '大模型对话格式全景'
date: 2025-08-22 11:00:00 +0800
last_modified_at: 2026-04-27 00:00:00 +0800
author: pprp
categories: tech
topics: [llm-systems, engineering]
---

# 大模型对话格式全景：从 Chat Template 到 Tool-Use，再到跨阶段 Token 设计

很多人第一次接入开源大模型时，最容易低估的不是推理参数，而是“格式”。

同样一句用户问题，放进不同模型，外层包装可能完全不同：有的需要 `[INST] ... [/INST]`，有的需要 `<|im_start|>user ... <|im_end|>`，有的还要把工具列表、函数调用结果、下一轮生成提示一起塞进 prompt。看起来只是字符串拼接，实际却是模型训练分布的一部分。格式错了，模型不是“不够聪明”，而是被带到了它没学过的输入空间里。

所以 Chat Template 的价值不只是省掉几行模板代码。它真正解决的是一个工程问题：**如何把结构化对话、工具调用和特殊 token 边界，稳定地翻译成模型认识的文本协议。**

---

## 1. Chat Template 不是包装层，而是训练分布的入口

### 1.1 为什么必须存在
- 不同模型在训练时采用了**互不兼容**的文本格式  
  - Mistral：`[INST] xxx [/INST]`  
  - Qwen：`<|im_start|>user\nxxx<|im_end|>`  
- 任何细微差异都会因分布漂移导致**回答质量骤降**  
- 因此需要“**一次性声明格式，全生命周期复用**”的机制

换句话说，Chat Template 是对话系统和 tokenizer 之间的格式契约。上层应用继续处理 `role/content/tools` 这样的结构化对象，底层模型只接收它训练时熟悉的 token 序列。这个边界一旦固定，推理、训练集预处理和微调数据生成就不再各写一套拼接逻辑。

### 1.2 技术实现
- 存储位置：Tokenizer 配置中的 `chat_template` 字段  
- 语法：Jinja2 模板，支持 `if/for/macro` 等逻辑  
- 入口 API：`tokenizer.apply_chat_template(messages, tools=..., add_generation_prompt=...)`

```python
prompt = tokenizer.apply_chat_template(
    messages=[
        {"role": "user", "content": "9.11 和 9.9 哪个大？"}
    ],
    add_generation_prompt=True,
    tokenize=False
)
# <s>[INST] 9.11 和 9.9 哪个大？ [/INST]
```

这段代码的重点不在示例问题，而在 `apply_chat_template` 的职责：它把应用层消息转换成模型层 prompt，并且可以通过 `add_generation_prompt=True` 补上“现在轮到 assistant 生成”的起始标记。

---

## 2. Tool-Use 的本质：把函数调用也纳入文本协议

| 维度 | 普通模板 | Tool-Use 模板 |
|---|---|---|
| 角色集合 | {user, assistant, system} | 增加 `{tool_calls, tool}` |
| 新增字段 | — | `tool_calls`, `tool_call_id`, `tools` |
| 模板片段 | 循环输出 `role: content` | 额外注入 `<|tools|>JSON<|/tools|>` 与 `<tool_call>JSON</tool_call>` |
| 解析动作 | 直接继续生成 | 遇 `<tool_call>` 停、调 API、回传 `role=tool` 后继续 |

工具调用并没有让模型真的“执行函数”。模型做的仍然是生成文本，只是这段文本被设计成一个可解析的调用协议。外部 runtime 负责识别 `<tool_call>`、执行真实 API、再把工具结果写回对话历史。Tool-Use Chat Template 的作用，就是让这套协议在 prompt 里可见、可学、可解析。

### 2.1 典型流程
1. 用户输入  
2. 模板拼接函数签名 → `<|tools|>[...]<|/tools|>`  
3. 模型输出 `<tool_call>` JSON  
4. 外部执行函数 → 结果写回 `role=tool`  
5. 再次进入模板 → 继续生成自然语言回答

### 2.2 示例
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "parameters": {"location": {"type": "string"}}
    }
}]
prompt = tokenizer.apply_chat_template(
    messages=messages,
    tools=tools,
    add_generation_prompt=True,
    tokenize=False
)
```

实际工程里，最重要的不是模板长什么样，而是三件事是否稳定：工具签名的序列化方式、模型输出 tool call 的边界、工具结果回填后的 role 表达。只要其中一个环节不一致，下游解析就会变脆。

---

## 3. 特殊 Token 的分化：从“全文结束”到“边界管理”

| 阶段 | 任务 | 所需“结束”语义 | 典型 Token |
|---|---|---|---|
| Pretrain | 文档级 LM | 全文结束 | `<|end_of_sequence|>` / `<|endoftext|>` |
| SFT | 多轮对话 | 单轮角色结束 + 全文结束 | `<|im_end|>` + `<|endoftext|>` |
| Tool-use SFT | 函数调用 | 工具片段结束 + 角色结束 + 全文结束 | `<|im_end|>` / `<|tool_end|>` + `<|endoftext|>` |

### 3.1 为什么不用同一个 eos 复用？
- **语义冲突**：单一 token 承担多种边界 ⇒ 模型分布漂移  
- **解析困难**：下游需额外正则区分“句子完”还是“全文完”  
- **成本极低**：新增 1~3 个 id 即可换取鲁棒性与可解析性

这里的关键变化是：大模型从“续写文档”进入“参与系统”。文档续写只需要知道全文何时结束；多轮对话需要知道一个角色的发言何时结束；工具调用还需要知道 JSON 片段、工具返回、assistant 自然语言回复之间的边界。特殊 token 的增加，本质上是在给 runtime 留出更明确的控制点。

---

## 4. 工程上真正要检查什么

| 任务 | 代码片段 |
|---|---|
| 普通推理 | `tok.apply_chat_template(messages, add_generation_prompt=True)` |
| 工具推理 | `tok.apply_chat_template(messages, tools=tools, add_generation_prompt=True)` |
| 训练集预处理 | `tok.apply_chat_template(chat, add_generation_prompt=False, tokenize=False)` |
| 自定义模板 | `tok.chat_template = "{% raw %}{% ... %}{% endraw %}"` |

如果要把一个新模型接入对话或 Agent 系统，我会优先检查四件事：

1. tokenizer 配置里是否已经带有可靠的 `chat_template`。
2. 训练数据、推理 prompt 和线上 runtime 是否使用同一套模板。
3. tool-use 输出是否有明确的开始、结束和 JSON 解析边界。
4. `eos_token`、`pad_token`、`im_end`、`tool_end` 等 token 是否被混用。

这些检查看起来琐碎，但它们决定了模型能力能不能被稳定释放出来。

---

## 5. 结论：格式是 Agent 系统的地基

1. **Chat Template = 对话格式 DSL**：一次编写，推理/训练/微调全通用。  
2. **Tool-Use 模板 = 在 DSL 里新增函数调用语法**，让模型输出可执行代码。  
3. **Token 演化 = 语义维度膨胀**：从“句子结束”到“角色结束、工具结束、文档结束”，每新增一种边界就引入一个不可冲突的特殊符号。

最后可以把这件事理解成三层：Chat Template 管消息格式，Tool-Use Template 管行动协议，特殊 token 管边界语义。模型本身负责生成，下游系统负责解释和执行，中间靠模板把两边对齐。

这也是为什么格式问题不应该被当作接入细节。对普通聊天应用来说，它决定回答质量；对 Agent 系统来说，它决定工具调用、状态流转和错误恢复是否可靠。掌握这三层，才谈得上把开源模型安全、无损、可扩展地接入真实系统。

## 引用

若想引用本文，请使用：

```bibtex
@misc{dong2025chattemplate,
  author = {Peijie Dong},
  title = {大模型对话格式全景},
  year = {2025},
  month = aug,
  day = {22},
  howpublished = {\url{https://pprp.github.io/tech/chat-template/}},
  url = {https://pprp.github.io/tech/chat-template/},
  note = {Blog post. Accessed: 2026-04-28},
  language = {Chinese}
}
```
