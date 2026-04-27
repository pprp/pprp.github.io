---
layout: note
title: "面向长时运行智能体的高效 Harness"
title_en: "Effective harnesses for long-running agents"
date: 2025-11-26 00:00:00 +0800
categories: notes
note_source: "Anthropic"
original_url: "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
---
随着 AI 智能体能力提升，开发者越来越多地让它们承担需要数小时甚至数天才能完成的复杂任务。但真正困难的地方，不是让智能体开始工作，而是让它跨越多个上下文窗口后仍能持续、稳定、可交接地推进。

长期运行智能体的核心挑战在于：它们必须在离散会话中工作，而每个新会话开始时，对之前发生的一切都没有天然记忆。想象一个软件项目由工程师轮班负责，但每位新来的工程师都不知道上一班做了什么。由于上下文窗口有限，大多数复杂项目又无法在单个窗口内完成，智能体需要一种机制来衔接不同编码会话之间的断层。

我们开发了一套双重解决方案，使 [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) 能够跨越多个上下文窗口有效工作：一个在首次运行时配置环境的**初始化智能体**，以及一个负责在每次会话中推进增量进展、同时为下一次会话留下清晰工件的**编码智能体**。你可以在配套的[快速入门](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding)中找到代码示例。

## 长期运行智能体的问题

Claude Agent SDK 是一个功能强大的通用智能体框架，擅长编码以及其他需要模型使用工具收集上下文、规划并执行的任务。它具备上下文管理能力（例如压缩），使智能体能够在不耗尽上下文窗口的情况下持续工作。理论上，在这种配置下，智能体应该能够无限期地持续完成有价值的工作。

然而，压缩机制并不足够。即便是 Opus 4.5 这样的前沿编码模型，在 Claude Agent SDK 中跨多个上下文窗口循环运行时，如果仅给出一个高层级提示（例如"构建一个 [claude.ai](http://claude.ai/redirect/website.v1.170892e1-6a87-42f0-a44f-145133230533) 的克隆"），也难以构建出生产级别的 Web 应用。

Claude 的失败主要体现在两种模式上。第一种是智能体倾向于一次性做太多事情——本质上是试图一步到位地完成整个应用。这往往导致模型在实现过程中耗尽上下文，使下一个会话面对一个只完成了一半、且没有文档说明的功能。智能体随后不得不猜测之前发生了什么，并花费大量时间尝试让基础应用重新运行。这种情况即便在开启压缩的情况下也会发生，因为压缩并不总能向下一个智能体传递足够清晰的指令。

第二种失败模式通常出现在项目后期。当某些功能已经构建完成后，后续的智能体实例会环顾四周，发现已经取得了进展，然后宣布任务完成。

这将问题分解为两个部分。首先，我们需要建立一个初始环境，为给定提示所需的_所有_功能奠定基础，引导智能体按步骤、逐功能地推进工作。其次，我们应该提示每个智能体在向目标推进增量进展的同时，在会话结束时将环境保持在干净的状态。所谓"干净状态"，是指适合合并到主分支的代码状态：没有重大 bug，代码整洁且文档完善，开发者通常无需先清理无关的混乱就能轻松开始新功能的开发。

在内部实验中，我们通过一套两部分的解决方案解决了这些问题：

1.   初始化智能体：第一个智能体会话使用专门的提示，要求模型配置初始环境：一个 `init.sh` 脚本、一个记录智能体工作日志的 claude-progress.txt 文件，以及一个显示已添加文件的初始 git 提交。
2.   编码智能体：每个后续会话要求模型推进增量进展，然后留下结构化更新。<sup>1</sup>

这里的关键洞察是找到一种方式，让智能体在以全新上下文窗口启动时能够迅速了解工作状态——这通过 claude-progress.txt 文件与 git 历史记录共同实现。这些实践的灵感来源于对优秀软件工程师日常工作方式的观察。

## 环境管理

