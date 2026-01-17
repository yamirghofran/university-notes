---
title: Ideal Discounted Cumulative Gain
---

- $REL_p$ is the ordered list of the documents relevant to the query up to position $p$.
- $REL_i$ is the ideal ranking, up to position $p$, that the algorithm/model should return.
- nDCG values for all queries are averaged to obtain a performance measure for a search engine, ranking algorithm, or model.
$$
IDCG_p \overset{\text{def}}{=} \sum_{i=1}^{|REL_p|} \frac{2^{rel_i} - 1}{\log_2(i + 1)}
$$