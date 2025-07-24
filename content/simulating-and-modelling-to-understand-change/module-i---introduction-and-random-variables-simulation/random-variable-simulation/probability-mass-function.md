---
title: Probability Mass Function
---

The outcome of a [[Y1Q2/Simulating and Modelling to Understand Change/Module I - Introduction & Random Variables Simulation/Random Variable Simulation/Discrete Random Variables | discrete random variable]] is, in general unknown, but we want to associate a probability to each element of $X$, denoted by $P$.

The pmf (probability mass function) of a random variable $X$ with sample space $X$ is defined as 
$$p(x)=P(X=x), \text{ for all } x \in X$$
Pmfs must obey two conditions:
- $p(x) \geq 0$, for all $x \in X$
- $\sum_{x \in X} p(x) = 1$

The pmf associated to each outcome is a **non-negative number** such that the **sum of all these numbers is equal to one**.

Take the example of a biased dice, such that 3 and 6 are twice as likely to appear than other numbers. Pmf:

| x    | 1   | 2   | 3   | 4   | 5   | 6   |
| ---- | --- | --- | --- | --- | --- | --- |
| p(x) | 1/8 | 1/8 | 2/8 | 1/8 | 1/8 | 2/8 |
![](../attachments/screenshot-2024-02-26-at-212739.png)