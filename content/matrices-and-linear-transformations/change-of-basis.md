---
title: Change of Basis
---

Given two bases $\mathcal{B}$ and $\mathcal{C}$ of a vector space $V$, a change of basis from $\mathcal{B}$ to $\mathcal{C}$ involves expressing the vectors of $\mathcal{B}$ as linear combinations of the vectors of $\mathcal{C}$.

The change of basis matrix $P$ from $\mathcal{B}$ to $\mathcal{C}$ is a matrix whose columns are the coordinate vectors of the vectors of $\mathcal{B}$ with respect to the basis $\mathcal{C}$.
## Example
Suppose we have two bases $\mathcal{B} = \{(1, 0), (0, 1)\}$ and $\mathcal{C} = \{(2, 1), (1, 1)\}$ of $\mathbb{R}^2$. To find the change of basis matrix $P$ from $\mathcal{B}$ to $\mathcal{C}$, we need to express the vectors of $\mathcal{B}$ as linear combinations of the vectors of $\mathcal{C}$.
Let's find the coordinate vectors of $(1, 0)$ and $(0, 1)$ with respect to the basis $\mathcal{C}$:
- $(1, 0) = a(2, 1) + b(1, 1)$
- $(0, 1) = c(2, 1) + d(1, 1)$
Solving these equations, we get:
- $a = \frac{1}{1}$, $b = -\frac{2}{1}$
- $c = \frac{1}{1}$, $d = -\frac{1}{1}$
So, the change of basis matrix $P$ is:
$$
P = \begin{pmatrix}
1 & 1 \\
2 & -1
\end{pmatrix}
$$

## Importance
The change of basis matrix $P$ can be used to:
- Express a vector in a new basis
- Find the matrix representation of a linear transformation with respect to a new basis
Note that the change of basis matrix $P$ is invertible, and its inverse $P^{-1}$ represents the change of basis from $\mathcal{C}$ to $\mathcal{B}$.