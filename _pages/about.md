---
permalink: /
title: ""
excerpt: ""
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


I am a **third-year Ph.D. candidate (expected: 2028)** of Computer Science at **[College of Electron and Computer Engineering](https://www.ece.pku.edu.cn/index.htm)**, **[Peking University (PKU)](https://www.pku.edu.cn/)**, advised by Prof. **[Li Yuan (PKU, 袁粒)](https://yuanli2333.github.io/)**. 

<!-- Before this, I got a B.E. degree of Computer Science at [College of Information Engineering](https://xxgc.sicau.edu.cn/), [Sichuan Agricultural University(SICAU)](https://www.sicau.edu.cn/). -->

My research interest includes multi-modal understanding, multi-modal generation and large unified model. <a href='https://scholar.google.com/citations?user=GCOVDKoAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
 
My huggingface at 🤗 [Huggingface home](https://huggingface.co/LanguageBind).



# 🔥 News
<!-- Allowed emojis: 🎉🎉for good news 📣📣for average news-->
- **2025.06**: &nbsp;📣📣 The <a href='https://github.com/PKU-YuanGroup/Open-Sora-Plan'>Open-Sora Plan</a> has released version 1.5 and reached **12,000 stars** on GitHub. At the same time, we are launching <a href='https://github.com/PKU-YuanGroup/UniWorld-V1'>UniWorld-V1</a>!
- **2025.03**: &nbsp;📣📣 Thrilled that <a href='https://github.com/PKU-YuanGroup/Video-LLaVA'>Video-LLaVA</a> ranks in **Top 1** of the <a href='https://resources.paperdigest.org/2025/03/most-influential-emnlp-papers-2025-03-version'>Most Influential EMNLP 2025 Papers</a>！
- **2025.02**: &nbsp;🎉🎉 One paper have been accepted by **CVPR 2025**! <a href='https://github.com/PKU-YuanGroup/WF-VAE'>WF-VAE</a>！
- **2025.01**: &nbsp;📣📣 Honored as [one of the most impactful users](https://huggingface.co/spaces/mvaloatto/TCTF) in the 🤗 Hugging Face community: ranked among the top 100 for **Spaces Likes** for 12 consecutive months (2024.02–2025.01), and for **Models Downloads** across 11 months, for **Datasets Downloads** for 2 months (2024.12–2025.01).
- **2024.09**: &nbsp;🎉🎉 One paper have been accepted by **EMNLP 2025**! <a href='https://github.com/PKU-YuanGroup/Video-LLaVA'>Video-LLaVA</a>！
- **2024.03**: &nbsp;📣📣 We launch a plan to create a simple and scalable repo, <a href='https://github.com/PKU-YuanGroup/Open-Sora-Plan'>Open-Sora Plan</a>, to reproduce Sora！
- **2024.01**: &nbsp;🎉🎉 One paper have been accepted by **ICLR 2024**! <a href='https://github.com/PKU-YuanGroup/LanguageBind'>LanguageBind</a>！
- **2023.06**: &nbsp;📣📣 I successfully completed my undergraduate studies from the College of Information Engineering, Sichuan Agricultural University!


# 📝 Selected Publications
*: Co-First Author, Equal Contribution




<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/open-sora-plan.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Open-Sora Plan: Open-Source Large Video Generation Model](https://arxiv.org/abs/2412.00131)

**Bin Lin\***, Yunyang Ge\*, Xinhua Cheng\*, Zongjian Li, Bin Zhu, Shaodong Wang, Xianyi He, Yang Ye, Shenghai Yuan, Liuhan Chen, Tanghui Jia, Junwu Zhang, Zhenyu Tang, Yatian Pang, Bin She, Cen Yan, Zhiheng Hu, Xiaoyi Dong, Lin Chen, Zhang Pan, Xing Zhou, Shaoling Dong, Yonghong Tian, Li Yuan. 【<span class='show_paper_citations' data='GCOVDKoAAAAJ:YOwf2qJgpHMC'></span>】 <br>
<b style="color: #ff0000;">The first open-source 3D full-attention video generation model.</b>

<b style="color: #ff0000;">The first open-source causal VAE for video.</b>

[![arXiv](https://img.shields.io/badge/Arxiv-2412.00131-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2412.00131)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/Open-Sora-Plan)


<a href="https://trendshift.io/repositories/8280" target="_blank"><img src="https://trendshift.io/api/badge/repositories/8280" alt="PKU-YuanGroup%2FOpen-Sora-Plan | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>
</div>





<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/uniworld-v1.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UniWorld-V1: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation](https://arxiv.org/abs/2506.03147)

**Bin Lin**, Zongjian Li, Xinhua Cheng, Yuwei Niu, Yang Ye, Xianyi He, Shenghai Yuan, Wangbo Yu, Shaodong Wang, Yunyang Ge, Yatian Pang, Li Yuan 【2025.06】 <br>

<b style="color: #ff0000;">2.7M samples enable 20+ tasks, including visual understanding, generation, and manipulation.</b>

[![arXiv](https://img.shields.io/badge/Arxiv-2506.03147-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2506.03147)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/UniWorld-V1?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/UniWorld-V1)

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP2025</div><img src='images/video-llava.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Video-LLaVA: Learning United Visual Representation by Alignment Before Projection](https://arxiv.org/abs/2311.10122)

**Bin Lin**, Yang Ye, Bin Zhu, Jiaxi Cui, Munan Ning, Peng Jin, Li Yuan 【2023.11】 <br>


<b style="color: #ff0000;">Top 1 of the <a href='https://resources.paperdigest.org/2025/03/most-influential-emnlp-papers-2025-03-version'>Most Influential EMNLP 2025 Papers</a>！</b>


[![arXiv](https://img.shields.io/badge/Arxiv-2311.10122-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2311.10122)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/Video-LLaVA?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/Video-LLaVA)

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/moe-llava.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MoE-LLaVA: Mixture of Experts for Large Vision-Language Models](https://arxiv.org/abs/2401.15947)

**Bin Lin**, Zhenyu Tang, Yang Ye, Jinfa Huang, Junwu Zhang, Yatian Pang, Peng Jin, Munan Ning, Jiebo Luo, Li Yuan 【2024.01】 <br>
[![arXiv](https://img.shields.io/badge/Arxiv-2401.15947-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2401.15947)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/MoE-LLaVA?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/MoE-LLaVA)

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR2025</div><img src='images/wf-vae.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[WF-VAE: Enhancing Video VAE by Wavelet-Driven Energy Flow for Latent Video Diffusion Model](https://arxiv.org/abs/2411.17459)

Zongjian Li\*, **Bin Lin\***, Yang Ye, Liuhan Chen, Xinhua Cheng, Shenghai Yuan, Li Yuan 【2024.11】 <br>
[![arXiv](https://img.shields.io/badge/Arxiv-2411.17459-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2411.17459)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/WF-VAE?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/WF-VAE)

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR2024</div><img src='images/languagebind.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LanguageBind: Extending Video-Language Pretraining to N-modality by Language-based Semantic Alignment](https://arxiv.org/abs/2310.01852)

Bin Zhu\*, **Bin Lin\***, Munan Ning, Yang Yan, Jiaxi Cui, HongFa Wang, Yatian Pang, Wenhao Jiang, Junwu Zhang, Zongwei Li, Wancai Zhang, Zhifeng Li, Wei Liu, Li Yuan 【2023.10】 <br>
[![arXiv](https://img.shields.io/badge/Arxiv-2310.01852-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2310.01852)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/LanguageBind?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/LanguageBind)

</div>
</div>

&nbsp;

My full paper list is shown at [my google scholar](https://scholar.google.com/citations?user=GCOVDKoAAAAJ&hl=en).


- ``Nature Communications`` [BASALT refines binning from metagenomic data and increases resolution of genome-resolved metagenomic analysis](https://arxiv.org/abs/2404.05014), Zhiguang Qiu, Li Yuan, Chun-Ang Lian, **Bin Lin**, et al. [![website](https://img.shields.io/badge/Paper-BASALT-orange?logo=homepage)](https://www.nature.com/articles/s41467-024-46539-7) 

- ``TPAMI`` [MagicTime: Time-lapse Video Generation Models as Metamorphic Simulators](https://arxiv.org/abs/2404.05014), Shenghai Yuan, Jinfa Huang, Yujun Shi, Yongqi Xu, Ruijie Zhu, **Bin Lin**, et al. [![arXiv](https://img.shields.io/badge/Arxiv-2404.05014-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2406.04325)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/MagicTime?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/MagicTime)

- ``ICME 2025`` [OD-VAE: An Omni-dimensional Video Compressor for Improving Latent Video Diffusion Model](https://arxiv.org/abs/2409.01199), Liuhan Chen, Zongjian Li, **Bin Lin**, et al. [![arXiv](https://img.shields.io/badge/Arxiv-2409.01199-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2402.17156)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/Open-Sora-Plan)

- ``NeurIPS 2024`` [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://arxiv.org/abs/2406.04325), Lin Chen, Xilin Wei, Jinsong Li, Xiaoyi Dong, Pan Zhang, Yuhang Zang, Zehui Chen, Haodong Duan, **Bin Lin**, et al. [![arXiv](https://img.shields.io/badge/Arxiv-2406.04325-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2406.04325)   [![](https://img.shields.io/github/stars/ShareGPT4Omni/ShareGPT4Video?style=social&label=Code+Stars)](https://github.com/ShareGPT4Omni/ShareGPT4Video)

- ``NeurIPS 2024 Workshop`` [TaxDiff: Taxonomic-Guided Diffusion Model for Protein Sequence Generation](https://arxiv.org/abs/2402.17156), Lin Zongying, Li Hao, Lv Liuzhenghao, **Bin Lin**, et al. [![arXiv](https://img.shields.io/badge/Arxiv-2402.17156-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2402.17156)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/TaxDiff?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/TaxDiff)

- ``Preprint`` [WISE: A World Knowledge-Informed Semantic Evaluation for Text-to-Image Generation](https://arxiv.org/abs/2503.07265), Yuwei Niu, Munan Ning, Mengren Zheng, **Bin Lin**, et al. [![arXiv](https://img.shields.io/badge/Arxiv-2503.07265-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2503.07265)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/WISE?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/WISE)

- ``Preprint`` [ImgEdit: A Unified Image Editing Dataset and Benchmark](https://arxiv.org/abs/2505.20275), Yang Ye\*, Xianyi He\*, Zongjian Li\*, **Bin Lin\***, et al. [![arXiv](https://img.shields.io/badge/Arxiv-2503.07265-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2505.20275)   [![](https://img.shields.io/github/stars/PKU-YuanGroup/ImgEdit?style=social&label=Code+Stars)](https://github.com/PKU-YuanGroup/ImgEdit)


# 🎖️ Honors and Awards
- **2023.06** Excellent graduates from Sichuan Province, China.
- **2022.10** National Scholarship (The highest scholarship awarded by the Ministry of Education, China).
- **2022.11** National First Prize of National Undergraduate Mathematical Modeling Contest.
- **2020.12** Outstanding Student of Sichuan Agricultural University (10 students).
- **2021.10** National Scholarship (The highest scholarship awarded by the Ministry of Education, China).


# 📖 Educations
- **2023.09 - now (expected: 2028)**, Ph.D. candidate, College of Electron and Computer Engineering, Peking University.
- **2019.09 - 2023.06**, Undergraduate, College of Information Engineering, Sichuan Agricultural University
