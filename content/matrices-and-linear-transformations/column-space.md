---
title: Column Space
---

The column space of a matrix $A$ is the set of all linear combinations of the columns of $A$.
Given a matrix $A$ with columns $\mathbf{a_1}, \mathbf{a_2}, \ldots, \mathbf{a_n}$, the column space of $A$ is denoted as $\col(A)$ or $C(A)$.
The column space can be thought of as the [Span](/matrices-and-linear-transformations/span) of the columns of $A$, and it represents the set of all possible linear combinations of the columns.
For example, consider a $2 \times 2$ matrix:
$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
$$
The column space of $A$ is the set of all linear combinations of the columns:
$$
\col(A) = \{c_1\begin{pmatrix} 1 \\ 3 \end{pmatrix} + c_2\begin{pmatrix} 2 \\ 4 \end{pmatrix} : c_1, c_2 \in \mathbb{R}\}
$$
The column space has the following properties:
- **Subspace**: The column space is a subspace of the ambient space (e.g., $\mathbb{R}^2$ or $\mathbb{R}^3$).
- **Span**: The column space is the span of the columns of $A$.
- **Basis**: The columns of $A$ form a basis for the column space if and only if they are [linearly independent](/matrices-and-linear-transformations/linear-independence).
The column space is important in many applications, including:
- [Linear Transformation](/matrices-and-linear-transformations/linear-transformation): The column space represents the range of the linear transformation represented by $A$.
- Solving systems of linear equations: The column space is used to determine the consistency of a system of linear equations.
- Least squares: The column space is used in least squares regression to find the best-fitting line or hyperplane.