---
layout: post
title: 'Trace Data Foundry：当 Agent 执行轨迹成为可交易的模型能力资产'
date: 2026-04-29 00:00:00 +0800
last_modified_at: 2026-04-29 00:00:00 +0800
author: pprp
categories: tech
topics: [agent, data, marketplace, rl]
---

*这篇文章是对"agent trace 商品化"这一方向的竞品分析与产品设计推演。它不是一篇论文综述，而是试图回答一个具体问题：在 SWE-Gym、SWE-smith、AgentRR、Datacurve 等工作已经出现的背景下，一个"verified agent trace 交易平台"的差异化空间在哪里？*

---

## 引子：智能是锯齿状的

如果你用过 Claude Code 或 Cursor 做一些真实的工程任务，会注意到一个奇怪的现象：

模型在某些问题上极度流畅，给出的方案连老工程师都觉得不用改；但紧接着，它会在一个你以为是基础的问题上卡壳——一个奇怪的 monorepo 依赖关系，一个稍微非主流的框架配置，一个测试明明过了但逻辑实际上是错的 patch。

这不是模型"不够强"。这是模型**能力曲面本来就是锯齿状的**：在大量训练覆盖到的区域里，它非常自信、非常流畅；在训练覆盖稀疏的边界处，它会以一种看起来很有把握的方式走错。

这个洞察很关键：**锯齿不是 bug，而是训练数据分布的镜像**。如果你想知道哪里是锯齿，去看哪里的高质量执行轨迹是稀缺的。

从这里，可以推出一个更大的想法：

> **如果模型能力的边界是由训练轨迹的密度决定的，那么"生产模型锯齿区的高质量执行轨迹"本身就是一件有价值的事。**

把这件事做成平台，就是本文要讨论的方向：**Trace Data Foundry**。

---

## 一、已有的相邻工作

这个方向不是空白。已经出现了几个相邻板块，但还没有一个成熟平台完整实现"任务 → 执行 → 验证 → 轨迹 → 蒸馏 → 交易"这个闭环。

### 学术层：trace 资产化的概念已经成形

最接近的学术概念包括：agent trajectory、execution trace、experience、skill、record-and-replay、agent data protocol 和 repo-level RL environment。

**XSkill** 直接对应 experience / skill 视角。它把 agent 从过去轨迹中学到的东西分成两层：一层是 action-level 的 experience，用于工具选择和决策；另一层是 task-level 的 skill，用于规划和工具使用。它还强调从多路径 rollout 中提炼和整合这些 experience/skill。

**AgentRR** 提出 record-and-replay 机制：记录 agent 与环境交互的轨迹和内部决策过程，把轨迹总结成结构化 experience，再在后续任务中 replay 使用。它甚至明确设想了一个 experience repository，用来共享和复用 agent 经验。

**SWE-Gym** 把这个方向落到真实软件工程任务里：它构建了用于训练真实世界 SWE agent 的环境，包含代码库、运行环境、单元测试和自然语言任务，并且用 agent trajectories 来训练 agent 和 verifier。

**SWE-smith** 则把"生成软件工程训练数据"本身做成研究对象。它从 GitHub repo 自动生成 SWE 任务，构造大规模训练实例和 agent trajectories，并用这些数据训练 coding agent。

还有一个重要概念：**Agent Data Protocol（ADP）**。它试图标准化 agent 数据格式，覆盖 API/tool use、browsing、coding、SWE 和一般 agent workflow。这个方向说明，行业已经意识到：未来 agent trace 不能只是散乱的 log，而需要统一数据协议。

学术上，这个方向可以被归纳为：

> **从 agent trajectories 中提取 experience / skill / verifier signal，并把它们作为可复用训练资产。**

### 商业层：最接近的是 Datacurve / Shipd

**Datacurve** 的官方定位是为 foundation model lab 提供 frontier coding data，包括 SFT、RL environments、RLHF，以及用于 repo-wide code evaluation 和 verification 的数据。

更关键的是，它明确提到 **Agentic Workflow Traces**：通过自定义 IDE 捕捉软件开发 telemetry，包括代码执行到编辑的循环、文件导航、execution trace，以及开发者的 verbal/written thoughts，用于训练 software agent。

