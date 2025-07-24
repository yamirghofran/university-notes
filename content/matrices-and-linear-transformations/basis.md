---
title: Basis
---

**Basis Definition**
A **basis** of a vector space is a set of vectors that satisfies two properties:
1. **[Linear Independence](/matrices-and-linear-transformations/linear-independence)**: No vector in the set can be expressed as a linear combination of the others.
2. **[Spanning](/matrices-and-linear-transformations/span)**: The set of vectors spans the entire vector space, meaning that any vector in the space can be expressed as a linear combination of the basis vectors.
In other words, a basis is a set of vectors that is:
- **Independent**: No vector is redundant.
- **Complete**: All vectors in the space can be formed using the basis vectors.
A basis is like a set of "building blocks" for the vector space, allowing us to represent any vector in the space as a unique combination of the basis vectors.
For example, in $\mathbb{R}^2$, the set of vectors ${(1, 0), (0, 1)}$ forms a basis, as it is both linearly independent and spanning.
The number of vectors in a basis is called the **dimension** of the vector space.
## Example
$$v_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \quad v_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \quad v_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$
is a basis of space $\mathbb{R}^3$, they are independent and span the space.
$$u_1 = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix} \quad u_2 = \begin{bmatrix} 2 \\ 1 \\ 4 \end{bmatrix} \quad u_3 = \begin{bmatrix} 4 \\ 1 \\ 6 \end{bmatrix}$$
is not a basis of space $\mathbb{R}^3$, they are not independent
$$-2 \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix} + 3 \begin{bmatrix} 2 \\ 1 \\ 4 \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \\ 6 \end{bmatrix}$$
or
$$2 \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix} - 3 \begin{bmatrix} 2 \\ 1 \\ 4 \end{bmatrix} + \begin{bmatrix} 4 \\ 1 \\ 6 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
or
$$\text{RREF} = \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \end{bmatrix}$$
$$u_1 = \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} \quad u_2 = \begin{bmatrix} 2 \\ 5 \\ 7 \end{bmatrix}$$
is not a basis of space $\mathbb{R}^3$, they are independent, but they don't span $\mathbb{R}^3$ only a plane in $\mathbb{R}^3$.
