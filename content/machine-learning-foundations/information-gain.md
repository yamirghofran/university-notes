---
title: Information Gain
---

The reduction in [entropy](/machine-learning-foundations/entropy) or [Gini](/machine-learning-foundations/gini-index) impurity after a split.
$$\text{Information Gain} = \text{Entropy}_{\text{before}} - \sum_{j=1}^{m} \frac{|S_j|}{|S|} \text{Entropy}_{\text{after}}$$
where $S_j$ is the subset of data after the split.