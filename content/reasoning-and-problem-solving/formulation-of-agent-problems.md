---
title: Formulation of Agent Problems
weight: 5
---

- Problem-solving agents
	- correct action is not obvious, need to plan ahead.
	- use [atomic](/reasoning-and-problem-solving/agent-representation) representation
- Search algorithms
	- Finding the right sequence of actions
	- Not to be confused with searching on a list for an element
	- [informed](/reasoning-and-problem-solving/informed-search-strategies) and [uninformed](/reasoning-and-problem-solving/uninformed-search-strategies)
	- Simple [environments](/reasoning-and-problem-solving/environments)
		- episodic, single-agent, fully observable, deterministic, static, discrete, and known
## 4 Phases of Problem Solving
1. Goal formulation
2. Problem formulation
3. [Search Problem](/reasoning-and-problem-solving/search-problem)
4. [Execution](/reasoning-and-problem-solving/execution)

## Representing Problems as a Graph
- Each state in the state space is a node
- Each action is an edge between states
- The [cost](/reasoning-and-problem-solving/search-problem) of each action is associated with each edge.
![](../attachments/cleanshot-2025-09-13-at-1332442x.png)
## Standard and Real-World Problems
### Standardized Problems
- For illustration or benchmarking
- Concise and exact description
#### Grid Problems
- Two-dimensional rectangular array of square cells
- Agent can move from cell to cell, as long as there are no obstacles
- Cells might contain objects
- Agent might pick, push, or act upon the objects
- e.g. [Vacuum Problem](/reasoning-and-problem-solving/vacuum-problem)
![](../attachments/cleanshot-2025-09-13-at-1336422x.png)
- States?
- Initial state?
- Transition model?
- Cost of actions?
- Goal state(s)?
![](../attachments/cleanshot-2025-09-13-at-1337232x.png)
other examples
![](../attachments/cleanshot-2025-09-13-at-1337372x.png)
### Real-world Problems
- For things that people actually use
- Formulation changes depending on many factors
- Route-finding problem
- Touring problem: similar but visiting a number of cities while limiting cost
- VLSI layout: designing a circuit with millions of components
- Robot navigation: needs to handle partial observability, unreliable sensors, etc.

