---
title: AC-3
---

```
function AC-3(csp) returns false if an inconsistency is found and true otherwise
	local variables: queue, a queue of arcs, initially all the arcs in csp
	while queue is not empty do
		(Xi, Xj) ← POP(queue)
		if REVISE(csp, Xi, Xj) then
			if size of Di = 0 then return false
			for each Xk in Xi.NEIGHBORS − {Xj} do
				add(Xk, Xi) to queue
	return true
```

```
function REVISE(csp, Xi, Xj) returns true iﬀ we revise the domain of Xi
	revised ← false
	for each x in Di do
		if no value y in Dj allows (x, y) to satisfy the constraint between Xi and Xj then
			delete x from Di
			revised ← true
	return revised
```


Time complexity: $O(cd^3)$
- c = the number of binary constraints
- d = the max domain size of variables