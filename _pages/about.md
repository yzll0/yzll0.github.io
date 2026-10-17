---
permalink: /
title: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am Weixuan Yuan (袁伟轩), a Ph.D. student in Computer Science at ETH Zürich, advised by Prof. Rasmus Kyng. My research spans graph algorithms and AI for mathematics and theoretical computer science. On the AI side, I am interested in LLM reasoning, post-training with verifiable rewards, formal verification in Lean, and agent harnesses for mathematical and algorithmic research.

Before my Ph.D., I received an M.Sc. in Data Science from ETH Zürich (2024; ranked 1st, Willi Studer Prize) and a B.Sc. in Mathematics from Xi'an Jiaotong University (2022; Honors Youth Program).

**I am looking for research internships in post-training, AI for math, and agent harnesses, starting January 2027 (3–6 months; open to relocation).** See my [CV](/cv/) ([PDF](/files/Weixuan_Yuan_CV.pdf)).

## Selected research

**AuXSpec: autoformalizing program specifications.** Formal specifications are the basis of verified code generation, but it is hard to check whether a generated specification is actually correct. We train LLMs to translate natural-language programming problems into Lean specifications. The key idea is *executable postconditions*: each declarative specification comes with an executable counterpart that can be checked on any test case via `#guard`, giving a cheap, automatic correctness signal for filtering training data and for RL rewards. After SFT and RL, a 27B model reaches 60.3% pass@4 on AuXSpec-Test (from 0.7%) and 84.7% on Verina (from 21.9%). Co-first author; under review at ICLR 2027.

**Deterministic Gomory–Hu trees.** A Gomory–Hu tree compactly encodes the minimum cuts between all pairs of vertices. Our [FOCS 2025 paper](https://arxiv.org/abs/2507.20354) gives the first deterministic algorithm that constructs it in almost-linear time, <i>m</i><sup>1+o(1)</sup>, matching the best known randomized running time up to an <i>m</i><sup>o(1)</sup> factor. I presented the paper with Wuwei Yuan at FOCS 2025. [[slides](https://ywwywwyww.github.io/files/DeterGHTreeSlides.pdf)]

See my [selected publications](/publications/) for paper details and my [CV](/cv/) for research experience.
