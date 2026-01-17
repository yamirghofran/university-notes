---
title: Satisficing Search
---

- Solutions that are suboptimal but "good enough"
- Weighted [A* Search](/reasoning-and-problem-solving/algorithms/a-search)
	- f(n) = g(n) + W x h(n) , W > 1
	- W is usecase-dependent
- Behaves partly like [Greedy Best-First Search](/reasoning-and-problem-solving/algorithms/greedy-best-first-search), but will still consider other paths
- Solution will be up to W times worse than the optimal (e.g. for roads is common to use 1.3, thus solutions can be 30% worse)