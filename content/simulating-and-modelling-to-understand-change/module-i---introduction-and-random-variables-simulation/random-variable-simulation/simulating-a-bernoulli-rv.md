---
title: Simulating a Bernoulli RV
---

A probability distribution where there are 2 possible outcomes. The success has the probability p and the failure 1-p. The pmf can be written as: $$p(x) = \begin{cases}
p^x(1-p)^{1-x}, & x=0,1 \\
0, & \text{otherwise}
\end{cases}
$$
#### Mean and Variance
The mean and variance of the Bernoulli distribution can be easily computed as: $$E(X) = 0 \cdot (1-p) + 1 \cdot p = p$$ $$V(X) = (0-p)^2(1-p) + (1-p)^2 p = p(1-p)$$
```python
from scipy.stats import binom
import numpy as np

binom.pmf(0, 1, 0.25) # probability of failure = 0.75

binom.pmf(1, 1, 0.25) # probability of success = 0.25

np.random.binomial(1, 0.25, 20) # generating 20 random numbers from a Bernoulli distribution with p = 0.25, 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 1 1 0
```
