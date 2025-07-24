---
title: A=LU Factorization
---

Given a base matrix A:
$$
A = \begin{pmatrix} 
1 & 4 & 5 & 3 \\ 
5 & 22 & 27 & 11 \\ 
6 & 19 & 27 & 31 \\ 
5 & 28 & 35 & -8 
\end{pmatrix}
$$
we decompose it into 2 simpler matrices L(ower triangular) and U(upper triangular).
$$
L = \begin{pmatrix} 
1 & 0 & 0 & 0 \\ 
5 & 1 & 0 & 0 \\ 
6 & -2.5 & 1 & 0 \\ 
5 & 4 & 1 & 1 
\end{pmatrix}
\quad
U = \begin{pmatrix} 
1 & 4 & 5 & 3 \\ 
0 & 2 & 2 & -4 \\ 
0 & 0 & 2 & 3 \\ 
0 & 0 & 0 & -10 
\end{pmatrix}
$$
U is the [Row Echelon Form](/matrices-and-linear-transformations/reduced-row-echelon-form) of the base matrix A. 

L is obtained by creating a lower triangular matrix with the multiples of the REF transformation of A:
$$
L = \begin{pmatrix}
1 & 0 & 0 \\
-m_{21} & 1 & 0 \\
-m_{31} & -m_{32} & 1
\end{pmatrix}
$$
After that, given the vector b:
$$
b = \begin{pmatrix} 
7 \\ 
13 \\ 
106 \\ 
- 94 
\end{pmatrix}
$$

we use the following method:
$$
Ax = b \rightarrow LUx = b \rightarrow L(Ux) = b \rightarrow \text{first solve } Ly = b \text{ where } y = Ux
$$
First, we solve $Ly = b$ using forward substitution:

1. $y_1 = b_1 = 7$

2. $5y_1 + y_2 = 13$
   $$y_2 = 13 - 5 \cdot 7 = 13 - 35 = -22$$
3. $6y_1 - 2.5y_2 + y_3 = 106$
   $$y_3 = 106 - 6 \cdot 7 + 2.5 \cdot 22 = 106 - 42 + 55 = 119$$
4. $5y_1 + 4y_2 + y_3 + y_4 = -94$   $$y_4 = -94 - 5 \cdot 7 - 4 \cdot (-22) - 119 = -94 - 35 + 88 - 119 = -160$$So, the vector $y$ is:

$$y = \begin{pmatrix}
7 \\
- 22 \\
119 \\
- 160
\end{pmatrix}$$
We have:

$$
U = \begin{pmatrix}
1 & 4 & 5 & 3 \\
0 & 2 & 2 & -4 \\
0 & 0 & 2 & 3 \\
0 & 0 & 0 & -10
\end{pmatrix}
$$

$$
y = \begin{pmatrix}
7 \\
- 22 \\
119 \\
- 160
\end{pmatrix}
$$

We solve $Ux = y$ using back substitution:

1. $-10x_4 = -160$   
   $$x_4 = \frac{-160}{-10} = 16$$
2. $2x_3 + 3x_4 = 119$
   $$2x_3 + 3 \cdot 16 = 119$$
   $$2x_3 = 119 - 48 = 71$$
   $$x_3 = \frac{71}{2} = 35.5$$
3. $2x_2 + 2x_3 - 4x_4 = -22$
4. $$2x_2 + 2 \cdot 35.5 - 4 \cdot 16 = -22$$
   $$2x_2 + 71 - 64 = -22$$
   $$2x_2 = -22 - 7 = -29$$
   $$x_2 = \frac{-29}{2} = -14.5$$
4. $x_1 + 4x_2 + 5x_3 + 3x_4 = 7$
   $$x_1 + 4 \cdot (-14.5) + 5 \cdot 35.5 + 3 \cdot 16 = 7$$$$x_1 - 58 + 177.5 + 48 = 7$$   $$x_1 = 7 + 58 - 177.5 - 48 = -160.5$$
So, the solution vector $x$ is:

$$
x = \begin{pmatrix}
- 160.5 \\
- 14.5 \\
35.5 \\
16
\end{pmatrix}
$$
which is the final solution.

## Exercise
Let $$A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 4 & 4 \\ 3 & 7 & 10 \end{pmatrix}$$

(a) Find the $A = LU$ factorization of the matrix $A$

(b) Solve the system \( Ax = b \) using factorization $LU$ where $$b = \begin{pmatrix} 3 \\ 10 \\ 20 \end{pmatrix}$$



# Frequently Asked Questions
### Why do we want to decompose a matrix into LU?
Solving linear systems of equations of the form Ax=b is the fundamental concept of linear algebra. LU factorization methods is one of the fastest ways to solve AX=b and numerical software like Matlab or Python libraries like Numpy, Scipy use LU factorization.

### Why don't we use [Gaussian Elimination](/matrices-and-linear-transformations/gauss-elimination)?
We use the Gaussian Elimination procedure to obtain the upper triangular matrix U, but this alone is not sufficient.
