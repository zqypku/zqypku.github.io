---
layout: page
title: "Peering Behind the Shield: Guardrail Identification in Large Language Models"
description:
img:
importance: 1
category: work
related_publications: false
toc:
  beginning: true
paper_url: https://arxiv.org/abs/2502.01241
# code_url:
venue: "AAAI 2026 TrustAgent Workshop & AICS Workshop"
---

**Ziqing Yang**<sup>1</sup>, **Yixin Wu**<sup>1</sup>, **Rui Wen**<sup>2</sup>, **Michael Backes**<sup>1</sup>, **Yang Zhang**<sup>1</sup>

<sup>1</sup>CISPA Helmholtz Center for Information Security
<sup>2</sup>Institute of Science Tokyo

**{{ page.venue }}**

## Resources

[Paper]({{ page.paper_url }}) | [Code]({{ page.code_url }})

## Contents

- [Motivation](#motivation)
- [Main Contributions](#main-contributions)
- [Method](#method)
- [Results](#results)
- [Citation](#citation)

## Motivation

AI agents rely on safety guardrails to block harmful behavior. In practice, these guardrails are hidden: users and attackers do not know which guardrail is deployed or how it operates.

An attacker without this knowledge is like someone trying to break into a house without knowing the key, so that attacks are inefficient and unreliable. Once the guardrail is identified, however, guard-specific attacks become far more effective.

Despite their importance, guardrails are treated as black-box components, and existing model identification methods fail to reveal them. This raises a key question:

- Can we identify the guardrail deployed inside a black-box AI agent?

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/1_guard/motivation.png" title="motivation" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    An attacker who does not know the guardrail is like someone trying to break into a house without knowing the key.
</div>

## Main Contributions

- First formulation of the guardrail identification problem
- AP-Test: a novel guardrail identification framework
- Unified identification of input and output guardrails
- Match Score: a principled decision metric
- Extensive empirical validation

## Method

AP-Test identifies guardrails in two phases:

- Adversarial Prompt Optimization
- Adversarial Prompt Testing

The core idea is to generate prompts that are unsafe for one specific guardrail while remaining safe for all others, then observe how a black-box AI agent responds.

## Results

AP-Test achieves perfect identification performance across a wide range of settings:

- Candidate Guardrails: WildGuard, LlamaGuard, LlamaGuard2, LlamaGuard3
- Base LLMs: Llama 3.1, GPT-4o
- Deployment Modes: Input guard, output guard, and combined input–output guards

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/1_guard/overview.png" title="Overview of an AI agent" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/1_guard/framework.png" title="Framework" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left: Overview of an AI agent. Right: Framework of our AP-Test.
</div>

#### Key Findings

- 100% classification accuracy and AUC = 1.00 for both input and output guard tests
- Robust to safety-aligned LLM behavior and additional guardrails
- Successfully identifies derivative guardrails (e.g., fine-tuned variants)
- Ablation studies confirm the necessity of each method component

These results demonstrate that AP-Test provides a practical and reliable path toward understanding and auditing real-world AI safety mechanisms.

## Citation

If you find this work useful, please cite:

**Formatted Citation:**

{% reference YWWBZ26 %}

**BibTeX:**

```bibtex
@inproceedings{YWWBZ26,
  author = {Ziqing Yang and Yixin Wu and Rui Wen and Michael Backes and Yang Zhang},
  title = {Peering Behind the Shield: Guardrail Identification in Large Language Models},
  booktitle = {The AAAI Workshop on Artificial Intelligence for Cyber Security (AICS)},
  publisher = {AAAI},
  arxiv = {2502.01241},
  pdf = {https://openreview.net/pdf?id=4lwwnbpkos},
  year = {2026}
}
```

{% if page.related_publications %}
{% bibliography --cited_in_order %}
{% endif %}
