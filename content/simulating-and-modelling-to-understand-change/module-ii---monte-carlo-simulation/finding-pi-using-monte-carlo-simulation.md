---
title: Finding pi Using Monte Carlo Simulation
---

We will carry out the experiment in 5 steps:
1. Generate 2 random numbers between 0 and 1 in total 100 times (x and y).
2. Calculate x2 + y2 (This is the point in the space).
- If the value is less than 1, the case will be inside the circle
- If the value is greater than 1, the case will be outside the circle.
3. Calculate the proportion of points inside the circle and multiply it by four to approximate the π value.
4. Repeat the experiment a thousand times, to get different approximations to π.
5. Calculate the average of the previous 1000 experiments to give a final value estimate.

### Step 1. Generating two random numbers between -1 and 1, 100 times

```python
np.random.seed(2023)
nPoints = 100
x = np.random.uniform(0,1,nPoints)
y = np.random.uniform(0,1,nPoints)
print(x[1:10])

#Returns 
[0.322 0.89 0.588 0.127 0.141 0.468 0.022 0.727 0.524]

print(y[1:10])

#Returns
[0.878 0.519 0.68 0.436 0.972 0.365 0.623 0.258 0.681]

```
![](../attachments/screenshot-2024-02-27-at-212302.png)

### Step 2. Calculate the Circumference Equation
- If the value is less than 1, the case will be inside the circle.
- If the value is greater than 1, the case will be outside the circle.
```python
def circum(x,y):
result = []
for i in range(len(x)):
point = x[i]**2 + y[i]**2
if(point<=1):
result.append(True)
else:
result.append(False)
return(result)
```
![](../attachments/screenshot-2024-02-27-at-212435.png)

A value of the vector result is TRUE if x[i]^2 + y[i]^2 <= 1, that is if the associated point
is within the circle. We can see that out of the first six simulated points, only one is
outside the circle.
```python
sim_points = circum(x,y)
print(sim_points[1:10])

# Returns
[True, False, True, True, True, True, True, True, True]
```

### Step 3. Calculate the proportion of points inside the circle and multiply it by 4 to approximate the pi value.
So using our 100 simulated points, we came up with an approximation of 3.16 for
the value of π.

Of course this number depends on the random numbers that were generated. If we
were to repeat it (without using the seed), we would get a different approximation.

```python
pi_val = 4*sum(sim_points)/nPoints
print(pi_val)

# Returns
3.16
```

### Step 4. Repeat the experiment a thousand times, to get different approximations
Now that we know how to approximate the π number we can replicate the
experiment N times to perform a monte carlo simulation and obtain a better result.
We will use a single function for doing this:
```python
def pi_val_func(nPoint=100):
x = np.random.uniform(0,1,nPoints)
y = np.random.uniform(0,1,nPoints)
values = []
for i in range(len(x)):
point = x[i]**2 + y[i]**2
if(point<=1):
values.append(True)
else:
values.append(False)
pi_val = 4*sum(values)/nPoints
return(pi_val)
```

```python
np.random.seed(2023)
pi_val_func() #Returns 3.16
```

So we can see that the function works since it gives us the same output as the code above.
Now we can replicate this experiment any number of times (e.g., 1000 times) to obtain
different measures of the π number.
In order to do that we need to define a “replicate” function:
```python
def replicate_pi(n_replicas = 1000, nPoints = 100):
replicas = []
for i in range(n_replicas):
replicas.append(pi_val_func(nPoints))
return(np.array(replicas))
```

Therefore, the following code replicates the experiment
```python
np.random.seed(2023)
pi_numbers = replicate_pi()
print(pi_numbers[1:10])

# Returns 
[3.36 2.64 3.04 3.4 3.04 3.16 3.2 3.08 3.24]
```

We can see that the first entry of the vector **pi_numbers** is indeed **pi_numbers[0]** which is the
same value we obtained running the function ourselves (in both cases we fixed the same seed).

### Step 5. Calculate the average of the previous 1000 experiments to give a final value estimate

```python
pi_numbers.mean() # Returns 3.1428
```
The average gives us a good approximation of π. A boxplot can give us a
visualization of the results.
```python
plt.boxplot(pi_numbers)
plt.xlabel("Replicas")
plt.ylabel("Pi number")
plt.title("Pi number MC Simulation")
plt.show()
```
![](../attachments/screenshot-2024-02-27-at-213342.png)
The boxplot tells us two important things:
- If we were to take the median of the 1,000 approximations of π as the value of
π, we would get a value very close to the actual value (see the horizontal line
inside the box).
- If we were to choose a value for π based on a single simulation, then we could
choose values between 2.6 and 3.6.

### Conclusions
One thing you might wonder now is the following. Why did we replicate the
experiment 1000 times and each time took only 100 points. Could have we not
taken a much larger number of points only once (for example 1000×100)?
On one hand that would have clearly given us a good approximation, using the
same total number of simulated points.

However this approach **does not give us any information about uncertainty or**
**about how good our approximation is**. We have just one single value.

On the other hand, using replication we have 1000 possible approximations of π
and we can construct **confidence intervals of plausible values**.

For instance, we would believe that the true value π is with 95% probability in the
interval which includes 95% of the central approximations of π.

### Additional step: extending our knowledge
We can store the results of the experiment increasing the number of points and
replicas to plot the optimization function of the π number estimation.
```python
def optim_func_pi(max_nPoints, max_Replicas, n_repetitions):
	nPoints_sequence = np.linspace(100,max_nPoints,n_repetitions).round(0)
	replicas_sequence = np.linspace(1000,max_Replicas,n_repetitions).round(0)
	pi_averages = []
	for i in range(n_repetitions):
		print("Starting the estimation ", i, " out of ", n_repetitions)
		pi_vector = replicate_pi(int(nPoints_sequence[i]), int(replicas_sequence[i]))
		pi_averages.append(pi_vector.mean())
	return(pi_averages)
```
Here we have the resulting plot. We see that the algorithm is estimating better as
we increase the simulated points and the replicas of the experiment.

![](../attachments/screenshot-2024-02-27-at-213741.png)
