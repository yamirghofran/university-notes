---
title: Dijkstra
---

https://www.youtube.com/watch?v=GazC3A4OQTE

Dijkstra’s algorithm is built on a simple rule: always visit the node with the smallest known distance first. By repeating this, it uncovers the shortest path from a starting node to all others in a weighted graph that doesn’t have negative edges.

```python
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    shortest_path = {node: float('inf') for node in graph}
    shortest_path[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < shortest_path[neighbor]:
                shortest_path[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return shortest_path

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('A',1), ('C',2), ('D',5)],
    'C': [('A',4), ('B',2), ('D',1)],
    'D': [('B',5), ('C',1)]
}

print(dijkstra(graph, 'A'))
```

- `graph` is an adjacency list: each node maps to a list of `(neighbor, weight)` pairs.
- `shortest_path` stores the current best-known distance to each node (∞ initially, 0 for `start`).
- `heap` (priority queue) holds frontier nodes as `(cost, node)`, always popping the smallest cost first.
- For each popped `node`, it relaxes its edges: for each `(neighbor, weight)`, compute `new_cost`. If `new_cost` beats `shortest_path[neighbor]`, update it and push the neighbor with that cost.

And here’s the output:

```python
{'A': 0, 'B': 1, 'C': 3, 'D': 4}
```