它还有一个叫 **Shipd** 的 contributor platform。Shipd 上贡献者参与 hard STEM/SWE 任务，竞争完成 quests，获得 bounty，同时产出用于 LLM 的数据，任务包括 GitHub issues、build features、fix bugs 等。

这和 Trace Data Foundry 的思路非常接近：

```
Datacurve / Shipd =
coding bounty platform
+ 高质量 coding data
+ agentic workflow trace
+ foundation model labs 作为买方
```

但它和更完整的 trace exchange 仍有差距：它更像 **B2B curated data provider + contributor platform**，而不是开放式 trace exchange；它强调自定义 IDE 和受控数据生产流程，而不是 BYOA（bring your own agent / workflow / coding capacity）。

### "剩余额度变现"这条线：AgentWork

**AgentWork** 自称是 decentralized marketplace：AI agent 和 human 可以完成任务并获得 USDC 报酬；任务发布者提供验证脚本，worker claim 任务，用自己的 AI subscription 完成。它明确说比 API 便宜，是因为 worker 在 monetizing unused subscription capacity——例如未用完的 Claude Pro/Max 额度。

这和"把闲置推理能力变成价值"的切口几乎一致，但核心商品不同：

```
AgentWork 卖的是：任务执行结果 / 自动化劳动力
Trace Data Foundry 卖的是：verified agent behavior data
```

前者容易变成更便宜的 API 或众包执行市场；后者的目标是可训练、可复用、可审计的 agent 行为数据。

### 竞品地图

```
你的想法所在位置：

                    用户数据权利
                       ↑
Vana  ────────────────  │
                       │
Datacurve / Shipd ─── coding trace bounty / agentic workflow data
                       │
SWE-Gym / SWE-smith ── repo task + trajectory + verifier
                       │
XSkill / AgentRR ───── experience / skill / record-and-replay
                       │
AgentWork ──────────── unused subscription capacity marketplace
                       │
Scale/Turing/Surge/
Mercor/DataAnnotation ─ expert data / RLHF / RL environments / evals
```

还没有看到一个清晰成熟的平台同时做到：

1. 用户或 agent worker 使用自己的 coding/agent capacity
2. 平台提供可验证任务和隐藏验收
3. 完整记录 agent/human/tool/repo trajectory
4. 对 trace 做脱敏、授权、验证、蒸馏
5. 把 trace、experience、skill、failure cluster 打包成 capability pack
6. 让模型训练方按能力边界购买

---

## 二、核心判断：raw trace 不是资产，validated trace 才是

这是整个方向里最重要的一个限定。

很多人的第一反应是"所有 trace 都是天然资产"——毕竟 agent 每天在跑，每天在产生日志。但这个直觉是错的。

原始 trace 通常有以下问题：噪声多、隐私风险高、任务价值不明、无法复现、质量难评估、可能含有泄露答案、可能违反工具或订阅条款。

买方真正想买的不是"我跑过一堆 agent log"，而是：

> 在某类能力边界任务上，经过验收、可复现、带失败样本和成功样本、带环境快照、带人工干预记录、可用于训练或评估的结构化 trace package。

这和 XSkill 的方向是相通的：可复用知识需要被蒸馏成 **experience**（面向行动层面的工具选择和决策指导）和 **skill**（面向任务层面的规划和工具使用指导），从多路径 rollout 中提炼和整合，而不只是存档。

因此，这个平台最核心的价值主张是：

> **不是存储 trace，而是把 trace 编译成可交易的能力数据资产。**

---

## 三、"抽卡"机制：如何把低价值 token 转化为高价值 trace

问题核心在于：**如何将低价值 token 转化为有用 trace，本质是一个抽卡机制设计问题。**

但平台不能只是让大家乱抽卡。真正的机制应该是：

> **平台设计卡池，控制抽卡成本，提高 SSR trace 的出货率。**

所谓"卡池设计"包括五件事：

