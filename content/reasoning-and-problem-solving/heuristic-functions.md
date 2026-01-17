---
title: Heuristic Functions
---

## Properties of a Heuristic Function
### Admissible
An admissible heuristic is on that **never overestimates** the true cost to reach the goal from any given state.
### Consistent
A consistent heuristic is a one where the estimated cost to the goal from a node $n$ should not be greater than the cost of taking one step from $n$ to a successor node $n'$ plus the estimated cost from $n'$ to goal node/state.

## Measuring the effect of Heuristic Functions
- Reducing the **effective branching factor** $b^*$
	- We can measure $b^*$ on a set of problems
	- $O((b^*)^d)$ instead of $O(b^d)$
- Reducing **effective depth** by kh
	- $O(b^{d-kh})$ instead of $O(b^d)$
![](../attachments/cleanshot-2025-09-24-at-1213252x.png)

## Sliding Puzzle Example
![](../attachments/cleanshot-2025-09-24-at-1138032x.png)
### Heuristics
1. $h_1$ = number of misplaced tiles (blank not included) = 8
2. $h_2$ = Manhattan distance for each tile to its position = 3 + 1 + 2 + 2 + 2 + 3 + 3 + 2 = 18
- $h_2$ is better than $h_1, h_2$ **dominates** $h_1$
- In general, if 2 heuristics are **admissible** and **consistent** the one with the higher values is better.
- Note: be careful about the cost of calculating the heuristic (not overestimate)

## Generating Heuristics
- relaxed problems
	- Consider what would be the cost if we make the rules more flexible
	- E.g. if instead of moving to blank spaces, we can always move to the contiguous space
- Composite heuristics (from multiple admissible ones):
	- h(n) = max{h1(n),...hk(n)}
- Sub-problems: pattern databases
	- Store exact solution cost for sub-problem instance
	- There are memory and computation costs
	- Diﬀerent sup-problem heuristics can turn into composite heuristics
- Disjoint pattern databases
	- Variation, where heuristics can be added instead of taken max
	- Not possible for all problems
- Precomputation of optimal paths
- Landmark points
- Differential heuristics