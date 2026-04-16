---
layout: note
title: "Claude Code：一次 source map 暴露了什么"
title_en: "How a Source Map Leaked Anthropic's Entire Claude Code CLI"
date: 2026-03-31 00:00:00 +0800
categories: notes
note_source: "Rushi"
original_url: "https://www.rushis.com/how-a-source-map-leaked-anthropics-entire-claude-code-cli/"
---
Rushi 这篇文章讲的是事件本身，但真正有价值的部分不是“泄露”二字，而是它借这个事件把 Claude Code 的应用层结构讲得很清楚。

## 中文译摘

作者指出，`@anthropic-ai/claude-code` 的 npm 包里一度带上了 `.map` 文件，结果让外界能顺着映射关系看到大量 TypeScript 源文件和目录结构。文章把这件事解读为一次对生产级 coding agent 的意外开窗：外界不再只能看打包后的单文件 CLI，而是能更系统地理解它的命令体系、工具注册、多智能体相关模块、持久记忆、IDE 桥接和 feature flag 设计。

作者的重点并不是鼓励围观，而是提醒读者：Claude Code 真正复杂的地方并不在“它会不会调一个模型”，而在那套把模型接入真实软件工程环境的外围系统。也就是说，真正暴露出来的是一门成熟的 agent runtime 工程学。

## 我记下来的点

- source map 带来的最大价值不是多看几行代码，而是看清目录、模块边界和编译前命名。
- 对 agent 产品来说，工具平面、权限平面和上下文平面往往比 API 调用本身更有研究价值。
- 这篇文章适合作为 2026 年这波 Claude Code 解读潮的时间起点。

