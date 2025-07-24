---
title: MM1 Queuing System
---
-   Arrivals follow an Exponential distribution with parameter $\lambda$ (rate).
-   Service times follow an Exponential distribution with parameter $\mu$ (rate).
-   The utilization $\rho = \lambda/\mu$.
   -  If $\rho < 1$, the steady-state probabilities $P_n$ exist (meaning the queue in the long-run stabilizes).
   -  If $\rho > 1$, the queue explodes.

For each $n \geq 0$, the rate at which the process enters state $n$ equals the rate at which it leaves the state $n$ under the assumption of [Steady-State Probabilities](/prob-cs/steady-state-probabilities).

## Balance Equation
$$
P_n = \left(\frac{\lambda}{\mu}\right)^n \left(1 - \frac{\lambda}{\mu}\right)
$$
## Quantities of Interest
- $L$: expected number of customers in the system.
- $L_Q$: expected number of customers in the queue.
- $W$: expected amount of time spent in the system.
- $W_Q$: expected amount of time spent in the queue.

### Computing L
$$
L = \sum_{n=0}^{\infty} n P_n
$$
$$
= \sum_{n=0}^{\infty} n \left(\frac{\lambda}{\mu}\right)^n \left(1 - \frac{\lambda}{\mu}\right)
$$
$$
= \left(1 - \frac{\lambda}{\mu}\right) \sum_{n=0}^{\infty} n \left(\frac{\lambda}{\mu}\right)^n
$$
$$
= \left(1 - \frac{\lambda}{\mu}\right) \frac{\lambda/\mu}{(1 - \lambda/\mu)^2}
$$
$$
= \frac{\lambda/\mu}{(1 - \lambda/\mu)} = \frac{\rho}{1 - \rho}
$$
$$
= \frac{\lambda}{\mu - \lambda}
$$

## Little's Law
$$
L = \lambda W
$$
The average number of customers in the system is equal to the arrival rate times the average time spent in the system.
This also holds true for the queue only:
$$
L_Q = \lambda W_Q
$$
### Example Derivation
$$
W = \frac{L}{\lambda} = \frac{\lambda}{\mu - \lambda} \cdot \frac{1}{\lambda} = \frac{1}{\mu - \lambda}
$$
$$
W_Q = W - E(S) = \frac{1}{\mu - \lambda} - \frac{1}{\mu} = \frac{\lambda}{\mu(\mu - \lambda)}
$$
where $E(S)$ is the expected service time.
$$
L_Q = \lambda W_Q = \frac{\lambda^2}{\mu(\mu - \lambda)}
$$
## Example
Customers arrive at a donut shop according to a Poisson process of parameter $\lambda = 1/12$ (time unit is minutes) and service time follows an exponential distribution with parameter $\mu = 1/8$. Suppose there is only one employee. Then this is a M/M/1 queue.
$$
L = \frac{\lambda}{\mu - \lambda} = \frac{1/12}{1/8 - 1/12} = 2
$$
$$
W = \frac{1}{1/8 - 1/12} = 24
$$
Now suppose the arrival rate increases by 20%, i.e. $\lambda = 1/10$, then $L = 4$ and $W = 40$.
