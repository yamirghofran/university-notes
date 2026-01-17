---
title: Simulated Annealing
---

```
function SIMULATED-ANNEALING(problem,schedule) returns a solution state
	current ← problem.INITIAL-STATE
	for t = 1 to ∞ do
		T ← schedule(t)
		if T = 0 then return current
		next ← a randomly selected successor of current
		ΔE ← VALUE(next) - VALUE(current)
		if ΔE > 0 then current ← next
		else current ← next only with probability e^ΔE/T
```

Combines [Hill-Climbing Search](/reasoning-and-problem-solving/algorithms/hill-climbing-search) with a Random Walk

Name comes from a simil with the process to harden metals or glass, by gradually cooling after heating.
Flip the problem from hill-climbing to gradient descent.
- e.g. ping-pong ball finding the lowest crevice in a table, start shaking the table and shake it increasingly less with time.

Depending on T, we will choose a worse node with probability e^ΔE/T

