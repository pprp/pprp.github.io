---
layout: post
title: '你和 AI 的关系，决定了你的能力走向'
date: 2026-04-29 00:00:00 +0800
last_modified_at: 2026-04-29 00:00:00 +0800
author: pprp
categories: tech
topics: [agent, skill, harness, education, memory]
---

过去两年，关于 AI 最流行的焦虑集中在一个错误的问题上：模型会不会替代我的工作？

这个问题问错了。

更值得问的是：当专家能力开始被压缩成可调用的软件模块，当一个人的学习历史开始被长期追踪和动态更新，当 agent 的行为目标开始被显式编码进系统约束——谁在设计这些模块？谁在控制这些系统？谁能在这个过程中让自己的能力实现真正跃迁，而不是悄悄被弱化？

这篇文章想厘清三件不同的事：**Skill 化**是什么、**Harness 化**是什么，以及为什么**超长周期 Agent** 是这套系统真正的关键。理解这三层区别，比关心"模型参数涨到多少"要重要得多。

---

## 一、Skill 化解决"会不会"，Harness 化解决"能不能稳定做对"

"一切职业职能均可以 skill 化和 harness 化"——这个判断方向正确，但把两件事混在一起讲，会错过最关键的分野。

### 1.1 Skill 化：把专家能力压缩成可调用的执行单元

**Skill 化**不是写一个更好的 prompt，而是把一个领域专家的工作方式蒸馏成一个有结构的可执行单元。OpenAI 对 Agent Skills 的定义是：一个 versioned bundle，里面通常包含 `SKILL.md`、说明、流程、约束、资源和示例，用来把某类流程、规范或多步骤工作 codify 成 agent 可调用的模块。

一个成熟 skill 至少应包括：

| 组成 | 作用 |
|---|---|
| 触发条件 | 什么时候该调用这个 skill |
| 专家流程 | 分几步做、每一步判断什么 |
| 输入/输出格式 | 防止模型发散 |
| 工具调用 | 是否要检索、计算、画图、写代码、查数据库 |
| 失败模式 | 常见错误与纠错路径 |
| 示例轨迹 | 好答案/坏答案的对照 |
| Evals | 如何判断 skill 是否执行成功 |

举一个具体例子："小学数学名师 skill"不是"你是一名数学老师，请讲清楚"，而应该包含：

- 如何识别学生的错误类型（概念不清、计算错误、题意误读、知识点断层）；
- 如何用苏格拉底式提问引导，而不是直接给答案；
- 如何记录学生掌握度并生成下一道题；
- 如何防止学生依赖模型抄答案。

把这六件事都写进 skill，才叫"名师能力蒸馏"。写一句"你是名师"，只是给了模型一个角色扮演的暗示。

### 1.2 Harness 化：把 skill 放进可控、可验证的运行框架

有了 skill，还不够。**Harness 化**解决的是另一层问题：即使 skill 写得再好，agent 仍然可能跑偏——在错误的上下文调用错误的能力，或者在"看起来完成"的状态下悄悄离题。

OpenAI 在 harness engineering 文章里强调，agent 生成的不只是代码，也包括测试、CI、文档、evaluation harness、review comments 和 dashboard；人类则更多转移到更高抽象层，负责 prioritization、acceptance criteria 和 outcome validation。Harness 是 agent 的运行约束系统，它决定 agent 能看到什么、能做什么、做完之后由谁来判断对不对。

Harness 的各个层次：

| Harness 层 | 作用 |
|---|---|
| Context harness | 控制 agent 当前能看到什么 |
| Tool harness | 控制 agent 能调用什么工具 |
| Memory harness | 控制长期记忆如何存、取、更新 |
| Curriculum harness | 控制学习路径与先修关系 |
| Evaluation harness | 检查输出是否达标 |
| Permission harness | 控制风险操作和权限 |
| Human-in-loop harness | 哪些决策必须人来拍板 |

两者的核心区别只有一句话：

