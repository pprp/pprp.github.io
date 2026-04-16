---
layout: note
title: "claude-code-reverse：从运行时行为反推 Claude Code"
title_en: "Claude Code Reverse Engineering"
date: 2026-04-16 00:00:00 +0800
categories: notes
note_source: "GitHub · Yuyz0112"
original_url: "https://github.com/Yuyz0112/claude-code-reverse"
---
这个仓库的思路和直接啃静态 bundle 不一样。它更关心 Claude Code 在真实对话中是怎么和 LLM API 交互的，以及这些交互暴露出哪些内部机制。

## 中文译摘

作者先尝试过基于大体积 uglify JS 的静态逆向，但后面把重点转向了更实用的 v2 路线：通过修改本地安装的 Claude Code，请求级记录它和模型之间的 messages 数据，再对日志做可视化分析。这样做的好处是，可以绕开一部分复杂实现细节，直接观察 agent 到底在不同任务场景下发出了什么请求、加载了哪些 prompt、何时触发压缩、何时启动 Task/Sub Agent。

仓库当前整理出的结果包括 quota check、topic detection、core agent workflow、context compaction、IDE integration、Todo 短期记忆、Task/Sub Agent workflow 和历史会话总结。它特别适合拿来理解“主上下文为什么会变干净”这一类运行时问题。

## 我记下来的点

- 研究 Claude Code 不一定只能看静态源码，日志和 API 行为同样有价值。
- 子代理的一个重要收益，是把脏上下文隔离在子任务里。
- 这个仓库最适合作为运行时补充材料，而不是架构总览入口。

