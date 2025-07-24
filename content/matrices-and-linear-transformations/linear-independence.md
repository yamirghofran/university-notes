---
title: Linear Independence
---

Vectors $u_1, u_2, \ldots, u_n$ are independent if no combination gives the zero vector (except the zero combination)
$$c_1u_1 + c_2u_2 + \cdots + c_nu_n \neq 0 \quad (\text{except when all } c_i = 0)$$
or it's the same if
$$a_1u_1 + a_2u_2 + \cdots + a_{n-1}u_{n-1} \neq u_n \quad (\text{except when all } a_i = 0)$$
**Example:**
$$u_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \quad u_2 = \begin{bmatrix} 5 \\ 10 \\ 15 \end{bmatrix}$$
$$5 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} - 1 \begin{bmatrix} 5 \\ 10 \\ 15 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
or
$$5 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 5 \\ 10 \\ 15 \end{bmatrix} \quad u_1, u_2 \text{ are not independent}$$
They are dependent because $c_1u_1 + c_2u_2 = 0$ for any $c_i \neq 0$ or $a_1u_1 = u_2$ for any $a_i \neq 0$
