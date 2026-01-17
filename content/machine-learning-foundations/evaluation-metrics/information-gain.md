---
title: Information Gain
---

The reduction in [Entropy](/machine-learning-foundations/evaluation-metrics/entropy) or [Gini](/machine-learning-foundations/evaluation-metrics/gini-index) impurity after a split.
$$\text{Information Gain} = \text{Entropy}_{\text{before}} - \sum_{j=1}^{m} \frac{|S_j|}{|S|} \text{Entropy}_{\text{after}}$$
where $S_j$ is the subset of data after the split.