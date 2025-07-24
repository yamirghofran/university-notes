---
title: QR Factorization
---

From independent vectors $u_1 \cdots u_n$, [Gram-Schmidt](/matrices-and-linear-transformations/gram-schmidt-processes) constructs orthonormal vectors $q_1 \cdots q_n$ .
The matrices with these columns satisfy $A=QR$ where R is upper triangular.
$$A = QR \rightarrow Q = \begin{pmatrix} \vert & & \vert \\ \mathbf{q}_1 & \cdots & \mathbf{q}_n \\ \vert & & \vert \end{pmatrix}$$
$$R = Q^T A \quad \text{because} \quad Q^{-1} = Q^T$$
## Exercises
### Exercise 1
- Find the $QR$ factorization of $A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}$ $\mathbf{u}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \mathbf{u}_2 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \mathbf{u}_3 = \begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}$
	- ![](../attachments/cleanshot-2025-03-25-at-1231052x.png)
	- ![](../attachments/cleanshot-2025-03-25-at-1231212x.png)
		- ![](../attachments/cleanshot-2025-03-25-at-1231512x.png)
### Exercise 2
- Find the $QR$ factorization of $A = \begin{pmatrix} 1 & 2 & 4 \\ 0 & 0 & 5 \\ 0 & 3 & 6 \end{pmatrix}$
	- ![](../attachments/cleanshot-2025-03-25-at-1236112x.png)
