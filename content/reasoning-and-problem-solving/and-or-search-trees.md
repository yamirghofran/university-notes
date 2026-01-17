---
title: AND-OR Search Trees
---

In past problems, all branching was defined by the actions (OR Nodes)
In [non-deterministic](/reasoning-and-problem-solving/non-deterministic-actions) [environments](/reasoning-and-problem-solving/environments), we also have AND Nodes.

A solution will:
- have a goal node at every leaf
- specifies one action at each OR node
- includes every outcome branch at each AND node

![](../attachments/cleanshot-2025-11-04-at-1507302x.png)
LOOP means that the same node is reachable from a previous state in the same path
- in implementations, we usually return *failure* to represent this.
- solutions can be [[Y3Q1/Reasoning and Problem Solving/Algorithms/BFS|BFS]], [Greedy Best-First Search](/reasoning-and-problem-solving/algorithms/greedy-best-first-search), or even [A* Search](/reasoning-and-problem-solving/algorithms/a-search)
- [And-Or Search](/reasoning-and-problem-solving/algorithms/and-or-search) algorithm