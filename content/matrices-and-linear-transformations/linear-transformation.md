---
title: Linear Transformation
---

A linear transformation is a function $T$ between two vector spaces $V$ and $W$ that satisfies:
$$T(a\mathbf{v} + b\mathbf{u}) = aT(\mathbf{v}) + bT(\mathbf{u})$$
where $a$ and $b$ are scalars, and $\mathbf{v}$ and $\mathbf{u}$ are vectors in $V$.
Defined by where it takes the [Basis](/matrices-and-linear-transformations/basis) vectors.  
In other words, a linear transformation preserves the operations of vector addition and scalar multiplication.
The formula can be broken down into two parts:
1.	**Additivity**: $T(\mathbf{v} + \mathbf{u}) = T(\mathbf{v}) + T(\mathbf{u})$
2.	**Homogeneity**: $T(a\mathbf{v}) = aT(\mathbf{v})$
This formula ensures that the transformation is linear, meaning that it can be represented by a matrix.
For example, a linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ can be represented by a $2 \times 2$ matrix:
$$T\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} ax + by \\ cx + dy \end{pmatrix}$$