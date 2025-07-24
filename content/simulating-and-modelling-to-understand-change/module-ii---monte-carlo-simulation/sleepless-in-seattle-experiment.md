---
title: Sleepless in Seattle Experiment
---

Sleepless in Seattle is a 1993 American Romantic Comedy. Annie and Sam are
supposed to meet on top of the Empire State Building where they would at last
meet. However, their arrival time depends on a variety of factors and may
actually not coincide and therefore never fall in love.

## Use Cases
Now, let A and S represent Annie ́s and Sam’s arrival times at the Empire State
Building, where we measure the arrival time as the number of hours after noon.
We assume:
- A and S are independent and uniformly distributed. That is, A and S are random variables symbolizing the arrival time of Annie and Sam, respectively.
- Annie arrives somewhere between 10:30 and midnight
- Sam arrives somewhere between 10:00 and 11:30PM.

Our Questions are:
- What is the probability that Annie arrives before Sam?
- What is the expected difference in arrival times?
- If they each wait only twenty minutes after their arrival, what is the probability that they meet?
- How much should they wait (assuming they wait the same amount of time), so that the probability they meet is at least 50%?

We start simulating a large number of values from distribution of (A,S) say, 1000,
where A and S are independent:

```python
np.random.seed(2023)
sam = np.random.uniform(10,11.5,1000)
annie = np.random.uniform(10.5, 12, 1000)
```

### Question 1: What is the probability that Annie arrives before Sam?
The following function outputs TRUE if Annie arrives before Sam and FALSE otherwise.

```python
def sam_annie_1():
sam = np.random.uniform(10,11.5,1)
annie = np.random.uniform(10.5, 12, 1)
return(annie < sam)
```

**What is the probability that Annie arrives before Sam?**
If we run a single simulation, for instance
```python
np.random.seed(2023)
sam_annie_1() # Returns [1] FASLE
```
We see that Annie does not arrive before Sam.

We can simply adapt sam_annie_1 to use 1000 random observations and give an estimate
of this probability.
```python
def sam_annie_1():
	sam = np.random.uniform(10,11.5,1000)
	annie = np.random.uniform(10.5, 12, 1000)
	return(sum(annie < sam)/1000)
np.random.seed(2023)
sam_annie_1() # [1] 0.246
```

We can even replicate the experiment 1000 times to get a sampling distribution and have an
estimate of the variability around this probability.

```python
def sam_annie_1_rep(replicas=1000):
results = []
for i in range(replicas):
results.append(sam_annie_1())
return(np.array(results))
np.random.seed(2023)
experiment_1 = sam_annie_1_rep()
```

![](../attachments/screenshot-2024-02-27-at-223010.png)
The probability that Annie arrives before Sam is around 0.22.

### Question 2: What is the expected difference in arrival time?
The function `sam_annie_2` computes this expectation using 1000 random observations.

```python
def sam_annie_2():
	sam = np.random.uniform(0,90,1000)
	annie = np.random.uniform(30, 120, 1000)
	return((sam-annie).mean())
```

We can replicate and create some plots.
```python
np.random.seed(2023)
sam_annie_2()
```
![](../attachments/screenshot-2024-02-27-at-223351.png)
So on average Sam arrives 30 minutes before Annie.

### Question 3: If they each wait only 20 minutes after their arrival, what is the probability that they meet?

The function sleepless below returns TRUE if Annie and Sam meets,FALSE otherwise.
```python
def sleepless(waiting = 20):
	sam = np.random.uniform(0,90,1)[0]
	annie = np.random.uniform(30, 120, 1)[0]
	if sam < annie:
		if sam + waiting > annie:
		return(True)
	elif annie + waiting > sam:
		return(True)
	return(False)
```

Let’s run it 10.000 times to get an estimate of the probability.
```python
def sleepless_rep(replicas=10000, waiting = 20):
	results = []
	for i in range(replicas):
		results.append(sleepless(waiting))
	return(np.array(results))
np.random.seed(2023)
experiment_3 = sleepless_rep()
experiment_3.mean() # Returns  0.2865
```
So we see that if they each wait 20 minutes, they have a probability of meeting around
0.2865.

### Question 4: How much should they wait (assuming they wait the same amount of time), so that the probability they meet is at least 50%?

In order to answer this question we can use the sapply function. We already know that if they wait 20 minutes, the probability of meeting is around 0.2865. So we consider longer waiting times like, for example 30 to 60 minutes, so we just have to use the same function over different waiting arguments.
![](../attachments/screenshot-2024-02-27-at-223729.png)

**waiting = 35** is the first one for which the probability is at least 0.50. So they
should wait 35 minutes or more if they want to have a probability of at least 50% to
actually meet.
