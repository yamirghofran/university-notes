---
title: Depth-Limited Search
---

[[Y3Q1/Reasoning and Problem Solving/Algorithms/DFS|Depth-first search]] but with limited fixed depth (L)

```
function DEPTH-LIMITED-SEARCH(problem, l) returns a solution, or failure, or cutoff
	frontier ← a LIFO queue initially containing one path, for the problem's initial state
	solution ← failure
	while frontier is not empty do
		parent ← pop(frontier)
		if depth(parent) > l then
			solution ← cutoff
		else
			for child in successors(parent) do
				if child is a goal then
					return child
				add child to frontier
	return solution
```

## Time and Space Complexity
- Time - $O(b^L)$
- Space $O(bL)$

Long cycles are eliminated, as we can only waste time on a path of length L.

The trick is finding the right L:
- if L is too small, depth-limited search is not complete.
- L can be the number of states
	- Usually this would be very big
- L can be the diameter of the state graph
	- That is, the longest number of actions to get from one state to any other.
- In most cases, we won't know what L to choose.
	
