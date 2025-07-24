---
title: Orthonormal Vectors
---

- [Orthogonal vectors](/matrices-and-linear-transformations/orthogonality): $\mathbf{q}_i^T \mathbf{q}_j = 0$ if $i \neq j$
- Orthonormal vectors:
$$\mathbf{q}_i^T \mathbf{q}_j =
\begin{cases}
0 & \text{if } i \neq j \text{ (orthogonal vectors)} \\
1 & \text{if } i = j \text{ (unit vectors)}
\end{cases}$$
**Example:**
$\begin{bmatrix} 3 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 2 \end{bmatrix}$ are orthogonal but not orthonormal:
$$\mathbf{q}_1^T \mathbf{q}_2 = \begin{bmatrix} 3 & 0 \end{bmatrix} \begin{bmatrix} 0 \\ 2 \end{bmatrix} = 0 + 0 = 0$$
$$\mathbf{q}_1^T \mathbf{q}_1 = \begin{bmatrix} 3 & 0 \end{bmatrix} \begin{bmatrix} 3 \\ 0 \end{bmatrix} = 9 \neq 1 \quad \text{and} \quad \mathbf{q}_2^T \mathbf{q}_2 = \begin{bmatrix} 0 & 2 \end{bmatrix} \begin{bmatrix} 0 \\ 2 \end{bmatrix} = 4 \neq 1$$
