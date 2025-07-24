---
title: Simulating an Exponential RV
---

The exponential distribution is the probability distribution of the time between events in a [ Poisson process](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/random-variable-simulation/simulating-a-poisson-rv).

## Exponential Distribution
**The exponential distribution random variable is continuous and usually measures**
**the passage of time, although it can be used in other applications**. 

Typical questions may be: "what is the probability that some event will occur in the next x
hours or days, or what is the probability that some event will occur between $x_1$
hours and $x_2$ hours, or what is the probability that the event will take more than $x_1$
hours to take place". 

In summary, **the random variable X is equal to (a) the time**
**between events or(b) the passage of time to complete an action, for example,**
**waiting for a customer**.

**Probability Density Function of Exponential Distribution**
$$f(x) = \begin{cases} 
\lambda e^{-\lambda x}, & x \geq 0 \\
0, & \text{otherwise}
\end{cases}$$
- Where λ = 1/E(X)
- **e**, constant, euler number, base for natural logarithms = 2.71828

In the previous example of the donut shop where the waiting time can be modelled by
$$f(x) = \begin{cases} 
\frac{1}{4} e^{-\frac{x}{4}}, & x \geq 0 \\
0, & \text{otherwise}
\end{cases}$$
The probability that the waiting time is between any two values (a,b) can be computed as
$$\int_{a}^{b} \frac{1}{4} e^{-\frac{x}{4}} \, dx.$$
e.g. between 2 and 5 minutes:
$$P(2 < X < 5) = \int_{2}^{5} f(x) \, dx = \int_{2}^{5} \frac{1}{4} e^{-\frac{x}{4}} \, dx = 0.32$$
![](../attachments/screenshot-2024-02-27-at-122306.png)
$$P(a \leq X \leq b) = P(a < X < b) = P(a \leq X < b) = P(a < X \leq b) = \int_{a}^{b} f(x) \, dx$$
**Cumulative Distribution Function of Exponential Distribution**
For a continuous random variable X the cumulative distribution function (cdf) is
equally defined as
$$F(x) = P(X \leq x),$$
where now
$$P(X \leq x) = P(X < x) = \int_{-\infty}^{x} f(t) \, dt.$$
In the donut shop example, the cdf is defined as 
$$F(x) = \int_{-\infty}^{x} f(t) \, dt = \int_{-\infty}^{x} \frac{1}{4} e^{-\frac{t}{4}} \, dt.$$
This integral can be solved and F(x) can be calculated as
$$F(x) = 1 - e^{-\frac{x}{4}}$$
Exponential random variables are very often used in dynamic simulations since they are very
often used to model inter-arrival times in process: for instance the time between arrivals of
customers at the donut shop. Its cdf can be derived as
$$F(x) = \begin{cases} 
0, & x < 0, \\
1 - e^{-\lambda x}, & x \geq 0.
\end{cases}$$
**Expected value and Variance of Exponential RV**
$$E(X) = \frac{1}{\lambda}, \quad V(X) = \frac{1}{\lambda^2}$$
![](../attachments/screenshot-2024-02-27-at-123201.png)

## Implementing Exponential Distribution in Python
Python provides an implementation of the exponential random variable with the
functions `stats.expon.pdf` and `stats.expon.cdf` whose details are as follows:
- the first argument **x** in pdf and **q** in cdf is the value at which to compute the function;
- the second argument, **scale**, is the expected value, **1/λ**, by default equal to one;
```python
stats.expon.pdf(x = 2, scale = 1/3) #0.007436257
#Computes the pdf at the point 2 of an exponential random variable with parameter λ = 3

stats.expon.cdf(x = 4) #0.9816844
#computes the cdf at the point 4 of an exponential random variable with parameter λ = 1
```

### Generating Random Numbers from an Exponential Distribution
For this `np.random.exponential` in Python function example, let’s assume we have
six computers, each of which is expected to last an average of seven years. Can
we simulate the expected failure dates for this set of machines?
```python
np.random.exponential(7, 6)

#Returns
array([0.18827471, 8.59723434, 6.92963474, 1.75944546, 1.00673017,
5.58482594])
```