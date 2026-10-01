---
permalink: /
title: ''
excerpt: ''
author_profile: true
homepage_style: bookish
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am **Peijie Dong** (董佩杰), a final-year Ph.D. candidate in the Data Science and Analytics Thrust at the Hong Kong University of Science and Technology (Guangzhou), advised by [Prof. Xiaowen Chu](https://sites.google.com/view/chuxiaowen) and [Prof. Junxian He](https://jxhe.github.io/). I am currently a research intern with the WorkBuddy/CodeBuddy Coding Agent team at Tencent CSIG, where I work on **post-training and evaluation for long-horizon coding agents**.


**Research Interests**

My research focuses on improving the ability of coding agents to solve long-horizon, repository-level software engineering tasks. I am particularly interested in transforming interaction trajectories and environment feedback into effective training signals. My current research interests include:

- Coding Agent Post-Training: Developing data and training recipes for coding agents, including trajectory curation, supervised fine-tuning, reinforcement learning, and reward design.
- Long-Horizon Agent Evaluation: Building benchmarks and agent harnesses to study planning, tool use, repository navigation, error recovery, and end-to-end task completion.
- Agent Data and Training-Evaluation Loops: Diagnosing behavioral failures from agent trajectories and translating them into targeted data, objectives, and evaluation signals.
- Efficient Large Language Models: Improving the efficiency of LLM training and inference through model compression, low-precision training, efficient architectures, and systems optimization.

My long-term goal is to build coding agents that can learn from complete interaction trajectories and reliably improve through real-world task feedback. I welcome discussions and collaborations on coding agents, post-training, evaluation, and efficient LLMs.

# 🔥 News

<div class="home-news" markdown="1">

- <time class="news-date" datetime="2026-10">2026.10</time> <span class="news-text">🎉🎉 Our paper "[CPA: Efficient and Stable FP4 RL Training via Cross-Precision Alignment](https://openreview.net/forum?id=jCqn6PPPpi)" is accepted by **NeurIPS 2026**.</span>

- <time class="news-date" datetime="2026-08">2026.08</time> <span class="news-text">🎉🎉 Our paper "Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning" is accepted by EMNLP 2026 Main Conference.</span>

- <time class="news-date" datetime="2026-07">2026.07</time> <span class="news-text">🎉🎉 Our tech report "Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction" is released to Arxiv.</span>

- <time class="news-date" datetime="2026-07">2026.07</time> <span class="news-text">🎉🎉 Our paper "An Empirical Study of Reasoning Degradation in Quantized Multimodal Large Language Models" is accepted by ACM MM 2026. </span>

- <time class="news-date" datetime="2026-06">2026.06</time> <span class="news-text">🎉🎉 Our paper "GreenMoE: Exploiting Dynamic Load Imbalance for Energy-Efficient Long-Context MoE Training" is accepted by ICML 2026 AdaptFM Workshop.</span>

<details markdown="1">
<summary>Earlier news</summary>

- <time class="news-date" datetime="2026-06">2026.06</time> <span class="news-text">🎉🎉 Our paper "Parameters as Agentic Memory: Internalizing Long-Horizon Memories for Efficient LLM Agents" is accepted by ICML 2026 AIWILD Workshop.</span>

- <time class="news-date" datetime="2026-06">2026.06</time> <span class="news-text">🎉🎉 Our paper "Enhancing Knowledge Injection with Surrounding Backgrounds in Continual Training LLMs" is accepted by ICML 2026 FoGen Workshop.</span>

- <time class="news-date" datetime="2026-05">2026.05</time> <span class="news-text">🎉🎉 Our paper "Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression" is accepted by ICML 2026.</span>

- <time class="news-date" datetime="2026-05">2026.05</time> <span class="news-text">🎉🎉 Our paper "VCG-Bench: Towards A Unified Visual-Centric Benchmark for Structured Generation and Editing" is accepted by ICML 2026.</span>

- <time class="news-date" datetime="2026-05">2026.05</time> <span class="news-text">🎉🎉 Our paper "Identifying and Mitigating Errors in Gradient Aggregation of Distributed Data Parallel Training" is accepted by ICML 2026.</span>

- <time class="news-date" datetime="2026-01">2026.01</time> <span class="news-text">🎉🎉 Our Paper "Smooth Reading: Bridging the Gap of Recurrent LLM to Self-Attention LLM on Long-Context Understanding" is accepted by ICLR2026.</span>

- <time class="news-date" datetime="2025-11">2025.11</time> <span class="news-text">🎉🎉 Two years after graduation, I was selected as an outstanding master's student at the NUDT in Hunan Province.</span>

- <time class="news-date" datetime="2025-09">2025.09</time> <span class="news-text">🎉🎉 Our Paper "ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference" is accepted by NeurIPS 2025. </span>

- <time class="news-date" datetime="2025-08">2025.08</time> <span class="news-text">🎉🎉 Our Paper "Perovskite-LLM: Knowledge-Enhanced Large Language Models for Perovskite Solar Cell Research" is accepted by EMNLP 2025 findings. </span>

- <time class="news-date" datetime="2025-08">2025.08</time> <span class="news-text">🎉🎉 Our Paper "Smooth Reading: Bridging the Gap of Recurrent LLM to Self-Attention LLM on Long-Context Tasks" is released to [arxiv.](https://arxiv.org/pdf/2507.19353)</span>

- <time class="news-date" datetime="2025-08">2025.08</time> <span class="news-text">🎉🎉 Our tech report "Intern-S1: A Scientific Multimodal Foundation Model" is released to [arxiv.](https://arxiv.org/abs/2508.15763) Great work by Intern-S1 team.</span>

- <time class="news-date" datetime="2025-05">2025.05</time> <span class="news-text">🎉🎉 Our Paper "Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compresssion" is accepted by ICML25. We are especially grateful to the reviewer who awarded us a '5 (Strong Accept)'.</span>

- <time class="news-date" datetime="2025-04">2025.04</time> <span class="news-text">🎉🎉 I've been invited to be an Area Chair in NeurIPS 2025.</span>

- <time class="news-date" datetime="2025-02">2025.02</time> <span class="news-text">🎉🎉 Congratulations to our team (lead by @Ruibo) to get "SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs" accepted by EuroSys 2025 as **Best Paper** !!!</span>

- <time class="news-date" datetime="2025-02">2025.02</time> <span class="news-text">🎉🎉 I am awarded the **Excellent Research Prize** for the 2024 DSA Excellent Research Award!!!</span>

- <time class="news-date" datetime="2025-01">2025.01</time> <span class="news-text">🎉🎉 Our STBLLM is accepted by ICLR25. STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs, International Conference on Learning Representations, 2025.</span>

- <time class="news-date" datetime="2025-01">2025.01</time> <span class="news-text">🎉🎉 Our Lottery LLM Hypothesis is accepted by ICLR25 Blogpost **Oral**. The Lottery LLM Hypothesis, Rethinking What Abilities Should LLM Compression Preserve?, International Conference on Learning Representations Blog Track **Oral**, 2025.</span>

- <time class="news-date" datetime="2025-01">2025.01</time> <span class="news-text">🎉🎉 Our ParZC is accepted by AAA25 (**Oral**). ParZC: Parametric Zero-Cost Proxies for Efficient NAS, Association for the Advancement of Artificial Intelligence, 2025.</span>

- <time class="news-date" datetime="2024-12">2024.12</time> <span class="news-text">🎉🎉 I was invited to give a talk to PDL about "Introduction to LLM Compression and Beyond".</span>

- <time class="news-date" datetime="2024-10">2024.10</time> <span class="news-text">🎉🎉 FuseFL is accepted by NeurIPS 2024 (Spotlight). FuseFL: One-Shot Federated Learning through the Lens of Causality with Progressive Layer Fusion, Neural Information Processing Systems (NeurIPS) Spotlight, 2024.</span>

- <time class="news-date" datetime="2024-10">2024.10</time> <span class="news-text">🎉🎉 DSA is accepted by NeurIPS 2024, Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models, Neural Information Processing Systems (NeurIPS), 2024.</span>

- <time class="news-date" datetime="2024-10">2024.10</time> <span class="news-text">🎉🎉 Our paper "Should we really edit language models? on the evaluation of edited language models" is accepted by NeurIPS 2024.</span>

- <time class="news-date" datetime="2024-10">2024.10</time> <span class="news-text">🎉🎉 LPZero is accepted by EMNLP 2024. LPZero: Language Model Zero-cost Proxy Search from Zero, Empirical Methods in Natural Language Processing (EMNLP), 2024. ([paper](https://arxiv.org/abs/2410.04808), [code](https://github.com/pprp/LPZero))</span>

- <time class="news-date" datetime="2024-10">2024.10</time> <span class="news-text">🎉🎉 LongGenBench is accepted by EMNLP 2024. LongGenBench: Long-context Generation Benchmark, Empirical Methods in Natural Language Processing (EMNLP), 2024.</span>

- <time class="news-date" datetime="2024-05">2024.05</time> <span class="news-text">🎉🎉 Pruner-Zero is accepted by ICML 2024. This work evolves symbolic pruning metrics from scratch for large language models. ([paper](https://arxiv.org/abs/2406.02924v1), [code](https://github.com/pprp/Pruner-Zero))</span>

- <time class="news-date" datetime="2024-03">2024.03</time> <span class="news-text">🎉🎉 VMRNN is available. This work proposes the VMRNN cell, a new recurrent unit that integrates the strengths of Vision Mamba blocks with LSTM. We construct a network centered on VMRNN cells to tackle spatiotemporal prediction tasks effectively. ([paper](https://arxiv.org/abs/2403.16536), [code](https://github.com/yyyujintang/VMRNN-PyTorch))</span>

- <time class="news-date" datetime="2023-12">2023.12</time> <span class="news-text">🎉🎉 KD-Zero is accepted by NeurIPS 2023. This work evolves knowledge distiller for any teacher-student pairs. ([paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/dbc8ce0fdfcd55172d73fb05dbae07fc-Paper-Conference.pdf))</span>

- <time class="news-date" datetime="2023-10">2023.10</time> <span class="news-text">🎉🎉 EMQ is accepted by ICCV 2023. This work evolves training-free proxies for automated mixed precision quantization. ([paper](https://arxiv.org/abs/2307.10554), [code](https://github.com/lliai/EMQ-series))</span>

- <time class="news-date" datetime="2023-10">2023.10</time> <span class="news-text">🎉🎉 AutoKD: Automated KD via MCTS is accepted by ICCV 2023. This work proposes automated knowledge distillation via Monte Carlo Tree Search. ([paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Automated_Knowledge_Distillation_via_Monte_Carlo_Tree_Search_ICCV_2023_paper.pdf))</span>

- <time class="news-date" datetime="2023-03">2023.03</time> <span class="news-text">🎉🎉 DisWOT is accepted by CVPR 2023. This work proposes student architecture search for distillation without training. ([paper](https://arxiv.org/abs/2303.15678), [code](https://github.com/lliai/DisWOT-CVPR2023))</span>

- <time class="news-date" datetime="2023-02">2023.02</time> <span class="news-text">🎉🎉 Progressive Meta-Pooling Learning is accepted by ICASSP 2023. This work proposes a lightweight image classification model. ([paper](https://arxiv.org/abs/2301.10038))</span>

- <time class="news-date" datetime="2023-02">2023.02</time> <span class="news-text">🎉🎉 RD-NAS is accepted by ICASSP 2023. This work enhances one-shot supernet ranking ability via ranking distillation. ([paper](https://arxiv.org/abs/2301.09850))</span>

- <time class="news-date" datetime="2023-01">2023.01</time> <span class="news-text">🎉🎉 AutoRF is accepted by MMM 2022. This work proposes auto learning receptive fields with spatial pooling. ([paper](https://link.springer.com/chapter/10.1007/978-3-031-27818-1_56))</span>

- <time class="news-date" datetime="2022-06">2022.06</time> <span class="news-text">🎉🎉 Prior-Guided One-shot NAS is accepted by CVPR Workshop 2022. This work proposes prior-guided one-shot neural architecture search. ([paper](https://arxiv.org/abs/2206.13329))</span>

</details>

</div>

## 📖 Educations

- _2023.09 - now_, The Hong Kong University of Science and Technology (Guangzhou), PhD Candidate in Computer Science

  - Supervisor: Prof. Xiaowen Chu
  - Research Interests: Large Language Models, Model Compression

- _2020.09 - 2023.06_, National University of Defence Technology, Master of Engineering

  - Supervisor: Prof. Xin Niu
  - Research Interests: AutoML, Neural Architecture Search
  - Achievement: Outstanding Graduate

- _2016.09 - 2020.06_, Northwest Agriculture & Forestry University, B.S. in Software Engineering
  - GPA: 3.78/4.0 (Ranked 1st out of 93)
  - Advisor: Prof. Hongming Zhang
  - Achievements: National Scholarship, Principal's Scholarship, Outstanding Graduate
  - Research Interests: Object Detection, Multi-Object Tracking

## 💻 Internship

- 06/2026-present: Research Intern, Tencent CSIG WorkBuddy/CodeBuddy - post-training and evaluation for long-horizon coding agents
- 10/2025–02/2026: Intern, Alibaba – large-scale model training  
- 03/2025–08/2025: Intern, Shanghai AI Lab – AI infrastructure for Xtuner project  
- 05/2022–08/2022: Intern, Shanghai AI Lab – model compression with MMRazor

<!-- # 📕 Teaching

- Teaching Assistant at HKBU
  - 2023 Spring Semester, COMP7940 Cloud Computing
  - 2022 Fall Semester, COMP7015 Artiﬁcial Intelligence
  - 2022 Spring Semester, COMP 7550 IT Project Management
  - 2021 Fall Semester, COMP 7015, Artificial Intelligence
  - 2021 Spring Semester, COMP 7930, Big Data Analytics -->

# 👔 Professional Activities

- **2022**: ICASSP
- **2023**: NeurIPS, ICASSP, CIM
- **2024**:
  - _Conferences_: NeurIPS, ICLR, CVPR, ECCV, ICASSP, ACL (ARR)
  - _Journals_: TPAMI, Neural Networks, Information Fusion, CIM
- **2025**:
  - _Conferences_: NeurIPS (AC), ICLR, CVPR, ECCV, ICASSP
  - _Journals_: IJCV, Neural Networks
- **2026**：
  - _Conferences_: AAAI (PC), WACV, NeurIPS, ICLR
  - _Journals_: Neural Networks

# 🎖 Honors and Awards

- 2024, Best Speaker in DSA Salon 2024.
- 2023, Outstanding Graduate at School Level, National University of Defense Technology.
- 2022, 1st Place, BDCI Retail Product Recognition based on MindSpore (CCF Big Data & Computing Intelligence Contest).
- 2022, 1st Place, DCIC Intelligent Ship Detection Competition (Digital China Innovation Contest).
- 2022, 2nd Place, DCIC Intelligent Cattle Segmentation Competition (Digital China Innovation Contest).
- 2022, 1st Place, Baidu AI Competition - Blurred Document Image Recovery.
- 2022, 3rd Place, Computer Vision and Pattern Recognition (CVPR) Third Workshop on NAS.
- 2021, Outstanding MindSpore Developer.
- 2020, Outstanding Dissertation, Northwest A&F University.
- 2020, Outstanding Graduate, Northwest A&F University.
- 2017, President's Scholarship, Northwest A&F University.
- 2016, National Scholarship, Northwest A&F University.

# 📝 Publications

Conference papers, workshop papers, technical reports, and blog publications.

<div class="home-publications" markdown="1">

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/cpa.png' | relative_url }}" aria-label="View cpa paper figure"><img src="{{ '/images/publications/cpa.png' | relative_url }}" alt="CPA: Efficient and Stable FP4 RL Training via Cross-Precision Alignment — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://openreview.net/forum?id=jCqn6PPPpi">CPA: Efficient and Stable FP4 RL Training via Cross-Precision Alignment</a></span><span class="publication-authors">G. Gong, Y. Wei, Y. Tao, T. Wu, **P. Dong**, R. Fan, W. Hu, Y. Yu, J. Wang, W. Su, G. Yang, L. Zhang, W. Wang, X. Chu.</span><span class="publication-venue">NeurIPS 2026.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/swarr.png' | relative_url }}" aria-label="View swarr paper figure"><img src="{{ '/images/publications/swarr.png' | relative_url }}" alt="Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning</span><span class="publication-authors">K. Liu, **P. Dong**, X. Xie, J. Gao, Q. Guo, X. Chu, S. Zhang, K. Chen.</span><span class="publication-venue">In EMNLP 2026 Main Conference.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/workbuddy.png' | relative_url }}" aria-label="View workbuddy paper figure"><img src="{{ '/images/publications/workbuddy.png' | relative_url }}" alt="Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://arxiv.org/abs/2607.20911">Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction</a></span><span class="publication-authors">Tencent WorkBuddy Bench Team (including **P. Dong**).</span><span class="publication-venue">Technical report, 2026.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/multimodal-reasoning.png' | relative_url }}" aria-label="View multimodal-reasoning paper figure"><img src="{{ '/images/publications/multimodal-reasoning.png' | relative_url }}" alt="An Empirical Study of Reasoning Degradation in Quantized Multimodal Large Language Models — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">An Empirical Study of Reasoning Degradation in Quantized Multimodal Large Language Models</span><span class="publication-venue">ACM MM 2026.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/greenmoe.png' | relative_url }}" aria-label="View greenmoe paper figure"><img src="{{ '/images/publications/greenmoe.png' | relative_url }}" alt="GreenMoE: Exploiting Dynamic Load Imbalance for Energy-Efficient Long-Context MoE Training — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://openreview.net/pdf/df733862c60e6a8de41f447b9b469479fd04b12f.pdf">GreenMoE: Exploiting Dynamic Load Imbalance for Energy-Efficient Long-Context MoE Training</a></span><span class="publication-venue">ICML 2026 AdaptFM Workshop.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/agentic-memory.png' | relative_url }}" aria-label="View agentic-memory paper figure"><img src="{{ '/images/publications/agentic-memory.png' | relative_url }}" alt="Parameters as Agentic Memory: Internalizing Long-Horizon Memories for Efficient LLM Agents — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Parameters as Agentic Memory: Internalizing Long-Horizon Memories for Efficient LLM Agents</span><span class="publication-authors">Z. Tang, F. Wei, Z. Tang, **P. Dong**, X. Liu, Q. Wang, X. Chu, B. Li.</span><span class="publication-venue">ICML 2026 AIWILD Workshop.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/knowcontext.png' | relative_url }}" aria-label="View knowcontext paper figure"><img src="{{ '/images/publications/knowcontext.png' | relative_url }}" alt="Enhancing Knowledge Injection with Surrounding Backgrounds in Continual Training LLMs — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://openreview.net/forum?id=sR4CtR5X1T">Enhancing Knowledge Injection with Surrounding Backgrounds in Continual Training LLMs</a></span><span class="publication-authors">Z. Tang, Z. Tang, Y. Hou, **P. Dong**, X. Liu, S. Shi, X. Chu, B. Li.</span><span class="publication-venue">ICML 2026 FoGen Workshop.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/semantic-integrity.png' | relative_url }}" aria-label="View semantic-integrity paper figure"><img src="{{ '/images/publications/semantic-integrity.png' | relative_url }}" alt="Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression</span><span class="publication-authors">X. Liu, Z. Tang, H. Chen, **P. Dong**, Z. Li, X. Zhou, B. Li, X. Hu, X. Chu.</span><span class="publication-venue">In ICML 2026.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/vcg-bench.png' | relative_url }}" aria-label="View vcg-bench paper figure"><img src="{{ '/images/publications/vcg-bench.png' | relative_url }}" alt="VCG-Bench: Towards A Unified Visual-Centric Benchmark for Structured Generation and Editing — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">VCG-Bench: Towards A Unified Visual-Centric Benchmark for Structured Generation and Editing</span><span class="publication-authors">X. Su, **P. Dong**, Z. Tang, S. Tang, Y. Zhai, K. Lin, L. Chen, Y. Gai, Y. Luo, Q. Wang, X. Chu.</span><span class="publication-venue">In ICML 2026.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/paft.png' | relative_url }}" aria-label="View paft paper figure"><img src="{{ '/images/publications/paft.png' | relative_url }}" alt="Identifying and Mitigating Errors in Gradient Aggregation of Distributed Data Parallel Training — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Identifying and Mitigating Errors in Gradient Aggregation of Distributed Data Parallel Training</span><span class="publication-authors">Z. Tang, J. Huang, Z. Tang, X. Kang, Y. Wang, **P. Dong**, S. Shi, X. Chu, B. Li.</span><span class="publication-venue">In ICML 2026.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/smooth-reading.png' | relative_url }}" aria-label="View smooth-reading paper figure"><img src="{{ '/images/publications/smooth-reading.png' | relative_url }}" alt="Smooth Reading: Bridging the Gap of Recurrent LLM to Self-Attention LLM on Long-Context Understanding — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://arxiv.org/abs/2507.19353">Smooth Reading: Bridging the Gap of Recurrent LLM to Self-Attention LLM on Long-Context Understanding</a></span><span class="publication-authors">K. Liu, Z. Su, **P. Dong**, F. Mo, J. Gao, S. Zhang, K. Chen.</span><span class="publication-venue">ICLR 2026.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/chunkkv.png' | relative_url }}" aria-label="View chunkkv paper figure"><img src="{{ '/images/publications/chunkkv.png' | relative_url }}" alt="ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://arxiv.org/abs/2502.00299">ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference</a></span><span class="publication-authors">X. Liu, Z. Tang, **P. Dong**, Z. Li, Y. Liu, B. Li, X. Hu, X. Chu.</span><span class="publication-venue">NeurIPS 2025.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/perovskite-llm.png' | relative_url }}" aria-label="View perovskite-llm paper figure"><img src="{{ '/images/publications/perovskite-llm.png' | relative_url }}" alt="Perovskite-LLM: Knowledge-Enhanced Large Language Models for Perovskite Solar Cell Research — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://arxiv.org/abs/2502.12669">Perovskite-LLM: Knowledge-Enhanced Large Language Models for Perovskite Solar Cell Research</a></span><span class="publication-authors">X. Liu, P. Sun, S. Chen, L. Zhang, **P. Dong**, H. You, Y. Zhang, C. Yan, X. Chu, T.-Y. Zhang.</span><span class="publication-venue">EMNLP 2025 Findings.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/intern-s1.png' | relative_url }}" aria-label="View intern-s1 paper figure"><img src="{{ '/images/publications/intern-s1.png' | relative_url }}" alt="Intern-S1: A Scientific Multimodal Foundation Model — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://arxiv.org/abs/2508.15763">Intern-S1: A Scientific Multimodal Foundation Model</a></span><span class="publication-authors">Intern-S1 Team, Shanghai AI Laboratory (including **P. Dong**).</span><span class="publication-venue">Technical report, 2025.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/acbench.png' | relative_url }}" aria-label="View acbench paper figure"><img src="{{ '/images/publications/acbench.png' | relative_url }}" alt="Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression</span><span class="publication-authors">**P. Dong**, Z. Tang, X. Liu, L. Li, X. Chu, B. Li.</span><span class="publication-venue">In ICML2025.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/spinfer.png' | relative_url }}" aria-label="View spinfer paper figure"><img src="{{ '/images/publications/spinfer.png' | relative_url }}" alt="SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs</span><span class="publication-authors">R. Fan, X. Yu, **P. Dong**, Z. Li, G. Gong, Q. Wang, W. Wang, X. Chu.</span><span class="publication-venue">In EuroSys2025, **Best Paper**.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/parzc.png' | relative_url }}" aria-label="View parzc paper figure"><img src="{{ '/images/publications/parzc.png' | relative_url }}" alt="ParZC: Parametric Zero-Cost Proxies for Efficient NAS — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">ParZC: Parametric Zero-Cost Proxies for Efficient NAS</span><span class="publication-authors">**P. Dong**, L. Li, Z. Tang, X. Liu, Z. Wei, Q. Wang, X. Chu.</span><span class="publication-venue">In AAAI2025, Oral.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/stbllm.png' | relative_url }}" aria-label="View stbllm paper figure"><img src="{{ '/images/publications/stbllm.png' | relative_url }}" alt="STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs</span><span class="publication-authors">**P. Dong**, L. Li, Y. Zhong, D. Du, R. Fan, Y. Chen, Z. Tang, Q. Wang, W. Xue, Y. Guo, X. Chu.</span><span class="publication-venue">In ICLR2025.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/lottery-llm.png' | relative_url }}" aria-label="View lottery-llm paper figure"><img src="{{ '/images/publications/lottery-llm.png' | relative_url }}" alt="The Lottery LLM Hypothesis, Rethinking What Abilities Should LLM Compression Preserve? — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://iclr-blogposts.github.io/2025/blog/the-lottery-llm-hyperthesis/">The Lottery LLM Hypothesis, Rethinking What Abilities Should LLM Compression Preserve?</a></span><span class="publication-authors">Z. Tang, X. Liu, Q. Wang, **P. Dong**, B. He, X. Chu, B. Li.</span><span class="publication-venue">ICLR 2025 Blogpost, **Oral**.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/dsa.png' | relative_url }}" aria-label="View dsa paper figure"><img src="{{ '/images/publications/dsa.png' | relative_url }}" alt="Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models</span><span class="publication-authors">L. Li, **P. Dong**, Z. Tang, X. Liu, X. Pan, X. Chu.</span><span class="publication-venue">In NeurIPS 2024.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/vmrnn.png' | relative_url }}" aria-label="View vmrnn paper figure"><img src="{{ '/images/publications/vmrnn.png' | relative_url }}" alt="VMRNN: Integrating Vision Mamba and LSTM for Efficient and Accurate Spatiotemporal Forecasting — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title"><a href="https://arxiv.org/abs/2403.16536">VMRNN: Integrating Vision Mamba and LSTM for Efficient and Accurate Spatiotemporal Forecasting</a></span><span class="publication-authors">Y. Tang, **P. Dong**, Z. Tang, X. Chu, J. Liang.</span><span class="publication-venue">Preprint, 2024.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/editing-evaluation.png' | relative_url }}" aria-label="View editing-evaluation paper figure"><img src="{{ '/images/publications/editing-evaluation.png' | relative_url }}" alt="Should We Really Edit Language Models? On the Evaluation of Edited Language Models — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Should We Really Edit Language Models? On the Evaluation of Edited Language Models</span><span class="publication-authors">Q. Li, X. Liu, Z. Tang, **P. Dong**, Z. Li, X. Pan, X. Chu,</span><span class="publication-venue">In NeurIPS 2024.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/pruner-zero.png' | relative_url }}" aria-label="View pruner-zero paper figure"><img src="{{ '/images/publications/pruner-zero.png' | relative_url }}" alt="Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models</span><span class="publication-authors">**P. Dong**, L. Li, Z. Tang, X. Liu, X. Pan, Q. Wang, X. Chu.</span><span class="publication-venue">In ICML 2024.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/lpzero.png' | relative_url }}" aria-label="View lpzero paper figure"><img src="{{ '/images/publications/lpzero.png' | relative_url }}" alt="LPZero: Language Model Zero-cost Proxy Search from Zero — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">LPZero: Language Model Zero-cost Proxy Search from Zero</span><span class="publication-authors">**P. Dong**, L. Li, X. Liu, Z. Tang, X. Liu, Q. Wang, X. Chu.</span><span class="publication-venue">Empirical Methods in Natural Language Processing (EMNLP), 2024.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/longgenbench.png' | relative_url }}" aria-label="View longgenbench paper figure"><img src="{{ '/images/publications/longgenbench.png' | relative_url }}" alt="LongGenBench: Long-context Generation Benchmark — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">LongGenBench: Long-context Generation Benchmark</span><span class="publication-authors">X. Liu, **P. Dong**, X. Hu, X. Chu.</span><span class="publication-venue">In EMNLP 2024.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/fusefl.png' | relative_url }}" aria-label="View fusefl paper figure"><img src="{{ '/images/publications/fusefl.png' | relative_url }}" alt="FuseFL: One-Shot Federated Learning through the Lens of Causality with Progressive Layer Fusion — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">FuseFL: One-Shot Federated Learning through the Lens of Causality with Progressive Layer Fusion</span><span class="publication-authors">Z. Tang, Y. Zhang, **P. Dong**, Y. Cheung, A. C. Zhou, B. Han, X. Chu.</span><span class="publication-venue">In NeurIPS Spotlight 2024.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/diswot.png' | relative_url }}" aria-label="View diswot paper figure"><img src="{{ '/images/publications/diswot.png' | relative_url }}" alt="DisWOT: Student Architecture Search for Distillation without Training — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">DisWOT: Student Architecture Search for Distillation without Training</span><span class="publication-authors">**P. Dong**, L. Li, Z. Wei.</span><span class="publication-venue">In CVPR 2023.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/emq.png' | relative_url }}" aria-label="View emq paper figure"><img src="{{ '/images/publications/emq.png' | relative_url }}" alt="EMQ: Evolving Training-free Proxies for Automated Mixed Precision Quantization — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">EMQ: Evolving Training-free Proxies for Automated Mixed Precision Quantization</span><span class="publication-authors">**P. Dong**, L. Li, Z. Wei, X. Niu$^*$, Z. Tian, H. Pan.</span><span class="publication-venue">In ICCV 2023.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/kd-zero.png' | relative_url }}" aria-label="View kd-zero paper figure"><img src="{{ '/images/publications/kd-zero.png' | relative_url }}" alt="Kd-zero: Evolving knowledge distiller for any teacher-student pairs — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Kd-zero: Evolving knowledge distiller for any teacher-student pairs</span><span class="publication-authors">L. Li, **P. Dong**, A. Li, Z. Wei, Y. Yang.</span><span class="publication-venue">In NeurIPS 2023.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/meta-pooling.png' | relative_url }}" aria-label="View meta-pooling paper figure"><img src="{{ '/images/publications/meta-pooling.png' | relative_url }}" alt="Progressive Meta-Pooling Learning for Lightweight Image Classification Model — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Progressive Meta-Pooling Learning for Lightweight Image Classification Model</span><span class="publication-authors">**P. Dong**, X. Niu, Z. Tian, et al.</span><span class="publication-venue">In ICASSP 2023.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/rd-nas.png' | relative_url }}" aria-label="View rd-nas paper figure"><img src="{{ '/images/publications/rd-nas.png' | relative_url }}" alt="RD-NAS: Enhancing One-shot Supernet Ranking Ability via Ranking Distillation — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">RD-NAS: Enhancing One-shot Supernet Ranking Ability via Ranking Distillation</span><span class="publication-authors">**P. Dong**, X. Niu, L. Li, et al.</span><span class="publication-venue">In ICASSP 2023.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/autorf.png' | relative_url }}" aria-label="View autorf paper figure"><img src="{{ '/images/publications/autorf.png' | relative_url }}" alt="AutoRF: Auto Learning Receptive Fields with Spatial Pooling — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">AutoRF: Auto Learning Receptive Fields with Spatial Pooling</span><span class="publication-authors">**P. Dong**, X. Niu, H. Pan, et al.</span><span class="publication-venue">In MMM 2023.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/prior-guided-nas.png' | relative_url }}" aria-label="View prior-guided-nas paper figure"><img src="{{ '/images/publications/prior-guided-nas.png' | relative_url }}" alt="Prior-Guided One-shot Neural Architecture Search — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Prior-Guided One-shot Neural Architecture Search</span><span class="publication-authors">**P. Dong**, X. Niu, L. Li, et al.</span><span class="publication-venue">In CVPR Workshop 2022.</span></span></span>

- <span class="publication--illustrated"><a class="publication-figure" href="{{ '/images/publications/auto-kd.png' | relative_url }}" aria-label="View auto-kd paper figure"><img src="{{ '/images/publications/auto-kd.png' | relative_url }}" alt="Automated Knowledge Distillation via Monte Carlo Tree Search — paper figure" loading="lazy" width="190" height="140"></a><span class="publication-info"><span class="publication-title">Automated Knowledge Distillation via Monte Carlo Tree Search</span><span class="publication-authors">L. Li, **P. Dong**, Z. Wei, Y. Ya.</span><span class="publication-venue">In ICCV 2023.</span></span></span>


</div>

<!--
[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
</div>
</div> -->

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=A14sfU1mQ29eKVjBuoPG6sP2CDJtNGaWlvKC81sqnrg&cl=ffffff&w=a"></script>
