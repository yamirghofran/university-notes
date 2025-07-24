---
title: Determinant
---

The determinant of a transformation is a scalar value that can be used to describe the scaling effect of the transformation on a region of space.
Given a $2 \times 2$ matrix:
$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$
The determinant of $A$ is denoted as $\det(A)$ or $|A|$ and is calculated as:
$$
\det(A) = ad - bc
$$
- Matrix is singular when $det(A) = 0$
- Notation: $det(A) = \abs{A}$
- Matrix is not singular or invertible when $det(A) \neq 0$
## Determinant Diagonal Method
Only works for matrices lower than 4x4.
![](../attachments/cleanshot-2025-03-24-at-2137152x.png)
![](../attachments/cleanshot-2025-03-24-at-2137452x.png)
## Determinant Properties
1. Det I = 1
2. Exchange Rows reverse sign: det P = 1 even or -1 odd
3. a)
   $$
   \begin{vmatrix}
   ta & tb \\
   c & d
   \end{vmatrix}
   = t
   \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
   $$
	b)
   $$
   \begin{vmatrix}
   a + a' & b + b' \\
   c & d
   \end{vmatrix}
   =
   \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
   +
   \begin{vmatrix}
   a' & b' \\
   c & d
   \end{vmatrix}
   $$
	3a and 3. b means linear each row
4. If 2 rows are equal then det = 0
   Exchange those rows equal so you have the same matrix. Determinant should change sign by property 2.
5. Subtract m times row i from row k then determinant doesn’t change:
   $$
   \begin{vmatrix}
   a & b \\
   c - ma & d - mb
   \end{vmatrix}
   =
   \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
   +
   \begin{vmatrix}
   a & b \\
-ma & -mb
   \end{vmatrix}
   = (by\ 3.b) =
   \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
   $$
6. Rows of zeros then Det A = 0
   $$
   \begin{vmatrix}
   0 & 0 \\
   c & d
   \end{vmatrix}
   = (by\ 3.a) =
   \begin{vmatrix}
   0 \cdot a & 0 \cdot b \\
   c & d
   \end{vmatrix}
   =
   \begin{vmatrix}
   0 & 0 \\
   c & d
   \end{vmatrix}
   $$
7. Determinant of Upper Triangular Matrix then determinant is the product of the elements of diagonal
   $$
   U =
   \begin{bmatrix}
   d_1 & * & * & * & * \\
   0 & d_2 & * & * & * \\
   0 & 0 & .. & * & * \\
   0 & .. & 0 & .. & * \\
   0 & .. & .. & 0 & d_n
   \end{bmatrix}
   \quad
   \text{det } U =
   \begin{bmatrix}
   d_1 & * & * & * & * \\
   0 & d_2 & * & * & * \\
   0 & 0 & .. & * & * \\
   0 & 0 & 0 & .. & * \\
   0 & .. & .. & 0 & d_n
   \end{bmatrix}
   = (d_1) \cdot (d_2) \cdot \cdots (d_n)
   $$
8. $\text{det } A = 0$ when $A$ is singular $\rightarrow$ row of zeros
   $\text{det } A \neq 0$ when $A$ is invertible
9. Det (AB) = (Det A)(Det B)
10. $\text{det } A^T = \text{det } A$
## Different Ways to Calculate Determinants

Let $A = \begin{bmatrix} 2 & 4 & 4 \\ 1 & 2 & 1 \\ 3 & -2 & 5 \end{bmatrix}$ then solve $\det A = \begin{vmatrix} 2 & 4 & 4 \\ 1 & 2 & 1 \\ 3 & -2 & 5 \end{vmatrix}$
- Using Diagonal formula
	- ![](../attachments/cleanshot-2025-03-25-at-1102172x.png)
- Using [Cofactors](/matrices-and-linear-transformations/cofactor-matrix) of Row 1
	- $\text{Det } A = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}$

	- ![](../attachments/cleanshot-2025-03-25-at-1102362x.png)
- Using [Cofactors](/matrices-and-linear-transformations/cofactor-matrix) of Column 3
	- $\text{Det } A = a_{13}C_{13} + a_{23}C_{23} + a_{33}C_{33}$
	- ![](../attachments/cleanshot-2025-03-25-at-1103002x.png)
## Applications
Hill Cipher