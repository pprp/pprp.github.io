---
layout: note
title: "Claude Code：所谓“源码泄露”其实早有公开线索"
title_en: "Claude Code's Source Didn't Leak. It Was Already Public for Years."
date: 2026-04-01 00:00:00 +0800
categories: notes
note_source: "AfterPack"
original_url: "https://www.afterpack.dev/blog/claude-code-source-leak"
---
这篇文章最重要的作用是纠偏。它反对把 2026 年 3 月底的事件简单描述成“Claude Code 源码第一次泄露”。

## 中文译摘

作者的观点是，Claude Code 的应用逻辑早就以打包后的 `cli.js` 形式公开发布在 npm 上了。对有经验的工程师来说，那个单文件 bundle 本来就可以被下载、格式化、阅读和分析。所以 2026 年真正新增的信息，不是“能不能看代码”，而是 source map 把原始文件名、模块路径、开发注释和更接近源码组织的上下文暴露了出来。

这篇文章把几个概念分得很清楚：bundle 不等于不可读，minify 不等于保护源码，source map 则会显著降低还原结构的成本。这个判断很值得记住，因为它让讨论回到工程现实：JavaScript 世界里，闭源客户端工具如果只是打包压缩，通常挡不住真正的研究型阅读。

## 我记下来的点

- 理解 Claude Code 的前提，是先分清 bundle、minify、obfuscation 和 source map。
- 对分析者而言，source map 主要提升的是结构理解效率，而不是把完全不可见变成可见。
- 这篇文章适合作为所有后续“源码解读”文章的校准器。

