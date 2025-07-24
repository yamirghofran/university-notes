---
title: Cross Product
---

The cross product of two vectors $\mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$ is defined as:
$$
\mathbf{a} \times \mathbf{b} = \begin{pmatrix} a_2b_3 - a_3b_2 \\ a_3b_1 - a_1b_3 \\ a_1b_2 - a_2b_1 \end{pmatrix}
$$


The cross product is a vector that is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$. It is used to:
- Calculate the area of a parallelogram: $\|\mathbf{a} \times \mathbf{b}\| = \text{area of parallelogram}$
- Determine the direction of a normal vector: $\mathbf{a} \times \mathbf{b}$ is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$
- Calculate the torque of a force: $\mathbf{r} \times \mathbf{F} = \text{torque}$

## Cross Product and Determinant
The cross product of two vectors $\mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$ can be calculated using the [determinant](/matrices-and-linear-transformations/determinant) of a $3 \times 3$ matrix:
$$
\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}
$$
where $\mathbf{i}$, $\mathbf{j}$, and $\mathbf{k}$ are the unit vectors in the $x$, $y$, and $z$ directions, respectively.
Expanding the determinant, we get:
$$
\mathbf{a} \times \mathbf{b} = \mathbf{i}(a_2b_3 - a_3b_2) - \mathbf{j}(a_1b_3 - a_3b_1) + \mathbf{k}(a_1b_2 - a_2b_1)
$$
This is equivalent to the cross product formula:
$$
\mathbf{a} \times \mathbf{b} = \begin{pmatrix} a_2b_3 - a_3b_2 \\ a_3b_1 - a_1b_3 \\ a_1b_2 - a_2b_1 \end{pmatrix}
$$
The determinant formulation of the cross product provides a convenient way to calculate the cross product of two vectors, and it also provides a geometric interpretation of the cross product as a vector that is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$.
Note that the determinant formulation of the cross product can be extended to higher dimensions, and it provides a powerful tool for calculating the cross product of vectors in higher-dimensional spaces.
Example
Consider the vectors $\mathbf{a} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$. The cross product of $\mathbf{a}$ and $\mathbf{b}$ can be calculated using the determinant formulation:
$$
\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 3 \\ 4 & 5 & 6 \end{vmatrix} = \mathbf{i}(2 \cdot 6 - 3 \cdot 5) - \mathbf{j}(1 \cdot 6 - 3 \cdot 4) + \mathbf{k}(1 \cdot 5 - 2 \cdot 4)
$$
Evaluating the determinant, we get:
$$
\mathbf{a} \times \mathbf{b} = \mathbf{i}(12 - 15) - \mathbf{j}(6 - 12) + \mathbf{k}(5 - 8) = \begin{pmatrix} -3 \\ 6 \\ -3 \end{pmatrix}
$$
This is the cross product of $\mathbf{a}$ and $\mathbf{b}$.

## Example
![](../attachments/cleanshot-2025-03-25-at-1107542x.png)