# Harness Engineering Blog Corpus

该目录整理了 OpenAI 与 Anthropic 官方博客中与 harness engineering、long-running agents、agent loop、context engineering、tooling 等主题强相关的文章，统一清洗为纯净 Markdown，并为每篇文章维护英文与中文两个版本。

## 选择标准

- 来源限定为 OpenAI 与 Anthropic 官方博客/工程文章。
- 优先选择与 `harness`、`long-running`、`agent loop`、`context engineering`、`agent tooling` 直接相关的内容。
- OpenAI 文章优先采用官方中文页；Anthropic 文章保留英文原文并补充中文整理译稿。

## 语料索引

| Source | Date | English Title | 中文标题 | Keywords | EN | ZH |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI | 2026-02-11 | Harness engineering: leveraging Codex in an agent-first world | 工程技术：在智能体优先的世界中利用 Codex | harness, agent-first engineering, Codex, repository legibility | [harness-engineering/en](openai/harness-engineering/en.md) | [harness-engineering/zh](openai/harness-engineering/zh.md) |
| OpenAI | 2026-01-23 | Unrolling the Codex agent loop | 深入解析 Codex 智能体循环 | agent loop, tool use, reasoning loop, Codex | [unrolling-the-codex-agent-loop/en](openai/unrolling-the-codex-agent-loop/en.md) | [unrolling-the-codex-agent-loop/zh](openai/unrolling-the-codex-agent-loop/zh.md) |
| OpenAI | 2026-02-04 | Unlocking the Codex harness: how we built the App Server | 解锁 Codex 运行框架：我们如何构建 App Server | harness, App Server, protocol, tool execution | [unlocking-the-codex-harness/en](openai/unlocking-the-codex-harness/en.md) | [unlocking-the-codex-harness/zh](openai/unlocking-the-codex-harness/zh.md) |
| Anthropic | 2025-11-26 | Effective harnesses for long-running agents | 面向长时运行智能体的高效 Harness | long-running agents, harness, context windows, progress files | [effective-harnesses-for-long-running-agents/en](anthropic/effective-harnesses-for-long-running-agents/en.md) | [effective-harnesses-for-long-running-agents/zh](anthropic/effective-harnesses-for-long-running-agents/zh.md) |
| Anthropic | 2026-03-24 | Harness design for long-running application development | 面向长时运行应用开发的 Harness 设计 | harness design, long-running application development, agents, app engineering | [harness-design-long-running-apps/en](anthropic/harness-design-long-running-apps/en.md) | [harness-design-long-running-apps/zh](anthropic/harness-design-long-running-apps/zh.md) |
| Anthropic | 2025-09-29 | Effective context engineering for AI agents | 面向 AI 智能体的高效上下文工程 | context engineering, agents, memory, prompting | [effective-context-engineering-for-ai-agents/en](anthropic/effective-context-engineering-for-ai-agents/en.md) | [effective-context-engineering-for-ai-agents/zh](anthropic/effective-context-engineering-for-ai-agents/zh.md) |
| Anthropic | 2025-09-11 | Writing effective tools for agents — with agents | 为智能体编写高效工具：借助智能体完成 | tools, agent tooling, MCP, developer workflow | [writing-tools-for-agents/en](anthropic/writing-tools-for-agents/en.md) | [writing-tools-for-agents/zh](anthropic/writing-tools-for-agents/zh.md) |
| Anthropic | 2025-06-13 | How we built our multi-agent research system | 我们如何构建多智能体研究系统 | multi-agent, research system, coordination, agents | [multi-agent-research-system/en](anthropic/multi-agent-research-system/en.md) | [multi-agent-research-system/zh](anthropic/multi-agent-research-system/zh.md) |
| Anthropic | 2025-04-18 | Claude Code: Best practices for agentic coding | Claude Code：智能体式编码最佳实践 | agentic coding, Claude Code, engineering workflow, best practices | [claude-code-best-practices/en](anthropic/claude-code-best-practices/en.md) | [claude-code-best-practices/zh](anthropic/claude-code-best-practices/zh.md) |

## 备注

- 文件内容已去除站点导航、页脚与推荐卡片，保留正文结构、标题层级、列表、表格、代码块与图片说明。
- Anthropic 中文稿为基于官方英文原文整理的中文译稿，不代表 Anthropic 官方发布版本。
- 如需继续扩展语料，可沿用当前目录结构：`publisher/slug/en.md` 与 `publisher/slug/zh.md`。
