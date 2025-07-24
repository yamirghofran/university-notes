---
title: Simulating a Normal RV
---

**PDF of Normal/Gaussian Distribution**
$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{1}{2} \frac{(x - \mu)^2}{\sigma^2}\right)$$
**Mean and Variance of Normal/Gaussian Distribution**
$$E(X) = \mu, \quad V(X) = \sigma^2$$
The form of the Normal pdf is the well-known so-called bell-shaped function. We
can notice some properties:

- it is symmetric around the mean: the function on the left-hand side and on the right-hand side of the mean is mirrored. **This implies that the median is equal to the mean**.
- the maximum value of the pdf occurs at the mean. This implies that **the mode is equal to the mean (and therefore also the median)**.
![](../attachments/screenshot-2024-02-27-at-123854.png)

**CDF of the Normal/Gaussian Distribution**
$$F(x) = P(X \leq x) = \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{1}{2} \frac{(x - \mu)^2}{\sigma^2}\right) \, dx$$
![](../attachments/screenshot-2024-02-27-at-124033.png)

## Z Distribution
The way to do this is transforming the normal distribution into a Z distribution.
And, then, look at the statistical tables to obtain the probability of the cdf at a point
in the distribution.
$$Z = \frac{X - \mu}{\sigma}, \quad X = \mu + \sigma Z$$
## Implementing Normal Distribution in Python
Instead of using the tables, we can use Python to tell us the values of Normal probabilities.
Python provides an implementation of the Normal random variable with the functions
`stats.norm.pdf` (pdf) and `stats.norm.cdf` (cdf) whose details are as follows:
- the first argument **x** is the value at which to compute the function;
- the second argument, **loc**, is the parameter μ, by default equal to zero;
- the third argument, **scale**, is the standard deviation, that is $\sqrt{\sigma^2}$, by default equal to one.

```python
stats.norm.pdf(x = 3) #Returns 0.004431848
#Computes the value of the standard Normal pdf at the value 3

stats.norm.cdf(x = 0.4, loc = 1, scale = 0.5) #Returns 0.1150697
#Computes the value of the Normal cdf with mean = 1, standard deviation = 0.5, and value = 0.4
```

### Generating Random Numbers from a Normal Distribution
For this `np.random.normal` in Python function example, you want to simulate a list
of 15 random numbers coming from a Normal data distribution with mean = 3 and
standard deviation = 1.
```python
np.random.normal(loc = 3, scale = 1, size = 15)

#Return
array([3.23253409, 3.49052645, 3.01819909, 4.07321322, 4.04757043,
2.87076029, 4.72248541, 3.52089105, 2.74081748, 2.26369556,
3.47533924, 4.01222016, 3.24568597, 3.00834037, 1.37014717])
```