> **Skill 化解决"会不会做"；Harness 化解决"什么时候做、按什么边界做、做完怎么验证、出错怎么纠偏"。**

一个没有 harness 的 skill，就像一名技术过硬但不受任何流程约束的员工：能力在，但不可靠。

---

## 二、名师 Skill 解决了"教什么"，但没解决"谁来决定教学路径"

教育场景是理解这套框架最好的切入点，也是最能暴露"只有 skill 不够"这个问题的地方。

如果只是把名师讲课方式做成 skill，系统仍然可能失败——因为学生教育不是单次问答，而是一个长期、动态、带目标约束的过程。今天的讲解再精彩，也解决不了"这个学生接下来应该学什么""他上周犯的错本周还在犯吗""他已经厌倦了这种提问方式"这类问题。

一个真正可用的学生 Agent 系统至少需要六层：

| 层级 | 功能 |
|---|---|
| 知识图谱层 | 记录课程知识点、先修关系、难度梯度 |
| 学生画像层 | 记录学生已掌握、未掌握、误区、兴趣、学习风格 |
| 教学 skill 层 | 名师讲解、错题分析、类比解释、苏格拉底提问 |
| 学习路径层 | 决定今天学什么、复习什么、跳过什么 |
| 记忆层 | 记录学生长期表现、情绪、偏好、历史错误 |
| 评估层 | 用小测、迁移题、复述、间隔复习判断是否真正掌握 |

这和已有研究方向是对齐的。Deep Knowledge Tracing 用神经网络建模学生在课程交互中的知识状态，目标就是根据学生历史行为推断当前掌握情况。近年的 TutorLLM 方向则进一步把 Knowledge Tracing 与 RAG 结合，用学生当前状态动态检索内容并生成个性化学习建议。CLASS 框架强调通过 step-by-step guidance 和用户反馈构建更自然的智能辅导系统；Google 的 Guided Learning 也强调通过提问、逐步引导和 quiz 促进主动学习，而不是简单给出答案。

这些研究都指向同一个结论，一个教育 agent 的核心问题不是"答案更准"，而是：

> **能否长期追踪一个人的知识状态，并持续选择最合适的下一步学习动作。**

名师 skill 解决了单次交互的质量，而第二至第六层——学生画像、学习路径、记忆、评估——才是让教育持续有效的 harness 基础设施。谁掌握这六层的数据和控制权，谁就掌握了真正的教育护城河。

---

## 三、超长周期 Agent：从"会话助手"到"终身认知操作系统"

这是整套框架里最难被单纯"堆 skill"解决的部分。

普通 chatbot 是 session-based 的：这次聊完，下次基本重来。两次对话之间，系统对你一无所知。

超长周期 Agent 是 life-cycle-based 的：它要知道你是谁、你经历过什么、你学过什么、忘记了什么、长期目标是什么、哪些能力正在形成、哪些偏差需要纠正。它不是你的工具，更像是一个持续运行的认知伴侣——只要你允许，它对你的了解会随着时间加深，而不是每次对话后归零。

这个系统需要四类记忆：

| 记忆类型 | 内容 |
|---|---|
| Episodic memory | 你昨天做了什么题、哪次考试错在哪里 |
| Semantic memory | 你已经掌握的知识、概念网络 |
| Procedural memory | 你做题、写作、研究、沟通的习惯模式 |
| Preference / identity memory | 你的兴趣、价值观、风格、长期目标 |

这一点和 MemoryBank、MemGPT、Generative Agents 等研究高度相关。MemoryBank 研究的是让 LLM 具备长期记忆、持续更新用户画像，并根据过去交互适应用户个性。MemGPT 则把 LLM 的上下文限制类比为操作系统内存管理问题，通过 fast/slow memory 和虚拟上下文机制扩展长期交互能力。Generative Agents 则展示了带有记忆、反思、计划能力的 agent 如何产生更连续、更可信的行为。

