---
title: Search in Partially Observable Environments
---

Problems where there is limited sensing of the environment:
- a sliding tile puzzle with just one corner visible
- a local sensing vacuum
For every action:
`RESULTS(b, a) = {b_0: b_0 = UPDATE(PREDICT(b,a), o) and o belongs to POSSIBLE-PERCEPTS(PREDICT(b,a))}`

Transition in local-sensing vacuum world:
- Action results in two belief states
- Sensing narrows the possible states
![](../attachments/cleanshot-2025-11-04-at-1620412x.png)
Solution will also use [Conditional Plan](/reasoning-and-problem-solving/conditional-plan)s

`[Suck, Right, if Rstate = {6} then Suck else []]`

![](../attachments/cleanshot-2025-11-04-at-1624562x.png)

Agents in partially observable environments:
- Solution will be a conditional plan (not a path or sequence)
- The agent will maintain a [Belief State](/reasoning-and-problem-solving/belief-state) `b' = UPDATE(PREDICT(b,a),o)`
	- Monitoring, filtering or state estimation

![](../attachments/cleanshot-2025-11-04-at-1626362x.png)
