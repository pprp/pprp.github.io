---
layout: note
title: "learn Claude Code：把源码解读变成 Harness 教程"
title_en: "Learn Claude Code -- Harness Engineering for Real Agents"
date: 2026-04-16 00:00:00 +0800
categories: notes
note_source: "GitHub · shareAI-lab"
original_url: "https://github.com/shareAI-lab/learn-claude-code"
---
`learn-claude-code` 不是 Claude Code 的镜像仓库，而是一套教学型 clean-room 项目。它的目标不是复制 Anthropic 的源码，而是把 Claude Code 值得学的机制拆成可以自己动手复现的 harness 课程。

## 中文译摘

仓库最核心的一句话是：agency 来自模型，agent product 等于 model 加 harness。作者反复强调，外部代码编排不会凭空“制造智能”，但一个真正可用的 agent 产品必须把工具、知识、观察接口、动作接口和权限系统组织成完整运行环境。也就是说，模型像驾驶员，harness 像车辆。

仓库后半部分把这个观点落成了 12 个渐进 session，从最小 agent loop 一直推进到任务图、子代理、上下文压缩、后台执行、异步邮箱、团队协作和 worktree 隔离。它对 Claude Code 的最大借鉴，不是代码抄写，而是教学式复现。

## 我记下来的点

- 这是“学 Claude Code 怎么造 harness”，不是“下载 Claude Code 源码”。
- 很适合想自己做 coding agent 的人，因为它把复杂系统拆成可逐步验证的小机制。
- 如果只打算复用一个理念，那就是：先把环境搭对，再谈 agent 表现。

