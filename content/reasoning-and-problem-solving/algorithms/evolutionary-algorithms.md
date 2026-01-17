---
title: Evolutionary Algorithms
---

Variant of stochastic [Beam Search](/reasoning-and-problem-solving/algorithms/beam-search), inspired by biology
- population of individuals (state)
- fittest individuals (highest values)
- produce offspring (successor states) via recombination
```
function GENETIC-ALGORITHM(population, fitness) returns an individual
	repeat
		weigths←WEIGHTED-BY(population, fitness)
		population2 ← empty list
		for i = 1 to SIZE(population) do
			parent1, parent2 ← WEIGHTED-RANDOM-CHOICES(population, weights, 2)
			child ← REPRODUCE(parent1, parent2)
			if (small random probability) then child ← MUTATE(child)
			add child to population2
		population ← population2
	until some individual is fit enough, or enough time has elapsed
	return the best individual in population, according to fitness
	
function REPRODUCE(parent1, parent2) returns an individual
	n ←LENGTH(parent1)
	c ← random number from 1 to n
	return APPEND(SUBSTRING(parent1, 1, c), SUBSTRING(parent2, c+1, n))
```

## Variations
- Genetic algorithms (state as string over finite alphabet), evolution strategies (states as sequence of numbers), or genetic programming (states as compute programs)
- Mixing number (i.e. parents of the next iteration) $\rho$
- Selection process
- Recombination procedure (e.g. crossover point for $\rho = 2$)
- Mutation rate
- Elitism (keep best from previous generation) and/or culling (discard individuals below a threshold)
- schema: substring in which some of the positions can be left unspecified
- instances of the schema: full states where the unspecified positions are specified
- if the average fitness of the instances of the schema is above the mean, then the number of instances of the schema will grow over time.

## 8-queen problem (represented as a genetic algorithm)
![](../attachments/cleanshot-2025-11-04-at-1449532x.png)