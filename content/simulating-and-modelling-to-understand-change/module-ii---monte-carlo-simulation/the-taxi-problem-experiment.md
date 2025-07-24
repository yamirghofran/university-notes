---
title: The Taxi Problem Experiment
---

Imagine that a person is walking through the streets of a city and notices the
following numbers of 5 taxis (n = 5) that pass by: 34,100,65,81,120. Can he/she
make an intelligent guess at the number of taxis in the city?: Is a problem of
statistical inference where population is the collection of taxis driven in the city
and one wishes to know the value of **N** (total number of taxis).
Assume taxis are numbered from 1 to N, **each equally likely to be observed** and
consider two possible estimates:
1. The largest taxi number observed.
2. Twice the sample mean.

The distribution of cabs will therefore be a uniform distribution of discrete values. The values
range from 1 to 100 (identifying number of each cab) and each and every one of them has
the same probability of appearing (0.01).

![](../attachments/screenshot-2024-02-27-at-223826.png)

### The largest taxi number observed
With the information we have, a sample of 5 taxis, this estimator is not going to be very
reliable. However, imagine that this person sees 5 taxis every day, for 1000 days. In this
case, it is more likely that the taxi with the highest number of all the taxis that this
person has seen coincides with **N**, since the total number of taxis **N** will be equal to the
number of the taxi with the highest number.

For example, if there are 100 taxis in total (N = 100), the number of the taxi with the
highest number will be 100 → N = highest number

**Twice the sample mean**
Taking into account the previously mentioned discrete uniform
distribution, the mean in the case of 100 cabs in total will be
50.5, but since the identifiers of each cab are integers, it will be
50, so → μ = 50, and, therefore 2μ = 100 = N

As you have already seen in Fundamentals of Data Analysis, the
best estimator of the population mean μ is the sample mean x̄,
so the best estimator for N using the information of the sample,
will be → 2x̄

$$E[X] = \frac{1}{n} \sum_{i=1}^{n} x_i$$

The problem here is that we don't know that N = 100, so we don't really know which of
the two is the better estimate. To test this, let's simulate two sampling distributions and
work with the expected value of each (mean) to see which of the two is less biased.

Which is a better estimator of the number of taxis N? We will compare these two
estimators using a Monte Carlo Simulation:
1. Simulate taxi numbers from a uniform distribution with a known number of
taxis N and compute the two estimates.
2. Repeat the simulation many times and obtain two empirical sampling
distributions.
3. Then compare the two estimators by examining various properties of their
respective sampling distributions.

The `taxi()` function will implement a single simulation. We have 2 arguments:
1. The actual number of taxis **N**.
2. The sample size **n**.

```python
def taxi(N,n):
	x = np.random.choice(np.arange(1,N+1), n, True)
	estimate1 = max(x)
	estimate2 = x.mean()*2
	return([estimate1, estimate2])
```

The sample() function simulates the observed taxi numbers and values of the two estimates
are stored in variables largest number and twice the mean. Let’s say actual number of taxis in
city is 100 (N = 100) and we observe numbers of n=5 taxis.

```python
np.random.seed(2023)
taxi(100,5)

# Returns largest number: 88, twice the mean: 110.0
```

We get values largestnumber= 88 and twicethemean= 110
Let’s simulate sampling process 1000 times. We are going to create a matrix with two rows
(largestnumber and twicethemean), and 1000 columns. This columns will hold the estimated
values of largestnumber and twicethemean for 1000 simulated experiments.

```python
def taxi_rep(replicas = 1000):
	results = np.zeros((replicas,2))
	for i in range(replicas):
		exp = taxi(100,5)
		results[i,] = exp
	return(results)
np.random.seed(2023)
taxi_experiment = taxi_rep()
```

In this way, we are simulating a thousand samples of 5 cabs each and obtaining
the estimates of each one of them.
We are thus generating a sampling distribution of largestnumber and another of
twicethemean.

Here we are looking for “unbiasedness,” which means that the **mean value of the**
**estimator (expected) should be equal to the parameter**. If we compare the
estimators assuming that the value of N is 100:
```python
largestNumber = taxi_experiment[:,0]
twiceTheMean = taxi_experiment[:,1]
print("Largest Number: ", largestNumber.mean(), "\n", "Twice the Mean: ", twiceTheMean.mean())

# Returns largest number: 84.105, twicethemean: 100.9328
```

In the same way, we can calculate its margin of error (composed by the standard
error and the z-value) to obtain a confidence interval and see which estimate is
closer to the N parameter.

```python
se1 = largestNumber.std()/math.sqrt(1000) # Returns 0.44756
se2 = twiceTheMean.std()/math.sqrt(1000) # Returns 0.83735
zalphaovertwo = 1.96
```

In the same way, we can calculate its margin of error (composed by the standard
error and the z-value) to obtain a confidence interval and see which estimate is
closer to the N parameter.

$$\bar{x} \pm z_{\alpha/2} \cdot \frac{s}{\sqrt{n}}$$


```python
CI_lower_LN = (largestNumber.mean() - (1.96*se1))
CI_upper_LN = (largestNumber.mean() + (1.96*se1))
print("Upper and Lower bounds for the Largest Number estimator are:",
CI_lower_LN, "and", CI_upper_LN)

#Returns
#Upper and Lower bounds for the Largest Number estimator
#are: 83.22777359458348 and 84.98222640541653
```

In the same way, we can calculate its margin of error (composed by the standard
error and the z-value) to obtain a confidence interval and see which estimate is
closer to the N parameter.

```python
CI_lower_LN = (twiceTheMean.mean() - (1.96*se2))
CI_upper_LN = (twiceTheMean.mean() + (1.96*se2))
print("Upper and Lower bounds for the Largest Number estimator are:",
CI_lower_LN, "and", CI_upper_LN)

#Returns
#Upper and Lower bounds for the Largest Number estimator
#are: 99.29159271066295 and 102.57400728933705
```

From the results, we can interpret that for both, the expected value estimation, and
the error estimation, the second method works much better, giving a more precise
prediction of the total number of taxis in the city, and having a lower variability in
the estimation.