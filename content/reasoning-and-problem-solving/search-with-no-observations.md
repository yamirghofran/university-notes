---
title: Search with No Observations
---

Sensorless or conformant problem: percepts provide no information at all.
Sensorless plans can save time and cost.
Instead of knowing the state, the agent will have a set of [Belief State](/reasoning-and-problem-solving/belief-state)s.
- In the belief states, the problem might be fully observable.
Solution is a sequence of actions (not a [Conditional Plan](/reasoning-and-problem-solving/conditional-plan))
- even if the [environment](/reasoning-and-problem-solving/environments) is non-deterministic, as we can't know what state we end up in.
![](../attachments/cleanshot-2025-11-04-at-1608072x.png)
We can adjust existing problems (P) into belief state problems:
- **States**
	- every possible subset of underlying states (i.e. $2^n$ states)
- **Initial state**
	- typically a set of all states in P.
- **Actions**
	- for `b={s_j,...,s_k} ACTIONS(b) = union of all ACTIONS_p(s_i)`
		- this only works if actions are legal from any state, or result in no effect.
- **Transition Model**
	- `RESULTS(b,a) = {s':s' = RESULT_p(s,a) for s in b}`
- **Goal test**
	- `IS-GOAL(b) if IS-GOAL_p(s) for every s in b`
- **Action Cost**
	- Complex if actions have different costs from different states, otherwise action cost is the same.

![](../attachments/cleanshot-2025-11-04-at-1612342x.png)