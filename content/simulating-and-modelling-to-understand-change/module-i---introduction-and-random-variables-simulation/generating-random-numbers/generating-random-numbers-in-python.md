---
title: Generating Random Numbers in Python
---

- [Properties of Random Numbers](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/generating-random-numbers/properties-of-random-numbers)
# Random Numbers Generation
Since we are not going to be able to generate purely random numbers, what we are
going to do is to generate pseudo random numbers that fulfill the properties of
uniformity and independence.
To do this, we are going to use Python.

Pseudo means false, in the sense that the numbers are not really random. They are
generated according to a deterministic algorithm whose goal is to mimic as much as
possible the appearance of randomness. In particular, for the sequence of random numbers
generated means that they must resemble independent instances of a Uniform distribution
between zero and one.

Possible deviations from the ideal numbers are:
- The numbers are not uniformly distributed
- The numbers may be discrete-valued instead of continuous
- Independence may not be satisfied


## Properties/Considerations for Generating Random Numbers
- The random generation should be **very fast**. In practice, we want to use random numbers to do other computations (for example simulate a little donut shop) and such computations might be computationally intensive: if random generation were to be slow, we would not be able to perform them.
- The cycle of random generated numbers should be **long**. The cycle is the length of the sequence before numbers start to repeat themselves.
- The random numbers should be **repeatable**. Given a starting point of the algorithm, it should be possible to repeat the exact same sequence of numbers. This is fundamental for debugging and for reproducibility.
- The method should be applicable in any programming **language/platform**.
- The random numbers should be **independent and uniformly distributed**.

## Generation
`random.seed()` or `np.random.seed()` allows us to reproduce the same sequence of random numbers for the purposes of replication of research.

Python has the ability to generate uniform random numbers
```python
np.random.seed(2024)
np.random.uniform(0,1,10) # (start, end, number of generations)

# returns
array([0.3219883 , 0.89042245, 0.58805226, 0.12659609, 0.14134122,
0.46789559, 0.02208966, 0.72727471, 0.52438734, 0.54493524])
```

[The Linear Congruential Method](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/generating-random-numbers/the-linear-congruential-method)
