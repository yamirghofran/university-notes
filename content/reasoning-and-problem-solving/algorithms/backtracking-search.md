---
title: Backtracking Search
---

- Keeps a single representation of the state, that is altered in each step
- Can be improved by domain-independent heuristics
	- Variable and value ordering
	- Interleaving search and inference
	- Intelligent backtracking
	- Constraint learning

```
function BACKTRACKING-SEARCH(csp) returns a solution, or failure
	return BACKTRACK(csp, {})
function BACKTRACK(csp, assignment) returns a solution, or failure
	if assignment is complete then return assignment
	var ← SELECT-UNASSIGNED-VARIABLE(csp, assignment)
	for each value in ORDER-DOMAIN-VALUES(csp, var, assignment) do
		if value is consistent with assignment then
			add {var = value} to assignment
			inferences ← INFERENCE(csp, var, assignment)
			if inferences ≠ failure then
				add inferences to csp
				result ← BACKTRACK(csp, assignment)
				if result ≠ failure then return result
				remove inferences from csp
			remove {var = value} and inferences from assignment
	return failure
```