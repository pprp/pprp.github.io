---
layout: note
title: "Claude Code：生产级 AI Agent 到底怎么运作"
title_en: "How Claude Code Actually Works: Reverse-Engineering 512K Lines of Production AI Agent"
date: 2026-04-02 00:00:00 +0800
categories: notes
note_source: "Karan Prasad"
original_url: "https://www.karanprasad.com/blog/how-claude-code-actually-works-reverse-engineering-512k-lines"
---
如果只选一篇英文长文来看 Claude Code 的工程内部结构，我会优先推荐这篇。它的信息密度最高，而且写法接近系统设计拆解。

## 中文译摘

作者把 Claude Code 视为一个大型生产级 agent runtime，而不是一个终端聊天工具。文章按子系统展开：启动流程、终端渲染引擎、权限决策流水线、上下文压缩、多智能体 IPC、系统提示拼装、feature flag 治理、跨云 provider 路由等，都被当成一等公民来分析。

这篇文章最强的地方，是它不断提醒读者“什么才是难点”。难点不是再包一层 API，而是怎样让一个长时运行的 agent 在上下文快满时继续工作，在权限不明确时默认保守，在多代理并行时还能保持状态隔离，在终端里提供足够流畅的反馈。它把 Claude Code 的价值准确地落在 harness 和 runtime 工程上。

## 我记下来的点

- Claude Code 的护城河很大一部分在系统工程，而不是模型接线。
- 安全和权限设计应该默认 fail-closed，而不是事后补救。
- 长会话 agent 一定要把上下文压缩、缓存和恢复能力当成基础设施来设计。

