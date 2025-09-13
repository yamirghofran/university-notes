---
title: Goal-based Agents
weight: 4
---

Goals describe the situations that are desirable
- Straightforward goals will be the result of the next actions
- Complex goals will require search or planning to figure out the next action

Goal based agent are more **flexible**, as the goal might adapt or change.
![](../attachments/cleanshot-2025-09-13-at-1302582x.png)
```
function MODEL-BASED-GOAL-AGENT(percept) returns an action
	persistent: state, the agent's current conception of the world state
		model, a description of how the next state depends on current state and action goal, a desired state
		action, the most recent action, initially none
	state ← UPDATE-STATE(state, action, percept, model)
	for action in POSSIBLE_ACTIONS(state)
		final_state ← UPDATE-STATE(state, action, percept, model)
		if final_state = goal then return action
	return none
```
