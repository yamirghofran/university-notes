---
title: Discounted Cumulative Gain
---

- Measures the usefulness, or gain, of a result item based on its position in the result list.
- Gain is accumulated from the top to the bottom of the result list, with the gain of each result discounted at the lower positions.
- Assumption: Highly relevant documents are more useful when appearing earlier in the result list.
- For a given search result, DCG accumulated at a particular rank position $p$ is:
$$
DCG_p \overset{\text{def}}{=} \sum_{i=1}^{p} \frac{rel_i}{\log_2(i + 1)}
$$
## Assumptions
1. Highly relevant documents are more useful when appearing earlier in the result list.
2. Highly relevant documents are more useful than marginally relevant documents, while the latter, in turn, are more useful than non-relevant documents.