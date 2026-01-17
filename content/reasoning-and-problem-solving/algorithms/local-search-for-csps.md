---
title: Local Search for CSPs
---

```
function MIN-CONFLICTS(csp, max_steps) returns a solution or failure
	inputs: csp, a constraint satisfaction problem
		max_steps, the number of steps allowed before giving up
	current ← an initial complete assignment for csp
	for i = 1 to max_steps do
		if current is a solution for csp then return current
		var ← a randomly chosen conflicted variable from csp.VARIABLES
		value ← the value v for var that minimizes CONFLICTS(var, v, current, csp)
		set var = value in current
	return failure
```

![](../attachments/cleanshot-2025-11-09-at-1541132x.png)