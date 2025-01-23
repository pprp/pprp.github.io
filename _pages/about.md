---
permalink: /
title: ''
excerpt: ''
author_profile: true
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


I am **Peijie Dong** (董佩杰), a Ph.D. candidate in Data Science and Analysis Thrust at the Hong Kong University of Science and Technology (Guangzhou). Under the guidance of [Prof. Xiaowen Chu](https://sites.google.com/view/chuxiaowen). I am currently interning at [OpenMMLab](https://www.openmmlab.com/). My research interests are in the fields of model compression, efficient large language models, and automated machine learning. 


**Research Interests**


My research focuses on enhancing the efficiency and accessibility of deep learning models, particularly in the following areas:

- Model Compression: Exploring pruning, quantization, and knowledge distillation techniques to reduce model size and computational demands.
- Efficient Large Language Models: Optimizing LLM training and inference through innovative architectures and deployment strategies.
- Automated Machine Learning (AutoML): Developing methods to streamline the ML pipeline, from architecture search to hyperparameter optimization.

My goal is to contribute significantly to the development of more efficient and accessible machine learning systems. Through my research, I strive to push the boundaries of what's possible in model compression, efficient large language models, and automated machine learning. If you share similar interests or would like to discuss potential collaborations, I warmly invite you to reach out to me. I'm always eager to connect with fellow researchers and industry professionals to exchange ideas and explore new opportunities in this exciting field.

# 🔥 News

- [2025.01] &nbsp;🎉🎉 Our STBLLM is accepted by ICLR25. STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs, International Conference on Learning Representations, 2025.

- [2025.01] &nbsp;🎉🎉 Our ParZC is accepted by AAA25 (**Oral**). ParZC: Parametric Zero-Cost Proxies for Efficient NAS, Association for the Advancement of Artificial Intelligence, 2025. 

- [2024.12] &nbsp;🎉🎉 I was invited to give a talk to PDL about "Introduction to LLM Compression and Beyond". 

- [2024.10] &nbsp;🎉🎉 FuseFL is accepted by NeurIPS 2024 (Spotlight). FuseFL: One-Shot Federated Learning through the Lens of Causality with Progressive Layer Fusion, Neural Information Processing Systems (NeurIPS) Spotlight, 2024.

- [2024.10] &nbsp;🎉🎉 DSA is accepted by NeurIPS 2024, Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models, Neural Information Processing Systems (NeurIPS), 2024.

- [2024.10] &nbsp;🎉🎉 Our paper "Should we really edit language models? on the evaluation of edited language models" is accepted by NeurIPS 2024.

- [2024.10] &nbsp;🎉🎉 LPZero is accepted by EMNLP 2024. LPZero: Language Model Zero-cost Proxy Search from Zero, Empirical Methods in Natural Language Processing (EMNLP), 2024. ([paper](https://arxiv.org/abs/2410.04808), [code](https://github.com/pprp/LPZero))

- [2024.10] &nbsp;🎉🎉 LongGenBench is accepted by EMNLP 2024. LongGenBench: Long-context Generation Benchmark, Empirical Methods in Natural Language Processing (EMNLP), 2024.

- [2024.05] &nbsp;🎉🎉 Pruner-Zero is accepted by ICML 2024. This work evolves symbolic pruning metrics from scratch for large language models. ([paper](https://arxiv.org/abs/2406.02924v1), [code](https://github.com/pprp/Pruner-Zero))

- [2024.03] &nbsp;🎉🎉 VMRNN is available. This work proposes the VMRNN cell, a new recurrent unit that integrates the strengths of Vision Mamba blocks with LSTM. We construct a network centered on VMRNN cells to tackle spatiotemporal prediction tasks effectively. ([paper](https://arxiv.org/abs/2403.16536), [code](https://github.com/yyyujintang/VMRNN-PyTorch))

- [2023.12] &nbsp;🎉🎉 KD-Zero is accepted by NeurIPS 2023. This work evolves knowledge distiller for any teacher-student pairs. ([paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/dbc8ce0fdfcd55172d73fb05dbae07fc-Paper-Conference.pdf))


- [2023.10] &nbsp;🎉🎉 EMQ is accepted by ICCV 2023. This work evolves training-free proxies for automated mixed precision quantization. ([paper](https://arxiv.org/abs/2307.10554), [code](https://github.com/lliai/EMQ-series))

- [2023.10] &nbsp;🎉🎉 AutoKD: Automated KD via MCTS is accepted by ICCV 2023. This work proposes automated knowledge distillation via Monte Carlo Tree Search. ([paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Automated_Knowledge_Distillation_via_Monte_Carlo_Tree_Search_ICCV_2023_paper.pdf))

- [2023.03] &nbsp;🎉🎉 DisWOT is accepted by CVPR 2023. This work proposes student architecture search for distillation without training. ([paper](https://arxiv.org/abs/2303.15678), [code](https://github.com/lliai/DisWOT-CVPR2023))

- [2023.02] &nbsp;🎉🎉 Progressive Meta-Pooling Learning is accepted by ICASSP 2023. This work proposes a lightweight image classification model. ([paper](https://arxiv.org/abs/2301.10038))

- [2023.02] &nbsp;🎉🎉 RD-NAS is accepted by ICASSP 2023. This work enhances one-shot supernet ranking ability via ranking distillation. ([paper](https://arxiv.org/abs/2301.09850))

- [2023.01] &nbsp;🎉🎉 AutoRF is accepted by MMM 2022. This work proposes auto learning receptive fields with spatial pooling. ([paper](https://link.springer.com/chapter/10.1007/978-3-031-27818-1_56))

- [2022.06] &nbsp;🎉🎉 Prior-Guided One-shot NAS is accepted by CVPR Workshop 2022. This work proposes prior-guided one-shot neural architecture search. ([paper](https://arxiv.org/abs/2206.13329))

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

<!-- ## 💻 Work & Research Experience

- 09/2023-present: Visiting Researcher, The Hong Kong University of Science and Technology (Guangzhou), advised by [Prof. Xiaowen Chu](https://sites.google.com/view/chuxiaowen).
- 02/2023-05/2023: Visiting Researcher, National University of Singapore, advised by [Prof. Bingsheng He](https://www.comp.nus.edu.sg/~hebs/).
- 06/2022-10/2022: Research Intern, [FedML Inc](https://www.fedml.ai/), advised by [Dr. Chaoyang He](https://chaoyanghe.com/).
- 10/2018-09/2020: Research Assistant, Hong Kong Baptist University, advised by [Prof. Xiaowen Chu](https://sites.google.com/view/chuxiaowen). -->

<!-- # 📕 Teaching

- Teaching Assistant at HKBU
  - 2023 Spring Semester, COMP7940 Cloud Computing
  - 2022 Fall Semester, COMP7015 Artiﬁcial Intelligence
  - 2022 Spring Semester, COMP 7550 IT Project Management
  - 2021 Fall Semester, COMP 7015, Artificial Intelligence
  - 2021 Spring Semester, COMP 7930, Big Data Analytics -->

# 👔 Professional Activities

- Invited Program Committee Member (Reviewer):

  - Machine Learning: 
    - NeurIPS'23,24, ICLR'24,25
  - Computer Vision: 
    - CVPR'24,25, ECCV'24, IJCV'25
  - Signal Processing: 
    - ICASSP'23,24,25
  - Natural Language Processing:
    - ACL'24

- Invited Reviewer for Journals
  - Machine Learning:
    - TPAMI'24
    - Neural Networks'25
    - Information Fusion'24
  - Signal Processing:
    - CIM'24

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

First-authored and co-first-authored papers: AAAIx1(Oral), NeurIPSx1(Spotlight), ICMLx1, EMNLPx1, CVPRx1, ICCVx1, ICASSPx2, 

- **P. Dong**, L. Li, Z. Tang, X. Liu, Z. Wei, Q. Wang, X. Chu. ParZC: Parametric Zero-Cost Proxies for Efficient NAS. In AAAI2025, Oral. 

- **P. Dong**, L. Li, Y. Zhong, D. Du, R. Fan, Y. Chen, Z. Tang, Q. Wang, W. Xue, Y. Guo, X. Chu. STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs. In ICLR2025. 

- L. Li, **P. Dong**, Z. Tang, X. Liu, X. Pan, X. Chu. Discovering Sparsity Allocation for Layer-wise Pruning of Large Language Models. In NeurIPS 2024.

- Q. Li, X. Liu, Z. Tang, **P. Dong**, Z. Li, X. Pan, X. Chu, Should We Really Edit Language Models? On the Evaluation of Edited Language Models. In NeurIPS 2024.

- **P. Dong**, L. Li, Z. Tang, X. Liu, X. Pan, Q. Wang, X. Chu. Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models. In ICML 2024.

- **P. Dong**, L. Li, X. Liu, Z. Tang, X. Liu, Q. Wang, X. Chu. LPZero: Language Model Zero-cost Proxy Search from Zero, Empirical Methods in Natural Language Processing (EMNLP), 2024.

- X. Liu, **P. Dong**, X. Hu, X. Chu. LongGenBench: Long-context Generation Benchmark. In EMNLP 2024.

- Z. Tang, Y. Zhang, **P. Dong**, Y. Cheung, A. C. Zhou, B. Han, X. Chu. FuseFL: One-Shot Federated Learning through the Lens of Causality with Progressive Layer Fusion. In NeurIPS Spotlight 2024.

- **P. Dong**, L. Li, Z. Wei. DisWOT: Student Architecture Search for Distillation without Training. In CVPR 2023.

- **P. Dong**, L. Li, Z. Wei, X. Niu$^*$, Z. Tian, H. Pan. EMQ: Evolving Training-free Proxies for Automated Mixed Precision Quantization. In ICCV 2023.

- L. Li, **P. Dong**, A. Li, Z. Wei, Y. Yang. Kd-zero: Evolving knowledge distiller for any teacher-student pairs. In NeurIPS 2023.

- **P. Dong**, X. Niu, Z. Tian, et al. Progressive Meta-Pooling Learning for Lightweight Image Classification Model. In ICASSP 2023.

- **P. Dong**, X. Niu, L. Li, et al. RD-NAS: Enhancing One-shot Supernet Ranking Ability via Ranking Distillation. In ICASSP 2023.

- **P. Dong**, X. Niu, H. Pan, et al. AutoRF: Auto Learning Receptive Fields with Spatial Pooling. In MMM 2023.

- **P. Dong**, X. Niu, L. Li, et al. Prior-Guided One-shot Neural Architecture Search. In CVPR Workshop 2022.

- L. Li, **P. Dong**, Z. Wei, Y. Ya. Automated Knowledge Distillation via Monte Carlo Tree Search. In ICCV 2023.

<!--
[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
</div>
</div> -->

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=A14sfU1mQ29eKVjBuoPG6sP2CDJtNGaWlvKC81sqnrg&cl=ffffff&w=a"></script>
