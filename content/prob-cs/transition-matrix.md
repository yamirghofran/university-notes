---
title: Transition Matrix
weight: 3
---
The [[matrix]] Q containing for each row the transition probabilities for a specific state is called the **transition matrix**.

![](../attachments/transition-matrix-0.png)
$$Q = \begin{pmatrix} 0.8 & 0.2 \\ 0.7 & 0.3 \end{pmatrix}$$

- The matrix $Q$ is always a square matrix.
- Each of its rows must add up to one.
- All its entries are non-negative.
- The entry $(i,j)$ is the probability of going from state $i$ to state $j$.

![](../attachments/transition-matrix-1.png)

$$
Q = \begin{pmatrix} 0 & 0.3 & 0.7 \\ 0.1 & 0.9 & 0 \\ 0 & 0.4 & 0.6 \end{pmatrix}
$$
---
- [[n-Step Transition Probability]]