但这些研究都在解决一个共同的难点——长期记忆并不难"存"，难的是：

> **如何在正确时刻取出正确记忆，并把它转化成正确行动。**

Anthropic 的 context engineering 文档强调，context 不是无限资源，长上下文会带来注意力预算和 context rot 问题，因此长期任务需要 compaction、structured note-taking、multi-agent architecture、just-in-time retrieval 等技术。存储不是瓶颈，检索和利用才是。

因此，超长周期 Agent 的技术核心可以写成：

```
Long-Horizon Agent
= Long-term Memory
+ Context Router
+ Skill Library
+ Planning System
+ Evaluation Harness
+ Human Governance
+ Periodic Reflection / Compression
```

对应教育场景，就是：

```
Student Lifetime Agent
= 学生长期画像
+ 知识状态追踪
+ 课程知识图谱
+ 名师教学 skills
+ 个性化学习路径
+ 错题与误区记忆
+ 元学习训练
+ 家长/老师/学生三方治理
```

Second Me 类项目强调建立一个开放、隐私保护、能保存和表达个人上下文的 AI self；相关 Memory 2.0 思路则试图让记忆不只是静态存储，而是能生成上下文感知响应、预填信息、对接外部系统。这个方向仍然很早期，但它指向的问题已经很清楚：**谁来存储你的长期认知数据，谁就掌握了你的认知延伸。**

---

## 四、Skill 会被模型吸收，但不会全部消失在权重里

一个常见的问题是：随着模型越来越强，是不是所有外部 skill 都会被吸进权重，最终变得不再必要？

答案是：部分会，部分不会。

现在很多 skill 是外部写的：prompt、workflow、tool calling、evaluation、examples。

但随着这些 skill 被大量使用，会产生高质量轨迹数据：

```
专家流程 → agent 执行轨迹 → 成功/失败 evals → 数据集 → 微调/蒸馏/RL → 模型内化能力
```

这和知识蒸馏方向是一致的。"Distilling Step-by-Step" 研究使用大模型生成的 rationale 作为额外监督信号，训练更小的任务模型，并降低对人工标注数据的需求。Voyager 也展示了一个 LLM agent 如何在 Minecraft 中通过自动课程、可增长 skill library 和 iterative prompting 不断积累能力。

### 4.2 为什么不会全部内化？

因为很多能力不适合放进模型权重里。

| 不适合完全内化的内容 | 原因 |
|---|---|
| 最新知识 | 权重训练有滞后，需要 retrieval |
| 私有流程 | 企业内部流程不能公开训练 |
| 个人记忆 | 属于用户隐私，不应进入公共模型 |
| 工具操作 | 需要实时 API、权限、环境状态 |
| 高风险决策 | 需要审计、责任和 human-in-loop |
| 快速变化规范 | 外部 skill 更新比重新训练更快 |

所以，未来不是"所有 skill 都进模型"，而是三种能力形态并存：

```
1. 内化能力：进入模型权重
2. 外挂能力：以 skill / tool / workflow 形式存在
3. 组织能力：存在于 harness / eval / governance / human decision 中
```

模型规模和训练计算确实长期呈现可预测的 scaling trend。Kaplan 等人的 scaling laws 研究显示，语言模型损失会随模型规模、数据和计算量按幂律变化；Chinchilla 进一步指出 compute-optimal training 中模型大小和训练 token 数量应平衡扩展。但这并不等于"无限进化"没有瓶颈，现实瓶颈包括数据质量、推理成本、对齐、安全、长期记忆、现实世界反馈、工具可靠性和责任归属。

### 4.3 任务结构被拆解，而不是职业按名称消失

> **未来相当大比例的"可形式化、可评估、重复率高、反馈周期短"的人类任务，会被模型、skill 和 harness 系统吸收；但"任务被影响"不等于"职业完全消失"。**

