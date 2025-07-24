---
title: Simulating a Uniform RV
---

We say that a random variable X is uniformly distributed on the interval [a,b] if its **pdf** is
$$f(x) = \begin{cases} 
\frac{1}{b-a}, & a \leq x \leq b, \\
0, & \text{otherwise}.
\end{cases}$$
![](../attachments/screenshot-2024-02-27-at-120107.png)

**CDF of Uniform Distribution**
$$F(x) = \begin{cases} 
0, & x < a, \\
\frac{x-a}{b-a}, & a \leq x \leq b, \\
1, & x > b.
\end{cases}$$
**Mean and Variance of Uniform Distribution**
$$E(X) = \frac{a + b}{2}, \quad V(X) = \frac{(b - a)^2}{12}$$
So the mean is equal to the middle point of the interval (a, b). The uniform distribution will
be fundamental in simulation. As we have seen, the starting point to simulate random
numbers from any distribution will require the [simulation of random numbers uniformly distributed between 0 and 1](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/generating-random-numbers/generating-random-numbers-in-python).

### Implementation of Uniform Distribution in Python
Python provides an implementation of the uniform random variable with the
functions `stats.uniform.pdf(x, a, b-a)` (pdf) and `stats.uniform.cdf(q, a, b-a)` (cdf) whose details are as follows:

- the first argument x (pdf) or q (cdf) is the value at which to compute the function;
- the second argument is the parameter a , by default equal to zero;
- the third argument is the parameter b−a , that is the range of values, by default equal to one.

```python
stats.uniform.pdf(5,2,6-2) #Returns 0.25
#Computes the pdf at the point 5 of a uniform variable with a=2 and b=6

stats.uniform.cdf(0.5) #Returns 0.5
#Computes the cdf at point 0.5 of a uniform rv with a=0 and b=1
```

### Generating Random Numbers from a Uniform runif
To generate random numbers coming from a uniform distribution we use the runif
function that takes three arguments:
- **n** that is the number of pseudo random numbers you want to generate
- the second argument, **min**, is the parameter a, by default equal to zero;
- the third argument, **max**, is the parameter b, by default equal to one

Returns a sequence of 20 observations from a uniform distribution [0,1].
```python
np.random.uniform(0,1,20)

#Returns
array([0.53386128, 0.73851944, 0.63916182, 0.22944076, 0.82266152,
0.82932874, 0.09476141, 0.73767873, 0.51442004, 0.03309404,
0.3375104 , 0.56975057, 0.08970204, 0.14797386, 0.56713439,
0.10025041, 0.91647504, 0.19672307, 0.96110704, 0.67803999])
```