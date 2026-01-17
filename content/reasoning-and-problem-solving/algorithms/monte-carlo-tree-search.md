---
title: Monte Carlo Tree Search
---

```
function MONTE-CARLO-TREE-SEARCH(state) returns an action
	tree ← NODE(state)
	while IS-TIME-REMAINING() do
		leaf ← SELECT(tree)
		child ← EXPAND(leaf )
		result ← SIMULATE(child)
		BACK-PROPAGATE(result, child)
	return the move in ACTIONS(state) whose node has highest number of playouts
```