OpenAI / UPenn 的 "GPTs are GPTs" 研究估计，美国约 80% 劳动力至少有 10% 工作任务可能受 LLM 影响，约 19% 劳动力可能有至少 50% 任务受影响。Yale Budget Lab 也提醒，occupational exposure 不等于岗位一定被自动化消灭，只是说明这些岗位更可能受到影响。

更精确的说法是：

```
岗位不会按职业名称消失，
而是按任务结构被拆解、重组、自动化、增强。
```

人类保留价值的位置会更集中在：责任承担、价值判断、审美与品味、信任关系、稀缺身份/IP、资源调度、前沿问题定义、高风险拍板、新范式创造。

未来稀缺的不是"会做某项标准技能的人"，而是**拥有不可替代的判断、身份、责任、信任或前沿创造力的人**。

---

## 五、AI 不会自动让学生变强：主动蒸馏者与被动依赖者的差距只会越来越大

很多人以为，AI 让教育变公平了——人人都有一个不睡觉的家教。但这个判断忽略了一件事：同样拥有一个好老师，有人学成了，有人学坏了。关键不在于老师，而在于学生怎么使用这个老师。

分化会发生在两种截然不同的使用方式上：

### 5.1 第一类：被动依赖型

这种学生把 LLM 当答案机器：

```
不会 → 问模型 → 复制答案 → 完成任务
```

结果是：表面效率提高，真实能力不增长，元认知下降，遇到新问题无法独立迁移，长期被 agent 反向弱化。

一些研究已经开始讨论 AI assistant 可能带来的 cognitive passivity，即用户在默认获得完整答案时，可能减少自己推理和形成领域素养的机会。

### 5.2 第二类：主动蒸馏型，也就是 LLM2Human Distillation

这类学生把 LLM 当"外部专家脑"，但目标不是拿答案，而是把模型的专家过程蒸馏进自己脑子里。

**LLM2Human Distillation** 定义为：

> **人类主动从 LLM 的解释、推理、纠错、类比、题目生成和反馈中提取认知结构，并通过复述、迁移、练习、反思和间隔复习，把外部智能转化为自己的长期能力。**

它的标准流程可以是：

```
1. Observe：看模型如何解决问题
2. Decompose：拆解步骤、概念、判断点
3. Self-explain：用自己的话解释
4. Reconstruct：关掉模型，独立重做
5. Transfer：换一道变式题迁移
6. Error audit：让模型指出错误类型
7. Retrieval：隔天/隔周主动回忆
8. Teach-back：把知识讲给别人或讲给模型听
```

这和学习科学中的 self-regulated learning、metacognition、retrieval practice 是一致的。Zimmerman 的自我调节学习模型强调学习者需要设定目标、选择策略、监控进度、管理时间、评估结果，并根据反馈调整未来学习方法。Dunlosky 等人的综述也指出，practice testing 和 distributed practice 是高效学习技术，而单纯 rereading 和 highlighting 的效果较低。

因此，Agent 时代的教育分化，本质上是：

```
AI as Answer Machine  → 能力萎缩
AI as Cognitive Coach → 能力跃迁
```

---

## 六、元学习：AI 时代唯一不会被压缩掉的竞争力

普通 skill 是"如何做一道题、写一篇文章、完成一个任务"。

Meta skill 是"如何快速获得一个新 skill"。

> **Meta skill 是对学习过程本身的建模、监控、优化和迁移能力。**

OECD / EEF 关于 meta-learning 的材料把它描述为学习者对自身感知、探究、学习和成长习惯的觉察与控制；metacognition 则是对自身内部过程的觉察、反思和表达。

两个核心 meta-skill 值得重点设计。

### 6.1 Meta Skill A：快速进入一个领域

这个 skill 的目标不是"马上成为专家"，而是在最短时间内建立一个领域的导航系统。

**输入**

```
领域名称 + 学习目标 + 当前水平 + 时间预算
```

**输出**

```
领域地图 + 核心概念 + 先修知识 + 经典问题 + 学习路径 + 练习任务
```

