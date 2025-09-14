---
title: A* Search
---

https://www.youtube.com/watch?v=ySN5Wnu88nE&t=1s

A* works like [Dijkstra](/reasoning-and-problem-solving/algorithms/dijkstra)’s but adds a **heuristic function** that estimates how close a node is to the goal. This makes it more efficient by guiding the search in the right direction.

```python
import heapq

def heuristic(node, goal):
    heuristics = {'A': 4, 'B': 2, 'C': 1, 'D': 0}
    return heuristics.get(node, 0)

def a_star(graph, start, goal):
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    came_from = {}

    heap = [(heuristic(start, goal), start)]

    while heap:
        f, node = heapq.heappop(heap)

        if f > g_costs[node] + heuristic(node, goal):
            continue

        if node == goal:
            path = [node]
            while node in came_from:
                node = came_from[node]
                path.append(node)
            return path[::-1], g_costs[path[0]]

        for neighbor, weight in graph[node]:
            new_g = g_costs[node] + weight
            if new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                came_from[neighbor] = node
                heapq.heappush(heap, (new_g + heuristic(neighbor, goal), neighbor))

    return None, float('inf')

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('A',1), ('C',2), ('D',5)],
    'C': [('A',4), ('B',2), ('D',1)],
    'D': []
}

print(a_star(graph, 'A', 'D'))
```

- `graph`: adjacency list – each node maps to `[(neighbor, weight), ...]`.
- `heuristic(node, goal)`: returns an estimate `h(node)` (lower is better). It’s passed `goal` but in this demo uses a fixed dict.
- `g_costs`: best known cost from `start` to each node (∞ initially, 0 for start).
- `heap`: min-heap of `(priority, node)` where `priority = g + h`.
- `came_from`: backpointers to reconstruct the path once we pop the goal.

Then in the main loop
- We pop the node with smallest priority.
- If it’s the goal, we backtrack via `came_from` to build the path and return it with `g_costs[goal]`.
- Otherwise, we relax the edges: for each `(neighbor, weight)`, compute `new_cost = g_costs[node] + weight`. If `new_cost` improves `g_costs[neighbor]`, update it, set `came_from[neighbor] = node`, and push `(new_cost + heuristic(neighbor, goal), neighbor)`.

Output:

```python
(['A', 'B', 'C', 'D'], 4)
```