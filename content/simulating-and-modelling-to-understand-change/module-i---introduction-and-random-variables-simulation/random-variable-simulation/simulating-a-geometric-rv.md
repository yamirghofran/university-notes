---
title: Simulating a Geometric RV
---

Repeating a [[Simulating a Bernoulli RV |Bernoulli]] experiment, of **p** parameter, until we get the first success.

Let X be the **random variable that counts the number of failures before the first success**. e.g. if we have had x failures, it will be a sequence of x failures culminated with a success. More specifically:
$$P(\underbrace{FFF\ldots FS}_{x}) = P(F)^{x} \cdot P(S) = (1-p)^{x} \cdot p = q^{x} \cdot p$$
- **F**: Failure
- **S**: Success
- **p**: probability of success
- **q = 1 - p**: probability of failure
- **x**: number of failures before the first success

This form of the geometric distribution is used for modelling the **number of failures until the first success**. The pmf follows:
$$P_X(x) = P(X = x) = \begin{cases}
(1-p)^x \cdot p, & \text{if } x=0,1,2,\ldots \\
0, & \text{otherwise}
\end{cases}
$$
The random variable X defined above is said to follow a geometric distribution of **p** parameter. We will denote it by **Ge(p)**. Its domain is $D_x = \{0, 1, 2, 3, ...\}$.

Imagine we want to calculate $P(X \leq 3)$. By the property of the probability of the complementary event we have that $$P(X \leq 3)=1-P(X \gt 3)=1-P(X \geq 4)$$
The $X \gt 3$ tells us that **we have failed 4 or more times** before getting the first success. We can symbolize this event in the following way:
$$\{X > 3\} = \{X \geq 4\} = \{\text{FFFF}\}$$
Now, since the attempts are independent, we have that:
$$P(X > 3) = P(\text{FFFF}) = P(F)^4 = (1-p)^4$$

Then, the value of the distribution function of X in x = 3 will be:
$$F_X(3) = P(X \leq 3) = 1 - P(X > 3) = 1 - (1 - p)^4$$
Generalizing, for any positive integer k:
$$F_X(k) = P(X \leq k) = 1 - (1 - p)^{k+1}, \text{ if } k = 0, 1, 2, 3, \ldots$$
Therefore, **the CDF is** 
$$F_X(x) = P(X \leq x) = \begin{cases}
0, & \text{if } x < 0,\\
1 - (1 - p)^{k+1}, & \text{if } k \leq x < k + 1, \text{ for } k = 0, 1, 2, \ldots
\end{cases}$$
**Mean**
$$E(X) = \frac{1 - p}{p}$$
**Variance**
$$\text{Var}(X) = \frac{1 - p}{p^2}$$
**Standard Deviation**
$$\sqrt{\text{Var}(X)} = \sqrt{\frac{1 - p}{p^2}}$$
Another interpretation of the Geometric RV is using **the number of attempts rather than the number of failures**. If we define **Y =** number of attempts to get the first success, then **Y = X + 1** where **X** will be denoted as **Ge(p)**. Its domain is **$D_y = \{1, 2, 3, ...\}$**.

The expectation increases by one and the variance stays the same:
$$E(Y) = E(X + 1) = E(X) + 1 = \frac{1 - p}{p} + 1 = \frac{1}{p}$$
$$\text{Var}(Y) = \text{Var}(X + 1) = \text{Var}(X) = \frac{1 - p}{p^2}$$
## Geometric RV in Python
Python provides a method for performing calculations with a geometric random variable. The `dgeom(pmf)` and `pgeom(cdf)` functions will have the arguments:
- **k**, will take the value of the geometric RV we want to evaluate, in this case, Python will evaluate the number of attempts (be careful this).
- **p**: the probability of success in each of the attempts

e.g. for Ge(p = 0.25).
$P(X = 1) = (1 - 0.25)^1 \cdot 0.25 = 0.1875$
```python
geom.pmf(k = 2, p = 0.25) # k = 2 because we try 2 times till the first success
(this is the same of having 1 failure)
# returns 0.1875
```

$P(X \leq 4) = 1 - (1 - 0.25)^{4+1} = 0.7626953$
```python
geom.cdf(k = 5, p = 0.25) # returns 0.7626953
```

### Random numbers from a Geometric Distribution
The `rgeom(prob, size)` function is a method for generating pseudo-random numbers using a geometric distribution.
- **prob**: probability of success in each of the attempts.
- **size**: amount of pseudo-random numbers we want to generate.

A random sample of size 25 of Ge(0.25) can be generated as:
```python
np.random.geometric(p=0.25, size=25)

#returns
array([ 1, 1, 5, 1, 4, 7, 9, 2, 3, 2, 5, 3, 3, 2, 3, 1, 4,
2, 3, 4, 8, 2, 1, 15, 1])
```

## Visual Geometric Distribution  PMF & CDF Interpretation
![](../attachments/screenshot-2024-02-26-at-231318.png)

### PMF
In the **pmf, the probability of getting your first success after x failures has a decreasing fashion** because the probability of success is 0.25, and therefore, in the first attempt, we have a probability of 0.35 of obtaining the first success after 0 failures (x=0).

However, in the second attempt, the probability of obtaining the first success after 1 failure (x = 1) is lower because it has to be fulfilled that you failed in the first attempt and also that you succeed in the second one. In the same way, when x = 2, the probability is lower because you have to fail in the first attempt, fail in the second and succeed in the third!
You can use the formulas of the pmf to demonstrate it.

### CDF
On the other hand, the **CDF shows the probability of success when the number of failures is less than or equal to x**.

We can see that the probability of success when the number of failures is less
than or equal to 0 is 0.25, which is the same as the probability of success of our
first attempt. However, the probability of success when the number of failures is
less than or equal to 30, is much higher because it includes all the previous cases,
therefore it is the sum of all the probabilities of previous x values.