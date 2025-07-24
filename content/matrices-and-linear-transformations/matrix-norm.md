---
title: Matrix Norm
---

The norm of a [Matrix](/matrices-and-linear-transformations/matrix) is a non-negative number denoted by $\|A\|$. It is a measure of how large its elements are.

$$
A = \begin{bmatrix}
a_{11} & \cdots & a_{1n} \\
a_{21} & \cdots & a_{2n} \\
\vdots & \ddots & \vdots \\
a_{m1} & \cdots & a_{mn} \\
\end{bmatrix}
\quad A \in M_{m \times n} \text{ size of this matrix is } m \times n
$$

$a_{ij}$ is the Matrix element in row $i$ and column $j$

## Types

- 1 Norm $\|A\|_1 = \max_{1 \leq j \leq n} \left( \sum_{i=1}^{m} |a_{ij}| \right)$ - Maximum of the sum of absolute column elements.
- Infinite Norm $\|A\|_{\infty} = \max_{1 \leq i \leq m} \left( \sum_{j=1}^{n} |a_{ij}| \right)$  - Maximum of the sum of absolute row elements.
- Frobenius Norm $\|A\|_F = \sqrt{\sum_{i=1}^{m} \sum_{j=1}^{n} |a_{ij}|^2}$ Square root of the sum of the square of all elements.
