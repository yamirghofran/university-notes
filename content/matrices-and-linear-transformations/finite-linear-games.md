---
title: Finite Linear Games
---



## Game of 5 Lights

**Rules**

A row of 5 lights is controlled by 5 buttons. Lights can be on/off Each push-button changes the state of the lights (on or off) of the light directly above it and the states of the lights immediately adjacent to the left and the right.
![](../attachments/cleanshot-2025-02-06-at-0832362x.png)

On/Off suggest binary notation, we should work with $\mathbb{Z}_2$

States of 5 lights are represented by a vector in $\mathbb{Z}_2^5$, for example:

$$
\begin{bmatrix}
1 \\
0 \\
1 \\
0 \\
1
\end{bmatrix}
$$

lights 1, 3, and 5 are on.

Actions of 5 buttons are given by:

$$
a = 
\begin{bmatrix}
1 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}
\quad
b = 
\begin{bmatrix}
1 \\
1 \\
1 \\
0 \\
0
\end{bmatrix}
\quad
c = 
\begin{bmatrix}
0 \\
1 \\
1 \\
1 \\
0
\end{bmatrix}
\quad
d = 
\begin{bmatrix}
0 \\
0 \\
1 \\
1 \\
1
\end{bmatrix}
\quad
e = 
\begin{bmatrix}
0 \\
0 \\
0 \\
1 \\
1
\end{bmatrix}
$$
$s$ is the initial configuration: $s = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}$ so find some combination of $s + a + b + c + d + e = t$ where $t = \begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \\ 1 \end{bmatrix}$

$t$ is the target configuration from an initial configuration $s$.

Actions of 5 buttons are given by $s + x_1 a + x_2 b + x_3 c + x_4 d + x_5 e = t \quad \text{where} \quad x_1, x_2, x_3, x_4, x_5 \in \mathbb{Z}_2$ and $a, b, c, d, e \in \mathbb{R}^5$

$$
x_1 a + x_2 b + x_3 c + x_4 d + x_5 e = t - s
$$

$$
\begin{bmatrix}
1 & 1 & 0 & 0 & 0 \\
1 & 1 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 \\
0 & 0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5
\end{bmatrix}
=
\begin{bmatrix}
t_1 - s_1 \\
t_2 - s_2 \\
t_3 - s_3 \\
t_4 - s_4 \\
t_5 - s_5
\end{bmatrix}
$$
**Solution**
$$
s = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix} \quad t = \begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \\ 1 \end{bmatrix} \quad \rightarrow \quad t - s = \begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \\ 1 \end{bmatrix} \text{ over } \mathbb{Z}_2
$$

$$
\text{Augmented Matrix} = 
\begin{pmatrix}
1 & 1 & 0 & 0 & 0 & \big| & 1 \\
1 & 1 & 1 & 0 & 0 & \big| & 0 \\
0 & 1 & 1 & 1 & 0 & \big| & 1 \\
0 & 0 & 1 & 1 & 1 & \big| & 0 \\
0 & 0 & 0 & 1 & 1 & \big| & 1
\end{pmatrix}
\rightarrow \text{Reduced Row Echelon Form}
\begin{pmatrix}
1 & 0 & 0 & 0 & 0 & \big| & 1 \\
0 & 1 & 0 & 0 & -1 & \big| & 1 \\
0 & 0 & 1 & 0 & 0 & \big| & -1 \\
0 & 0 & 0 & 1 & 1 & \big| & 1 \\
0 & 0 & 0 & 0 & 0 & \big| & 0
\end{pmatrix}
$$

$$
\rightarrow 
\begin{pmatrix}
1 & 0 & 0 & 0 & 0 & \big| & 1 \\
0 & 1 & 0 & 0 & 1 & \big| & 1 \\
0 & 0 & 1 & 0 & 0 & \big| & 1 \\
0 & 0 & 0 & 1 & 1 & \big| & 1 \\
0 & 0 & 0 & 0 & 0 & \big| & 0
\end{pmatrix}
\text{ Reduced over } \mathbb{Z}_2 \, (-1 \equiv 1)
$$
$$
\begin{pmatrix}
1 & 0 & 0 & 0 & 1 & \big| & 0 \\
0 & 1 & 0 & 0 & 1 & \big| & 1 \\
0 & 0 & 1 & 0 & 0 & \big| & 1 \\
0 & 0 & 0 & 1 & 1 & \big| & 1 \\
0 & 0 & 0 & 0 & 0 & \big| & 0
\end{pmatrix}
$$

$$
x_1 = -x_5 \\
x_2 = 1 - x_5 \\
x_3 = 1 \\
x_4 = 1 - x_5 \\
x_5 \text{ is free variable}
$$

$$
\rightarrow \text{Solutions when } x_5 = 0 \text{ or } x_5 = 1
$$

Operations in $\mathbb{Z}_2$ is modulo(2), so values are only 0, 1 and $2 \equiv 0$ and $-1 \equiv 1$.

**Solutions** $(x_5 = 0) \rightarrow$

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5
\end{bmatrix}
=
\begin{bmatrix}
0 \\
1 \\
1 \\
1 \\
0
\end{bmatrix}
\quad \text{and } (x_5 = 1) \rightarrow
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5
\end{bmatrix}
=
\begin{bmatrix}
- 1 \\
0 \\
1 \\
0 \\
1
\end{bmatrix}
\equiv
\begin{bmatrix}
1 \\
0 \\
1 \\
0 \\
1
\end{bmatrix}
$$

**Solutions:** Press 1B + 1C + 1D or Press 1A + 1C + 1E