---
title: n-Step Transition Probability
---
Consider a Markov chain with [transition matrix](/prob-cs/transition-matrix) $Q$. The probability of going from state $i$ to state $j$ in exactly $n$ steps is given by the entry $(i,j)$ of the matrix $Q^n$

This is a corollary of a very important result called Chapman-Kolmogorov Equations (not discussed).

### Example
What is the probability of going from state 1 to state 2 in exactly three steps for the Markov chain with transition matrix
$$
Q = \begin{pmatrix} 0.4 & 0.6 \\ 0.5 & 0.5 \end{pmatrix}?
$$
$$
Q^2 = Q \times Q = \begin{pmatrix} 0.4 & 0.6 \\ 0.5 & 0.5 \end{pmatrix} \times \begin{pmatrix} 0.4 & 0.6 \\ 0.5 & 0.5 \end{pmatrix} = \begin{pmatrix} 0.46 & 0.54 \\ 0.45 & 0.55 \end{pmatrix}
$$
$$
Q^3 = Q^2 \times Q = \begin{pmatrix} 0.46 & 0.54 \\ 0.45 & 0.55 \end{pmatrix} \times \begin{pmatrix} 0.4 & 0.6 \\ 0.5 & 0.5 \end{pmatrix} = \begin{pmatrix} 0.454 & 0.546 \\ 0.455 & 0.545 \end{pmatrix}
$$
