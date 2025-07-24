---
title: Diagnalizing a Matrix
---

$$
AX = X\Lambda
$$
X Matrix of eigenvectors
$\Lambda$ Diagonal Matrix of eigenvalues
$$
AXX^{-1} = X\Lambda X^{-1} \quad \text{Multiplying by } X^{-1} \text{ both right sides}
$$
$$\boxed{A = X\Lambda X^{-1}}$$
$$
A =
\begin{bmatrix}
| & | &  & | \\
x_1 & x_2 & \ldots & x_n \\
| & | &  & |
\end{bmatrix}
\begin{bmatrix}
\lambda_1 & 0 & 0 & 0 \\
0 & \lambda_2 & \ldots & 0 \\
0 & 0 & \ldots & \lambda_n
\end{bmatrix}
\begin{bmatrix}
| & | &  & | \\
x_1 & x_2 & \ldots & x_n \\
| & | &  & |
\end{bmatrix}^{-1}
$$
## Conditions to be diagonalizable
A is sure to have $n$ independent eigenvectors (be _diagonalizable_) if all the $\lambda$'s are different (no repeated eigenvalues).
If $\lambda$'s are repeated, it may or may not have $n$ independent eigenvectors.
$$
A = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}
$$
$$
A - \lambda I = \begin{bmatrix} 2 - \lambda & 1 \\ 0 & 2 - \lambda \end{bmatrix} \quad \lambda_1 = 2 \text{ only one eigenvalue}
$$
$$(A - 2I)x = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = 0 \quad \rightarrow \quad x_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \text{ only one indep. eigenvector } \rightarrow A \text{ is not diagonalizable}
$$
## Example
$$
A = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix} \quad \text{Find diagonalization of } A
$$
**Eigenvalues:** $\lambda_1 = 5, \lambda_2 = -1$
**Eigenvectors:** $x_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$, $x_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$
$$
A = X\Lambda X^{-1} \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} 5 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix}^{-1} \begin{bmatrix} 1 \\ 2 \end{bmatrix}
$$
$$
A = X\Lambda X^{-1} \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} 5 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} \frac{1}{3} & \frac{1}{3} \\ \frac{2}{3} & -\frac{1}{3} \end{bmatrix}
$$
