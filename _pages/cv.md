---
layout: single
title: "CV"
permalink: /cv/
author_profile: false
redirect_from:
  - /resume
---

<div class="cv-download"><a href="/files/Weixuan_Yuan_CV.pdf">Open PDF</a> · <a href="/files/Weixuan_Yuan_CV.pdf" download>Download PDF</a></div>

# Weixuan Yuan

Zürich, Switzerland · [weixuan.yuan@inf.ethz.ch](mailto:weixuan.yuan@inf.ethz.ch) · [yzll0.github.io](https://yzll0.github.io/)

Research interests: LLM reasoning and post-training; AI for mathematics and theoretical computer science.

## Education & Research Positions

**ETH Zürich — Ph.D. in Computer Science** <span class="cv-date">May 2025–Present</span>  
Advisor: Prof. Rasmus Kyng.

**ETH Zürich — Research Assistant** <span class="cv-date">October 2024–April 2025</span>  
Rasmus Kyng's group.

**ETH Zürich — M.Sc. in Data Science** <span class="cv-date">September 2022–October 2024</span>  
Willi Studer Prize (2025), awarded to the best graduate of the M.Sc. in Data Science program.

**Xi'an Jiaotong University — B.Sc. in Mathematics** <span class="cv-date">September 2018–July 2022</span><br>
<small>Honors Youth Program</small>

## Selected Research

### AuXSpec — Formalizing Programming Problems with LLMs

We study LLM-based translation of natural-language programming problems into formal specifications in Lean.

- Proposed using executable postconditions to test generated specifications efficiently; co-designed the Lean specification format.
- Co-developed a multistage LLM-based pipeline for data synthesis, verification, and repair. The team produced 3,037 formalized LeetCode problems and approximately 19.5K SFT samples.
- Independently reviewed 300 benchmark problems and audited 60 model-generated specifications.
- Contributed to discussions on post-training methods and reward design, and to analysis of results. After SFT/RL, the team's 27B model achieved SpecGen pass@4 of 60.3% on AuXSpec-Test and 84.7% on Verina.

### Graph algorithms — FOCS 2025

Co-authored a paper giving the first deterministic almost-linear-time Gomory-Hu tree algorithm: <i>m</i><sup>1+o(1)</sup> time for graphs with <i>m</i> edges. Presented the paper with Wuwei Yuan at FOCS 2025. [[slides](https://ywwywwyww.github.io/files/DeterGHTreeSlides.pdf)]

## Selected Publications

**Deterministic Almost-Linear-Time Gomory-Hu Trees**  
Amir Abboud, Rasmus Kyng, Jason Li, Debmalya Panigrahi, Maximilian Probst Gutenberg, Thatchaphol Saranurak, **Weixuan Yuan**, Wuwei Yuan.  
*IEEE Symposium on Foundations of Computer Science (FOCS 2025)*. [[paper](https://arxiv.org/abs/2507.20354)]

**Optimal subsampling for principal component analysis**  
Xuehu Zhu<sup>†</sup>, **Weixuan Yuan**<sup>†</sup>, Zongben Xu, Wenlin Dai.  
*Science China Mathematics* 68, 2993-3016, 2025. [[paper](https://doi.org/10.1007/s11425-023-2343-7)]

**Optimal subsampling for estimation of dimension reduction directions**  
Xinru Jia<sup>†</sup>, **Weixuan Yuan**<sup>†</sup>, Xingqiu Zhao, Xuehu Zhu.  
*Scandinavian Journal of Statistics* 53(1), 575-611, 2026. [[paper](https://doi.org/10.1111/sjos.70052)]

<sup>†</sup> Equal contribution. FOCS authors are listed alphabetically. Statistics work dates to my undergraduate studies (before 2023).

## Under-Review Manuscript

**AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions**  
Co-first author; under review at ICLR 2027. Manuscript not yet publicly available.

## Technical Skills

**Programming:** Python, Lean 4.  
**Theory:** Algorithms; probability and statistics; optimization, including gradient-based methods.