**执行流程**

```
Step 1：定义领域边界
  - 这个领域解决什么问题？
  - 它和相邻领域的区别是什么？
  - 典型产出是什么？

Step 2：建立概念地图
  - 10 个核心概念
  - 5 个常见误区
  - 3 个底层原理
  - 关键术语表

Step 3：识别先修知识
  - 哪些数学/语言/工具/背景必须先补？
  - 哪些可以边学边查？

Step 4：找领域中的"压缩入口"
  - 一本经典教材
  - 三篇综述论文
  - 五个代表性案例
  - 一个可复现项目

Step 5：构造 30/60/90 天路径
  - 第 30 天：能读懂基础材料
  - 第 60 天：能复现典型任务
  - 第 90 天：能提出自己的问题

Step 6：建立反馈循环
  - 每周小测
  - 每周复盘
  - 每两周一次迁移任务
```

这个 skill 的重点是：**先建立结构，再填充细节**。

### 6.2 Meta Skill B：理解晦涩知识

很多难知识不是因为"信息不够"，而是因为前置概念缺失、抽象层级太高、缺少例子、符号系统陌生。

```
Step 1：定位卡点
  - 是术语不懂？
  - 是数学形式不懂？
  - 是背景知识不懂？
  - 是逻辑跳跃太大？
  - 是没有具体例子？

Step 2：降维解释
  - 用儿童版解释
  - 用高中生版解释
  - 用领域入门版解释
  - 用专家版解释

Step 3：例子优先
  - 先给具体例子
  - 再抽象成规则
  - 再给反例
  - 最后回到形式化表达

Step 4：构建前置知识清单
  - 理解这个概念必须先懂哪 5 个东西？

Step 5：生成最小练习集
  - 3 道基础题
  - 3 道变式题
  - 1 道迁移题
  - 1 道反例判断题

Step 6：Teach-back
  - 学生必须用自己的话解释
  - 模型判断是否真正理解
```

这比"请解释一下"强很多，因为它把理解过程本身 harness 化了。

---

## 七、Prompt 是行为宪法，但光有宪法不够：稳定 Agent 需要五层约束

把 Claude Code / Agent SDK 的 override system prompt 类比为《三体》里的"思想钢印"，这个比喻很有启发，但需要加一个边界：

> **System prompt 可以强烈塑造 agent 的行为倾向，但它不是绝对控制。真正稳定的"思想钢印"必须由 system prompt + tool permissions + evals + memory policy + runtime harness 共同构成。**

Anthropic 文档说明，Claude Code / Agent SDK 里有几种方式修改系统行为：output styles、append to Claude Code prompt，以及 fully custom prompt。system prompt 会塑造工具使用、代码风格、语气、安全、环境上下文等行为。自定义 `systemPrompt` 可以完全替换默认 prompt，但如果这样做，默认工具、内置安全和环境上下文也需要显式补回。

所以它不是"覆盖一切底层约束"的万能开关，更像是：

```
行为宪法层：你是谁、你的目标是什么、你绝不做什么
操作策略层：面对任务如何分解、调用工具、检查结果
约束执行层：权限、eval、审计、回滚、人类确认
```

如果只靠 prompt，就容易被上下文污染、prompt injection、目标漂移影响。

如果把它做成完整 harness，则更接近真正的"思想钢印"：

```
Prompt       = 价值观与角色定义
Memory       = 长期身份连续性
Tools        = 行动能力边界
Evals        = 行为是否合格
Permissions  = 什么不能做
Human Review = 最终责任归属
```

在教育 agent 里，这很重要。一个儿童 lifelong agent 的"思想钢印"不应该只是：

```
你是一个友善的学习助手。
```

而应该是：

```
你的第一目标不是替学生完成任务，而是提高学生的长期独立能力。
当学生请求答案时，优先进行引导、提问、拆解和检查。
只有在学生多次尝试后，才允许展示完整答案。
你必须记录学生误区，但不得制造羞辱感。
你必须保护学生隐私。
你不得操纵学生形成非自主依赖。
```

