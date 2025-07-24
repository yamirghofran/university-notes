---
title: Exponential Distribution
---
A random variable $X$ is said to have an **Exponential Distribution** with parameter $\lambda \gt 0$ if its pdf is
$$
\lambda e^{-\lambda x}, \quad \text{for } x \geq 0
$$
- $P(X < x) = \int_{-\infty}^{x} f(x) \, dx = 1 - e^{-\lambda x}$
- $P(X > x) = e^{-\lambda x}$
- $E(X) = \frac{1}{\lambda}$
- $V(X) = \frac{1}{\lambda^2}$

The Exponential is (the only) [Memoryless Random Variable](/prob-cs/memoryless-random-variable):
$$
P(X > t + s \mid X > s) = \frac{P(X > t + s, X > s)}{P(X > s)}
$$
$$
= \frac{P(X > t + s)}{P(X > s)}
$$
$$
= \frac{e^{-\lambda(t+s)}}{e^{-\lambda s}} = e^{-\lambda t}
$$
$$
= P(X > t)
$$
