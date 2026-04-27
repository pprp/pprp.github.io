---
layout: note
title: "Claude Code：智能体式编码最佳实践"
title_en: "Claude Code: Best practices for agentic coding"
date: 2025-04-18 00:00:00 +0800
categories: notes
note_source: "Anthropic"
original_url: "https://www.anthropic.com/engineering/claude-code-best-practices"
---
# Claude Code 最佳实践

这份笔记整理自 Anthropic 的 Claude Code 最佳实践文档。它的核心不是提示词技巧清单，而是一套围绕上下文、验证、权限、环境和多会话协作的工程工作法。

Claude Code 是一个具有智能体能力的编码环境。与那种回答问题然后等待的聊天机器人不同，Claude Code 能够读取你的文件、运行命令、进行修改，并在你观察、引导或完全离开的情况下自主解决问题。这改变了你的工作方式。你不再需要自己编写代码后让 Claude 来审查，而是描述你想要什么，由 Claude 来决定如何构建。Claude 会自主探索、规划并实现。但这种自主性仍然有一条学习曲线。Claude 在某些你需要理解的约束条件下工作。本指南涵盖了在 Anthropic 内部团队以及在各种代码库、语言和环境中使用 Claude Code 的工程师中被证明有效的模式。关于智能体循环在底层的工作原理，请参阅 [Claude Code 的工作原理](http://www.anthropic.com/docs/en/how-claude-code-works)。

---

大多数最佳实践都基于一个约束：Claude 的上下文窗口填满得很快，而随着填充程度增加，性能会下降。Claude 的上下文窗口保存着你的整个对话记录，包括每一条消息、Claude 读取的每一个文件以及每一条命令的输出。然而，这个窗口可能填满得非常快。单次调试会话或代码库探索就可能产生并消耗数万个 token。这很关键，因为随着上下文填充，大语言模型的性能会下降。当上下文窗口即将填满时，Claude 可能开始"遗忘"早期的指令或犯更多错误。上下文窗口是最重要的需要管理的资源。要了解一次会话在实践中如何填满，可以[观看交互式演示](http://www.anthropic.com/docs/en/context-window)，了解启动时加载了什么以及每次文件读取的代价。通过[自定义状态栏](http://www.anthropic.com/docs/en/statusline)持续跟踪上下文使用情况，并参阅[减少 token 用量](http://www.anthropic.com/docs/en/costs#reduce-token-usage)了解降低 token 消耗的策略。

---

## 给 Claude 提供验证工作成果的方式

提供测试、截图或预期输出，让 Claude 能够自我检查。这是你能做的单项杠杆效益最高的事情。

当 Claude 能够验证自己的工作成果时（例如运行测试、对比截图、验证输出），其表现会显著提升。若缺乏明确的成功标准，它可能产出看似正确但实际有误的结果。你将成为唯一的反馈环节，每一个错误都需要你亲自介入。

| 策略 | 改进前 | 改进后 |
| --- | --- | --- |
| **提供验证标准** | _"实现一个验证邮件地址的函数"_ | _"编写 validateEmail 函数。示例测试用例：[[email protected]](http://www.anthropic.com/cdn-cgi/l/email-protection#d8adabbdaa98bda0b9b5a8b4bdf6bbb7b5) 应为 true，invalid 应为 false，[[email protected]](http://www.anthropic.com/cdn-cgi/l/email-protection#99eceafcebd9b7faf6f4) 应为 false。实现后运行测试"_ |
| **可视化验证 UI 变更** | _"让仪表盘看起来更好看"_ | _"[粘贴截图] 实现该设计。对结果截图并与原图对比，列出差异并修复"_ |
| **解决根因而非表象** | _"构建失败了"_ | _"构建报如下错误：[粘贴错误信息]。修复它并验证构建成功。解决根本原因，不要屏蔽错误"_ |

UI 变更可通过 [Claude in Chrome 扩展](http://www.anthropic.com/docs/en/chrome)进行验证。它会在浏览器中打开新标签页，测试 UI，并持续迭代直到代码正常运行。你的验证手段也可以是测试套件、代码检查工具，或检查输出的 Bash 命令。请务必让你的验证机制足够可靠。

---

## 先探索，再规划，再编码

将调研与规划从实现中分离，避免解决错误的问题。

让 Claude 直接跳到编码阶段可能会产出解决了错误问题的代码。使用[计划模式](http://www.anthropic.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis)将探索与执行分离。推荐的工作流分为四个阶段：

1

探索

进入计划模式。Claude 读取文件、回答问题，但不做任何修改。

claude (Plan Mode)

```
read /src/auth and understand how we handle sessions and login.
also look at how we manage environment variables for secrets.
```

2

规划

让 Claude 创建详细的实现方案。

claude (Plan Mode)

```
I want to add Google OAuth. What files need to change?
What's the session flow? Create a plan.
```

按 `Ctrl+G` 可在文本编辑器中打开方案，在 Claude 继续执行前直接编辑。

3

实现

切换回普通模式，让 Claude 编码，并对照方案进行验证。

claude (Normal Mode)

```
implement the OAuth flow from your plan. write tests for the
callback handler, run the test suite and fix any failures.
```

4

提交

让 Claude 附上描述性提交信息并创建 PR。

claude (Normal Mode)

```
commit with a descriptive message and open a PR
```

计划模式很有用，但也会带来额外开销。对于范围明确、改动较小的任务（如修复拼写错误、添加日志行或重命名变量），可直接让 Claude 执行。当你对方案不确定、变更涉及多个文件，或你对被修改的代码不熟悉时，规划最为有用。如果你能用一句话描述 diff 的内容，则可跳过规划环节。

---

## 在提示中提供具体上下文

指令越精确，需要纠正的次数就越少。

Claude 能推断意图，但无法读心。请指定具体文件、说明约束条件，并指向示例模式。

| 策略 | 改进前 | 改进后 |
| --- | --- | --- |
| **限定任务范围。** 指定文件、场景和测试偏好。 | _"为 foo.py 添加测试"_ | _"为 foo.py 编写测试，覆盖用户已退出登录的边界情况。避免使用 mock。"_ |
| **指向信息来源。** 引导 Claude 找到能回答问题的来源。 | _"ExecutionFactory 为什么 API 设计这么奇怪？"_ | _"查看 ExecutionFactory 的 git 历史，梳理其 API 演变过程并进行总结"_ |
| **引用已有模式。** 指向代码库中的现有模式。 | _"添加一个日历组件"_ | _"参考首页现有组件的实现方式以理解其模式，HotDogWidget.php 是一个很好的示例。遵循该模式实现一个新的日历组件，允许用户选择月份并前后翻页选择年份。从零构建，只使用代码库中已有的依赖库。"_ |
| **描述现象。** 提供现象、可能所在位置以及"修复完成"的判断标准。 | _"修复登录 bug"_ | _"用户反映会话超时后登录失败。检查 src/auth/ 中的认证流程，尤其是 token 刷新部分。先编写复现问题的失败测试，再修复它"_ |

当你处于探索阶段且能够接受方向调整时，模糊的提示也有其价值。例如 `"你会如何改进这个文件？"` 这样的提示，可能会发现你未曾想到的问题。

### 提供丰富的内容

使用 `@` 引用文件、粘贴截图/图片，或直接管道传入数据。

你可以通过多种方式向 Claude 提供丰富的数据：

- **使用 `@` 引用文件**，而非描述代码所在位置。Claude 会在响应前读取该文件。
- **直接粘贴图片**。将图片复制粘贴或拖放到提示框中。
- **提供 URL** 以引用文档和 API 参考。使用 `/permissions` 将常用域名加入白名单。
- **管道传入数据**，运行 `cat error.log | claude` 直接发送文件内容。
- **让 Claude 自行获取所需内容**。告诉 Claude 使用 Bash 命令、MCP 工具或读取文件来自行拉取上下文。

---

## 配置你的环境

几个设置步骤可让 Claude Code 在所有会话中显著提升效能。关于扩展功能的完整概览及各功能的适用场景，请参阅[扩展 Claude Code](http://www.anthropic.com/docs/en/features-overview)。

### 编写有效的 CLAUDE.md

运行 `/init` 根据当前项目结构生成一个初始 CLAUDE.md 文件，然后随时间不断完善。

CLAUDE.md 是一个特殊文件，Claude 在每次对话开始时都会读取它。其中可包含 Bash 命令、代码风格和工作流规则，让 Claude 获得仅凭代码无法推断的持久上下文。`/init` 命令会分析你的代码库，自动检测构建系统、测试框架和代码模式，为你提供一个扎实的起点。CLAUDE.md 文件没有固定格式，但应保持简洁、便于人类阅读。例如：

CLAUDE.md

```
# 代码风格
- 使用 ES 模块（import/export）语法，而非 CommonJS（require）
- 尽可能解构导入（例如 import { foo } from 'bar'）

# 工作流
- 完成一系列代码修改后，务必进行类型检查
- 优先运行单个测试，而非整个测试套件，以提高性能
```

CLAUDE.md 在每次会话时都会加载，因此只应包含广泛适用的内容。对于仅在特定场景下才相关的领域知识或工作流，请改用 [skills](http://www.anthropic.com/docs/en/skills)——它们按需加载，不会让每次对话都变得臃肿。保持简洁：对每一行内容，都问自己：_"删掉这行会导致 Claude 犯错吗？"_ 如果不会，就删掉。臃肿的 CLAUDE.md 文件会让 Claude 忽略你真正的指令！

| ✅ 应包含 | ❌ 不应包含 |
| --- | --- |
| Claude 无法猜到的 Bash 命令 | Claude 读代码就能推断的内容 |
| 与默认值不同的代码风格规则 | Claude 已知的标准语言惯例 |
| 测试说明和首选测试运行器 | 详细的 API 文档（改为链接到文档） |
| 仓库规范（分支命名、PR 惯例） | 频繁变动的信息 |
| 项目特有的架构决策 | 冗长的解释或教程 |
| 开发环境的特殊要求（必需的环境变量） | 对代码库的逐文件描述 |
| 常见陷阱或非显而易见的行为 | 诸如"编写整洁代码"之类不言而喻的做法 |

如果 Claude 不断重复你明确禁止的行为，说明文件可能太长，规则被淹没了。如果 Claude 询问的问题 CLAUDE.md 中已有解答，说明措辞可能存在歧义。像对待代码一样对待 CLAUDE.md：出问题时复盘、定期精简，并通过观察 Claude 的行为变化来验证修改效果。你可以在规则前加上强调词（如"IMPORTANT"或"YOU MUST"）来提高遵从度。将 CLAUDE.md 纳入 git 管理，让团队共同维护——这个文件会随时间积累出越来越高的价值。CLAUDE.md 文件可以使用 `@path/to/import` 语法导入其他文件：

CLAUDE.md

```
See @README.md for project overview and @package.json for available npm commands.

# 补充说明
- Git 工作流：@docs/git-instructions.md
- 个人覆盖配置：@~/.claude/my-project-instructions.md
```

你可以将 CLAUDE.md 放置在以下几个位置：
- **主目录（`~/.claude/CLAUDE.md`）**：适用于所有 Claude 会话
- **项目根目录（`./CLAUDE.md`）**：纳入 git 管理，与团队共享
- **项目根目录（`./CLAUDE.local.md`）**：个人项目专属备注；将此文件添加到 `.gitignore`，避免与团队共享
- **父级目录**：适用于 monorepo，`root/CLAUDE.md` 和 `root/foo/CLAUDE.md` 都会被自动加载
- **子目录**：当 Claude 处理相应目录中的文件时，会按需加载子目录中的 CLAUDE.md 文件

### 配置权限

使用[自动模式](http://www.anthropic.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)让分类器处理审批，用 `/permissions` 将特定命令加入白名单，或用 `/sandbox` 实现操作系统级隔离。每种方式都能减少打断，同时让你保持掌控。

默认情况下，Claude Code 会对可能修改系统的操作（文件写入、Bash 命令、MCP 工具等）请求权限。这样做很安全，但繁琐。当你点击到第十次审批时，其实已经不是在认真审查了，只是在机械地点击而已。有三种方式可以减少这类打断：
- **自动模式**：由独立的分类器模型审查命令，仅拦截看起来有风险的操作：权限升级、未知基础设施或由恶意内容驱动的操作。当你信任任务的整体方向但不想逐步点击审批时，最为适用
- **权限白名单**：允许你确认安全的特定工具，例如 `npm run lint` 或 `git commit`
- **沙盒**：启用操作系统级隔离，限制文件系统和网络访问，让 Claude 在定义的边界内更自由地工作

了解更多关于[权限模式](http://www.anthropic.com/docs/en/permission-modes)、[权限规则](http://www.anthropic.com/docs/en/permissions)和[沙盒](http://www.anthropic.com/docs/en/sandboxing)的内容。

### 使用 CLI 工具

让 Claude Code 在与外部服务交互时使用 `gh`、`aws`、`gcloud`、`sentry-cli` 等 CLI 工具。

CLI 工具是与外部服务交互时上下文效率最高的方式。如果你使用 GitHub，请安装 `gh` CLI。Claude 知道如何用它创建 issue、开启 pull request 和读取评论。没有 `gh` 时，Claude 也可以使用 GitHub API，但未经身份验证的请求往往会触发速率限制。Claude 也很擅长学习它尚不熟悉的 CLI 工具。可以尝试这样的提示语：`使用 'foo-cli-tool --help' 了解 foo 工具，然后用它解决 A、B、C 问题。`

### 接入 MCP 服务器

运行 `claude mcp add` 接入 Notion、Figma 或数据库等外部工具。

通过 [MCP 服务器](http://www.anthropic.com/docs/en/mcp)，你可以让 Claude 从问题追踪器中实现功能、查询数据库、分析监控数据、集成 Figma 设计，以及自动化工作流。

### 配置 Hooks

对于必须每次都执行、不允许有任何例外的操作，请使用 hooks。

[Hooks](http://www.anthropic.com/docs/en/hooks-guide) 会在 Claude 工作流的特定节点自动运行脚本。与 CLAUDE.md 中的说明不同（那些只是建议性的），hooks 是确定性的，能保证操作一定发生。你可以让 Claude 为你编写 hooks。可以尝试这样的提示语：_"编写一个在每次文件编辑后运行 eslint 的 hook"_ 或 _"编写一个阻止向 migrations 文件夹写入的 hook。"_ 也可以直接编辑 `.claude/settings.json` 手动配置 hooks，并运行 `/hooks` 浏览当前配置。

### 创建技能

在 `.claude/skills/` 中创建 `SKILL.md` 文件，为 Claude 提供领域知识和可复用的工作流。

[技能](http://www.anthropic.com/docs/en/skills)通过特定于你的项目、团队或领域的信息来扩展 Claude 的知识。Claude 会在相关时自动应用它们，你也可以通过 `/skill-name` 直接调用。在 `.claude/skills/` 中添加一个包含 `SKILL.md` 的目录来创建技能：

.claude/skills/api-conventions/SKILL.md

```
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

技能还可以定义可直接调用的可重复工作流：

.claude/skills/fix-issue/SKILL.md

```
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

运行 `/fix-issue 1234` 来调用它。对于有副作用、希望手动触发的工作流，请使用 `disable-model-invocation: true`。

### 创建自定义子智能体

在 `.claude/agents/` 中定义专用助手，Claude 可以将独立任务委托给它们。

[子智能体](http://www.anthropic.com/docs/en/sub-agents)在各自的上下文中运行，并拥有各自允许使用的工具集。它们适用于需要读取大量文件或需要专项聚焦、又不希望占用主会话上下文的任务。

.claude/agents/security-reviewer.md

```
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

明确告知 Claude 使用子智能体：_"使用子智能体来审查此代码的安全问题。"_

### 安装插件

运行 `/plugin` 浏览插件市场。插件无需配置即可添加技能、工具和集成。

[插件](http://www.anthropic.com/docs/en/plugins)将技能、钩子、子智能体和 MCP 服务器打包成单一可安装单元，来源于社区和 Anthropic。如果你使用的是强类型语言，请安装[代码智能插件](http://www.anthropic.com/docs/en/discover-plugins#code-intelligence)，为 Claude 提供精确的符号导航以及编辑后的自动错误检测。关于如何在技能、子智能体、钩子和 MCP 之间做出选择，请参阅[扩展 Claude Code](http://www.anthropic.com/docs/en/features-overview#match-features-to-your-goal)。

---

## 有效沟通

与 Claude Code 的沟通方式对结果质量有显著影响。

### 提问代码库问题

像向高级工程师提问一样向 Claude 提问。

在熟悉新代码库时，使用 Claude Code 进行学习和探索。你可以像向其他工程师提问一样向 Claude 提问：

- 日志是如何工作的？
- 如何新建一个 API 端点？
- `foo.rs` 第 134 行的 `async move { ... }` 有什么作用？
- `CustomerOnboardingFlowImpl` 处理了哪些边界情况？
- 为什么第 333 行调用的是 `foo()` 而不是 `bar()`？

以这种方式使用 Claude Code 是一种有效的上手工作流，既能缩短熟悉代码库所需的时间，又能减少对其他工程师的依赖。无需特殊的提示技巧：直接提问即可。

### 让 Claude 访谈你

对于较大的功能，先让 Claude 访谈你。从一个简洁的提示开始，让 Claude 使用 `AskUserQuestion` 工具对你进行访谈。

Claude 会就你可能尚未考虑到的方面提问，包括技术实现、UI/UX、边界情况和权衡取舍。

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

规格说明完成后，开启一个新会话来执行它。新会话拥有完全聚焦于实现的干净上下文，同时你也有了一份可供参考的书面规格说明。

---

## 管理你的会话

对话是持久的，也是可撤销的。善加利用这一特性！

### 尽早且频繁地纠偏

一旦发现 Claude 偏离方向，立即纠正。

最佳结果来自紧密的反馈循环。尽管 Claude 偶尔能在第一次尝试时完美解决问题，但快速纠正通常能更快地产出更好的解决方案。

- **`Esc`**：用 `Esc` 键在 Claude 执行操作途中将其停止。上下文会被保留，因此你可以重新引导。
- **`Esc + Esc` 或 `/rewind`**：按两次 `Esc` 或运行 `/rewind` 打开回退菜单，恢复之前的会话和代码状态，或从选定的消息处进行摘要。
- **`"撤销那个"`**：让 Claude 还原其更改。
- **`/clear`**：在不相关的任务之间重置上下文。包含无关上下文的长会话可能会降低性能。

如果你在同一会话中就同一问题纠正了 Claude 超过两次，说明上下文已被失败的尝试所干扰。运行 `/clear` 重新开始，并使用融入了你所学到的经验的更具体的提示。一个拥有更好提示的干净会话几乎总是优于一个积累了大量纠正的长会话。

### 积极管理上下文

在不相关的任务之间运行 `/clear` 以重置上下文。

Claude Code 会在你接近上下文限制时自动压缩对话历史，在释放空间的同时保留重要的代码和决策。在长会话中，Claude 的上下文窗口可能被无关的对话、文件内容和命令填满，这会降低性能，有时还会分散 Claude 的注意力。

- 频繁使用 `/clear` 在任务之间彻底重置上下文窗口
- 当自动压缩触发时，Claude 会汇总最重要的内容，包括代码模式、文件状态和关键决策
- 如需更多控制，运行 `/compact <instructions>`，例如 `/compact Focus on the API changes`
- 若只想压缩部分对话，使用 `Esc + Esc` 或 `/rewind`，选择一个消息检查点，然后选择**从此处摘要**。这会压缩从该点往后的消息，同时保留更早的上下文完好无损。
- 在 CLAUDE.md 中自定义压缩行为，例如添加 `"压缩时，始终保留已修改文件的完整列表以及所有测试命令"` 等说明，以确保关键上下文在摘要后得以留存
- 对于无需保留在上下文中的快速问题，使用 [`/btw`](http://www.anthropic.com/docs/en/interactive-mode#side-questions-with-btw)。答案会显示在一个可关闭的浮层中，永远不会进入对话历史，让你在不增加上下文的情况下随时查阅细节。

### 使用子智能体进行调查

使用 `"use subagents to investigate X"` 委托研究任务。子智能体在独立的上下文中进行探索，让你的主对话保持整洁，专注于实现。

由于上下文是你的根本限制，子智能体是最强大的工具之一。当 Claude 研究代码库时，它会读取大量文件，这些文件都会消耗你的上下文。子智能体在独立的上下文窗口中运行，并以摘要的形式汇报结果：

```
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

子智能体探索代码库、读取相关文件，并汇报发现结果，整个过程不会污染你的主对话。你也可以在 Claude 实现某些功能后，使用子智能体进行验证：

```
use a subagent to review this code for edge cases
```

### 使用检查点回退

Claude 的每次操作都会创建一个检查点。你可以将对话、代码，或两者同时恢复到任意之前的检查点。

Claude 会在更改前自动创建检查点。双击 `Escape` 或运行 `/rewind` 打开回退菜单。你可以选择仅恢复对话、仅恢复代码、同时恢复两者，或从选定消息开始生成摘要。详情请参阅 [检查点](http://www.anthropic.com/docs/en/checkpointing)。不必事先谨慎规划每一步，你可以让 Claude 大胆尝试。如果结果不理想，回退后换一种方式再试。检查点跨会话持久保存，即使关闭终端，之后仍可回退。

检查点只追踪 _Claude_ 所做的更改，不追踪外部进程的操作。这不能替代 git。

### 恢复对话

运行 `claude --continue` 从上次中断处继续，或使用 `--resume` 从最近的会话中选择。

Claude Code 在本地保存对话记录。当一项任务跨越多个会话时，你无需重新说明上下文：

```
claude --continue    # Resume the most recent conversation
claude --resume      # Select from recent conversations
```

使用 `/rename` 为会话指定描述性名称，如 `"oauth-migration"` 或 `"debugging-memory-leak"`，方便日后查找。将会话视为分支：不同的工作流可以拥有各自独立且持久的上下文。

---

## 自动化与扩展

在熟练使用单个 Claude 之后，通过并行会话、非交互模式和扇出模式成倍提升产出。以上所有内容都假设一个用户、一个 Claude、一次对话。但 Claude Code 支持水平扩展。本节介绍如何完成更多工作。

### 运行非交互模式

在 CI、pre-commit 钩子或脚本中使用 `claude -p "prompt"`。添加 `--output-format stream-json` 可获得流式 JSON 输出。

使用 `claude -p "your prompt"`，你可以以非交互方式运行 Claude，无需建立会话。非交互模式适合将 Claude 集成到 CI 流水线、pre-commit 钩子或任何自动化工作流中。多种输出格式支持以编程方式解析结果：纯文本、JSON 或流式 JSON。

```
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json
```

### 运行多个 Claude 会话

并行运行多个 Claude 会话，以加快开发速度、运行隔离实验或启动复杂工作流。

并行运行会话主要有三种方式：
- [Claude Code 桌面应用](http://www.anthropic.com/docs/en/desktop#work-in-parallel-with-sessions)：可视化管理多个本地会话。每个会话拥有独立的隔离工作树。
- [Web 版 Claude Code](http://www.anthropic.com/docs/en/claude-code-on-the-web)：在 Anthropic 安全云基础设施的隔离虚拟机中运行。
- [智能体团队](http://www.anthropic.com/docs/en/agent-teams)：自动协调多个会话，支持共享任务、消息传递和团队负责人。

除了并行化工作，多会话还支持以质量为核心的工作流。全新上下文能改善代码审查效果，因为 Claude 不会对自己刚写的代码存在偏见。例如，使用编写者/审查者模式：

| 会话 A（编写者） | 会话 B（审查者） |
| --- | --- |
| `Implement a rate limiter for our API endpoints` |  |
|  | `Review the rate limiter implementation in @src/middleware/rateLimiter.ts. Look for edge cases, race conditions, and consistency with our existing middleware patterns.` |
| `Here's the review feedback: [Session B output]. Address these issues.` |  |

测试场景同样可以如此操作：让一个 Claude 编写测试，再让另一个编写代码来通过测试。

### 跨文件扇出

循环遍历任务，为每个任务调用 `claude -p`。对于批量操作，使用 `--allowedTools` 限制权限范围。

对于大规模迁移或分析，你可以将工作分发给多个并行的 Claude 实例：

1

生成任务列表

让 Claude 列出所有需要迁移的文件（例如，`list all 2,000 Python files that need migrating`）

2

编写脚本循环遍历列表

```
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

3

在少量文件上测试，然后大规模运行

根据前 2-3 个文件出现的问题优化提示词，再对完整文件集运行。`--allowedTools` 标志可限制 Claude 的操作范围，在无人值守运行时尤为重要。

你也可以将 Claude 集成到现有的数据/处理流水线中：

```
claude -p "<your prompt>" --output-format json | your_command
```

开发调试时使用 `--verbose`，生产环境中关闭该选项。

### 使用自动模式自主运行

如需无中断执行并在后台进行安全检查，请使用 [自动模式](http://www.anthropic.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)。分类器模型会在命令执行前进行审查，阻止权限范围升级、访问未知基础设施以及由恶意内容驱动的操作，同时允许常规工作无需提示地继续进行。

```
claude --permission-mode auto -p "fix all lint errors"
```

对于使用 `-p` 标志的非交互式运行，若分类器反复阻止操作，自动模式将中止执行，因为没有用户可以接管处理。请参阅 [自动模式的回退时机](http://www.anthropic.com/docs/en/permission-modes#when-auto-mode-falls-back) 了解相关阈值。

---

## 避免常见的失败模式

以下是常见错误。尽早识别它们可以节省时间：
- **大杂烩会话。** 你从一个任务开始，然后问 Claude 一些不相关的事情，再回到第一个任务。上下文中充满了无关信息。
> **解决方案**：在不相关的任务之间使用 `/clear`。

- **反复纠错。** Claude 做错了某件事，你纠正它，它仍然错误，你再次纠正。上下文被失败的方法所污染。
> **解决方案**：两次纠正失败后，使用 `/clear` 并结合你所学到的内容编写更好的初始提示词。

- **过度详细的 CLAUDE.md。** 如果你的 CLAUDE.md 太长，Claude 会忽略其中一半，因为重要规则淹没在噪音中。
> **解决方案**：无情地精简。如果 Claude 已经在没有指令的情况下正确执行某些操作，删除该指令或将其转换为钩子。

- **信任后验证的缺口。** Claude 产生了看似合理的实现，但未处理边缘情况。
> **解决方案**：始终提供验证（测试、脚本、截图）。如果无法验证，就不要发布。

- **无限探索。** 你要求 Claude "调查"某事而没有限定范围。Claude 读取了数百个文件，填满了上下文。
> **解决方案**：缩小调查范围，或使用子智能体，以免探索消耗主要上下文。

---

## 培养你的直觉

本指南中的模式并非一成不变。它们是在一般情况下效果良好的起点，但可能并非适用于每种情况。有时你_应该_让上下文积累，因为你正深入处理一个复杂问题，而历史记录很有价值。有时你应该跳过规划，让 Claude 自行解决，因为任务本身是探索性的。有时模糊的提示词恰恰是正确的，因为你想在加以限制之前先看看 Claude 如何解读问题。注意哪些方法有效。当 Claude 产出优质输出时，留意你做了什么：提示词结构、你提供的上下文、你所处的模式。当 Claude 遇到困难时，思考原因。是上下文太嘈杂？提示词太模糊？任务太大而无法一次完成？随着时间推移，你将培养出任何指南都无法传授的直觉。你会知道何时该具体、何时该开放，何时该规划、何时该探索，何时该清除上下文、何时该让其积累。

## 相关资源

- [Claude Code 工作原理](http://www.anthropic.com/docs/en/how-claude-code-works)：智能体循环、工具和上下文管理
- [扩展 Claude Code](http://www.anthropic.com/docs/en/features-overview)：技能、钩子、MCP、子智能体和插件
- [常见工作流程](http://www.anthropic.com/docs/en/common-workflows)：调试、测试、PR 等的分步指南
- [CLAUDE.md](http://www.anthropic.com/docs/en/memory)：存储项目约定和持久化上下文
