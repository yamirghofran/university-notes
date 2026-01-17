---
title: Online Search Agents
---

Online search interleaves action and computation.

Applies to dynamic and semi-dynamic environments:
- in this environment, time is important.

Can also apply to non-determenistic environments. For now we will assume a deterministic and full observable environment.

## Online Search Problems
In online search, we no longer know the state space or the transition model.
- Initial state
- goal state(s)
- action(s)
- action cost function
- heuristic function

After every action, the agent can determine the state via the percepts
- information can be used to augment a map of the environment
Agents will explore the "real" world, not the "model" of it
- Agents can only discover a successor for a state it occupies (can't jump around the "model" states)
- Nodes will need to get expanded in local order (e.g. DFS)
### Competitive Ratio
- Total cost of the path, compared with the cost if we had known the environment
- No bounded ratio can be guaranteed if there are paths with unbounded cost.
### Dead ends
- States from where the goal state is no longer reachable.
- No algorithm can always avoid dead ends if they exist (adversary argument)
- Causes: cliffs, one-way street etc.
- **safely explorable** state spaces: some goal state is reachable from every reachable state.
---
- [Online Local Search](/reasoning-and-problem-solving/algorithms/online-local-search)
- [Online DFS](/reasoning-and-problem-solving/algorithms/online-dfs)
- [Learning Real-Time A* (LRTA*)](/reasoning-and-problem-solving/algorithms/learning-real-time-a-lrta)

