---
layout: note
title: "Claude Code：Harness Engineering 完全指南"
title_en: "Claude Code Reverse Engineering and Systematic Analysis"
date: 2026-04-02 00:00:00 +0800
categories: notes
note_source: "青稞社区"
original_url: "https://qingkeai.online/archives/Claude%20Code"
---
这篇长文的价值，在于它不只把 Claude Code 当成一个“源码泄露事件”，而是把它重新命名成一个更值得学习的主题：Harness Engineering。

## 中文译摘

作者把 Claude Code 拆成一整套围绕 agent 的支撑结构来讲，而不是只盯着模型调用。文章的主线是：真正让 Claude Code 可用的，不是“模型在命令行里回答问题”，而是模型外面那一圈工具系统、权限门控、Hook、设置层、上下文工程、安全边界和沙盒策略。

文章特别强调一点：Agent loop 本身未必复杂，复杂的是如何让 loop 在真实机器上安全、长期、可恢复地工作。Claude Code 的很多工程设计，都是在解决这个问题。比如为什么要把权限判断做成分层规则，为什么需要 settings 覆盖体系，为什么要把上下文和记忆单独当成基础设施，而不是临时塞在 prompt 里。

## 我记下来的点

- Claude Code 最值得学的不是“提示词技巧”，而是外层 runtime 结构。
- 一个可用的 coding agent，本质上是 model 加上治理严格的 harness。
- 想复刻 Claude Code，最好先按“工具、权限、上下文、记忆、扩展点”分层，而不是先追多智能体。

