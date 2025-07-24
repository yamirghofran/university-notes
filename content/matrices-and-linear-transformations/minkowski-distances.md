---
title: Minkowski Distances
---

Given two points $x = (x_1, x_2, \ldots, x_n)$ and $y = (y_1, y_2, \ldots, y_n)$ in $\mathbb{R}^n$, the Minkowski distance of order $p$ is defined as:
$$d_p(x, y) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{\frac{1}{p}}$$
![](../attachments/cleanshot-2025-01-14-at-1206482x.png)
## Special Cases
- Euclidean distance ($p = 2$): $d_2(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$
- Manhattan distance ($p = 1$): $d_1(x, y) = \sum_{i=1}^{n} |x_i - y_i|$
- Chebyshev distance ($p = \infty$): $d_\infty(x, y) = \max_{i=1}^{n} |x_i - y_i|$
## Properties
- The Minkowski distance is a metric, meaning it satisfies the properties of non-negativity, symmetry, and triangle inequality.
- The Minkowski distance is sensitive to the choice of $p$, with smaller values of $p$ giving more weight to smaller differences and larger values of $p$ giving more weight to larger differences.
## Applications
Minkowski distances are used in various fields, including:
- Data analysis and machine learning
- Image and signal processing
- Clustering and classification algorithms
- Optimization problems