这才是教育 agent 的真正系统边界。

---

## 八、Agent 不会消灭顶尖人类，它会把前沿的入口往下移

> **Agent 时代不会消灭顶尖人类，反而可能放大顶尖人类。因为 agent 会压缩通识学习时间，降低进入复杂领域的门槛，让高天赋、高主动性的人更早接触前沿问题。**

但这里要注意：教育不只是知识传输，还包括心智成熟、社会化、身体发展、情绪调节、价值形成和长期动机建设。

更稳健的表述是：

```
对高天赋、高主动性、拥有优质 agent 与家庭/学校支持的学生，
通识知识获取速度可能大幅提升；
但完整人的成长不可能完全被压缩为知识传输。
```

真正被加速的是：资料检索、概念解释、练习生成、错误反馈、跨学科迁移、论文阅读、实验设计、编程实现、数学推导辅助。

难以被完全替代的是：提出真正重要的问题、判断什么方向值得追、建立新范式、承担失败成本、形成原创审美、建立科学共同体信任、对现实世界做高风险决策。

所以，在科学前沿，人类的角色会从"知识搬运工"转向：

```
问题选择者
范式创造者
实验方向设计者
价值判断者
责任承担者
```

---

## 九、下一个真正的教育平台：不是 AI 家教，而是儿童认知操作系统

从以上分析出发，可以推演出一个非常清晰的产品方向：

```
Personal Cognitive Operating System for Children
儿童个人认知操作系统
```

核心功能不是"AI 家教"，而是：

| 模块 | 功能 |
|---|---|
| 知识追踪 | 记录所有学科掌握度 |
| 认知画像 | 识别孩子的推理风格、兴趣、误区 |
| 学习路径 | 动态规划每日/每周学习任务 |
| 元学习训练 | 教孩子如何学习、如何复盘 |
| 情绪与动机 | 检测挫败、倦怠、过度依赖 |
| 家长仪表盘 | 给家长看趋势，不是监控细节 |
| 老师协同 | 让人类老师查看 agent 总结 |
| 隐私治理 | 明确哪些数据可存、可删、可共享 |
| Talent acceleration | 对高天赋儿童提前开放高阶内容 |
| Human review | 关键教育决策由人类确认 |

商业上可能出现三种形态：

1. **富人家庭版**：极高客单价，深度定制，覆盖学习、阅读、科研、语言、艺术、运动。
2. **学校 SaaS 版**：面向老师，提高班级内个性化教学能力。
3. **Skill Marketplace 版**：名师、科学家、艺术家、工程师把自己的教学法打包成 skill 出售。

这里真正的护城河不是模型本身，而是：

```
高质量学生长期数据
+ 名师 skill library
+ 学科知识图谱
+ 学习路径 harness
+ 家长/老师 trust layer
+ 安全与隐私治理
```

---

## 十、结语：稀缺的从来不是技能，而是能设计技能的人

Agent 时代最容易被误读的变化，不是"模型替代人"，而是一次更深的重新编码：**人类的能力结构本身，正在被改写。**

职业能力会先被 skill 化——蒸馏成可调用的能力包；再被 harness 化——放进可控、可验证、可长期运行的系统；随后一部分进入模型权重，一部分以外部工具与流程的形式留存。与此同时，教育系统会从统一课程演化成个体生命周期 agent——每个人拥有自己的知识追踪、学习路径、元学习训练和长期记忆。由此产生的分化，不是"会不会用 AI"，而是能否把 AI 的能力蒸馏进自身，形成 LLM2Human Distillation。

这不是一个孤立的技术趋势，而是一条完整的链条：

