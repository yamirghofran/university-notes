---
title: Network Flow
---

A network consists of a set of points called nodes with lines called branches.
## Rules
- Total flow into the network is equal to total flow out of the network.
- Total flow into the node is equal to the total flow out of the node.
![](../attachments/cleanshot-2025-02-01-at-1228412x.png)
## Example 1
Find the general flow pattern of the network shown in the figure.
Assuming that the flows are all non-negative. Maximum value for $x_3$?

![](../attachments/cleanshot-2025-02-01-at-1229462x.png)

| INTERSECTION | FLOW IN     | FLOW OUT    |
| ------------ | ----------- | ----------- |
| A            | $x_1 + x_3$ | 20          |
| B            | $x_2$       | $x_3 + x_4$ |
| C            | 80          | $x_1 + x_2$ |
| Total Flow   | 80          | $20 + x_4$  |
### Equations
1. $x_1 + x_3 = 20$
2. $x_2 = x_3 + x_4$
3. $80 = x_1 + x_2$
4. $80 = x_4 + 20$
### Rearranged
1. $x_1 + x_3 = 20$
2. $x_2 - x_3 - x_4 = 0$
3. $x_1 + x_2 = 80$
4. $x_4 = 60$
### Matrix form

$$
\begin{bmatrix}
1 & 0 & 1 & 0 \\
0 & 1 & -1 & -1 \\
1 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4
\end{bmatrix}
=
\begin{bmatrix}
20 \\
0 \\
80 \\
60
\end{bmatrix}
$$
### Augmented Matrix
$$
\begin{bmatrix}
1 & 0 & 1 & 0 \\
0 & 1 & -1 & -1 \\
1 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4
\end{bmatrix}
=
\begin{bmatrix}
20 \\
0 \\
80 \\
60
\end{bmatrix}
\rightarrow
\begin{bmatrix}
1 & 0 & 1 & 0 & | & 20 \\
0 & 1 & -1 & -1 & | & 0 \\
1 & 1 & 0 & 0 & | & 80 \\
0 & 0 & 0 & 1 & | & 60
\end{bmatrix}
$$

### Apply [RREF](/matrices-and-linear-transformations/reduced-row-echelon-form)
$$
\begin{bmatrix}
1 & 0 & 1 & 0 & | & 20 \\
0 & 1 & -1 & 0 & | & 60 \\
0 & 0 & 0 & 1 & | & 60 \\
0 & 0 & 0 & 0 & | & 0
\end{bmatrix}
$$
### From the RREF matrix, the solutions are
-  $x_1 = 20 - x_3$
-  $x_2 = 60 + x_3$
-  $x_3$ is free
-  $x_4 = 60$
### Constraints
-  $x_1 = 20 - x_3 \geq 0 \Rightarrow x_3 \leq 20$
## Example 2 (video)
put video here.