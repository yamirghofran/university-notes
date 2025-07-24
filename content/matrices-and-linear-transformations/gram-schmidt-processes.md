---
title: Gram-Schmidt Processes
---

Let vectors $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$ construct [Orthogonal](/matrices-and-linear-transformations/orthogonality) vectors $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ and then [Orthonormal](/matrices-and-linear-transformations/orthonormal-vectors) vectors $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$.
![](../attachments/cleanshot-2025-03-25-at-1223102x.png)
![](../attachments/cleanshot-2025-03-25-at-1223522x.png)
$$\mathbf{v}_1 = \mathbf{u}_1 \rightarrow \mathbf{q}_1 = \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|}$$
$$\mathbf{v}_2 = \mathbf{u}_2 - \frac{\mathbf{v}_1^T \mathbf{u}_2}{\mathbf{v}_1^T \mathbf{v}_1} \mathbf{v}_1 \rightarrow \mathbf{q}_2 = \frac{\mathbf{v}_2}{\|\mathbf{v}_2\|}$$
$$\mathbf{v}_3 = \mathbf{u}_3 - \frac{\mathbf{v}_1^T \mathbf{u}_3}{\mathbf{v}_1^T \mathbf{v}_1} \mathbf{v}_1 - \frac{\mathbf{v}_2^T \mathbf{u}_3}{\mathbf{v}_2^T \mathbf{v}_2} \mathbf{v}_2 \rightarrow \mathbf{q}_3 = \frac{\mathbf{v}_3}{\|\mathbf{v}_3\|}$$
## Exercise
- Let vectors $\mathbf{u}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, $\mathbf{u}_2 = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}$. Find vectors $\mathbf{q}_1, \mathbf{q}_2$ and matrix $Q$.
	- ![](../attachments/cleanshot-2025-03-25-at-1226272x.png)
