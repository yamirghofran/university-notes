---
title: Hierarchical Search
---

Hierarchical planning BFS - [Automated Planning](/reasoning-and-problem-solving/automated-planning)
```
function HIERARCHICAL-SEARCH(problem, hierarchy) returns a solution or failure 
	frontier ← a FIFO queue with [Act] as the only element 
	while true do
	if IS-EMPTY(frontier ) then return failure
	plan ← POP(frontier ) // chooses the shallowest plan in frontier 
	hla ← the first HLA in plan, or null if none
	prefix,suffix ← the action subsequences before and after hla in plan
	outcome ← RESULT(problem.INITIAL, prefix )
	if hla is null then // so plan is primitive and outcome is its result 
		if problem.IS-GOAL(outcome) then return plan 
	else for each sequence in REFINEMENTS(hla, outcome, hierarchy) 
		do add APPEND(prefix, sequence, suffix ) to frontier
```