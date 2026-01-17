---
title: Learning Real-Time A* (LRTA*)
---

```
function LRTA*-AGENT(s') returns an action
	inputs: s', a percept that identifies the current state
	persistent: result, a table, indexed by state and action, initially empty
		H, a table of cost estimates indexed by state, initially empty
		s, a, the previous state and action, initially null
	if GOAL-TEST(s') then return stop
	if s' is a new state (not in H) then H[s'] ← h(s')
	if s is not null then
		result[s, a] ← s'
		H[s] ← minb ∈ ACTIONS(s) LRTA*-COST(s, b, result[s, b], H)
	a ← an action b in ACTIONS(s') that minimizes LRTA*-COST(s', b, result[s', b], H)
	s ← s'
	return a
function LRTA*-COST(s, a, s', H) returns a cost estimate
	if s' is undefined then return h(s)
	else return c(s, a, s') + H[s']
```

LRTA* is guaranteed to find a goal in a finite safely explorable environment
- not so if the environment is infinite

Can take $O(2^n)$ to explore n states in the worst case.
We can modify the algorithm by changing the action selection and updates rules