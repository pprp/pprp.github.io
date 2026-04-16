---
layout: note
title: "Claude Code：记忆系统与 CLAUDE.md"
title_en: "How Claude Code Designs Its Memory System"
date: 2026-04-01 00:00:00 +0800
categories: notes
note_source: "ChooseAI"
original_url: "https://www.chooseai.net/news/3125/"
---
这篇文章专门回答一个很实用的问题：Claude Code 的“记忆”到底是什么，它和很多人理解的向量数据库式记忆有多大差别。

## 中文译摘

文章把 Claude Code 的记忆拆成两层。第一层是 `CLAUDE.md`，它更像人类维护的长期规则和工作偏好，负责告诉 Claude 在这个项目里该怎么做事。第二层是运行过程中沉淀下来的自动记忆，用来保留任务上下文、工作习惯和可复用经验。两层都落在本地文件系统里，而且都可以被人直接读写、审查和纳入版本管理。

作者进一步把 `CLAUDE.md` 解释成一套层级化规则系统，而不是单个文件。企业、团队、项目、用户、本地目录都可以叠加自己的约束。这种设计的好处很明显：Claude Code 的“记忆”不是藏在模型黑盒里，而是外置成可审计、可覆盖、可回滚的知识层。对工程团队来说，这比神秘的自动记忆更重要。

## 我记下来的点

- Claude Code 的长期记忆更像文件化规则系统，不像传统 AI 应用里的隐式 memory store。
- `CLAUDE.md` 的价值不只是提示词，而是把团队约束变成机器可加载的工程接口。
- 这套设计很适合迁移到自己的 agent harness，因为它天然支持审计和版本控制。

