---
title: Rank
---

Number of dimensions in the output of a [transformation](/matrices-and-linear-transformations/linear-transformation).
 
 The rank of a matrix is the maximum number of [linearly independent](/matrices-and-linear-transformations/linear-independence) rows or columns in the matrix.
Given a matrix $A$, the rank of $A$ is denoted as $\rank(A)$ or $\rho(A)$.
- **Full rank**: If the rank of $A$ is equal to the number of rows or columns, the matrix is said to have full rank.
- **Row rank**: The row rank of $A$ is the maximum number of linearly independent rows in $A$
- **Column rank**: The column rank of $A$ is the maximum number of linearly independent columns in $A$.
The row rank and column rank of a matrix are always equal, so we can simply refer to the rank of the matrix.
For example, consider a $2 \times 2$ matrix:
$$
A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}
$$
The rank of $A$ is 1, because the second row is a multiple of the first row, and therefore the rows are not linearly independent.
In contrast, consider a $2 \times 2$ matrix:
$$
B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$
The rank of $B$ is 2, because the rows are linearly independent, and the matrix has full rank.
The rank of a matrix has important implications for:
- [Linear independence](/matrices-and-linear-transformations/linear-independence): A set of vectors is linearly independent if and only if the matrix formed by the vectors has full rank.
- Solving systems of linear equations: The rank of the coefficient matrix determines the number of free variables in the solution.
- [Matrix inversion](/matrices-and-linear-transformations/inverse-matrix): A matrix is invertible if and only if it has full rank.