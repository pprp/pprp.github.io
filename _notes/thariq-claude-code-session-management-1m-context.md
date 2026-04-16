---
layout: note
title: "Claude Code：会话管理与 1M 上下文"
title_en: "Using Claude Code: Session Management & 1M Context"
date: 2026-04-16 00:00:00 +0800
categories: notes
note_source: "Thariq / X"
original_url: "https://x.com/trq212/status/2044548257058328723"
---
这是一份围绕 Claude Code 长会话管理的实战指南。重点不在于“把 1M context 用满”，而在于当上下文窗口大到足以承载超长任务时，如何避免噪声、失败路径和过时信息把模型一步步拖偏。

![配图：Using Claude Code - Session Management & 1M Context](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/2.png)

## 上下文、压缩与上下文退化

上下文窗口，指的是模型在生成下一条回复时“同时看得到”的全部信息。它不仅包括系统提示词和当前对话，还包括每一次工具调用的输出、已经读过的文件，以及会话里已经发生过的中间推理。

在 Claude Code 里，这个窗口现在可以达到 **100 万 token**。这确实让更长、更复杂的任务变得可行，但代价是会出现 **上下文退化（context rot）**：上下文越长，注意力越分散，越老、越无关的信息越容易干扰当前任务。对 1M context 模型来说，这种退化大致会在 **30 万到 40 万 token** 左右开始明显出现，但它强依赖任务类型，不能当成硬阈值。

上下文窗口还有一个现实约束：它终究是有上限的。接近上限时，你必须把当前任务做一次摘要，然后在新的上下文里继续推进，这就是 **压缩（compaction）**。你可以等自动压缩触发，也可以主动手动执行。

![配图：上下文窗口与 context rot 示意图](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/4.png)

## 每一轮结束，都是一次分叉点

Claude 完成一轮输出之后，你接下来其实有五种选择：

- `Continue`：继续在当前会话里发下一条消息
- `/rewind` 或双击 `Esc`：跳回之前某个消息节点，从那里重新开始
- `/clear`：开启一个全新会话，通常带着你提炼过的一段 brief
- `/compact`：把当前会话压缩成摘要，再基于摘要继续
- `Subagent`：把下一段工作委托给一个拥有干净上下文的子智能体

多数人最自然的动作是继续聊下去，但这五个选项本质上都是上下文管理工具。它们的差别，不是“哪个更高级”，而是 **你想把多少旧上下文带进下一步**。

| 方式 | 带入下一步的上下文 |
| --- | --- |
| 新会话 | 只有你重新写下的 brief |
| `/compact` | 一份有损摘要 |
| `Subagent` | 父上下文 + 子智能体结论 |
| `/rewind` | 保留前缀，裁掉错误分支 |
| `Continue` | 原样保留全部上下文 |

![配图：不同操作保留上下文的多少](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/7.png)

## 什么时候该开新会话

1M context 的直接收益，是你现在可以更稳地完成超长任务，比如从零搭一个全栈应用。但“还没到窗口上限”并不等于“应该继续留在同一个会话里”。

一个很实用的经验法则是：**只要你开始的是一个新任务，就应该同步开启一个新 session。**

真正的灰区在于“相关但不完全相同”的任务。例如你刚做完一个功能，接着写它的文档。这时候如果清空重来，Claude 还得重新读一遍文件，会更慢也更贵。而文档编写通常又不是对推理质量最敏感的环节，那么多带一点旧上下文，往往是值得的。

换句话说，是否新开会话，不只是看 token 余额，还要看下一步任务对“上下文纯净度”和“执行效率”哪一个更敏感。

![配图：何时启动新会话](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/8.png)

## 出错后，优先 rewind，而不是补救式纠错

如果只能挑一个最能体现“会话管理水平”的习惯，Thariq 选的是 **rewind**。

在 Claude Code 里，双击 `Esc` 或执行 `/rewind`，可以回到任意一条更早的消息，然后从那里重新提示。那个节点之后的消息会被整个裁掉，不再进入当前上下文。

如果你只是顺着失败路径继续纠错，比如：

> 不对，别用 A，试试 B  
> 还是不对，再试试 C

那么失败尝试、纠偏指令和多轮噪声会一起留在上下文里。最后上下文长这样：

> context = 文件读取 + 两次失败尝试 + 两次纠错 + 最终修复

而 `rewind` 的思路是：回到失败发生前，但保留你已经获得的关键信息，然后重新给出一个更准确的提示。这样上下文会变成：

> context = 文件读取 + 一条更知情的提示 + 最终修复

这个差别很重要。比如 Claude 已经读了 5 个文件，尝试了一条路径，但你发现方向错了。大多数人的第一反应是输入“这个不对，换成 X”。更干净的做法是 rewind 到读完文件之后，再重新提示：“不要走 A 路径，`foo` 模块并没有暴露那个接口，直接走 B。”

