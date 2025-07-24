---
title: System of Linear Equations
---

The central problem of linear algebra is to solve linear equations.
- System: 2 or more equations
- Linear: unknowns are multiplied by numbers
- Equation: Value of 2 mathematical expressions are equal
![](../attachments/cleanshot-2025-01-18-at-1415172x.png)
- Can I solve every Ax = b for every b?
- Does the [Linear Combination](/matrices-and-linear-transformations/linear-combination) of the columns fill the n-space?
If columns are independent and A is not singular → yes, else no.

**Not singular** = the inverse exists.
## Types of Solutions
- Unique solution
- Infinite solutions
- No solution

## 2X2 Row Picture
![](../attachments/cleanshot-2025-01-18-at-1416352x.png)

## 2X2 Column Picture
![](../attachments/cleanshot-2025-01-18-at-1416562x.png)

## 2X2 Matrix Picture
![](../attachments/cleanshot-2025-01-18-at-1417232x.png)

## 3X3 Row Picture
![](../attachments/cleanshot-2025-01-18-at-1417452x.png)

## 3X3 Column Picture
![](../attachments/cleanshot-2025-01-18-at-1418182x.png)

## 3X3 Matrix Picture
Example:

$$
\begin{cases} 
x + 2y + 3z = 6 \\
2x + 5y + 2z = 4 \\
6x - 3y + z = 2 
\end{cases}
$$

$$
\begin{bmatrix} 
1 & 2 & 3 \\ 
2 & 5 & 2 \\ 
6 & -3 & 1 
\end{bmatrix}
\begin{bmatrix} 
x \\ 
y \\ 
z 
\end{bmatrix}
=
\begin{bmatrix} 
6 \\ 
4 \\ 
2 
\end{bmatrix}
$$

$$
A \cdot x = b
$$




## Applications
- [Balancing Chemistry Equations](/matrices-and-linear-transformations/balancing-chemistry-equations)
- [Leontieff](/matrices-and-linear-transformations/leontieff)
- [Kirchoff Electronic Circuits](/matrices-and-linear-transformations/kirchoff-electronic-circuits)
- [Network Flow](/matrices-and-linear-transformations/network-flow)
- [Finite Linear Games](/matrices-and-linear-transformations/finite-linear-games)