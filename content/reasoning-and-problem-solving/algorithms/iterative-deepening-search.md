---
title: Iterative Deepening Search
---

Instead of picking L (like in [Depth-Limited Search](/reasoning-and-problem-solving/algorithms/depth-limited-search)), we just try L = 0, L = 1, L = 2, ...

```
function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution, or failure
	for depth = 0 to ∞ do
		result ← DEPTH-LIMITED-SEARCH(problem,depth)
		if result ≠ cutoff then return result
```

## Time and Space Complexity
- Time - $O(b^d)$ if there is a solution, $O(b^m)$ if there is not
- Space - O(bd) if there is a solution, O(bm) if there is not

The cost is effectively equal to that of the last call to depth-limited search