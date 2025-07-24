---
title: Simulating a Binomial RV
---

The [Bernoulli random variable](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/random-variable-simulation/simulating-a-bernoulli-rv) is a special case of the so-called **Binomial random variable.** Instead of having **just one trial**, the experiments are **repeated multiple times**.
- Each experiment is repeated **n** times.
- Each time there is a probability of success **p**.
- The outcome of each experiment is **independent** of the others.

## Binomial Distribution
Pmf of a Binomial random variables with parameters **n** and **p** can be written as: $$p(x) = \begin{cases}
\binom{n}{x} p^x (1-p)^{n-x}, & x = 0,1,\ldots,n \\
0, & \text{otherwise}
\end{cases}
$$
- If X=x there are x successes and each success has probability p, so $p^x$ counts the overall probability of successes.
- If X = x there. are n-x failures and each failure has a probability $1-p$, so $(1-p)^{n-x}$ counts the overall probability of failures.
- Failures and successes can appear according to many orders. To see this, suppose that $x=1$: there is only one success out of $n$ trials. This could have happened in the first trial, the second or the $n$th. The term $\binom{n}{x}$  counts all the possible ways the outcome $x$ could have happened.

$$E(X)=np$$ $$V(X)=np(1-p)$$
The formulae for the Bernoulli can be retrieved by setting n=1.

- n = 10, p = 0.3 - In this figure, we can see that the **number of successes** is more likely to be **small**. Being **3 successes** what seems more likely (**close to 30%** probability to happen).
- n = 10, p = 0.8 - In this figure, we can see that the **number of successes** is more likely to be **large**. **Being 8 successes** what seems more likely (**close to 30%** probability to happen).
![](../attachments/screenshot-2024-02-26-at-221729.png)

Python provides binomial functions `binom.pdf` for the pmf and `binom.cdf`  for the cdf. They require 3 arguments
1. **value** at which to compute the pmf or cdf.
2. **size** of the Binomial
3. **p** parameter of the Binomial

```python
binom.pmf(3, 10, 0.3) #pmf when x=3 , returns 0.266827
# Returns P(X=3) = p(3) for a Binomial random variable with parameter n=10 and p=0.3

binom.cdf(8, 10, 0.8) #cdf when x=8, returns 0.6241904
# Returns P(X <= 8) = F(8) for a Binomial random variable with parameter n=10 and p=0.8
```

### Random numbers from a Binomial rbinom
Python provides a method for **generating pseudo-random numbers using a binomial distribution** through the function `np.random.binomial`. This function will require three arguments:
1. **N** is the parameter **n** of the Binomial
2. **p**, the parameter **p** of the Binomial
3. **Size**, the parameter for specifying the **number of pseudo-random numbers we want to generate**.

This example would be equivalent to repeating 100 times the experiment of tossing a coin 20 times and counting the number of heads.
```python
import numpy as np
np.random.binomial(n=20, p=0.5, size=100)

#Returns
array([12, 15, 12, 10, 8, 11, 8, 8, 12, 11, 11, 11, 10, 9, 8, 8, 12,
10, 9, 10, 7, 5, 11, 9, 6, 11, 13, 8, 8, 11, 8, 10, 11, 11,
10, 10, 10, 8, 7, 10, 12, 11, 11, 9, 12, 8, 10, 8, 9, 12, 13,
8, 10, 11, 12, 10, 10, 11, 9, 6, 12, 11, 5, 11, 10, 7, 12, 12,
12, 10, 13, 10, 12, 14, 7, 10, 9, 6, 10, 11, 6, 4, 9, 9, 12,
10, 8, 9, 11, 14, 12, 14, 12, 9, 9, 13, 14, 16, 8, 9])
```

