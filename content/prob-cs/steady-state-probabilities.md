---
title: Steady-State Probabilities
---
The limit
$$
P_n = \lim_{t \to \infty} P_n(t)
$$
if it exists is called **steady-state** probability that exactly $n$ customers are in the system.

The steady-state probabilities exist if
$$
\rho = \frac{\lambda}{s \mu} < 1
$$
-   $L$: expected number of customers in the system is $\sum_{n=0}^{\infty} n P_n$
-   $L_q$: expected queue length is $\sum_{n=s}^{\infty} (n - s) P_n$
### Example
Suppose $\lambda = 6$ customers/hour and $\mu = 2$ customers/hour

-   If there is one server $s = 1$ then $\rho = \lambda/s\mu = 6/1 \cdot 2 = 3 > 1$ and steady-state will never be reached, queue length will increase to infinity in the long run.

-   If there are four servers $s = 4$, then $\rho = \lambda/s\mu = 6/4 \cdot 2 = 3/4 < 1$, the queue will reach steady state and $L$ is finite.
