---
title: Non-deterministic Actions
---

The [agent](/reasoning-and-problem-solving/agents) does not know what state it transitions to after taking action.
An agent goes form a set of possible initial states ([Belief State](/reasoning-and-problem-solving/belief-state)s).
Instead of a path, we want a [Conditional Plan](/reasoning-and-problem-solving/conditional-plan) (or strategy).

## Erratic Vacuum Example
![](../attachments/cleanshot-2025-11-04-at-1456402x.png)
- 8 states, with 2 goal states
- Suck action
	- when applied to dirty square, sometimes even cleans adjacent
	- when applied to clean square, sometimes drops more dirt
- Transition model returns possible values
	- RESULTS(1, Suck) = {5, 7}
- Conditional plan
	- `[Suck, if State = 5 then [Right, Suck] else []]`