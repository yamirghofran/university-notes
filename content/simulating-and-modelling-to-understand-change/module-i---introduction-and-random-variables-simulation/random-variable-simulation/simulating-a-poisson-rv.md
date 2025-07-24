---
title: Simulating a Poisson RV
---

The Poisson distribution is a discrete probability distribution, **which describes the**
**number of times an event occurs during a specific interval**; which can be of time,
distance, area, volume, among others.
For example, Poisson variables are: the number of calls received by a telephone
exchange in a period of 1 minute, the number of bacteria in a volume of 1 liter of
water or the number of faults on the surface of a rectangular piece of ceramic.

e.g. If we expect 4 patients to arrive every day, is it possible to calculate the probability of 3  arriving in a day, or 5 patients in a day? Yes, Poisson.

## Poisson Distribution
In a Poisson distribution, the following assumptions are always met:
- The **random variable is the number of times an event occurs during a defined interval.** The interval can be time, distance, area, volume, etc.
		X = number of times an event occurs during a defined interval.
- The **probability of occurrence is the same for any 2 intervals of equal length**.
- The occurrence or non-occurrence in any interval is **independent** of the occurence or non-occurrence in any other interval.
- **Two events cannot occur at exactly the same time**.

If these conditions are met, the discrete random variable X follows a Poisson distribution and will have the pmf:
$$p(x) = \begin{cases}
\frac{e^{-\lambda} \lambda^x}{x!}, & x=0,1,2,3,\ldots \\
0, & \text{otherwise}
\end{cases}$$
where: 
- **f(x) = P(X  = x) = p(x)**: probability of **x** occurrences in an interval
- **$\lambda = E(X)=V(X)$**: mean number of events within a given interval
- **e**: constant, euler number, base for natural logarithms = 2.71828
- The **sample space** of a Poisson RV is the **set of all non-negative numbers**
![](../attachments/screenshot-2024-02-26-at-234215.png)
The interesting thing about Poisson variables is that we can modify (if the model
allows it) the time interval (0, t] in which we count the events. Of course, this does
not necessarily have to be possible. But in general if the variable is poisson in (0, t]
it will be also in any sub-interval (0, t’] for all t’ such that 0 < t’ < t.
So we will be able to define a series of variables $X_t$ of distribution Po(t).

## Poisson Process Definition

Let’s consider a Poisson experiment with **λ equal to the average number of events in a**
**unit of time**. If **t** is an **amount of time in time units**, the random variable $X_t$ = number of events in the interval **(0,t] is a Po(λ⋅t)**. The set of variables $\{X_t\}_{t \gt 0}$ is called a Poisson process.
Python provides a straightforward implementation of the Poisson distribution through
the stats library, using the functions `dpois` for the **pmf** and `ppois` for the **cdf**. They
require two arguments:
- first argument is the value at which to compute the pmf or the cdf;
- second is the parameter λ of the Poisson;

So for instance poisson.pmf returns P(X=3) = p(3) for a Poisson random variable with parameter λ = 1.
```python
poisson.pmf(3,1) #returns 0.06131324
```

Returns P(X ≤ 8) = F(8) for a Poisson random variable with parameter λ = 4.
```python
poisson.cdf(8,4) #return 0.9786366
```


## Random numbers from a Poisson rpois
We can also generate pseudo-random numbers from a poisson distribution using the `np.random.possion(lambda, n)`. Arguments:
- **lambda**: the expectation for a specific time interval.
- **n**: amount of pseudo-random numbers
```python
np.random.poisson(4,100)

#returns
array([ 3, 2, 0, 4, 5, 6, 2, 0, 5, 7, 5, 3, 4, 1, 4, 3, 1,
3, 11, 6, 5, 2, 3, 2, 6, 2, 6, 3, 2, 1, 5, 5, 2, 1,
3, 4, 6, 4, 3, 7, 1, 3, 3, 3, 1, 3, 1, 4, 4, 3, 4,
7, 1, 2, 3, 1, 3, 4, 2, 4, 3, 3, 4, 6, 2, 3, 7, 2,
5, 5, 8, 4, 5, 4, 4, 10, 2, 3, 6, 4, 2, 2, 6, 3, 6,
4, 5, 3, 7, 3, 3, 2, 3, 5, 3, 2, 6, 7, 6, 4])
```
Returns a sequence of 100 observations for a Poisson distribution of **λ = 4.**