---
title: DFS
---

DFS works differently from [BFS](/reasoning-and-problem-solving/algorithms/bfs). Instead of moving level by level, it follows one path as far as it can go before **backtracking**. Think of it as diving deep down a trail, then returning to explore the others.

We can implement DFS in two ways:
- **Recursive DFS**, which uses the function call stack
- **Iterative DFS**, which uses an explicit stack

DFS is especially useful for
- Cycle detection
- Maze solving and puzzles
- Topological sorting

## Recursive DFS

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

dfs_recursive(graph, 'A')
```

- `visited` is a set that tracks nodes already processed so you don’t loop forever on cycles.
- On each call, if `node` hasn’t been seen, it’s printed, marked visited, then the function recurses into each neighbor.

Traversal order:

```python
A B D E F C
```

## Iterative DFS

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))

dfs_iterative(graph, 'A')
```

- `visited` tracks nodes you’ve already processed so you don’t loop on cycles.
- `stack` is LIFO (last in, first out) – you `pop()` the top node, process it, then push its neighbors.  
- `reversed(graph[node])` pushes neighbors in reverse so they’re visited in the original left-to-right order (mimicking the usual recursive DFS).  

Here’s the output:

```python
A B D E F C
```