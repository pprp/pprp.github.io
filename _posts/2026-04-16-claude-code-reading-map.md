---
layout: post
title: "Claude Code 与 Agent Harness 阅读地图"
title_en: "A Reading Map for Claude Code and Agent Harnesses"
date: 2026-04-16 00:00:00 +0800
last_modified_at: 2026-07-15 00:00:00 +0800
author: pprp
categories: tech
topics: [agent, source-reading]
excerpt: '一张理解 Claude Code 与 Agent Harness 的分层阅读地图：从智能体循环和 App Server 出发，再进入上下文、工具、长任务与多智能体系统。'
---

## 读 Claude Code，不能只盯着模型或客户端

理解 Claude Code 最容易走入两个极端：要么把它当成“更会写代码的模型”，只讨论提示词与模型能力；要么把注意力全部放在 CLI、编辑器或某段实现细节上。两种视角都只覆盖了局部。

生产级 Coding Agent 是一个系统：模型负责推理，智能体循环协调工具，权限与沙盒限制动作，协议连接不同客户端，上下文与制品维持任务状态，测试和评估器提供反馈。只有把这些层放在一起，才能解释为什么同一个模型在不同 Harness 中会表现出完全不同的可靠性。

我把相关资料拆成「多篇 notes + 一篇 blog」，正是因为这些材料分别回答运行时、上下文、工具、长任务和多智能体等不同问题。逐篇笔记便于追溯原始来源；这篇文章则负责给出阅读顺序和跨文结论。

更合理的结构是：

- `notes` 里放单篇材料的中文译摘和我的简短理解
- `blog` 里放总览、比较、阅读顺序和跨文统一结论

所以这篇文章不再逐段翻译某一篇原文，而是回答一个更实用的问题：

**如果你想系统理解 Claude Code 与 Agent Harness，应该先读什么，后读什么，每篇到底解决了什么问题？**

## 先把资料分成三层，阅读才不会散

### 1. 运行时骨架：Agent 到底怎样循环

- [深入解析 Codex 智能体循环](/notes/openai-unrolling-the-codex-agent-loop/)
- [解锁 Codex 运行框架：我们如何构建 App Server](/notes/openai-unlocking-the-codex-harness/)
- [Harness Engineering：在智能体优先的世界中利用 Codex](/notes/openai-harness-engineering/)

这三篇回答的是同一个问题的不同尺度：单轮内部如何在模型与工具之间循环，核心能力如何通过协议提供给多个客户端，以及整个代码库与工程组织如何改造成 Agent 可理解、可操作、可验证的环境。

先建立这层骨架，才能看清 CLI 或编辑器只是入口；真正决定系统能力的是循环、协议、工具、权限、状态和反馈回路。

### 2. 日常工作法：怎样让 Coding Agent 稳定产出

- [Claude Code：智能体式编码最佳实践](/notes/anthropic-claude-code-best-practices/)
- [Claude Code：会话管理与 1M 上下文](/notes/thariq-claude-code-session-management-1m-context/)
- [面向 AI 智能体的高效上下文工程](/notes/anthropic-effective-context-engineering-for-ai-agents/)
- [为智能体编写高效工具：借助智能体完成](/notes/anthropic-writing-tools-for-agents/)

这一层从系统结构转向操作者视角：怎样给出可验证目标，什么时候继续当前会话，什么时候回退、压缩或清空，哪些信息值得进入上下文，以及工具接口怎样减少歧义和无效 token。

这组材料最可复用的结论是：Agent 的上限不只取决于模型，也取决于它能否获得清晰任务、紧凑上下文、合适工具和及时验证。

### 3. 长任务与多智能体：怎样跨会话持续交付

- [面向长时运行智能体的高效 Harness](/notes/anthropic-effective-harnesses-for-long-running-agents/)
- [面向长时运行应用开发的 Harness 设计](/notes/anthropic-harness-design-long-running-apps/)
- [我们如何构建多智能体研究系统](/notes/anthropic-multi-agent-research-system/)

这一层讨论单个上下文窗口之外的问题。初始化制品、进度日志和 Git 历史负责交接；规划器、生成器和评估器形成质量闭环；主智能体与子智能体通过任务分解和结果压缩控制并行研究成本。

这里需要特别区分两件事：多智能体不是目的，角色分工也不是越多越好。只有当任务可以并行、上下文需要隔离，或评估必须独立于生成时，额外 Agent 才能带来稳定收益。

## 推荐阅读顺序：先建立循环，再扩展时间尺度

如果你第一次系统理解 Coding Agent，可以按下面四步阅读：

