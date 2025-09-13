---
title: Simple Reflex Agents
weight: 4
---

Ignore the history of precepts, just select actions based on current percept.

Uses a set of **if-else** statements, or condition-action rules:
```
if A then B
```

Maps well to real situations (including human reflexes, deeply learned behaviors, etc.)

Biggest limitation: environment needs to be fully observable.
![](../attachments/cleanshot-2025-09-13-at-1254472x.png)
```
function SIMPLE-REFLEX-AGENT(percept) returns an action
	persistent: rules, a set of condition-action rules
	
	state ← INTERPRET-INPUT(percept)
	
	rule ← RULE-MATCH(state,rules)
	
	action ← rule.ACTION
	
	return action
```