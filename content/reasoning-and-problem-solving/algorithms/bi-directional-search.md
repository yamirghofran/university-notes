---
title: Bi-directional Search
---

Search both from the initial and goal state (backwards) simultaneously.

```
	function BIBF-SEARCH(problemF , fF , problemB, fB) returns a solution node, or failure
	nodeF ← NODE(problemF.INITIAL) // Node for a start state
	nodeB ← NODE(problemB.INITIAL) // Node for a goal state
	frontierF ← a priority queue ordered by fF, with nodeF as an element
	frontierB ←a priority queue ordered by fB, with nodeB as an element
	reachedF ← a lookup table, with one key nodeF.STATE and value nodeF
	reachedB ← a lookup table, with one key nodeB.STATE and value nodeB
	solution ←failure
		while not TERMINATED(solution, frontierF, frontierB) do
			if fF (TOP(frontierF)) < fB(TOP(frontierB)) then
				solution ← PROCEED(F, problemF, frontierF, reachedF, reachedB, solution)
			else solution ← PROCEED(B, problemB, frontierB, reachedB, reachedF, solution)
	return solution
```

This reduces the time complexity significantly: $O(2 * b^{d/2})$