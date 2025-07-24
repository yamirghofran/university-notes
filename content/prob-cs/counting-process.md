---
title: Counting Process
weight: 4
---
A stochastic process $\{N(t), t \geq 0\}$ is said to be a **counting process** if $N(t)$ represents the total number of events that occurred by time $t$.

A counting process $N(t)$ must satisfy:
-  $N(t) \geq 0$
-  $N(t)$ is integer-valued
-  If $s < t$ then $N(s) \leq N(t)$
-  For $s < t$, $N(t) - N(s)$ equals the number of events that occur in the interval $(s, t]$.

A counting process has **independent increments** if the number of events that occur in disjoint time intervals are independent.
For example, the number of events before time 5, N(5), is independent of the number of events occurring between times 5 and 10, N(10) - N(5).

A counting process has **stationary increments** if the distribution of the number of events that occur in any time interval depends only on the length of the interval. In other words, N(t) - N(0) and N(t+s) - N(s) have the same distribution that depends only on t.
