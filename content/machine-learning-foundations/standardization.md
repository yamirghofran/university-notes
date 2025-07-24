---
title: Standardization
---

aka z-score [[Y2Q2/Machine Learning Foundations/Normalization|Normalization]]
-   Procedure to rescale the feature values to have the properties of a standard normal distribution with sample mean $\mu = 0$ and standard deviation from the sample mean $\sigma = 1$.
-   Standardization formula:

  $$
  \hat{x}^{(j)} \leftarrow \frac{x^{(j)} - \mu^{(j)}}{\sigma^{(j)}}
  $$

  where $\mu^{(j)}$ is the sample mean of the values of feature $j$, and $\sigma^{(j)}$ is the standard deviation of the values of feature $j$ from the sample mean.
