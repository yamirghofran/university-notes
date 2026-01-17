---
title: Normalized Discounted Cumulative Gain
---

$$nDCG_p \overset{\text{def}}{=} \frac{DCG_p}{IDCG_p}$$
where IDCG is the ideal discounted cumulative gain.
$$\text{IDCG}_p \overset{\text{def}}{=} \sum_{i=1}^{|\text{REL}_p|} \frac{2^{rel_i} - 1}{\log_2(i + 1)},$$
