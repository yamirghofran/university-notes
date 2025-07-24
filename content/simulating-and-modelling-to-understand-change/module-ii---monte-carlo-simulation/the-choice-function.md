---
title: The Choice Function
---

The `choice` function is a function we will use often in simulation when we want to randomly choose between a possibility of options (e.g. a dice). It takes 4 arguments:
- **a**: a numpy array of values we want to sample from.
- **size**: the size of the sample we want.
- **replace**: if True sampling is done with replacement. That is if a value has been selected, it can be selected again. By default equal to False.
- **p**: a numpy array of the **same length of a** giving the probabilities that the elements of **a** are selected. By default equal to a uniform probability.
So, for example, if we wanted to simulate ten tosses of a fair dice we can write:

```python
np.random.seed(2023)
np.random.choice(a = [1,2,3,4,5,6], size = 10, replace = True)

# Returns
array([2, 2, 5, 4, 5, 5, 6, 1, 2, 6])
```

Notice that the vector a does not necessarily needs to be numeric. It could be a vector of
characters.

For example, let’s simulate the toss of 7 coins, where the probability of heads is
2/3 and the probability of tails is 1/3.

```python
np.random.seed(2023)
np.random.choice(a = ["heads", "tails"], size = 7, replace = True, p = [2/3, 1/3])

# Returns
array(['heads', 'tails', 'heads', 'heads', 'heads', 'heads', 'heads'])
```
