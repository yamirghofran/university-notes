---
title: Sojourn Times
weight: 4
---
The **sojourn time** is the time from when a [Markov Chain](/prob-cs/markov-chains) reaches a certain state to when in leaves that state and it is usually denoted as $\tau_i$ for state $i$.

$$
\tau_i \sim \text{Geom}(1 - q_{ii})
$$
and therefore
$$
E(\tau_i) = \frac{1}{1 - q_{ii}}
$$
