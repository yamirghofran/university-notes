---
title: Leontieff
---

## Rules
There exist equilibrium prices that can be assigned to the total outputs of the various sectors in such a way that the income of each sector exactly balances its expenses.
A sector looks down a column to see where its output goes and it looks across a row to see what it needs as inputs.

## Example 1
A simple economy with 3 sectors: Coal, Electric, and Steel.
-  **Coal** receives 40% of Electric output & 60% Steel.
-  **Electric** receives 60% Coal, 10% Electric & 20% Steel.
-  **Steel** receives 40% Coal, 50% Electric & 20% Steel.
### Exchange Table

| Output   |              |           | Purchased by |
| -------- | ------------ | --------- | ------------ |
| **Coal** | **Electric** | **Steel** |              |
| 0.0      | 0.4          | 0.6       | **Coal**     |
| 0.6      | 0.1          | 0.2       | **Electric** |
| 0.4      | 0.5          | 0.2       | **Steel**    |

### Equations
$$
\begin{align*}
p_C &= 0p_C + 0.4p_E + 0.6p_S \\
p_E &= 0.6p_C + 0.1p_E + 0.2p_S \\
p_S &= 0.4p_C + 0.5p_E + 0.2p_S 
\end{align*}
$$

Move unknowns to the left and numbers to the right
$$
\begin{cases}
p_C - 0.4p_E - 0.6p_S = 0 \\
- 0.6p_C + 0.9p_E - 0.2p_S = 0 \\
- 0.4p_C - 0.5p_E + 0.8p_S = 0
\end{cases}
$$
Matrix form ([Reduced Row Echelon Form](/matrices-and-linear-transformations/reduced-row-echelon-form))
$$
\begin{bmatrix}
10 & -4 & -6 & 0 \\
- 6 & 9 & -2 & 0 \\
- 4 & -5 & 8 & 0
\end{bmatrix}
\rightarrow \text{RREF} \rightarrow
\begin{bmatrix}
1 & 0 & -0.94 & 0 \\
0 & 1 & -0.85 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Move to equations to solve

-  Only 2 equations because the last row is all 0's:
$$
\begin{align*}
p_C - 0.94p_S &= 0 \\
p_E - 0.85p_S &= 0
\end{align*}
$$
Solutions dependent on one variable:
$$
\begin{align*}
p_C &= 0.94p_S \\
p_E &= 0.85p_S \\
p_S &= p_S
\end{align*}
$$

For $( p_S = 1 )$, the other prices are proportional:
$$
\begin{align*}
p_C &= 0.94 \\
p_E &= 0.85 \\
p_S &= 1
\end{align*}
$$
## Example 2 (Video)
put video here
