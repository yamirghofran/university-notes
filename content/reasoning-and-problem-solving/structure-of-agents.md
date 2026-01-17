---
title: Structure of Agents
weight: 3
---

- [Agent](/reasoning-and-problem-solving/agents) = Architecture + Program
- Agent architecture: computing device with physical/software sensors and actuators
- Job of AI: design an agent program

Basic agent Program: take an input from the sensors and return an action to the actuators.

Agent function can be explicitly represented as a table-driven agent

```
function TABLE-DRIVEN-AGENT(percept) returns an action
	persistent: percepts, a sequence, initially empty
		table, a table of actions, indexed by percept sequences, initially fully specified

	append percept to the end of percepts
	action ← LOOKUP(percepts, table)
	return action
```

Table-driven approach does not work in practice:
- The table will be potentially infinite, but even in a limited lifetime agent, will likely be massive
- Filling in the table is by no means trivial, taking infinite time potentially
- Does not allow for learning, as the table is set from the start
E.g. for chess, there would be $10^{123}$ entries. For go, that number is $10^{360}$
![](../attachments/cleanshot-2025-09-10-at-1344002x.png)

**Key challenge**: Write minimal programs that, to the extent possible, produce rational behavior
## Vacuum Agent Example
[Vacuum Problem](/reasoning-and-problem-solving/vacuum-problem)
sensors: current position, dirtiness
actions: suck, right, left

```
function REFLEX-VACUUM-AGENT([location,status]) returns an action
	if status = Dirty then return Suck
	else if location = A then return Right
	else if location = B then return Left
```