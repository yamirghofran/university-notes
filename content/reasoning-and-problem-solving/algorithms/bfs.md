---
title: BFS
---


Both [complete and cost-optimal](/reasoning-and-problem-solving/performance) (with equal action costs). Tradeoffs regarding time and space complexity.
BFS explores the graph one layer at a time. It looks at all the neighbors of a starting node before moving on to the next level. A queue is used to keep track of what comes next.

BFS is particularly useful for
- Finding the shortest path in unweighted graphs
- Detecting connected components
- Crawling web pages

```
function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
	if problem's initial state is a goal then return empty path to initial state
	frontier ← a FIFO queue initially containing one path, for the problem's initial state
	reached ← a set of states; initially empty
	solution ← failure
	while frontier is not empty do
		parent ← the first node in frontier
		for child in successors(parent) do
			s ← child.state
			if s is a goal then
				return child
			if s is not in reached then
				add s to reached
				add child to the end of frontier
	return solution
```

## Time Complexity
- We generate b nodes in each node.
- Each level n has $b^n$ nodes and will generate $b^{n+1}$ nodes.
- 1 + b + b2 + b3 + … + bd-1 + bd = $O(b^d)$
## Memory Complexity
The same as time complexity $O(b^d)$, as we need to keep all generated nodes in memory.

Early Goal Test is important here, otherwise it would be $O(b^{d+1})$

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

bfs(graph, 'A')
```

- `graph` is a dict where each node maps to a list of neighbors.
- `deque` is used as a FIFO queue so we visit nodes level-by-level.
- `visited` keeps track of nodes we’ve already processed so we don’t loop forever on cycles.
- In the loop, we pop a node, print it, then for each unvisited neighbor, we mark it visited and enqueue it.

And here’s the output:
```python
A B C D E F
```


**early goal test** (return as soon as you find answer) - works in BFS but not DFS and Dijkstra.