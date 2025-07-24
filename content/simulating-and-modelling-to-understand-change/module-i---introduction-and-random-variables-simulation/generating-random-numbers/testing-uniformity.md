---
title: Testing Uniformity
---

A simple first method to check if the numbers are uniform is to create a histogram of the
data and to see if the **histogram is reasonably flat**. In order to do this, we can use the
`plt.hist` function of Python importing `matplotlib.pyplot as plt`.

```python
np.random.seed(2023)
u = np.random.uniform(0,1,5000)
plt.hist(u)
plt.show()
```
![](../attachments/screenshot-2024-02-27-at-110824.png)
We can see that the histogram is reasonably flat and therefore the assumption of uniformity
seems to hold. **Although the histogram is quite informative, it is not a fairly formal method**.

We could do a hypothesis test that follows this form:
- $H_0$: $u_i$ is uniform between zero and one, i = 1,2,...
- $H_a$: $u_i$ is **not** uniform between zero and one, i = 1,2,...
If we reject the null hypothesis, which happens if the p-value of the test is very small (or
smaller than a critical value α of our choice), then we would say that, with a confidence level
of (1-α) * 100%, we have enough statistical evidence to reject the $H_0$.

## Kolmogrov-Smirnov Test
There are several ways to carry out such a test, but we will consider here only one:
the so-called **Kolmogorov-Smirnov Test**.
The ecdf $\hat{F}$ is the cumulative distribution function computed from a sequence of N numbers as:
$$\hat{F}(t) = \frac{\text{numbers in the sequence} \leq t}{N}$$
```python
u = [0.1, 0.2, 0.4, 0.8, 0.9]
x = [i/len(values) for i in range(1, len(values)+1)]
plt.step(x, u, where='post')
plt.show()
```
![](../attachments/screenshot-2024-02-27-at-111358.png)
For instance, since there are 3 numbers in **u** that are less or equal than 0.7, then: $\hat{F}(0.7)=3/5$

The idea behind this test is to **quantify how similar the ecdf computed from a sequence of data is to the one of the uniform distribution** which is represented by a straight line.
![](../attachments/screenshot-2024-02-27-at-111553.png)

The test formally embeds this idea of similarity between the ecdf and the cdf of the uniform
in a test of hypothesis. The function `stats.kstest` from the `scipy` library implements this
test in Python. For the two sequences u1 and u2 of the previous slide, the test can be
implemented as following:

```python
stats.ktest(u1, 'uniform')
#D-statistic: 0.0092
#p-value: 0.787176

stats.ktest(u2, 'uniform')
#D-statistic: 0.4868
#p-value: 0.0
```
From the results that the **p-value of the test for the sequence u1 is 0.787** and so
we would **not be able to reject the $H_0$** that the sequence is **uniformly distributed**.

On the other hand the **p-value for the test over the sequence u2 has an extremely**
**small p-value** therefore suggesting that **we reject the $H_0$** and conclude that the sequence is **not uniformly distributed**.

This confirms our intuition.