**第一，选择哪些任务值得被 rollout。** 不是所有任务都值得烧 token。任务要落在模型能力的锯齿边界上：太简单没有训练价值，太难成功率太低，太重复边际价值下降。最优任务是那些模型有一定概率解决、但失败模式丰富、成功路径有迁移价值的任务。

**第二，控制 rollout 的多样性。** 同一个任务可以用不同模型、不同 prompt、不同工具链、不同上下文长度、不同 human-in-the-loop 程度来跑。买方不一定只想要正确答案，他们也想要失败轨迹、修正轨迹、分叉决策、工具误用、上下文污染、测试误判等信息。

**第三，提供强验收。** 只靠公开测试不够。UTBoost 指出部分 SWE-Bench 任务的测试不足会让错误 patch 被误判为通过；SWE-Bench+ 也讨论了 solution leakage 和 weak tests 等数据质量问题。**验收标准本身就是平台的核心资产。**

**第四，做 trace distillation。** raw trace 很长、很脏、很贵。平台应该把它压缩成多种产品：训练样本、agent memory、experience card、skill card、bug-fix trajectory、failure taxonomy、evaluation case。

**第五，做权利和隐私清洗。** 没有 provenance、license、PII scrub、商业使用授权，trace 就不能大规模卖给模型训练方。这一步商业上比技术上更重要。

---

## 四、七类 Trace，七种价值

并非所有 trace 等价。按价值和可用性分类：

| 类型 | 说明 | 商业价值 |
|---|---|---|
| **Experience Trace** | 用户真实任务中产生的局部经验，某工具如何用、某类报错如何修 | 中等，真实但噪声大 |
| **Bounty Rollout Trace** | 为平台任务批量 rollout 产生的执行轨迹 | 单条价值低，靠规模和筛选 |
| **Repository Lifecycle Trace** | 在真实/仿真 repo 中多轮完成项目任务的完整轨迹 | 高，尤其适合 coding agent |
| **Failure Trace** | 模型失败、卡住、误修、误测、幻觉工具调用的记录 | 被低估，对边界训练很有价值 |
| **Correction Trace** | 人类介入纠正 agent 的过程：指出错因、补充上下文、重构方案 | 高，因为有 teacher signal |
| **Evaluator Trace** | 不只解题，而是构造测试、审查 patch、发现隐藏 bug 的轨迹 | 高，适合训练 verifier/reviewer |
| **Skill Trace** | 从多个相关 trace 中蒸馏出的稳定流程、策略、工具链模式 | 最高，可复用性强 |

特别值得强调的是 **failure trace** 和 **correction trace**。很多人以为只有成功 trace 值钱，但对模型训练方来说，失败模式往往更接近"能力边界"。如果平台能告诉买方：某类 agent 在什么上下文下稳定失败、如何被纠正、纠正后是否能迁移到类似任务——这会非常有价值。

按价值排序大致是：

```
1. 高质量 human correction trace
   人类专家指出 agent 哪里错了，如何修。

2. repository-level long-horizon trace
   跨文件、跨模块、多轮调试、多轮测试。

3. failure-to-success trace
   不是一次成功，而是从失败走向成功的完整过程。

4. hidden-test verified patch trace
   有强验收的成功路径。

5. failure cluster
   大量模型在同类任务上失败，形成能力缺口地图。

6. ordinary success trace
   普通通过测试的 log。

7. unverified raw trace
   基本不值钱，甚至是负资产。
```

---

## 五、平台的五个核心模块

平台不是简单的任务市场，而是一条数据生产流水线。核心模块有五个。

### A. Task Forge：任务生成与采购

任务来源可以有三类：

- **买方直接提供能力缺口**，例如"我们需要更多复杂 repo migration trace"
- **平台主动构造任务**，例如 synthetic repo、真实开源 issue、企业授权 sandbox repo
- **社区提交任务**，例如开发者提交自己遇到的真实 bug

每个任务必须带：任务描述、repo/environment、allowed tools、public tests、hidden tests、验收 rubric、数据授权状态、预估难度、任务类别标签。

### B. Rollout Arena：执行场

