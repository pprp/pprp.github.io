---
layout: post
title: "为智能体编写高效工具：借助智能体完成"
title_en: "Writing effective tools for agents — with agents"
date: 2025-09-11 00:00:00 +0800
categories: notes
note_source: "Anthropic"
original_url: "https://www.anthropic.com/engineering/writing-tools-for-agents"
---
来源：Anthropic 官方英文博客
发布日期：2025-09-11
链接：https://www.anthropic.com/engineering/writing-tools-for-agents
说明：中文为基于官方英文原文整理的中文译稿。
英文原文：https://www.anthropic.com/engineering/writing-tools-for-agents

[模型上下文协议（MCP）](https://modelcontextprotocol.io/docs/getting-started/intro)可以为大语言模型智能体赋予数百种工具，从而解决现实世界中的任务。但我们如何才能让这些工具发挥最大效用？

在本文中，我们介绍了在各类智能体 AI 系统中提升性能的最有效技术 1。

我们首先介绍如何：

*   构建并测试工具原型
*   与智能体协同创建并运行对工具的全面评估
*   借助 Claude Code 等智能体自动提升工具性能

最后，我们总结了在此过程中归纳出的高质量工具编写核心原则：

*   选择正确的工具来实现（以及哪些不应实现）
*   通过命名空间定义工具功能的清晰边界
*   从工具向智能体返回有意义的上下文
*   优化工具响应的 token 效率
*   对工具描述和规范进行提示词工程

![图1：该图展示了工程师如何使用 Claude Code 评估智能体工具有效性。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&w=3840&q=75)

构建评估体系，让你系统地衡量工具性能。你可以使用 Claude Code 自动针对该评估体系对工具进行优化。

## 什么是工具？

在计算机科学中，确定性系统在给定相同输入时始终产生相同输出，而_非确定性_系统（如智能体）即使在相同起始条件下也可能生成不同的响应。

传统编写软件时，我们是在确定性系统之间建立契约。例如，函数调用 `getWeather("NYC")` 每次调用时都会以完全相同的方式获取纽约市的天气。

工具是一种新型软件，体现的是确定性系统与非确定性智能体之间的契约。当用户询问"今天我需要带伞吗？"时，智能体可能调用天气工具、根据常识作答，甚至先反问用户所在位置。有时，智能体可能产生幻觉，甚至无法理解如何使用某个工具。

这意味着我们在为智能体编写软件时需要从根本上转变思路：不应像为其他开发者或系统编写函数和 API 那样编写工具和 [MCP 服务器](https://modelcontextprotocol.io/)，而是要专门为智能体进行设计。

我们的目标是通过工具扩展智能体能够有效解决各类任务的适用范围，使其能够采取多种成功策略。幸运的是，根据我们的经验，对智能体最"符合人体工程学"的工具，往往也是人类最容易直观理解的。

## 如何编写工具

本节介绍如何与智能体协作，既用于编写工具，也用于改进工具。首先快速搭建工具原型并在本地测试。接着运行全面评估以衡量后续改动的效果。与智能体协同合作，反复迭代评估与优化，直到智能体在真实任务上取得优异表现。

### 构建原型

如果不亲自动手，很难预判哪些工具对智能体来说符合人体工程学，哪些不符合。首先快速搭建工具原型。如果你使用 [Claude Code](https://www.anthropic.com/claude-code) 编写工具（可能一次性完成），建议向 Claude 提供工具所依赖的软件库、API 或 SDK（包括可能用到的 [MCP SDK](https://modelcontextprotocol.io/docs/sdk)）的文档。LLM 友好的文档通常可以在官方文档网站的 `llms.txt` 文件中找到（这是我们 [API 的文档](https://docs.anthropic.com/llms.txt)）。

将工具封装在[本地 MCP 服务器](https://modelcontextprotocol.io/docs/develop/connect-local-servers)或[桌面扩展](https://www.anthropic.com/engineering/desktop-extensions)（DXT）中，可以让你在 Claude Code 或 Claude 桌面应用中连接并测试工具。

要将本地 MCP 服务器连接到 Claude Code，请运行 `claude mcp add <name> <command> [args...]`。

要将本地 MCP 服务器或 DXT 连接到 Claude 桌面应用，请分别导航至 `Settings > Developer` 或 `Settings > Extensions`。

工具也可以直接传入 [Anthropic API](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) 调用，以进行程序化测试。

亲自测试工具，找出任何不顺畅的地方。收集用户反馈，建立对工具预期应用场景和提示词的直觉认知。

### 运行评估

接下来，你需要通过运行评估来衡量 Claude 使用工具的效果。首先生成大量植根于真实世界使用场景的评估任务。我们建议与智能体协作，共同分析结果并确定改进方向。在我们的[工具评估食谱](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation)中可以查看这一完整流程。

![图2：该图表衡量了人工编写与 Claude 优化的 Slack MCP 服务器在测试集上的准确率。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&w=3840&q=75)

我们内部 Slack 工具的留出测试集性能表现

**生成评估任务**

有了早期原型之后，Claude Code 可以快速探索你的工具，并生成数十个提示词与响应对。提示词应来源于真实世界的使用场景，并基于真实的数据源和服务（例如内部知识库和微服务）。我们建议避免使用过于简单或流于表面的"沙盒"环境，因为这类环境无法以足够的复杂度对工具进行压力测试。优质的评估任务可能需要多次工具调用——有时多达数十次。

以下是一些优质任务示例：

*   安排下周与 Jane 的会议，讨论我们最新的 Acme Corp 项目。附上上次项目规划会议的记录，并预订一间会议室。
*   客户 ID 9182 反映其单次购买操作被重复扣款三次。查找所有相关日志条目，并确认是否有其他客户受到同一问题的影响。
*   客户 Sarah Chen 刚刚提交了取消订阅申请。请准备一份挽留方案，确定：（1）她离开的原因；（2）最具吸引力的挽留方案；（3）在提出方案前需注意的风险因素。

以下是一些较弱的任务示例：

*   安排下周与 jane@acme.corp 的会议。
*   在支付日志中搜索 `purchase_complete` 和 `customer_id=9182`。
*   查找客户 ID 45892 的取消订阅申请。

每个评估提示词都应配备可验证的响应或结果。验证器可以简单到将真实答案与采样响应进行精确字符串比较，也可以复杂到邀请 Claude 对响应进行评判。避免使用过于严格的验证器，以免因格式、标点或有效的替代表述等细微差异而拒绝正确响应。

对于每个提示词-响应对，你还可以选择性地指定期望智能体在解决任务时调用的工具，以衡量智能体在评估过程中是否能够正确理解每个工具的用途。但由于解决任务可能存在多条有效路径，请尽量避免过度规定或过度拟合于某种特定策略。

**运行评估**

我们建议通过直接调用 LLM API 以编程方式运行评估。使用简单的智能体循环（`while` 循环，交替调用 LLM API 和工具调用）：每个评估任务对应一个循环。每个评估智能体应接收单一任务提示词以及你的工具集。

在评估智能体的系统提示词中，我们建议指示智能体不仅输出用于验证的结构化响应块，还要输出推理和反馈块。指示智能体在工具调用和响应块_之前_输出这些内容，可以通过触发思维链（CoT）行为来提升大语言模型的有效智能。

如果你使用 Claude 运行评估，可以开启[交错思考](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking)功能，"开箱即用"地实现类似效果。这将帮助你探究智能体调用或不调用某些工具的原因，并找出工具描述和规范中需要改进的具体方向。

除整体准确率外，我们还建议收集其他指标，例如单次工具调用和任务的总运行时间、工具调用总次数、token 总消耗量以及工具错误情况。追踪工具调用有助于揭示智能体常用的工作流，并为工具整合提供优化空间。

![图3：该图表衡量了人工编写与 Claude 优化的 Asana MCP 服务器在测试集上的准确率。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&w=3840&q=75)

我们内部 Asana 工具的留出测试集性能表现

**分析结果**

智能体是你发现问题、获取反馈的得力助手，能够帮助你识别从矛盾的工具描述到低效的工具实现以及令人困惑的工具 schema 等各类问题。但请记住，智能体在反馈和响应中_未提及_的内容，往往比它明确说出的更为重要。大语言模型并不总是[言为心声](https://www.anthropic.com/research/tracing-thoughts-language-model)。

观察你的智能体在哪些地方遇到困难或感到困惑。通读评估智能体的推理与反馈（或思维链），以识别粗糙的边缘。查看原始记录（包括工具调用和工具响应），捕捉智能体思维链中未明确描述的行为。学会读懂字里行间；要记住，你的评估智能体不一定知道正确答案和策略。

分析你的工具调用指标。大量冗余的工具调用可能意味着需要对分页或令牌限制参数进行适当调整；大量因参数无效而导致的工具报错，则可能说明工具描述需要更清晰，或需要提供更好的示例。当我们推出 Claude 的[网页搜索工具](https://www.anthropic.com/news/web-search)时，我们发现 Claude 会不必要地在工具的 `query` 参数后追加 `2025`，从而导致搜索结果出现偏差、性能下降（我们通过改进工具描述将 Claude 引导回了正确方向）。

### 与智能体协作

你甚至可以让智能体帮你分析结果并改进工具。只需将评估智能体的记录拼接起来，粘贴到 Claude Code 中即可。Claude 擅长分析记录并一次性重构大量工具——例如，在进行新的更改时，确保工具实现与描述保持自洽。

事实上，本文中的大部分建议都来自于反复使用 Claude Code 优化我们内部工具实现的过程。我们的评估构建于内部工作区之上，涵盖了内部工作流的复杂性，包括真实的项目、文档和消息。

我们依赖留存测试集来确保不对"训练"评估产生过拟合。这些测试集表明，即使超出"专家"级工具实现所达到的水平，我们仍能获得额外的性能提升——无论这些工具是由我们的研究人员手工编写，还是由 Claude 自己生成的。

在下一节中，我们将分享从这一过程中学到的经验。

## 编写高效工具的原则

本节将我们的经验提炼为几条编写高效工具的指导原则。

### 为智能体选择合适的工具

工具越多并不总是越好。我们观察到一个常见错误：工具只是简单地封装现有软件功能或 API 端点，而不考虑这些工具是否适合智能体使用。这是因为智能体与传统软件相比具有不同的"可供性"（affordance），即它们以不同的方式感知自身可以使用这些工具采取的潜在行动。

大语言模型智能体的"上下文"有限（即它们一次能处理的信息量有限），而计算机内存却廉价且充裕。考虑在通讯录中搜索联系人这一任务。传统软件程序可以高效地逐一存储和处理联系人列表，逐个检查后再继续。

然而，如果大语言模型智能体使用一个返回所有联系人的工具，然后逐个令牌地读取每一条记录，它就会将有限的上下文空间浪费在无关信息上（想象一下从头到尾逐页翻阅通讯录来查找联系人——这就是暴力搜索）。更好、更自然的做法（对智能体和人类来说都是如此）是先跳转到相关页面（例如按字母顺序查找）。

我们建议构建少量经过深思熟虑的工具，针对特定的高影响力工作流，与你的评估任务相匹配，然后再逐步扩展。在通讯录的案例中，你可以选择实现 `search_contacts` 或 `message_contact` 工具，而非 `list_contacts` 工具。

工具可以整合功能，在底层处理多个离散操作（或 API 调用）。例如，工具可以用相关元数据丰富工具响应，或在单次工具调用中处理频繁链式调用的多步骤任务。

以下是一些示例：

*   与其实现 `list_users`、`list_events` 和 `create_event` 工具，不如考虑实现一个 `schedule_event` 工具，由它负责查找空闲时间并安排事件。
*   与其实现 `read_logs` 工具，不如考虑实现一个 `search_logs` 工具，只返回相关日志行及其上下文。
*   与其实现 `get_customer_by_id`、`list_transactions` 和 `list_notes` 工具，不如实现一个 `get_customer_context` 工具，一次性汇总客户所有近期相关信息。

确保你构建的每个工具都有清晰、明确的用途。工具应使智能体能够以人类在获得相同底层资源时的方式来分解和解决任务，同时减少中间输出所消耗的上下文。

工具过多或工具功能重叠，也会分散智能体对高效策略的注意力。对你构建（或不构建）的工具进行审慎、有选择性的规划，往往能带来显著回报。

### 为工具命名空间

你的 AI 智能体可能会访问数十个 MCP 服务器和数百种不同工具，其中包括其他开发者提供的工具。当工具在功能上存在重叠或用途模糊时，智能体可能会对该使用哪个工具感到困惑。

命名空间（将相关工具归入共同前缀下）有助于划清大量工具之间的边界；MCP 客户端有时会默认执行此操作。例如，按服务（如 `asana_search`、`jira_search`）和按资源（如 `asana_projects_search`、`asana_users_search`）对工具进行命名空间划分，可以帮助智能体在正确的时机选择正确的工具。

我们发现，在基于前缀和基于后缀的命名空间方案之间进行选择，对我们的工具使用评估会产生不可忽视的影响。不同大语言模型的效果各异，我们建议你根据自己的评估结果选择命名方案。

智能体可能会调用错误的工具、以错误的参数调用正确的工具、调用的工具数量不足，或错误地处理工具响应。通过有选择性地实现名称能反映任务自然划分的工具，你可以同时减少加载到智能体上下文中的工具数量和工具描述，并将智能体的计算量从上下文转移回工具调用本身。这从整体上降低了智能体犯错的风险。

### 从工具中返回有意义的上下文

同理，工具实现应注意只将高价值信息返回给智能体。它们应优先考虑上下文相关性而非灵活性，并避免使用底层技术标识符（例如：`uuid`、`256px_image_url`、`mime_type`）。`name`、`image_url` 和 `file_type` 等字段更有可能直接指导智能体的下游行动和响应。

智能体处理自然语言名称、术语或标识符的能力，也往往远优于处理晦涩标识符的能力。我们发现，仅仅将任意字母数字组成的 UUID 解析为更具语义意义和可解释性的语言（甚至采用从 0 开始的索引 ID 方案），就能通过减少幻觉显著提高 Claude 在检索任务中的精确度。

在某些情况下，智能体可能需要灵活地同时处理自然语言和技术标识符输出，哪怕只是为了触发下游工具调用（例如，`search_user(name='jane')` → `send_message(id=12345)`）。你可以通过在工具中暴露一个简单的 `response_format` 枚举参数来实现两者兼顾，让智能体控制工具返回 `"concise"`（简洁）还是 `"detailed"`（详细）响应（见下方图片）。

你还可以添加更多格式以获得更大的灵活性，类似于 GraphQL 中可以精确选择想要接收哪些信息的方式。以下是一个用于控制工具响应详细程度的 ResponseFormat 枚举示例：

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

以下是详细工具响应的示例（206 个令牌）：

![图 4：此代码片段展示了详细工具响应的示例。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&w=3840&q=75)

以下是简洁工具响应的示例（72 个令牌）：

![图 5：此代码片段展示了简洁工具响应的示例。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&w=3840&q=75)

Slack 话题及话题回复通过唯一的 `thread_ts` 进行标识，获取话题回复时需要用到它。`thread_ts` 及其他 ID（`channel_id`、`user_id`）可从 `"detailed"` 工具响应中获取，以便进行需要这些 ID 的后续工具调用。`"concise"` 工具响应只返回话题内容，不包含 ID。在此示例中，使用 `"concise"` 工具响应大约只消耗三分之一的令牌。

即使是工具响应的结构——例如 XML、JSON 或 Markdown——也会对评估性能产生影响：没有放之四海而皆准的解决方案。这是因为大语言模型基于下一个令牌预测进行训练，往往在与其训练数据匹配的格式上表现更好。最优响应结构因任务和智能体的不同而存在很大差异。我们建议你根据自己的评估结果选择最佳响应结构。

### 优化工具响应的 token 效率

优化上下文质量固然重要，但同样重要的是优化工具响应返回给 Agent 的上下文**数量**。

我们建议对任何可能消耗大量上下文的工具响应，综合采用分页、范围选择、过滤和/或截断等方式，并为相关参数设置合理的默认值。在 Claude Code 中，我们默认将工具响应限制在 25,000 个 token 以内。我们预计 Agent 的有效上下文长度会随时间增长，但对上下文高效工具的需求将持续存在。

如果选择截断响应，请务必通过有效的提示引导 Agent。你可以直接鼓励 Agent 采用更节省 token 的策略，例如在知识检索任务中进行多次小而精准的搜索，而非一次宽泛的搜索。同样，如果工具调用引发错误（例如在输入验证期间），你可以通过提示工程设计错误响应，使其清晰传达具体且可操作的改进建议，而非晦涩的错误码或堆栈跟踪。

以下是一个截断工具响应的示例：

![图 6：该图展示了一个截断工具响应的示例。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&w=3840&q=75)

以下是一个无效错误响应的示例：

![图 7：该图展示了一个无效工具响应的示例。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&w=3840&q=75)

以下是一个有效错误响应的示例：

![图 8：该图展示了一个有效错误响应的示例。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&w=3840&q=75)

工具截断和错误响应能够引导 Agent 采用更节省 token 的工具使用行为（例如使用过滤或分页），或提供格式正确的工具输入示例。

### 通过提示工程优化工具描述

现在我们来讨论改进工具最有效的方法之一：对工具描述和规格进行提示工程。由于这些内容会被加载到 Agent 的上下文中，它们可以共同引导 Agent 形成有效的工具调用行为。

在撰写工具描述和规格时，请设想如何向团队新成员介绍你的工具。思考你可能隐式带入的上下文——专门的查询格式、小众术语的定义、底层资源之间的关系——并将其明确表达出来。通过清晰描述（并以严格的数据模型约束）预期的输入和输出来消除歧义。尤其是输入参数的命名应无歧义：例如，将名为 `user` 的参数改为 `user_id`。

借助评估体系，你可以更有把握地衡量提示工程的效果。即便是对工具描述的细微调整，也能带来显著提升。Claude Sonnet 3.5 在 [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) 评估中取得了最先进的性能，正是因为我们对工具描述进行了精准的优化，大幅降低了错误率并提升了任务完成度。

你可以在我们的[开发者指南](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions)中找到其他工具定义的最佳实践。如果你正在为 Claude 构建工具，我们还建议阅读工具如何被动态加载到 Claude [系统提示](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt)中的相关内容。最后，如果你正在为 MCP 服务器编写工具，[工具注解](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)有助于说明哪些工具需要开放式访问或会产生破坏性变更。

## 展望未来

要为 Agent 构建有效的工具，我们需要将软件开发实践从可预测的确定性模式转向非确定性模式。

通过本文所述的迭代式、评估驱动的过程，我们识别出了工具成功的一致规律：有效的工具经过精心且清晰的定义，审慎地使用 Agent 上下文，能够在多样化的工作流中组合使用，并使 Agent 能够直观地解决真实世界的任务。

未来，我们预计 Agent 与世界交互的具体机制将不断演进——从 MCP 协议的更新到底层大语言模型本身的升级。通过系统化、评估驱动的方法持续改进 Agent 工具，我们可以确保随着 Agent 能力的增强，其所使用的工具也能同步进化。

## 致谢

本文由 Ken Aizawa 撰写，并得到了来自各团队同事的宝贵贡献：研究团队（Barry Zhang、Zachary Witten、Daniel Jiang、Sami Al-Sheikh、Matt Bell、Maggie Vo）、MCP 团队（Theodora Chu、John Welsh、David Soria Parra、Adam Jones）、产品工程团队（Santiago Seira）、市场营销团队（Molly Vorwerck）、设计团队（Drew Roper）以及应用 AI 团队（Christian Ryan、Alexander Bricken）。

1 不包括对底层大语言模型本身的训练。
