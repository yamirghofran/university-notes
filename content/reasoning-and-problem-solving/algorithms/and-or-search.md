---
title: And-Or Search
---

```
function AND-OR-GRAPH-SEARCH(problem) returns a conditional plan, or failure
	OR-SEARCH(problem.INITIAL-STATE, problem, [])
function OR-SEARCH(state, problem, path) returns a conditional plan, or failure
	if problem.GOAL-TEST(state) then return the empty plan
	if state is on path then return failure
	for each action in problem.ACTIONS(state) do
		plan ← AND-SEARCH(RESULTS(state,action), problem, [state | path])
		if plan ≠ failure then return [action | plan]
	return failure
function AND-SEARCH(states, problem, path) returns a conditional plan, or failure
	for each si in states do
		plan_i ← OR-SEARCH(si, problem, path)
		if plani = failure then return failure
	return [if s1 then plan1 else if s2 then plan2 else ... if s_n-1 then plan_n-1 else plan_n]
```