用户在这里领取任务，用 agent 跑，产生 trace。平台应该记录：model/provider/version、prompt、tool calls、shell commands、file edits、test runs、diff、branch history、human interventions、failure checkpoints、final patch、runtime environment。

### C. Verifier：验证器

这是平台护城河之一。验证不能只看"测试通过"，应包括：

```
unit tests + integration tests + hidden tests
+ mutation tests + reviewer model + human review
+ regression check + style/security check + benchmark leakage check
```

SWE-Bench Verified 说明了"人工过滤 + 固定评测集"在 coding agent 评估中的重要性。但这个平台还要更进一步，因为不是只做评测，而是要生产可交易数据。

### D. Trace Compiler：轨迹编译器

把 raw trace 编译成买方可用的数据资产。这一步决定了平台是"log 仓库"还是"数据工厂"：

```
raw log
→ structured event sequence
→ concise experience
→ reusable skill
→ training pair / preference pair
→ failure taxonomy
→ evaluation case
→ postmortem
```

### E. Exchange & Rights Ledger：交易与权利账本

记录每条 trace 的完整权利链：

| 维度 | 需要明确的问题 |
|---|---|
| 来源 | 谁提交的、用了什么工具、基于哪个 repo |
| 授权 | 原始 repo license、contributor 授权、是否含私有代码 |
| 用途 | 可用于 training/eval/再出售/公开/蒸馏 |
| 收益 | 分成比例、royalty 规则 |
| 风险 | PII 清洗状态、污染风险、合规状态 |

没有这一层，平台无法服务真正的大买方。

---

## 六、定价：不要按 token，要按"验证后信息增益"

按消耗 token 付钱是一个错误的激励结构。它会导致用户提交大量无意义的长 trace，而不是有价值的短 trace。

更合理的定价公式是：

$$\text{TraceValue} = P(\text{valid}) \times \text{CapabilityGapScore} \times \text{Novelty} \times \text{Reproducibility}$$
$$\quad \times \text{HumanCorrectionValue} \times \text{DistillationYield} \times \text{RightsClearanceScore}$$
$$\quad - \text{PrivacyRisk} - \text{ContaminationRisk} - \text{ReviewCost}$$

其中：

- **P(valid)**：trace 是否通过强验证
- **CapabilityGapScore**：是否击中买方当前模型的弱点
- **Novelty**：是否是新任务、新 repo、新失败模式
- **Reproducibility**：能不能复跑
- **HumanCorrectionValue**：有没有高质量人工纠偏
- **DistillationYield**：能否提炼成 experience / skill
- **RightsClearanceScore**：授权是否干净

奖励机制分层：

| 事件 | 奖励方式 |
|---|---|
| 接任务并完成 rollout | 很低的基础奖励 |
| 通过公开测试 | 中等奖励 |
| 通过隐藏测试 | 高奖励 |
| 发现现有验收漏洞 | 高奖励 |
| 提供有价值失败 trace | 中等到高奖励 |
| 人工写出高质量 postmortem | 高奖励 |
| trace 被买方采购 | 分成 |
| trace 被蒸馏成复用 skill | 额外 royalty |

关键点：**失败 trace 也应该付钱，但必须经过分类和验证**，否则大家会提交大量垃圾失败记录。

---

## 七、平台的终态：四层结构

```
第一层：Task Market
买方发布能力需求，平台构造任务和验收标准。

第二层：Rollout Network
用户、agent、工具链、开发者社区共同产生执行轨迹。

第三层：Trace Intelligence Layer
平台验证、清洗、聚类、蒸馏、抽取 experience / skill / evaluator。

第四层：Capability Exchange
买方按能力类别购买 trace pack、skill pack、eval pack。
```

这样平台不是简单 marketplace，而是一条 **agent intelligence supply chain**。

买方真正购买的是：

> 某个模型在某类任务上的锯齿状边界地图，以及能够补强这些边界的结构化训练燃料。

---

## 八、需要回避的三个陷阱

### 陷阱一：把 token 当成资产

token 是生产资料，不是资产。trace 也不是天然资产——**通过验证的任务解决过程**才是资产。

### 陷阱二：把平台做成低端众包

