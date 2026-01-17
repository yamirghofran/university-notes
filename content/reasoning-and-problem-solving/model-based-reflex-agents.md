---
title: Model-based Reflex Agents
weight: 4
---

Keeps track (i.e. **a model**) of the part of the world it can't see.
Requires some internal state that depends on percept history.

**Transition model**: Knowledge of how the world changes based on the agent actions or external events.
**Sensor model**: knowledge about how the sensors reflect the world.

The model of the world is not usually perfect, just a best guess.
![](../attachments/cleanshot-2025-09-13-at-1257482x.png)

```
function MODEL-BASED-REFLEX-AGENT(percept) returns an action
	persistent: state, the agent's current conception of the world state
		model, a description of how the next state depends on current state and action
		rules, a set of condition-action rules
		action, the most recent action, initially none
	state ← UPDATE-STATE(state, action, percept, model)
	rule ← RULE-MATCH(state,rules)
	action ← rule.ACTION
	return action
```

This is still a reflex-based agent but instead of just the current percept, it operates based on its **knowledge of the world**.

This fixes the issue of needing full observability, but we still need a set of **condition-actions** (if-else statements) to determine what to do.