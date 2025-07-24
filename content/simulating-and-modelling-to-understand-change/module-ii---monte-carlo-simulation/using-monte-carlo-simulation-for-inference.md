---
title: Using Monte Carlo Simulation for Inference
---

- [Sleepless in Seattle Experiment](/simulating-and-modelling-to-understand-change/module-ii---monte-carlo-simulation/sleepless-in-seattle-experiment)
- [The Taxi Problem Experiment](/simulating-and-modelling-to-understand-change/module-ii---monte-carlo-simulation/the-taxi-problem-experiment)

We have already used Monte Carlo for Inference in the previous section. Monte
Carlo Simulation will allow us to infer general conclusions by replicating an
experiment and calculating parametrized statistics.

We did infer the probability of Peter breaking even after 50 games, but as we have
learned, this probability can be calculated with the Binomial distribution. Now we
will see some more examples in which we can only approximate the solution to
infer the result.

We will try to answer to the following questions:
- How often Peter will be on the lead?
- What is the maximum possible fortune for Peter during the game?
- What will be value of Peter’s fortune at the end?

We can add additional lines of code to our function peter_paul to compute several
statistics of interest in our experiment. To answer our questions, we focus on the
final fortune F, the number of times Peter is in the lead L, and the maximum
cumulative winning M. The output of the function is a list consisting of the values
of F, L, and M.

```python
def peter_paul(n = 50):
	win = np.random.choice([-1,1],n,True)
	cumul_win = np.cumsum(win)
	results = [sum(win), sum(cumul_win > 0), max(cumul_win)]
	return(np.array(results))
```

```python
np.random.seed(2023)
peter_paul()

#Returns
array([ 6, 46, 7])
```

Now that we have defined all the parameters to estimate in our experiment, the next step will be to replicate the experiment. Since the output of `peter_paul` is a vector, S will be a matrix of 3 columns and 1000 rows, where the columns correspond to the simulated draws of F, L, and M. We can verify the dimension of the matrix of S using the shape attribute.

```python
def peter_paul_rep(n_replicas = 1000, n = 50):
	results = np.zeros((n_replicas,3))
	for i in range(n_replicas):
		exp = peter_paul(n)
		results[i,] = exp
	return(results)
S = peter_paul_rep()
S.shape

#Returns (1000, 3)
```

How many times Peter in the lead? The likely answer to this question (we do not know for sure) is
in the L column (the second). We will create the **times_in_lead** variable with all the values and print the first 10.

```python
times_in_lead = S[:,1]
print(times_in_lead[:9])

# Returns [16. 5. 1. 0. 2. 0. 48. 31. 30.]
```

We can use the same strategy as for the Peter final fortune and plot the value counts.
```python
times_in_lead_df = pd.Series(sorted(times_in_lead))
times_in_lead_df = pd.DataFrame(times_in_lead_df.value_counts(sort = False))
times_in_lead_df.T
```
![](../attachments/screenshot-2024-02-27-at-220933.png)

In this case can be also useful to understand the results to use the proportions for each value in
**times_in_lead** to understand them better:

![](../attachments/screenshot-2024-02-27-at-221006.png)

Finally, we can compute some statistics of this variable from the S matrix:
```python
pd.DataFrame(S)[1].describe()
```
Outputs:
![](../attachments/screenshot-2024-02-27-at-221046.png)

**How many times Peter in the lead?**
We can not ensure this result, but we can say that is more likely for Peter to be all
the time or never in the lead than middle situations. We can also say that the
average of times in the lead for Peter is 23 out of 50.

**What is the maximum possible fortune for Peter during the game?**
Let’s consider the distribution of M, Peter’s maximum winning during the 50 plays.
We store the 1000 simulated values of M in the variable **maximum_lead** and
extract some valuable information as before:
![](../attachments/screenshot-2024-02-27-at-221128.png)

We can tell Peter that the maximum winnings he can have is 24€, so it could be a
good idea to end the game if he can at that point. We can also tell him that, in 75%
of the games his maximum winnings are of 8€, 5€ in 50% of them, and 2€ in 25%,
so those are also good and safer options to end the game.
On average the maximum winning for Peter during the game is of 5.37€.

**What will be value of Peter’s fortune at the end?**
Finally, we can estimate Peter's most likely final fortune in order to add more information to
the game. We will compute the same plots and statistics. As we have seen previously in this
Notebook, being this a game of chance, the most likely final fortune is around 0€.

![](../attachments/screenshot-2024-02-27-at-221243.png)
