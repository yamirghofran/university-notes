---
title: Uniform Cost Search (Dijkstra)
---

```plaintext
function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    if problem's initial state is a goal then return empty path to initial state
    frontier ← a priority queue ordered by pathCost, with a node for the initial state
    reached ← a table of {state: the best path that reached state}; initially empty
    solution ← failure
    while frontier is not empty and top(frontier) is cheaper than solution do
        parent ← pop(frontier)
        for child in successors(parent) do
            s ← child.state
            if s is not in reached or child is a cheaper path than reached[s] then
                reached[s] ← child
                add child to the frontier
                if child is a goal and is cheaper than solution then
                    solution = child
    return solution
```

- Code is the same as best-first search, using the path cost to sort the priority queue.
	- as in best-first search, the frontier cost might need updating, needing late goal test.
- Results are (almost) those of [[Y3Q1/Reasoning and Problem Solving/Algorithms/BFS|BFS]] if all actions cost the same
- Is [complete and cost-optimal](/reasoning-and-problem-solving/performance) (as long as actions cost greater than 0)
## Time and Space Complexity
- Depends on cost of the best solution $C^*$
- Depends on the lower bound cost of an action $\epsilon$
- O(b1+⌊C*/∈ ⌋) → if all actions cost the same $O(b^{1+d})$
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