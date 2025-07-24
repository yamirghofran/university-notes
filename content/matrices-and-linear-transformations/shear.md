---
title: Shear
---

A **shear** is a [linear transformation](/matrices-and-linear-transformations/linear-transformation) that "slides" a vector or object by a certain amount in a certain direction, while keeping it parallel to its original orientation. In 2D, a shear can be represented by a matrix:
$$
S(a, b) = \begin{pmatrix} 1 & a \\ b & 1 \end{pmatrix}
$$
where $a$ and $b$ are the shear factors in the $x$ and $y$ directions, respectively.
For example, shearing a vector $\begin{pmatrix} x \\ y \end{pmatrix}$ by a factor of $a$ in the $x$ direction and $b$ in the $y$ direction results in:
$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 1 & a \\ b & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + ay \\ bx + y \end{pmatrix}
$$
Note that rotation and shear are both linear transformations, meaning that they can be represented by matrices and can be composed together to form more complex transformations.