在更新版的 [Claude 4 提示指南](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#multi-context-window-workflows)中，我们分享了多上下文窗口工作流的一些最佳实践，包括一种"在第一个上下文窗口使用不同提示"的框架结构。这个"不同的提示"要求初始化智能体建立包含所有必要上下文的环境，以便未来的编码智能体能够有效工作。在此，我们深入探讨此类环境的一些关键组成部分。

### 功能列表

为了解决智能体一步到位完成应用或过早认为项目已完成的问题，我们提示初始化智能体编写一个全面的功能需求文件，对用户的初始提示进行扩展。在 [claude.ai](http://claude.ai/redirect/website.v1.170892e1-6a87-42f0-a44f-145133230533) 克隆示例中，这意味着超过 200 个功能，例如"用户可以开启新对话、输入查询、按回车键并看到 AI 响应"。这些功能最初全部标记为"失败"，以便后续编码智能体对完整功能的全貌有清晰的轮廓。

```
{
    "category": "functional",
    "description": "New chat button creates a fresh conversation",
    "steps": [
      "Navigate to main interface",
      "Click the 'New Chat' button",
      "Verify a new conversation is created",
      "Check that chat area shows welcome state",
      "Verify conversation appears in sidebar"
    ],
    "passes": false
  }
```

我们提示编码智能体只能通过修改 `passes` 字段的状态来编辑此文件，并使用措辞强硬的指令，例如"删除或编辑测试是不可接受的，因为这可能导致功能缺失或存在 bug"。经过一些实验，我们最终选择使用 JSON 格式，因为模型不太可能对 JSON 文件进行不当修改或覆盖，而 Markdown 文件则更容易被误操作。

### 增量进展

在完成上述初始环境脚手架之后，下一个编码智能体被要求每次只处理一个功能。事实证明，这种增量方式对于解决智能体一次性做太多事情的倾向至关重要。

在采用增量方式工作后，模型在每次代码更改后将环境保持在干净状态同样至关重要。在我们的实验中，引导此类行为的最佳方式是要求模型使用描述性提交信息将进展提交到 git，并在进度文件中写入进展摘要。这使得模型能够利用 git 回滚错误的代码更改并恢复代码库的正常工作状态。

这些方法还提升了效率，消除了智能体需要猜测之前发生了什么、并花时间重新让基础应用运行起来的需要。

### 测试

我们观察到的最后一个主要失败模式是 Claude 倾向于在没有进行充分测试的情况下将功能标记为已完成。在没有明确提示的情况下，Claude 倾向于进行代码更改，甚至通过单元测试或针对开发服务器的 `curl` 命令进行测试，但无法识别功能端到端并未正常运行的情况。

在构建 Web 应用的场景中，一旦明确提示 Claude 使用浏览器自动化工具、以真实用户的方式进行所有测试，它大多数情况下都能很好地进行端到端功能验证。

![图 1：Claude 通过 Puppeteer MCP 服务器在测试 claude.ai 克隆时截取的屏幕截图。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff94c2257964fb2d623f1e81f874977ebfc0986bc-1920x1080.gif&w=3840&q=75)

Claude 通过 Puppeteer MCP 服务器在测试 claude.ai 克隆时截取的屏幕截图。

为 Claude 提供这类测试工具显著提升了性能，因为智能体能够识别并修复那些仅凭代码本身难以发现的 bug。

部分问题仍然存在，例如 Claude 视觉能力的局限性以及浏览器自动化工具的限制，使得识别某些类型的 bug 较为困难。例如，Claude 无法通过 Puppeteer MCP 看到浏览器原生的 alert 模态框，因此依赖这些模态框的功能往往存在更多 bug。

## 快速上手

在完成上述所有配置后，每个编码智能体都会被提示按照一系列步骤来熟悉环境，其中一些步骤虽然基础，但依然很有帮助：

1.   _运行 `pwd` 查看当前工作目录。你只能编辑该目录中的文件。_
2.   _读取 git 日志和进度文件，了解最近的工作内容。_
3.   _读取功能列表文件，选择优先级最高的未完成功能来处理。_

这种方式在每次会话中为 Claude 节省了一些 token，因为它无需自行摸索如何测试代码。同时，也建议要求初始化智能体编写一个能够启动开发服务器的 `init.sh` 脚本，并在实现新功能之前运行基础的端到端测试。

在 claude.ai 克隆的案例中，这意味着智能体每次都会启动本地开发服务器，并使用 Puppeteer MCP 开启新对话、发送消息并接收响应。这确保了 Claude 能够快速识别应用是否处于异常状态，并立即修复现有 bug。如果智能体直接开始实现新功能，很可能会使问题进一步恶化。

基于以上所有配置，一次典型会话的助手消息如下：

```
[Assistant] I'll start by getting my bearings and understanding the current state of the project.
[Tool Use] <bash - pwd>
[Tool Use] <read - claude-progress.txt>
[Tool Use] <read - feature_list.json>
[Assistant] Let me check the git log to see recent work.
[Tool Use] <bash - git log --oneline -20>
[Assistant] Now let me check if there's an init.sh script to restart the servers.
<Starts the development server>
[Assistant] Excellent! Now let me navigate to the application and verify that some fundamental features are still working.
<Tests basic functionality>
[Assistant] Based on my verification testing, I can see that the fundamental functionality is working well. The core chat features, theme switching, conversation loading, and error handling are all functioning correctly. Now let me review the tests.json file more comprehensively to understand what needs to be implemented next.
<Starts work on a new feature>
```

智能体失败模式与解决方案

| **问题** | **初始化智能体行为** | **编码智能体行为** |
| --- | --- | --- |
| Claude 过早宣布整个项目完成。 | 建立功能列表文件：根据输入规范，建立包含端到端功能描述列表的结构化 JSON 文件。 | 在会话开始时读取功能列表文件。选择单个功能开始处理。 |
| Claude 将环境遗留在存在 bug 或进展未记录的状态。 | 初始化 git 仓库并创建进度记录文件。 | 会话开始时读取进度记录文件和 git 提交日志，并对开发服务器运行基础测试以捕获未记录的 bug。会话结束时写入 git 提交和进度更新。 |
| Claude 过早将功能标记为已完成。 | 建立功能列表文件。 | 对所有功能进行自我验证。仅在经过仔细测试后才将功能标记为"通过"。 |
| Claude 需要花时间搞清楚如何运行应用。 | 编写能够启动开发服务器的 `init.sh` 脚本。 | 会话开始时读取 `init.sh`。 |

归纳长期运行 AI 智能体的四种常见失败模式及其解决方案。

## 未来工作

本研究展示了在长期运行智能体框架中实现跨多个上下文窗口增量进展的一套可行解决方案。然而，仍存在一些悬而未决的问题。

最值得关注的是，目前尚不清楚单一的通用编码智能体是否能在跨上下文场景中表现最佳，还是通过多智能体架构能够实现更好的性能。合理推测，测试智能体、质量保证智能体或代码清理等专业智能体，或许能在软件开发生命周期的各个子任务中表现得更为出色。

此外，本演示针对全栈 Web 应用开发进行了优化。未来的方向是将这些发现推广到其他领域。这些经验中的部分或全部很可能适用于其他类型的长期智能体任务，例如科学研究或金融建模。

### 致谢

作者：Justin Young。特别感谢 David Hershey、Prithvi Rajasakeran、Jeremy Hadfield、Naia Bouscal、Michael Tingley、Jesse Mu、Jake Eaton、Marius Buleandara、Maggie Vo、Pedram Navid、Nadine Yasser 和 Alex Notov 的贡献。

本工作凝聚了 Anthropic 多个团队的集体努力，正是他们使 Claude 能够安全地完成长周期自主软件工程任务，尤其是代码强化学习团队与 Claude Code 团队。有意贡献的候选人欢迎通过 [anthropic.com/careers](http://anthropic.com/careers) 申请。

### 脚注

1. 我们在此处将其称为独立的智能体，仅因为它们具有不同的初始用户提示。系统提示、工具集以及整体智能体框架在其他方面完全相同。
