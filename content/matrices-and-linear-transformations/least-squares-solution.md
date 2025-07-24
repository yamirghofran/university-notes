---
title: Least Squares Solution
---

Suppose $A\mathbf{x} = \mathbf{b}$ has no solution.
We can compute an approximate solution by determining the least-squares solution.
Let $A$ be the $m \times n$ matrix and $\mathbf{b}$ a vector in $\mathbb{R}^m$.
A least-squares solution of $A\mathbf{x} = \mathbf{b}$ are the solutions to $A^T A \hat{\mathbf{x}} = A^T \mathbf{b}$.
**Steps:**
1. Compute $A^T A$ and $A^T \mathbf{b}$.
2. Form augmented matrix $[A^T A | A^T \mathbf{b}]$ for equation $A^T A \hat{\mathbf{x}} = A^T \mathbf{b}$.
3. Find RREF of $[A^T A | \mathbf{b}']$ where $\mathbf{b}' = A^T \mathbf{b}$.
4. $\hat{\mathbf{x}}$ least squares solution to $A'\hat{\mathbf{x}} = \mathbf{b}'$ is the best approximation to $A\mathbf{x} = \mathbf{b}$.
5. The approximation error is $\|\mathbf{b} - A\hat{\mathbf{x}}\|$.

## Exercise
![](../attachments/cleanshot-2025-03-25-at-1141132x.png)
![](../attachments/cleanshot-2025-03-25-at-1141322x.png)
![](../attachments/cleanshot-2025-03-25-at-1141412x.png)