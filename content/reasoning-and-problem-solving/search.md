---
title: Search
---

## Search Problem
- **State space**: set of possible states the [environment](/reasoning-and-problem-solving/environments) can be in
- **Initial state**
- Set of one or more [goal states](/reasoning-and-problem-solving/goal-based-agents): `IS-GOAL(s)`
- Finite set of **actions** available for a given state: `ACTION(s)`
	- Actions are applicable to a state
- **Transition model** describes the resulting state of an action: `RESULT(s,a)`
- **Action cost function**: ACTION-COST(s, a, s') or c(s, a, s')
	- Cost function should reflect the [Agents](/reasoning-and-problem-solving/agents) performance measure.
## Solution
- **Path**: sequence of actions
- **Solution**: path from the initial to a goal state.
- **Optimal solution**: lowest path cost among all the solutions.