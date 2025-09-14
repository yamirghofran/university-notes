---
title: BFS
---

BFS explores the graph one layer at a time. It looks at all the neighbors of a starting node before moving on to the next level. A queue is used to keep track of what comes next.

BFS is particularly useful for
- Finding the shortest path in unweighted graphs
- Detecting connected components
- Crawling web pages


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