1. **看懂基本循环。** 先读 [Codex 智能体循环](/notes/openai-unrolling-the-codex-agent-loop/)，明确输入、推理、工具调用、观察与最终响应怎样组成一轮。
2. **把循环放进产品。** 再读 [Codex App Server](/notes/openai-unlocking-the-codex-harness/) 与 [Harness Engineering](/notes/openai-harness-engineering/)，理解协议边界和 Agent-friendly 环境。
3. **掌握日常控制面。** 接着读 [Claude Code 最佳实践](/notes/anthropic-claude-code-best-practices/)、[会话管理](/notes/thariq-claude-code-session-management-1m-context/) 和 [上下文工程](/notes/anthropic-effective-context-engineering-for-ai-agents/)。
4. **进入长时与并行任务。** 最后读 [长时运行 Harness](/notes/anthropic-effective-harnesses-for-long-running-agents/)、[三智能体应用开发](/notes/anthropic-harness-design-long-running-apps/) 与 [多智能体研究系统](/notes/anthropic-multi-agent-research-system/)。

这条顺序背后的逻辑是：先理解一轮怎样正确执行，再理解多轮怎样保持状态，最后才讨论多个 Agent 怎样分工。跳过前两层直接堆叠多智能体，往往只会把单 Agent 的模糊性并行放大。

## 放在一起看，真正的线索是 harness

把这些文章和仓库一起看，会出现几个非常稳定的结论。

### 1. 价值主要在 harness，不在终端壳子

这是所有高质量材料最一致的地方。

Claude Code 当然依赖强模型，但社区真正反复学到的，是模型外部那套支撑系统：工具调用、权限规则、上下文压缩、记忆文件、子代理、任务隔离、Hook 和配置覆盖。这些内容才构成了一个能长期跑、能真实执行、能逐步恢复的 coding agent。

### 2. 权限系统不是边角料，而是产品核心

很多人最初看到 Claude Code，只会注意它“会写代码”“会跑命令”。但越往下读越会发现，真正决定它能不能进真实环境的，是权限模型。只要 agent 可以直接操作本地机器，权限判断就不是用户体验细节，而是产品本体。

### 3. 长任务的难点几乎都落在上下文管理上

只要任务变长，问题就会变成：

- 上下文快满了怎么办
- 旧信息怎么压缩
- 哪些东西应该留在主上下文
- 哪些东西应该让子代理带走
- 哪些规则应该写进 `CLAUDE.md`
- 哪些经验应该自动沉淀成记忆

这也是为什么看完这些材料以后，你对 Claude Code 的印象会从“强大的模型”变成“非常认真地在管理上下文和状态的一套系统”。

### 4. 多智能体很多时候是更便宜的上下文隔离

这点很容易被神话，但其实很多材料都在指向同一个现实：子代理的一个核心价值，并不是模仿人类团队，而是把探索过程中生成的大量脏上下文隔离出去，主上下文只保留结果。这个视角非常工程化，也非常实用。

## 我刻意没有收录的东西

我没有把直接分发 Claude Code 专有源码镜像的仓库列进这组资料里。

理由很简单：对学习者来说，更有长期价值的是“解释源码”和“复用模式”的材料，而不是法律边界模糊、可持续性也不稳定的源码搬运仓库。真正值得学的，是这些材料提炼出的设计方法，而不是把代码原样抄回来。

## 结尾：先做 harness，再谈 agent

如果你读 Claude Code 只是为了满足好奇心，那么读到系统结构那一层其实就够了。

但如果你是为了自己做 agent，那么我觉得最应该带走的不是某个具体 prompt，也不是某段实现，而是下面这句话：

**先做 harness，再谈 agent。**

换句话说，先把工具、权限、上下文、记忆、验证回路和扩展点搭好，再去期待模型表现稳定。Claude Code 之所以值得研究，不是因为它藏着某种魔法，而是因为它把“让模型在真实机器上长期工作”这件事拆成了一组可以学习、可以复用、也可以被审视的工程机制。

## 引用

若想引用本文，请使用：

```bibtex
@misc{dong2026claudecodereadingmap,
  author = {Peijie Dong},
  title = {Claude Code 与 Agent Harness 阅读地图},
  year = {2026},
  month = apr,
  day = {16},
  howpublished = {\url{https://pprp.github.io/tech/claude-code-reading-map/}},
  url = {https://pprp.github.io/tech/claude-code-reading-map/},
  urldate = {2026-07-15},
  note = {Blog post. Accessed: 2026-07-15},
  language = {Chinese}
}
```
