---
title: Poisson Process
weight: 5
---
Can be used to model:
- number of car accidents at a site.
- location of users in a wireless network.
- requests for individual documents on a web-server.
- the outbreak of wars.
- photons landing on a photodiode.
Also forms the basis for spatial and spatio-temporal models (e.g. number of infected people throughout Spain evolving by day)
---
A [counting process](/prob-cs/counting-process) $\{N(t), t \geq 0\}$ is a **Poisson process** with rate $\lambda > 0$ if
-  $N(0) = 0$
-  the process has independent increments
-  the process has stationary increments and
$$
P(N(t+s) - N(s) = n) = P(N(t) = n) = \frac{e^{-\lambda t}(\lambda t)^n}{n!}
$$
The number of events in an interval of width $t$ is distributed as a Poisson with parameter $\lambda t$.
$$
E(N(t)) = \lambda t \quad \text{and} \quad V(N(t)) = \lambda t
$$
## Inter-Arrival Times
Let $T_1$ be the time of the first event and $T_n$ be the time between the $(n-1)$st event and the $n$th event. These are called **inter-arrival times**.
![](../attachments/poisson-1.png)
$T_1, \ldots, T_n$ are independent and [exponential](/prob-cs/exponential-distribution) with parameter $\lambda$.

$$
P(T_1 > t) = P(N(t) = 0) = e^{-\lambda t},
$$
which is the expression for the Exponential. For the other $T$'s, the argument is similar, also using the independent and stationary increments property.

## Waiting Times
The time of the $n$th event, $S_n$, is called the **waiting time** until the $n$-th event.

$S_n$ can be seen as $\sum_{i=1}^{n} T_n$, the sum of independent exponential distribution. This can be shown to be a **Gamma distribution** with parameters $n$ and $\lambda$. Its mean is $n/\lambda$ and its variance is $n/\lambda^2$.