如果你想保留失败过程里学到的经验，可以借助 **“summarize from here”**，让 Claude 把当前分支的教训压成一段交接信息，再交给回退后的自己。

![配图：纠错与 rewind 的差别](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/10.png)

## `/compact` 和 `/clear` 看起来像，实际上差很多

当一个 session 已经很长时，你通常有两种减重方式：`/compact`，或者 `/clear` 后自己带着 brief 重开。

`/compact` 的做法，是让模型自己总结到目前为止发生了什么，然后用这段摘要替换原历史。它的优点是快、便宜、不中断工作流；缺点是 **有损**。你把“什么重要”这件事交给了 Claude 自己判断。

你也可以给压缩加一点引导，例如：

```text
/compact focus on the auth refactor, drop the test debugging
```

这适合那种任务还没切换、你只是想甩掉一部分陈旧调试噪声的场景。

`/clear` 则完全相反。你要自己写清楚：当前任务是什么、约束是什么、关键文件有哪些、哪些方向已经被排除。它更费力，但压进去的是 **你明确挑选过的上下文**。

一个可以直接拿来用的判断方式是：

- **任务还在继续，只是会话有点臃肿**：优先 `/compact`
- **下一步很关键，你刚刚从一大堆探索里只提炼出一个核心事实**：优先 `/clear` + 人工 brief

![配图：Compact 与 Fresh Session 的对比](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/12.png)

## 为什么会出现“坏压缩”

很多长会话用户都碰到过一个问题：压缩之后，Claude 反而像“忘了重点”。这通常不是因为模型完全没能力，而是因为 **压缩发生时，它无法预测你下一步真正要做什么**。

典型例子是：你刚经历了一大段 debugging，会话自动压缩，把整个调查过程总结了出来。结果你的下一条消息却是：“现在顺手把 `bar.ts` 里那个 warning 也修掉。”如果那条 warning 不是刚才调试主线的一部分，它就很可能在压缩摘要里被丢掉。

更麻烦的是，压缩往往发生在上下文已经很长的时候，而这恰恰是模型最容易被上下文退化影响的时候。1M context 的好处之一，就是给了你更大的提前量，让你可以在模型还比较清醒的时候，主动执行一次 **带目标提示的压缩**。

![配图：坏压缩是怎么发生的](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/13.png)

## 子智能体，本质上也是上下文管理

`Subagent` 不只是并行化工具，它同样是一种上下文治理手段。适合它的场景是：你预先知道，下一段工作会产出很多中间噪声，而你最终真正需要带回父会话的，其实只有结论。

当 Claude 通过 Agent 工具拉起一个子智能体时，子智能体会拥有自己的全新上下文窗口。它可以自由读文件、搜索代码、走几条死路，最后再把结果压成一份汇报返回给父上下文。

一个很好用的判断问题是：

**我下一步还需要这堆工具输出本身，还是只需要最终结论？**

如果答案是后者，就应该优先考虑子智能体。这样 20 次文件读取、12 次 grep、3 次失败尝试，都会随着子智能体退出一起被“垃圾回收”，父会话只接收最后那份报告。

一些典型的指令长这样：

- 拉一个子智能体验证当前改动是否满足某份 spec
- 拉一个子智能体去读另一个代码库，总结其认证流程，然后按同样方式在当前项目里实现
- 拉一个子智能体基于当前 git diff 写文档

![配图：子智能体如何隔离上下文噪声](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/15.png)

## 总结

当 Claude 结束一轮输出、你准备发下一条消息时，其实你正在做一个很关键的上下文决策。短期内，这个决策还需要人来帮模型做；长期看，Claude 也许会越来越自动化，但现在会话管理仍然是高质量输出的重要杠杆。

| 场景 | 优先使用 | 原因 |
| --- | --- | --- |
| 还是同一个任务，而且上下文仍然关键 | `Continue` | 现有窗口里的信息仍然都在承重，没必要重建 |
| Claude 走偏了 | `/rewind` | 保留有用的读取结果，裁掉失败分支，再带着新认识重提示 |
| 任务没变，但会话里堆满了旧调试和探索噪声 | `/compact <hint>` | 成本低，让 Claude 帮你提炼重点，必要时给提示语约束 |
| 真正开始了一个新任务 | `/clear` | 彻底清零上下文退化，由你决定哪些信息继续携带 |
| 下一步会产生大量中间输出，而你只需要最终结论 | `Subagent` | 噪声留在子会话里，父上下文只接收压缩后的结果 |

![配图：最终决策表](https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/assets/thariq-16-apr-26/19.png)

## 来源

- [Thariq 在 X 上的原始线程](https://x.com/trq212/status/2044548257058328723)
- [社区整理稿（用于补全线程中的文字与配图顺序）](https://github.com/shanraisshan/claude-code-best-practice/blob/main/tips/claude-thariq-tips-16-apr-26.md)
