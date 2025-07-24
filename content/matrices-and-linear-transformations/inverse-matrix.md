---
title: Inverse Matrix
---

The inverse matrix of a square matrix $A$ is a matrix $A^{-1}$ that, when multiplied by $A$, produces the identity matrix $I$:
$$
AA^{-1} = A^{-1}A = I
$$
The inverse matrix exists only if the determinant of $A$ is non-zero:
$$
\det(A) \neq 0
$$
The inverse matrix can be used to:
- Solve systems of linear equations: $A\mathbf{x} = \mathbf{b}$ can be solved by multiplying both sides by $A^{-1}$: $\mathbf{x} = A^{-1}\mathbf{b}$
- Find the inverse transformation: If $A$ represents a linear transformation, $A^{-1}$ represents the inverse transformation.
For a $2 \times 2$ matrix:
$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$
The inverse matrix is:
$$
A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$
Note that the inverse matrix is **unique**, meaning that if $A$ has an inverse, it is the only matrix that satisfies the equation $AA^{-1} = I$.
## General Formula
- [Determinant](/matrices-and-linear-transformations/determinant)
$$A^{-1} = \frac{1}{\det A} C^T$$
$$\mathbf{x} = A^{-1} \mathbf{b}$$
$$\mathbf{x} = \frac{1}{\det A} C^T \mathbf{b}$$

## Example
![](../attachments/cleanshot-2025-03-25-at-1109572x.png)

## Properties
$$(A^T)^{-1} = (A^{-1})^T$$
$$(AB)^{-1} = B^{-1}A^{-1}$$
$$(A^{-1})^{-1} = A.$$
