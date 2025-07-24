---
title: Probability Density Function
---

Let X be a continuous random variable with sample space X. The probability that X take a
value within the interval [a,b] is given by
$$P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx$$
where f(x) is the **probability density function (pdf)**. Pdfs, just like pmfs must obey two conditions:
- $f(x) \geq 0$ for all the x values in X.
- The integral of the f(x) for all the values in X is equal to 1.

For any specific value $x_0$ in X, $P(X=x_0) = 0$ since
$$\int_{x_0}^{x_0} f(x) \, dx = 0.$$
For example, if the waiting time of customers of a donuts shop is
$$f(x) = \begin{cases} 
\frac{1}{4} e^{-\frac{x}{4}}, & x \geq 0 \\
0, & \text{otherwise}
\end{cases}$$
Then the probability that the waiting time is between any two values (a,b) can be computes as
$$\int_{a}^{b} \frac{1}{4} e^{-\frac{x}{4}} \, dx.$$
In particular if we were interested in the probability that the waiting time is
between two and five minutes, we could compute it as
$$P(2 < X < 5) = \int_{2}^{5} f(x) \, dx = \int_{2}^{5} \frac{1}{4} e^{-\frac{x}{4}} \, dx = 0.32$$
![](../attachments/screenshot-2024-02-27-at-115625.png)
$$P(a \leq X \leq b) = P(a < X < b) = P(a \leq X < b) = P(a < X \leq b) = \int_{a}^{b} f(x) \, dx$$