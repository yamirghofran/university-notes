---
title: Search Problem
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

| Component | Meaning |
|-----------|---------|
| **State space** | All possible states the environment can be in |
| **Initial state** | The starting state of the agent |
| **Goal test** | Function `IS-GOAL(s)` that returns true if `s` is a goal |
| **Actions** | Finite set of applicable actions in a state: `ACTION(s)` |
| **Transition model** | Function `RESULT(s,a)` that yields the state reached after doing `a` in `s` |
| **Action cost** | Function `c(s,a,s')` giving the step cost; reflects performance measure |