---
title: F-Score
---

Harmonic mean of [Precision](/machine-learning-foundations/evaluation-metrics/precision) and [Recall](/machine-learning-foundations/evaluation-metrics/recall), parametrized with a positive real number, chosen such that recall is considered $\beta$ times as important as precision.

-  $\beta=2$: recall twice as high as precision,
- $\beta=0.5$, weighs recall twice as low as precision.
$$\mathrm{F}_{\beta}=(1+\beta^{2})\times{\frac{\mathrm{precision}\times\mathrm{recall}}{(\beta^{2}\times\mathrm{precision})+\mathrm{recall}}}$$
