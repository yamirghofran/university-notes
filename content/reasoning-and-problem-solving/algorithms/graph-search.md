---
title: Graph Search
---

```
function GRAPH-SEARCH(problem) returns a solution, or failure
	frontier ← a queue initially containing one path, for the problem's initial state
	reached ← a table of {state: node}; initially empty
	solution ← failure
	while frontier is not empty and solution can possibly be improved do
		parent ← some node that we choose to remove from frontier
		for child in EXPAND(parent) do
			s ← child.state
			if s is not in reached or child is a cheaper path than reached[s] then
				reached[s] ← child
				add child to frontier
				if s is a goal and child is cheaper than solution then
					solution = child
	return solution
```

```
function EXPAND(problem, parent) returns a list of nodes
	s ← parent.state
	nodes ← an empty list
	for action in problem.actions(s) do
		s' ← problem.result(s, action)
		cost ← parent.path-cost + problem.step-cost(s, action, s')
		add node to nodes
	return nodes
```

Time and space complexity measured in terms of state space:

- d, the depth or number of actions in an optimal solution
- m, the maximum number of actions in any path
- b, the branching factor or number of possible successors for a node