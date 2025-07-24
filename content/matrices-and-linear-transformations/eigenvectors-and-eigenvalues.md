---
title: Eigenvectors and Eigenvalues
---

- [Diagnalizing a Matrix](/matrices-and-linear-transformations/diagnalizing-a-matrix)
Given a linear transformation $T: V \to V$, a non-zero vector $v \in V$ is called an eigenvector of $T$ if there exists a scalar $\lambda$ such that:
$$
T(v) = \lambda v
$$
The scalar $\lambda$ is called the eigenvalue corresponding to the eigenvector $v$.
## Finding Eigenvectors and Eigenvalues
### Eigenvalues
To find the eigenvectors and eigenvalues of a linear transformation $T$ represented by a matrix $A$, we need to solve the equation:
$$
Ax = \lambda x
$$
This equation can be rewritten as:
$$
(A - \lambda I)x = 0
$$
where $I$ is the identity matrix.
## Characteristic Equation
The equation:
$$
\det(A - \lambda I) = 0
$$
is called the characteristic equation. The solutions to this equation are the eigenvalues of $A$.
## Example
Suppose we have a matrix:
$$
A = \begin{pmatrix}
2 & 1 \\
1 & 1
\end{pmatrix}
$$
To find the eigenvalues of $A$, we need to solve the characteristic equation:
$$
\det(A - \lambda I) = \det\begin{pmatrix}
2 - \lambda & 1 \\
1 & 1 - \lambda
\end{pmatrix} = (2 - \lambda)(1 - \lambda) - 1 = 0
$$
Solving this equation, we get:
$$
\lambda^2 - 3\lambda + 1 = 0
$$
Using the quadratic formula, we get:
$$
\lambda = \frac{3 \pm \sqrt{5}}{2}
$$
So, the eigenvalues of $A$ are $\lambda_1 = \frac{3 + \sqrt{5}}{2}$ and $\lambda_2 = \frac{3 - \sqrt{5}}{2}$.
### Eigenvectors
Once we have determined the eigenvalues, we can find the corresponding eigenvectors. For each eigenvalue $\lambda$, we solve the equation:
$$(A - \lambda I)x = 0$$
#### Finding Eigenvectors for $\lambda_1 = \frac{3 + \sqrt{5}}{2}$
Substitute $\lambda_1$ into the equation:
$$A - \lambda_1 I = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} - \begin{pmatrix} \frac{3 + \sqrt{5}}{2} & 0 \\ 0 & \frac{3 + \sqrt{5}}{2} \end{pmatrix} = \begin{pmatrix} 2 - \frac{3 + \sqrt{5}}{2} & 1 \\ 1 & 1 - \frac{3 + \sqrt{5}}{2} \end{pmatrix}$$
Simplifying the matrix:
$$= \begin{pmatrix} \frac{4 - \sqrt{5}}{2} & 1 \\ 1 & \frac{2 - \sqrt{5}}{2} \end{pmatrix}$$
We solve the system:
$$\begin{pmatrix} \frac{4 - \sqrt{5}}{2} & 1 \\ 1 & \frac{2 - \sqrt{5}}{2} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
From the first row:
$$\left(\frac{4 - \sqrt{5}}{2}\right)x_1 + x_2 = 0 \quad \Rightarrow \quad x_2 = -\left(\frac{4 - \sqrt{5}}{2}\right)x_1$$
Thus, the eigenvector corresponding to $\lambda_1$ is:
$$x = \begin{pmatrix} x_1 \\ -\left(\frac{4 - \sqrt{5}}{2}\right)x_1 \end{pmatrix} = x_1 \begin{pmatrix} 1 \\ -\left(\frac{4 - \sqrt{5}}{2}\right) \end{pmatrix}$$
#### Finding Eigenvectors for $\lambda_2 = \frac{3 - \sqrt{5}}{2}$
Substitute $\lambda_2$ into the equation:
$$A - \lambda_2 I = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} - \begin{pmatrix} \frac{3 - \sqrt{5}}{2} & 0 \\ 0 & \frac{3 - \sqrt{5}}{2} \end{pmatrix} = \begin{pmatrix} 2 - \frac{3 - \sqrt{5}}{2} & 1 \\ 1 & 1 - \frac{3 - \sqrt{5}}{2} \end{pmatrix}$$
Simplifying the matrix:
$$= \begin{pmatrix} \frac{4 + \sqrt{5}}{2} & 1 \\ 1 & \frac{2 + \sqrt{5}}{2} \end{pmatrix}$$
We solve the system:
$$\begin{pmatrix} \frac{4 + \sqrt{5}}{2} & 1 \\ 1 & \frac{2 + \sqrt{5}}{2} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
From the first row:
$$\left(\frac{4 + \sqrt{5}}{2}\right)x_1 + x_2 = 0 \quad \Rightarrow \quad x_2 = -\left(\frac{4 + \sqrt{5}}{2}\right)x_1$$
Thus, the eigenvector corresponding to $\lambda_2$ is:
$$x = \begin{pmatrix} x_1 \\ -\left(\frac{4 + \sqrt{5}}{2}\right)x_1 \end{pmatrix} = x_1 \begin{pmatrix} 1 \\ -\left(\frac{4 + \sqrt{5}}{2}\right) \end{pmatrix}$$
#### Summary
The eigenvalues of matrix $A$ are $\lambda_1 = \frac{3 + \sqrt{5}}{2}$ and $\lambda_2 = \frac{3 - \sqrt{5}}{2}$. The corresponding eigenvectors are:
- For $\lambda_1$: $\begin{pmatrix} 1 \\ -\left(\frac{4 - \sqrt{5}}{2}\right) \end{pmatrix}$
- For $\lambda_2$: $\begin{pmatrix} 1 \\ -\left(\frac{4 + \sqrt{5}}{2}\right) \end{pmatrix}$