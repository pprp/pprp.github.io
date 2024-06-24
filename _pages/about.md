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

<!-- Hi! This year, I'm expected to graduate as a Computer Science PhD in [Hong Kong Baptist University](https://www.hkbu.edu.hk) under the supervision of [Prof. Xiaowen Chu](https://sites.google.com/view/chuxiaowen) and [Prof. Amelie Chi Zhou](https://www.comp.hkbu.edu.hk/~amelieczhou/), and co-supervised by [Prof. Bo Han](https://bhanml.github.io/). After PhD journey, I'm going to work as a Postdoctoral Fellow in HKUST under supervision of [Prof. Bo Li](https://www.cse.ust.hk/~bli/) and [Prof. Xiaowen Chu](https://sites.google.com/view/chuxiaowen). Before HKBU, I got my Bachelor degree of HUST. -->

My name is **Peijie Dong** (董佩杰), a Ph.D. student in Data Science and Analysis at the Hong Kong University of Science and Technology (Guangzhou). Under the supervision of [Prof. Xiaowen Chu](https://sites.google.com/view/chuxiaowen), my research focuses on auto machine learning, deep learning, and model compression.

Before that, I obtained my B.S. in Software Engineering from Northwest Agriculture & Forestry University supervised by [Prof. Hongming Zhang](https://cie.nwsuaf.edu.cn/szdw/js/2008117820/index.htm) and A.P Yaojun Geng, where I ranked first in my class with a GPA of 3.78/4.0. Additionally, I completed my Master of Engineering at the National University of Defense Technology under the guidance of supervisor Xin Niu and [Zhiliang Tian](https://tianzhiliang.github.io/).

**Research Interests**

<!-- Democratizing large deep learning models needs high efficiency, scalability, robustness and privacy. Achieving these goals needs to understand _both ML and systems_ at first. To this end, I'm studying following aspects:

- Training: ML optimizer, Distributed training (and federated learning), HPO, ML-system co-designs, Fault-tolerance training.
- Inference: Memory saving, Model compression, MoE routing, Accelerating LLM inference (both edge and server).
- Understanding Deep Learning/LLM: How model/LLM is trained, how knowledge is stored in the model/LLM, how knowledge is retrieved from the model/LLM.
- Data-centric: RAG, Dataset selection, Data quality, Data generation.
- LLM privacy: Privacy preserved inference.

Hope that finally we can design an _ML system_ to learn and generate knowledge at anywhere and anytime. I'm open for academic collaborations. If you are interested, please feel free to contact me. -->

My research focuses on enhancing the efficiency and accessibility of deep learning models, particularly in the following areas:

- Model Compression: Exploring pruning, quantization, and knowledge distillation techniques to reduce model size and computational demands.
- Efficient Large Language Models: Optimizing LLM training and inference through innovative architectures and deployment strategies.
- Automated Machine Learning (AutoML): Developing methods to streamline the ML pipeline, from architecture search to hyperparameter optimization.

I aim to contribute to the development of more efficient and accessible ML systems. If you are interested, please feel free to contact me.

# 🔥 News

<!-- - [2024.06] &nbsp;🎉🎉 Our paper "Bandwidth-Aware and Overlap-Weighted Compression for Communication-Efficient Federated Learning." is accepted at ICPP 2024. This work finds that the overlapness between indexes of compressed client model parameters demonstrates important information that can be utilized to adjust averging weights. ([paper]())
- [2024.05] &nbsp;🎉🎉 Our paper "Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models." is accepted at ICML 2024. This work finds new pruning metric to prune LLMs to achieve SOTA performance under the same sparsity ratio. ([paper](https://arxiv.org/abs/2406.02924))
- [2024.03] &nbsp;🎉🎉 VMRNN is available. This work proposes the VMRNN cell, a new recurrent unit that integrates the strengths of Vision Mamba blocks with LSTM. We construct a network centered on VMRNN cells to tackle spatiotemporal prediction tasks effectively. ([paper](https://arxiv.org/abs/2403.16536), [code](https://github.com/yyyujintang/VMRNN-PyTorch))
- [2024.01] &nbsp;🎉🎉 Our paper "FedImpro: Measuring and Improving Client Update in Federated Learning" is accepted at ICLR 2024. ([paper](https://arxiv.org/pdf/2402.07011.pdf),[code](https://github.com/wizard1203/FedImpro)). This work trains the high-level neural network on reconstructed feature distributions, to accelerate FL training and enhance the model performance.
- [2024.01] &nbsp;🎉🎉 Our paper "Towards Efficient and Reliable LLM Serving: A Real-World Workload Study" is available. ([paper](https://arxiv.org/pdf/2401.17644.pdf)),[code](https://github.com/HPMLL/BurstGPT). This paper introduces the first real-world trace dataset of LLM serving workloads, detailing user, system, and LLM behaviors. Many new insights of GPT services are found in this work.
- [2023.10] &nbsp;🎉🎉 Our paper "Reliable and Efficient In-Memory Fault Tolerance of Large Language Model Pretraining" is available. ([paper](https://arxiv.org/pdf/2310.12670.pdf)). This work desings an in-memory fault-tolerance framework for large-scale LLM pretraining.
- [2023.09] &nbsp;🎉🎉 Our paper "FusionAI: Decentralized Training and Deploying LLMs with Massive Consumer-Level GPUs" is available. ([paper](https://arxiv.org/abs/2309.01172)). This paper envisions a decentralized system unlocking the potential vast untapped consumer-level GPUs in pre-training, inference and fine-tuning of LLMs with privacy protection.
- [2023.02] &nbsp;🎉🎉 Our paper "FedML Parrot: A Scalable Federated Learning System via Heterogeneity-aware Scheduling on Sequential and Hierarchical Training" is available. ([paper](https://arxiv.org/pdf/2303.01778.pdf)). This work aims to democratize simulating large-scale FL experiments. BTW, our open-source FL framework [FedML](https://github.com/FedML-AI/FedML) has reached 2.6k stars at github.
- [2022.12] &nbsp;🎉🎉 Our paper "GossipFL: A Decentralized Federated Learning Framework with Sparsified and Adaptive Communication" has been accepted by _IEEE TPDS_. ([paper](https://ieeexplore.ieee.org/document/9996127)).
- [2022.10] &nbsp;🎉🎉 Our paper “NAS-LID: Efficient Neural Architecture Search with Local Intrinsic Dimension” is accepted at AAAI 2023. ([paper](https://arxiv.org/abs/2211.12759)).
- [2022.05] &nbsp;🎉🎉 Our paper "Virtual Homogeneity Learning: Defending against Data Heterogeneity in Federated Learning" is accepted at ICML 2022. ([paper](https://proceedings.mlr.press/v162/tang22d.html), [code](https://github.com/wizard1203/VHL)).
- [2022.03] &nbsp;🎉🎉 Our paper "FedCV: A Federated Learning Framework for Diverse Computer Vision Tasks" is accepted to FL-AAAI workshop '22 as Oral Presentation. [paper](https://arxiv.org/pdf/2111.11066.pdf).
- [2021.07] &nbsp;🎉🎉 Our paper "Data Resampling for Federated Learning with Non-IID Labels." is accepted to FTL-IJCAI workshop '21 [paper](https://federated-learning.org/fl-ijcai-2021/FTL-IJCAI21_paper_3.pdf).
- [2020.10] &nbsp;🎉🎉 Our survey paper "A Quantitative Survey of Communication Optimizations in Distributed Deep Learning" \[[code](https://github.com/HKBU-HPML/ddl-benchmarks), [paper](https://arxiv.org/abs/2005.13247)\] has been accepted by _IEEE Network Magazine_. -->

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

  - Machine Learning: NeurIPS'23,24, ICLR'24, CVPR'24, ECCV'24
  - Signal Processing: ICASSP'23,24

- Invited Reviewer for Journals
  - Machine Learning:
    - IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)
    - Neural Networks
    - Information Fusion
  - Signal Processing:
    - IEEE Computational Intelligence Magazine (CIM)

<!-- # 🎖 Honors and Awards

- 2023/24, Research Performance Award, HKBU CS Department ([Link](https://www.comp.hkbu.edu.hk/v1/?pid=48)).
- 2022/23, Research Performance Award, HKBU CS Department ([Link](https://www.comp.hkbu.edu.hk/v1/?pid=48)).
- 2022/23 Fall, Teaching Performance Award, HKBU CS Department ([Link](https://www.comp.hkbu.edu.hk/v1/?pid=48)).
- 2021/22, Research Performance Award, HKBU CS Department ([Link](https://www.comp.hkbu.edu.hk/v1/?pid=48)).
- 2021/22 Fall, Teaching Performance Award, HKBU CS Department ([Link](https://www.comp.hkbu.edu.hk/v1/?pid=48)).
- 2020, Scholarship for Nominees of Hong Kong PhD Fellowship Scheme, HKBU CS Department ([Link](https://www.comp.hkbu.edu.hk/v1/?pid=48)).
- 2018, Outstanding Graduate, HUST
- 2016, Scholarship of Academic Excellence, HUST -->

# 🎖 Honors and Awards

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

- **P. Dong**, L. Li, Z. Tang, X. Liu, X. Pan, Q. Wang, X. Chu. Pruner-Zero: Evolving Symbolic Pruning Metric From Scratch for Large Language Models. In ICML 2024.

- **P. Dong**, L. Li, Z. Wei. DisWOT: Student Architecture Search for Distillation without Training. In CVPR 2023.

- **P. Dong**, L. Li, Z. Wei, X. Niu$^*$, Z. Tian, H. Pan. EMQ: Evolving Training-free Proxies for Automated Mixed Precision Quantization. In ICCV 2023.

- L. Li, **P. Dong**, A. Li, Z. Wei, Y. Yang. Kd-zero: Evolving knowledge distiller for any teacher-student pairs. In NeurIPS 2023.

- **P. Dong**, X. Niu, Z. Tian, et al. Progressive Meta-Pooling Learning for Lightweight Image Classification Model. In ICASSP 2023.

- **P. Dong**, X. Niu, L. Li, et al. RD-NAS: Enhancing One-shot Supernet Ranking Ability via Ranking Distillation. In ICASSP 2023.

- **P. Dong**, X. Niu, H. Pan, et al. AutoRF: Auto Learning Receptive Fields with Spatial Pooling. In MMM 2023.

- **P. Dong**, X. Niu, L. Li, et al. Prior-Guided One-shot Neural Architecture Search. In CVPR Workshop 2022.

- L. Li, **P. Dong**, Z. Wei, Y. Ya. Automated Knowledge Distillation via Monte Carlo Tree Search. In ICCV 2023.

<!-- The \* represents the equal contribution, \# corresponding author, $\dagger$ project lead. -->

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
 -->
<!--
- Z. Tang, J. Huang, R. Yan, Y. Wang, **Z. Tang**$\dagger$, S. Shi, A. C. Zhou, X. Chu. Bandwidth-Aware and Overlap-Weighted Compression for Communication-Efficient Federated Learning. In ICPP 2024.

- P. Dong, L. Li, **Z. Tang**, X. Liu, X. Pan, Q. Wang, X. Chu. Evolving Symbolic Pruning Metric From Scratch for Large Language Models. In ICML 2024.

- Y. Tang, P. Dong, **Z. Tang**, X. Chu, J. Liang. VMRNN: Integrating Vision Mamba and LSTM for Efficient and Accurate Spatiotemporal Forecasting. In CVPR Workshop 2024.

- **Z. Tang**, Y. Zhang, S. Shi, X. Tian, T. Liu, B. Han, X. Chu. FedImpro: Measuring and Improving Client Update in Federated Learning. In ICLR 2024.

- Y. Wang, Y. Chen, Z. Li, **Z. Tang**, R. Guo, X. Wang, Q. Wang, AC Zhou, X. Chu. Towards Efficient and Reliable LLM Serving: A Real-World Workload Study. arXiv preprint arXiv:2401.17644.

- Y. Wang, S. Shi, X. He, **Z. Tang**, X. Pan, Y. Zheng, X. Wu, AC Zhou, B. He, X. Chu. Reliable and Efficient In-Memory Fault Tolerance of Large Language Model Pretraining. arXiv preprint arXiv:2310.12670.

- **Z. Tang**, Y. Wang, X. He, L. Zhang, X. Pan, Q. Wang, R. Zeng, K. Zhao, S. Shi, B. He, X. Chu. FusionAI: Decentralized Training and Deploying LLMs with Massive Consumer-Level GPUs. In IJCAI-LLM Workshop 2023.09.,

- **Z. Tang**, S. Shi, B. Li, X. Chu. GossipFL: A Decentralized Federated Learning Framework with Sparsified and Adaptive Communication. In IEEE Transactions on Parallel and Distributed Systems, 2022.

- X. He , J. Yao, Y. Wang, **Z. Tang**, C. K. Chun, S. Simon, B. Han, and X. Chu. NAS-LID: Efficient Neural Architecture Search with Local Intrinsic Dimension. In AAAI 2023.

- **Z. Tang\***, Y. Zhang\*, S. Shi, X. He, B. Han, X. Chu. Virtual Homogeneity Learning: Defending against Data Heterogeneity in Federated Learning. In Proceedings of the 39th International Conference on Machine Learning, 2022.

- C. He, A. D. Shah, **Peijie Dong**, D. Fan, A. N. Sivashunmugam, K. Bhogaraju, M. Shimpi, L. Shen, X. Chu, M. Soltanolkotabi and S. Avestimehr. FedCV: A Federated Learning Framework for Diverse Computer Vision Tasks. In FL-AAAI-22 workshop, 2022. [Best Paper Award]
- Z. Liao, H. Yan, **Z. Tang**, X. Chu, T. Tao. Deep learning identifies leak in water pipeline system using transient frequency response. In Process Safety and Environmental Protection 2021.

- **Z. Tang**, Zhikai Hu, Shaohuai Shi, Yiu-ming Cheung, Yilun Jin, Zhenghang Ren, Xiaowen Chu. Data Resampling for Federated Learning with Non-IID Labels. In FTL-IJCAI workshop, 2021.

- S. Shi, **Z. Tang**, X. Chu, C. Liu, W. Wang, and B. Li. A quantitative surveyof communication optimizations in distributed deep learning. IEEE Network,35(3):230–237, 2021.

- S. Shi, **Z. Tang**, Q. Wang, K. Zhao, and X. Chu. Layer-wise adaptive gradientsparsification for distributed deep learning with convergence guarantees. In ECAI 2020 \* 24th European Conference on Artificial Intelligence, pages 1467–1474. IOS Press, 2020.

- **Z. Tang**, S. Shi, and X. Chu. Communication-efficient decentralized learning withsparsification and adaptive peer selection. In ICDCS 2020.

- Y. Wang, Q. Wang, S. Shi, X. He, **Z. Tang**, K. Zhao, X. Chu. Benchmarking the Performance and Energy Efficiency of AI Accelerators for AI Training. In CCGRID 2020.

- **Z. Tang**, Y. Wang, Q. Wang, and X. Chu. The impact of gpu dvfs on the energy andperformance of deep learning: An empirical study. In Proceedings of the Tenth ACM International Conference on Future Energy Systems, e-Energy ’19.

- S. Shi, K. Zhao, Q. Wang, **Z. Tang**, and X. Chu. A convergence analysis ofdistributed sgd with communication-efficient gradient sparsification. IJCAI-19.

- S. Shi, Q. Wang, K. Zhao, **Z. Tang**, Y. Wang, X. Huang, and X. Chu. A distributedsynchronous sgd algorithm with global top-k sparsification for low bandwidthnetworks. In ICDCS 2019.

- X. Zhou, **Z. Tang**, W. Xu, F. Meng, X. Chu, K. Xin, and G. Fu. Deep learningidentifies accurate burst locations in water distribution networks. Water Research,166:115058, 2019.

- X. He, S. Wang, S. Shi, **Z. Tang**, Y. Wang, Z. Zhao, J. Dai, R. Ni, X. Zhang, X. Liu,Z. Wu, W. Yu, and X. Chu. Computer-aided clinical skin disease diagnosis usingcnn and object detection models. In 2019 IEEE International Conference on BigData (Big Data), pages 4839–4844, 2019.

## Preprint

- **Z. Tang**, X. Chu, R. Ran, S. Lee, S. Shi, Y. Zhang, Y. Wang, A. Liang, S. Avestimehr, C. He. FedML Parrot: A Scalable Federated Learning System via Heterogeneity-aware Scheduling on Sequential and Hierarchical Training. arXiv preprint arXiv:2303.01778.

- **Z. Tang**, S. Shi, X. Chu, W. Wang, and B. Li. Communication-efficient distributeddeep learning: A comprehensive survey. CoRR, abs/2003.06307, 2020. -->

<!--
[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun -->

<!--
[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
</div>
</div> -->

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=A14sfU1mQ29eKVjBuoPG6sP2CDJtNGaWlvKC81sqnrg&cl=ffffff&w=a"></script>
