---
title: Cumulative Gain
---

- Sum of the graded relevance values of all results in a search result list. CG at a particular rank position $p$ is $CG_p = \sum_{i=1}^{p} rel_i$, where $rel_i$ is the graded relevance of the result at position $i$.
- $rel_i$ is numeric, e.g., ranging between $[0, 1]$.
- Note: $CG_p$ is independent of each document's position in the ranked result list. It only characterizes the documents ranked up to position $p$ as relevant or irrelevant to the query.
$$
CG_p \overset{\text{def}}{=} \sum_{i=1}^{p} rel_i
$$
---
- [Discounted Cumulative Gain](/machine-learning-foundations/evaluation-metrics/discounted-cumulative-gain)

```python
def calculate_cumulative_gain(relevance_scores):
    cumulative_gain = []
    current_sum = 0
    for score in relevance_scores:
        current_sum += score
        cumulative_gain.append(current_sum)
    return cumulative_gain

```