```
Skill 化：把专家能力封装。
Harness 化：把能力放进可控系统。
Long-horizon Agent：把系统绑定到人的长期成长。
元学习：让人学会学习。
LLM2Human Distillation：让人从 AI 中反向吸收能力。
五层约束：让 agent 的行为目标稳定化。
教育分化：主动蒸馏者进化，被动依赖者退化。
```

从能力的封装，到系统的约束，再到人的成长，最终到 agent 时代人类价值的重新定位——这条链条的每一环都很重要，但最终的判断可以用一句话来收：

> **真正稀缺的，从来不是普通技能本身，而是能设计 skill、构建 harness、训练元学习、驾驭长期 agent、提出前沿问题并承担责任的人。**

换一种表达方式：**在 AI 大规模压缩执行层的时代，稀缺的是会出题的人，而不是会答题的人。**

---

## 参考文献

- [Skills \| OpenAI API](https://platform.openai.com/docs/guides/tools-skills)
- [Testing Agent Skills Systematically with Evals \| OpenAI Developers](https://developers.openai.com/blog/eval-skills)
- [Harness engineering: leveraging Codex in an agent-first world \| OpenAI](https://openai.com/index/harness-engineering/)
- [Effective context engineering for AI agents \| Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Modifying system prompts - Claude Code Docs](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)
- [Introducing the Model Context Protocol \| Anthropic](https://www.anthropic.com/news/model-context-protocol)
- [Deep Knowledge Tracing (arXiv:1506.05908)](https://arxiv.org/abs/1506.05908)
- [TutorLLM: Customizing Learning Recommendations (arXiv:2502.15709)](https://arxiv.org/html/2502.15709v2)
- [CLASS: A Design Framework for Intelligent Tutoring Systems (arXiv:2305.13272)](https://arxiv.org/abs/2305.13272)
- [Guided Learning in Gemini \| blog.google](https://blog.google/products-and-platforms/products/education/guided-learning/)
- [MemoryBank: Enhancing Large Language Models with Long-Term Memory (arXiv:2305.10250)](https://arxiv.org/abs/2305.10250)
- [MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560)
- [Generative Agents: Interactive Simulacra of Human Behavior (arXiv:2304.03442)](https://arxiv.org/abs/2304.03442)
- [AI-native Memory 2.0: Second Me (arXiv:2503.08102)](https://arxiv.org/html/2503.08102v2)
- [Distilling Step-by-Step! (arXiv:2305.02301)](https://arxiv.org/abs/2305.02301)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models (arXiv:2305.16291)](https://arxiv.org/html/2305.16291)
- [Scaling Laws for Neural Language Models (arXiv:2001.08361)](https://arxiv.org/abs/2001.08361)
- [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of LLMs (arXiv:2303.10130)](https://arxiv.org/abs/2303.10130)
- [Labor Market AI Exposure: What Do We Know? \| The Budget Lab](https://budgetlab.yale.edu/research/labor-market-ai-exposure-what-do-we-know)
- [Disrupting Cognitive Passivity: Rethinking AI-Assisted Data... (arXiv:2604.02783)](https://arxiv.org/html/2604.02783v1)
- [Improving Students' Learning With Effective Learning Techniques \| Dunlosky et al. (2013)](https://journals.sagepub.com/doi/abs/10.1177/1529100612453266)
- [Meta-learning \| OECD Learning Compass](https://www.oecd.org/content/dam/oecd/en/topics/policy-issues/future-of-education-and-skills/learning-compass-constructs/Meta-learning.pdf)

## 引用

若想引用本文，请使用：

```bibtex
@misc{dong2026skillharness,
    author = {Dong, Peijie},
    title = {Skill 化、Harness 化与长期智能系统：AI 时代的能力重新编码},
    year = {2026},
    month = apr,
    day = {29},
    howpublished = {\url{https://pprp.github.io/tech/skill-harness-agent/}},
    url = {https://pprp.github.io/tech/skill-harness-agent/},
    urldate = {2026-04-29},
    note = {Blog post. Accessed: 2026-04-29},
    language = {Chinese}
}
```
