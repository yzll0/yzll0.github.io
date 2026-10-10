---
lang: zh-CN
translation_key: cv
layout: single
title: "简历"
permalink: /zh/cv/
author_profile: false
---

<div class="cv-download">CV: <a href="/files/Weixuan_Yuan_CV.pdf" lang="en" download>English PDF</a> | <a href="/files/Weixuan_Yuan_CV_zh.pdf" lang="zh-CN" download>中文 PDF</a></div>

# 袁伟轩 · Weixuan Yuan

瑞士苏黎世 · [weixuan.yuan@inf.ethz.ch](mailto:weixuan.yuan@inf.ethz.ch) · [yzll0.github.io](https://yzll0.github.io/zh/)

研究实习方向：LLM 推理与后训练、AI for Math / TCS。

## 教育与研究任职

**苏黎世联邦理工学院｜计算机科学博士在读** <span class="cv-date">2025年5月–至今</span>  
导师：Rasmus Kyng 教授。

**苏黎世联邦理工学院｜研究助理** <span class="cv-date">2024年10月–2025年4月</span>  
Rasmus Kyng 研究组。

**苏黎世联邦理工学院｜数据科学硕士** <span class="cv-date">2022年9月–2024年10月</span>  
Willi Studer Prize（2025），数据科学硕士项目第一名。

**西安交通大学｜数学学士（少年班）** <span class="cv-date">2018–2022</span>

## 代表性研究

### AuXSpec：用 LLM 形式化编程问题

研究如何训练 LLM，将自然语言编程题转化为刻画正确输出的形式化数学规格。

- 提出 executable-postcondition 的核心思路，用于高效检查模型生成的规格，并共同设计 Lean specification format。
- 与合作者共同开发基于 LLM 的多阶段数据合成、验证与修复流程。团队形成了 3,037 道形式化的 LeetCode 题目及约 19.5K 条 SFT 样本。
- 参与 post-training 方法、奖励设计的研究讨论及结果分析。团队的 27B 模型经 SFT/RL 后，在 AuXSpec-Test 和 Verina 上的 SpecGen pass@4 分别达到 60.3% 和 84.7%。

### 图算法 — FOCS 2025

参与提出首个确定性的近线性时间 Gomory-Hu 树算法，运行时间为 <i>m</i><sup>1+o(1)</sup>。我在 IEEE Symposium on Foundations of Computer Science（FOCS 2025）作了会议报告。[[报告幻灯片](https://ywwywwyww.github.io/files/DeterGHTreeSlides.pdf)]

## 代表性论文

**Deterministic Almost-Linear-Time Gomory-Hu Trees**  
Amir Abboud, Rasmus Kyng, Jason Li, Debmalya Panigrahi, Maximilian Probst Gutenberg, Thatchaphol Saranurak, **Weixuan Yuan**, Wuwei Yuan.  
*FOCS 2025*. [[论文](https://arxiv.org/abs/2507.20354)]

**Optimal subsampling for principal component analysis**  
Xuehu Zhu<sup>†</sup>, **Weixuan Yuan**<sup>†</sup>, Zongben Xu, Wenlin Dai.  
*Science China Mathematics* 68, 2993-3016, 2025. [[论文](https://doi.org/10.1007/s11425-023-2343-7)]

**Optimal subsampling for estimation of dimension reduction directions**  
Xinru Jia<sup>†</sup>, **Weixuan Yuan**<sup>†</sup>, Xingqiu Zhao, Xuehu Zhu.  
*Scandinavian Journal of Statistics* 53(1), 575-611, 2026. [[论文](https://doi.org/10.1111/sjos.70052)]

<sup>†</sup> 表示共同贡献。理论计算机科学论文的作者按姓名字母顺序排列。统计学研究均于本科期间（2023 年之前）完成。

## 审稿中的论文

**AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions**  
共同第一作者；ICLR 2027 审稿中。论文全文尚未公开。

## 技术与理论基础

**编程：** Python、Lean 4。  
**理论：** 算法、概率与统计、优化（包括基于梯度的方法）。
