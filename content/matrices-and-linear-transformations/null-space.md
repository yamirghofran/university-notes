---
title: Null Space
---

The null space of a matrix $A$ is the set of all vectors $\mathbf{x}$ that satisfy the equation:
$$
A\mathbf{x} = \mathbf{0}
$$
The null space is denoted as $\null(A)$ or $N(A)$.
In other words, the null space is the set of all vectors that are mapped to the zero vector by the linear transformation represented by $A$.
For example, consider a $2 \times 2$ matrix:
$$
A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
$$
The null space of $A$ is the set of all vectors $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$ that satisfy the equation:
$$
\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$
This simplifies to:
$$
x_1 + x_2 = 0
$$
So, the null space of $A$ is the set of all vectors of the form:
$$
\mathbf{x} = \begin{pmatrix} x_1 \\ -x_1 \end{pmatrix} = x_1 \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$
The null space has the following properties:
- **Subspace**: The null space is a subspace of the ambient space (e.g., $\mathbb{R}^2$ or $\mathbb{R}^3$).
- **Kernel**: The null space is also known as the kernel of the linear transformation represented by $A$.
- **Trivial null space**: If the null space contains only the zero vector, it is said to be trivial.
The null space is important in many applications, including:
- Solving homogeneous systems of linear equations: The null space represents the set of all solutions to the homogeneous system $A\mathbf{x} = \mathbf{0}$.
- [Linear independence](/matrices-and-linear-transformations/linear-independence): The null space can be used to determine the linear independence of a set of vectors.
- Eigenvalues and eigenvectors: The null space is related to the eigenvalues and eigenvectors of a matrix.