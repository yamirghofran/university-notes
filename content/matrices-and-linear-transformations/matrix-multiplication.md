---
title: Matrix Multiplication
---

**Matrix multiplication** is a way of combining two matrices to form a new matrix. Given two matrices $A$ and $B$, the product $C = AB$ is defined as:

$$

C_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}

$$

where $C_{ij}$ is the element in the $i$th row and $j$th column of the resulting matrix $C$, $A_{ik}$ is the element in the $i$th row and $k$th column of matrix $A$, and $B_{kj}$ is the element in the $k$th row and $j$th column of matrix $B$.

In other words, to multiply two matrices, we take the dot product of each row of the first matrix with each column of the second matrix.

Note that matrix multiplication is not commutative, meaning that the order of the matrices matters: $AB \neq BA$ in general.

For example, given two matrices:

$$

A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}

$$

$$

B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}

$$

The product $C = AB$ is:

$$\begin{equation}C = \begin{pmatrix} 1_5 + 2_7 & 1_6 + 2_8 \\ 3_5 + 4_7 & 3_6 + 4_8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}\end{equation}$$

Let's consider two matrices:
$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$
$$
B = \begin{pmatrix} e & f \\ g & h \end{pmatrix}
$$
To multiply these two matrices, we take the dot product of each row of $A$ with each column of $B$:
$$
AB = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} e & f \\ g & h \end{pmatrix}
$$
The resulting matrix $C = AB$ is:
$$
C = \begin{pmatrix} ae + bg & af + bh \\ ce + dg & cf + dh \end{pmatrix}
$$
Let's break it down:
- The top-left element of $C$ is the dot product of the first row of $A$ with the first column of $B$: $ae + bg$
- The top-right element of $C$ is the dot product of the first row of $A$ with the second column of $B$: $af + bh$
- The bottom-left element of $C$ is the dot product of the second row of $A$ with the first column of $B$: $ce + dg$
- The bottom-right element of $C$ is the dot product of the second row of $A$ with the second column of $B$: $cf + dh$
Note that the number of columns in $A$ must be equal to the number of rows in $B$ for the multiplication to be valid. In this case, both $A$ and $B$ are $2 \times 2$ matrices, so the multiplication is valid.

# Dimensions
![](../attachments/cleanshot-2025-01-14-at-1215362x.png)![](../attachments/cleanshot-2025-01-14-at-1216062x.png)

# Matrix Multiplication with Vectors
![](../attachments/cleanshot-2025-01-14-at-1218452x.png)

# Block Matrix Multiplication
![](../attachments/cleanshot-2025-01-14-at-1216362x.png)