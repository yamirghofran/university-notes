---
title: Queuing Systems
weight: 6
---
![](../attachments/queuing-systems-1.png)
## Labeling Convention (Kendall-Lee)
![](../attachments/queuing-systems-2.png)
### Examples
![](../attachments/queuing-systems-3.png)

## Terminology and Notation
- **State of the system**: number of customers in the queueing system (includes customers in service)
- **Queue Length**: number of customers waiting for service = state of the system - number of customers being served.
- s = number of servers in the system.
- N(t) = state of the system at time t.
- $P_n(t)$: probability that exactly $n$ customers are in the queuing system at time $t$.
- L = expected number of customers in the system.
- $L_q$ = expected number of customers in the queue.
- $\lambda$ = mean arrival rate (expected number of arrivals per unit time)
- $\mu$ = mean service rate for a busy server.
-  $1/\lambda =$ expected inter-arrival time
-  $1/\mu =$ expected service time
-  $\rho = \frac{\lambda}{s \mu}$ is the **utilization** factor for the service facility (expected fraction of time the system’s service capacity is being utilized by arriving customers)
Assuming that $\lambda \text{ and } \mu$ are independent of the state of the system.
