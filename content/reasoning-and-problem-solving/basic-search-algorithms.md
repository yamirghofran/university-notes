---
title: Basic Search Algorithms
---

Given a [Search Problem](/reasoning-and-problem-solving/search-problem), a [search algorithm](/reasoning-and-problem-solving/algorithms/graph-search) returns a solution. If there is no solution, it might return a failure instead.

**Search Tree** is a tree representation of the path through the space graph where nodes represent states and edges represent actions.

>[!>Note]- This is different to the state space/graph.
>A state space/graph is the full map of every reachable state and the actions that connect them.  
>
>A search tree is a tree-shaped trace of the _paths_ the algorithm actually considers; it can repeat states and is rooted at the start state.

- A tree always has a unique path from a node to a root
- A search tree represents the paths between states to reach the goal.

For a problem, we start at the root then expand each node. To get the next possible nodes:
- We consider all available ACTIONS for a state
- and use the RESULT for the transition function to generate new nodes
- Every new node is called a child or successor node, and has a parent node.
- Frontier is the set of nodes with no children yet
- A state in the state graph is reached if there is a corresponding node in the search tree
## Search Tree Data Structure
- node.STATE
	- the state in the state graph this node corresponds to
- node.PARENT
	- the parent node
- node.ACTION
	- action applied to the parent to get to this node
- node.PATH-COST
	- total cost from the initial state
## Frontier Data Structure
The frontier will be some kind of queue
- IS-EMPTY(frontier)
	- true if there are no more nodes
- POP(frontier): removes and returns the top node
- TOP(frontier): returns the top node without removing
- ADD(node, frontier): inserts a node in the proper place
## Different types of Queues
- Priority queue
	- pop returns the node with the lowest cost according to `f(n)`. 
	- Used by **best-first-search**
- FIFO queue
	- pop returns the node that was added to the queue first.
	- used for **breadth-first search**
- LIFO queue (or stack)
	- pop returns the node that was added to the queue last. 
	- Used for **depth-first search**

## Redundant Paths
- Cycles in the state graph result in **repeated states** in the search tree
	- the search tree can be infinite, if we can visited the same node indefinitely
- Cycles are just one example of redundant paths
- **graph-search**
	- we will keep a set of all previously known states
	- it might keep the best path for each, or just ignore redundant paths
- **tree-like search**
	- problems where there is no need to check.
	- this would use less memory.
	- might check parents to avoid short cycles.
## Systematic Algorithms
- Explore the state space making sure that any state connected to the initial state would be visited
- On infinite state spaces it might still never terminate
---
Pseudocode - [Graph Search](/reasoning-and-problem-solving/algorithms/graph-search)
Ways to evaluate [Performance](/reasoning-and-problem-solving/performance)


