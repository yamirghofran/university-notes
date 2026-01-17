---
title: Hill-Climbing Search
---

```
function HILL-CLIMBING(problem) returns a state that is a local maximum
	current ← problem.INITIAL-STATE

	loop do
		neighbor ← a highest-valued successor of current
		if VALUE(neighbour) ≤ VALUE(current) then return current
		current ← neighbor
```

Applicability and success depends on shape of the state-space landscape. Even in NP-hard problems, with exponential local maxima, it can result in good enough solutions.
## Challenges that result in no progress
### Local Maxima
- Peak that is not the global maximum
- No next move that improves the situation → it gets stuck
### Ridges
- Sequence of local maxima that is difficult to navigate
- Effectively local maxima not connected to each other
### Plateaus (or shoulder)
- Can be a local maxima or not
- Hill-climbing can't decide where to go next

## 8-queens Problem
- h = number of pairs of queens attacking each other
- start with a random board.
- example board: h = 1
![](../attachments/cleanshot-2025-11-04-at-1434212x.png)

- h = 17
- heuristic cost of moving each queen in its column
- Hill-climbing will pick one of the h = 12 options
![](../attachments/cleanshot-2025-11-04-at-1435272x.png)
- hill-climbing gets stuck 86% of the time, solving 14% of problems
- but it succeeds in 4 steps when it does
- and gets stuck in 3 when it does not

There are $8^8 = \text{17 million}$ states!

## Potential Improvements
- Sideways moves
	- Assuming we are in a plateau or shoulder, keep moving
	- Need to limit the number of steps
	- 14% → 94% success in 8-queens, but 21 steps for success and 64 for failure.
- Stochastic hill-climbing
	- Probability proportional to steepness
	- Usually slower, but can avoid some pitfalls
- First-choice hill-climbing
	- Randomly generate next candidates, instead of calculating the h for all possible ones
- Random-restart hill-climbing
	- Good solution for 8-queens: if we get stuck, just start over from a random state.
