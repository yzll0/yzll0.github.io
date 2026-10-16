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

**Research interests:** LLM post-training with verifiable feedback (formal specifications, executable checks); agent harnesses for mathematical and algorithmic research; formal verification in Lean 4.

**Available for internships** from January 2027 (3–6 months, location flexible).

## Education

**ETH Zürich — Ph.D. in Computer Science** <span class="cv-date">May 2025–Present</span>  
Advisor: Prof. Rasmus Kyng. Research Assistant in the same group, October 2024–April 2025.

**ETH Zürich — M.Sc. in Data Science** <span class="cv-date">September 2022–October 2024</span>  
Willi Studer Prize (2025), awarded to the best graduate of the M.Sc. in Data Science program.

**Xi'an Jiaotong University — B.Sc. in Mathematics** <span class="cv-date">September 2018–July 2022</span>  
Honors Youth Program

## Selected Research

### AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions

Co-first author · under review at ICLR 2027. Training LLMs to translate natural-language programming problems into formal specifications in Lean.

- Proposed *executable postconditions*: an executable counterpart of each declarative Lean specification that can be checked on any test case via `#guard`, turning specification correctness into a cheap automatic signal for data filtering and a core component of the RL reward.
- Co-designed the Lean specification format and co-built a multistage LLM pipeline for specification synthesis, verification, and repair, producing 3,037 formalized programming problems and ~19.5K SFT samples.
- Reviewed 300 benchmark problems and audited 60 model-generated specifications.
- With SFT + RL, a 27B model improved SpecGen pass@4 from 0.7% to 60.3% on AuXSpec-Test and from 21.9% to 84.7% on Verina.

### Deterministic Gomory–Hu Trees — FOCS 2025

Co-authored the first deterministic almost-linear-time algorithm for Gomory–Hu trees (all-pairs minimum cuts), running in <i>m</i><sup>1+o(1)</sup> time on graphs with <i>m</i> edges. Presented the paper with Wuwei Yuan at FOCS 2025. [[slides](https://ywwywwyww.github.io/files/DeterGHTreeSlides.pdf)]

## Publications

**AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions**  
Co-first author. Under review at ICLR 2027; manuscript not yet publicly available.

**Deterministic Almost-Linear-Time Gomory-Hu Trees**  
Amir Abboud, Rasmus Kyng, Jason Li, Debmalya Panigrahi, Maximilian Probst Gutenberg, Thatchaphol Saranurak, **Weixuan Yuan**, Wuwei Yuan.  
*IEEE Symposium on Foundations of Computer Science (FOCS 2025)*. Authors listed alphabetically. [[paper](https://arxiv.org/abs/2507.20354)]

**Statistics (undergraduate work, before 2023; <sup>†</sup> equal contribution)**  
Xuehu Zhu<sup>†</sup>, **Weixuan Yuan**<sup>†</sup>, Zongben Xu, Wenlin Dai. Optimal subsampling for principal component analysis. *Science China Mathematics* 68, 2993–3016, 2025. [[paper](https://doi.org/10.1007/s11425-023-2343-7)]  
Xinru Jia<sup>†</sup>, **Weixuan Yuan**<sup>†</sup>, Xingqiu Zhao, Xuehu Zhu. Optimal subsampling for estimation of dimension reduction directions. *Scandinavian Journal of Statistics* 53(1), 575–611, 2026. [[paper](https://doi.org/10.1111/sjos.70052)]

## Technical Skills

**Programming:** Python, Lean 4.  
**Theory:** Algorithms; probability and statistics; optimization, including gradient-based methods.
