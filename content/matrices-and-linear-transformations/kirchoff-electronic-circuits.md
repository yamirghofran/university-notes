---
title: Kirchoff Electronic Circuits
---

## Rules
- Current flow described by a system of linear equations
- A voltage source such as a battery forces a current to flow the network.
- When current passes through resistor some voltage is used by by Ohm's law.
- The current flowing in loops with direction arbitrary. If a current turns out to be negative, then the actual direction is opposite to the figure.
- If current direction shown is away from the positive (longer) around the negative (shorter) side, voltage is positive; otherwise, it's negative.

## Example 1
![](../attachments/cleanshot-2025-02-01-at-1218342x.png)
### Loop 1:

$4I_1 + 4I_1 + 3I_1 = 11I_1$ and direction in loop 1 is opposite to loop 2, so$3I_2$ is negative. Voltage 30 is in loop 1 direction then is positive

$$11I_1 - 3I_2 = 30$$

### Loop 2:

$I_2 + I_2 + 3I_2 + I_2 = 6I_2$ direction in loop 2 is opposite to loop 1, so $3I_1$ is negative and direction in loop 2 is also opposite to loop 3, so $I_3$ is negative. Voltage 5 is in loop 2 direction then is positive
$$-3I_1 + 6I_2 - I_3 = 5$$
### Loop 3
$I_3 + I_3 + I_3 = 3I_3$ direction in loop 3 is opposite to loop 2, so $I_2$ is negative
Both voltages: 20 + 5 are in opposite direction then they are negative
$$-I_2 + 3I_3 = -25$$
### Equations
$$
\begin{align*}
11I_1 - 3I_2 = 30 \\
-3I_1 + 6I_2 - I_3 = 5 \\
-I_2 + 3I_3 = -25 
\end{align*}
$$
### Matrix Form

$$
\begin{bmatrix}
11 & -3 & 0 \\
- 3 & 6 & -1 \\
0 & -1 & 3
\end{bmatrix}
\begin{bmatrix}
I_1 \\
I_2 \\
I_3
\end{bmatrix}
=
\begin{bmatrix}
30 \\
5 \\
- 25
\end{bmatrix}
\rightarrow
\begin{bmatrix}
11 & -3 & 0 & | & 30 \\
- 3 & 6 & -1 & | & 5 \\
0 & -1 & 3 & | & -25
\end{bmatrix}
$$

### [RREF](/matrices-and-linear-transformations/reduced-row-echelon-form)

$$
RREF \rightarrow
\begin{bmatrix}
1 & 0 & 0 & | & 3 \\
0 & 1 & 0 & | & 1 \\
0 & 0 & 1 & | & -8
\end{bmatrix}
$$

### Solution

$$\boxed{I_1 = 3 \quad I_2 = 1 \quad I_3 = -8}$$
## Example 2 (video)
put video here