---
title: Informed Search Strategies
---

Using [Heuristic Functions](/reasoning-and-problem-solving/heuristic-functions) where h(n) = estimated cost of the cheapest path from state at node n to goal state.
- [Greedy Best-First Search](/reasoning-and-problem-solving/algorithms/greedy-best-first-search)
- [A* Search](/reasoning-and-problem-solving/algorithms/a-search)
- [Satisficing Search](/reasoning-and-problem-solving/algorithms/satisficing-search)

## Memory-bounded Search
- A* search uses memory for:
	- Frontier
	- Reached states
- In general, there are ways to remove nodes from the reached states (depending on the problem)
- Other options:
	- [Beam search](/reasoning-and-problem-solving/algorithms/beam-search)
	- [Iterative-deepening A* search (IDA*)](/reasoning-and-problem-solving/algorithms/iterative-deepening-a-search-ida)
	- [Recursive best-first search (RBFS)](/reasoning-and-problem-solving/algorithms/recursive-best-first-search-rbfs)
	- [Simplified Memory-bounded A* (SMA*)](/reasoning-and-problem-solving/algorithms/simplified-memory-bounded-a-sma)
	- [Bi-directional heuristic search](/reasoning-and-problem-solving/algorithms/bi-directional-heuristic-search)