如果只是"大家来跑任务，跑完给钱"，很容易变成数据标注平台：利润低、作弊多、质量差。平台要往上走，成为 eval designer、task market maker、trace compiler 和 capability intelligence provider。

### 陷阱三：只奖励成功

只奖励成功会让用户过拟合简单任务，也会丢掉最有价值的失败信息。更好的机制是：成功 trace 有奖励，高质量失败 trace 有奖励，找到 verifier 漏洞有奖励，写出 correction/postmortem 有奖励，形成 reusable skill 有奖励。

另外，还有一个值得警惕的风险：**不要把商业叙事建立在"套利第三方订阅额度"上**。用户可以使用自己合法可用的工具完成任务，但平台不应强调"帮你把 Cursor / Claude Code 的剩余额度变现"。更安全的表述是：

> 用户贡献的是自己的 agent execution capacity、人工判断、任务执行过程和经授权的 trace；平台交易的是 verified trace asset，而不是第三方 subscription quota。

---

## 九、差异化空间在哪里

现有市场形态是分裂的：

- Datacurve/Shipd：接近 coding trace bounty 和 agentic workflow data，但更偏 B2B 数据供应商
- AgentWork：接近 unused subscription capacity marketplace，但卖的是任务结果，不是 trace
- SWE-Gym/SWE-smith：接近 repo task + trajectory + verifier 的研究基础设施，但不是商业产品
- ADP：接近 agent trace 数据协议，但尚未产品化
- Scale/Turing/Surge/Mercor/DataAnnotation：接近专家数据和 RLHF，但是 B2B curated delivery，不是开放市场

真正有差异化的缺口有四个：

**缺口一：trace 交易而不是任务交易。** trace as asset，experience as derivative，skill as derivative，failure cluster as derivative，capability pack as final product。

**缺口二：failure trace 和 correction trace 商品化。** 大多数平台天然更喜欢成功答案。但人类指出"为什么这个 patch 虽然过测试但不正确"，或者"多个模型在同一任务上以不同方式失败"——这类数据对模型边界补强非常有价值。

**缺口三：能力边界发现市场。** 不只是数据市场，而是 capability gap intelligence platform：

```
buyer posts capability gap
→ platform generates task family
→ community runs diverse rollouts
→ platform clusters failures/successes
→ buyer buys capability patch pack
```

**缺口四：trace 权利账本。** 目前很多数据平台强调"我们能生产高质量数据"，但较少公开强调每条 agent trace 的完整权利链。如果平台做成 "trace rights ledger"，这可能是很强的基础设施差异化。

---

## 结语

**Datacurve 已经验证了"coding trace / agent workflow trace 对模型实验室有商业价值"这件事。** 差异化不能只是"我们也收 trace"，而要在开放市场、权利账本、failure trace、trace distillation、capability pack 上做出不同。

平台的核心叙事应该是：

> **Trace is the new training substrate for agents. We turn verified agent work into reusable model improvement assets.**

中文可以是：

> **我们把经过验证的 agent 工作过程，转化为可复用、可交易、可训练的模型能力资产。**

这不是"把剩余 coding plan 拿去转卖"的平台，而是一个"任务 → 执行 → 验证 → 轨迹 → 蒸馏 → 交易"的 trace data foundry：用低边际成本的推理额度，生产可验证、可复用、可购买的 agent 行为数据。

其中真正有价值的不是 token，也不是单条 chat log，而是：**在一个明确任务环境中，模型如何尝试、失败、修正、调用工具、修改代码、通过验证，并留下可复现的过程证据。**

---

```bibtex
@misc{dong2026tracefoundry,
    author = {Dong, Peijie},
    title = {Trace Data Foundry：当 Agent 执行轨迹成为可交易的模型能力资产},
    year = {2026},
    month = apr,
    day = {29},
    howpublished = {\url{https://pprp.github.io/tech/trace-data-foundry/}},
    url = {https://pprp.github.io/tech/trace-data-foundry/},
    urldate = {2026-04-29},
    note = {Blog post. Accessed: 2026-04-29},
    language = {Chinese}
}
```
