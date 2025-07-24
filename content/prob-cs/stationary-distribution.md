---
title: Stationary Distribution
---
The **stationary distribution** of a [Markov Chain](/prob-cs/markov-chains.md) with [transition matrix](/prob-cs/transition-matrix) $Q$ is the vector $\pi$ for which
$$
\pi Q = \pi
$$
It can be interpreted as the proportion of times we would be in a specific state if we let the Markov Chain run for a very long time.

Consider an **irreducible** Markov chain with a **finite number of states**. Then:
- the stationary distribution exists and is unique.
- $\pi_i = 1/r_i$, where $r_i$ is the expected amount of time it takes to return to state $i$.

Consider an **irreducible** and **aperiodic** Markov chain with a finite number of states (such a chain is usually called **ergodic**). Then any row of $Q^n$ is the unique stationary distribution, for $n$ large enough.
