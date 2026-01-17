---
title: Online DFS
---

```
function ONLINE-DFS-AGENT(s') returns an action
	inputs: s', a percept that identifies the current state
	persistent: result, a table indexed by state and action, initially empty
		untried, a table that lists, for each state, the actions not yet tried
		unbacktracked, a table that lists, for each state, the backtracks not yet tried
		s, a, the previous state and action, initially null
	if GOAL-TEST(s') then return stop
	if s' is a new state (not in untried) then untried[s'] ← ACTIONS(s')
	if s is not null and s' != result[s, a] then
		result[s, a] ← s'
		add s to front of unbacktracked[s']
	if untried[s'] is empty then
		if unbacktracked[s'] is empty then return stop
		else a ← an action b such that result[s', b] = POP(unbacktracked[s'])
	else a ← POP(untried[s'])
	s ← s'
	return a
```