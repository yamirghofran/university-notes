---
title: Properties of Random Numbers
---

It's very important to have random numbers but achieving true randomness on purpose is practically impossible.
## Statistical Randomness
A random number is a result of a **random** variable combination specified by a **probability** distribution function. When no distribution is specified, it is assumed that the continuous
uniform distribution in the interval [0, 1] is used.

A numerical sequence is said to be statistically random when it contains no recognizable
patterns or regularities; sequences such as the results of an ideal dice roll or the digits of π
exhibit statistical randomness.
Statistical randomness does not necessarily imply "true" randomness, i.e., objective
unpredictability. Pseudo-randomness is sufficient for many uses, such as statistics, hence the
name statistical randomness.

A sequence of random numbers must have 2 important properties
- **Uniformity**: All numbers have the same probability of appearing.
- **Independence**: The current value of a random variable has no relation to previous values.

The first step to simulate numbers from a distribution is to be able to independently simulate random numbers from a **continuous uniform distribution** between 0 and 1.

## Uniform Distribution [0,1]
To extract a **random value x** that represents a number between 0 and 1, given that **the random variable x** takes any value of this interval with **all values being equally likely**, it is said that the random variable x has a **continuous uniform probability distribution.**

**PDF**
$$f(x) = \begin{cases}
\frac{1}{b-a}, & a \leq x \leq b \\
0, & \text{otherwise}
\end{cases}$$
where a=0 and b=1, so $$f(x) = \begin{cases}
1, & 0 \leq x \leq 1 \\
0, & \text{otherwise}
\end{cases}$$![](../attachments/screenshot-2024-02-27-at-000609.png)
With the **cumulative distribution function**, we can determine the probability that a random number we take from this interval is less than or equal to a certain value.

**CDF**
$$F(x) = \begin{cases}
0, & \text{for } x < a, \\
\frac{x-a}{b-a}, & \text{for } a \leq x \leq b, \\
1, & \text{for } x > b.
\end{cases}$$
where a=0 and b=1, so $$F(x) = \begin{cases}
0, & x < 0, \\
x, & 0 \leq x \leq 1, \\
1, & \text{otherwise}.
\end{cases}$$
Mean = 1/2 (a+b). Variance = 1/12 $(b-a)^2$

![](../attachments/screenshot-2024-02-27-at-000655.png)

### Uniformity
[Testing Uniformity](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/generating-random-numbers/testing-uniformity)
Example of uniform vs non-uniform:
![](../attachments/screenshot-2024-02-27-at-000910.png)

### Independence
The second requirement the random numbers of the sequence generated need to
respect is independence. This means that the probability of observing a value in a
particular sub-interval of (0,1) is independent of the previous values drawn.
[Testing Independence](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/generating-random-numbers/testing-independence)

