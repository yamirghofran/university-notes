---
title: A Game of Chance - Monte Carlo Simulation
---

We start simulating a little game of chance.
Peter and Paul play a simple game that consists of repeatedly tossing a fair coin.
On a given toss, if it comes up heads, Peter wins 1 euro from Paul; otherwise, if it
comes up tails, Peter gives 1 euro to Paul. Peter starts with zero euros, let's
simulate the game for 50 tosses and see how lucky he is.

We can simulate this game using the Python `choice()` function. Peter’s winning
on a particular toss will be 1€ or -1€ with equal probability. His winnings on 50
repeated tosses can be considered to be a sample of size 50 selected with
replacement from the set {1€, -1€}.

```python
np.random.seed(2023)
win = np.random.choice(a = [-1,1], size = 50, replace = True)
print(win[0:9])

# Returns
[ 1 1 -1 1 1 -1 1 -1 -1]
```

For this particular game Peter won the first game, then won the second, lost the third
and won the fourth...

Suppose Peter is interested in his cumulative winnings as he plays this game. The
function `cumsum()` computes the cumulative winnings of the individual values and we
store the cumulative values in a vector named `cumul.win`.

```python
cumul_win = np.cumsum(win)
print(cumul_win[0:9])

# Returns
[1 2 1 2 3 2 3 2 1]
```

So at the end of this specific game Peter lost 6€. The figure below reports Peter’s
fortune as the game evolved.

```python
cumul_win = np.array(cumul_win)
plt.plot(cumul_win, 'o-', label = 'Euros')
plt.legend()
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Cumulative Winnings for Peter')
plt.xlabel('Game plays')
plt.ylabel('Cumulative wins')
plt.show()
```
![](../attachments/screenshot-2024-02-27-at-215554.png)

Of course this is the result of a single simulation and the outcome may be totally
different than the one we saw.

The next figure reports four simulated games: we can see that **in the first one**
**Peter wins, in the second he loses, in the third he wins again and in the fourth he loses again.**

![](../attachments/screenshot-2024-02-27-at-215701.png)

Suppose we are interested in the following question.
**What is the probability that Peter breaks even at the end of the game?**
Evidently we cannot answer by simply looking at the outputs of the previous
simulations. We need to do a formal Monte Carlo study. In this type of experiment,
**we simulate the random process and compute the statistic of interest.** By
repeating the random process many times, we obtain a collection of values of the
statistic, which can then be used to approximate probabilities or expectations that
answer the questions.

As you may recall from the [estimation of π experiment](/simulating-and-modelling-to-understand-change/module-ii---monte-carlo-simulation/finding-pi-using-monte-carlo-simulation), **we first need to write a**
**function that simulates the experiment**. In particular we need to write a function
which outputs Peter’s winning at the end of the game. To make this function more
general, we define n to be the number of tosses and let the default value of n be
50.

```python
def peter_paul(n = 50):
return(sum(np.random.choice(a = [-1,1], size = 50, replace = True)))
np.random.seed(2023)
peter_paul()

# Returns 6
```

The output is the same as the previous code, so it seems that our function works correctly.
Let’s replicate the experiment many times.

So the vector experiment stores Peter’s final fortune in 1000 games. Since Peter’s
fortune is an integer-value variable, it is convenient to summarize it using the
**table** function.

```python
def peter_paul_rep(replicas = 1000, n = 50):
	results = []
	for i in range(replicas):
		results.append(peter_paul(n))
	return(results)
np.random.seed(2023)
experiment = peter_paul_rep()
experiment[:9]

# Returns
[6, 12, -8, -2, 12, 0, 2, -2, 4]
```

```python
experiment = pd.Series(sorted(experiment))
experiment_df = pd.DataFrame(experiment.value_counts(sort=False))
experiment_df.T
```
![](../attachments/screenshot-2024-02-27-at-220112.png)

```python
plt.vlines(experiment_df["values"], 0, experiment_df["counts"], colors='b', lw=5)
plt.plot(experiment_df["values"], experiment_df["counts"], 'bo', markersize=10)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Frequency of different results in Peter Paul experiment")
plt.show()
```
![](../attachments/screenshot-2024-02-27-at-220157.png)

**What is the probability that Peter breaks even at the end of the game?**
So we can see that Peter breaks even 109 out of 1000 times. Furthermore the plot shows us
that most commonly Peter will win/lose little money and that big wins/losses are unlikely.
To conclude our experiment we need to calculate our estimated probability of Peter breaking
even. Clearly this is equal to 109/1000= 0.109. In Python:

```python
sum(experiment==0)/1000 # Returns 0.109
```

Notice that we could have also answered this question exactly. The event Peter
breaking even coincides with a number of successes **n/2** in a Binomial experiment
with parameters **n=50** and **p=0.5**. This can be computed in Python as:
```python
np.random.binom(25, 50, 0.5) # Returns [1] 0.1122752
```
