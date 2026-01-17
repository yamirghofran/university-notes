---
title: Solving CSPs
---

Sometimes, even after constraint propagation, we still have variables with multiple possible values
- [Backtracking Search](/reasoning-and-problem-solving/algorithms/backtracking-search) works on partial assignments
- [Local Search for CSPs](/reasoning-and-problem-solving/algorithms/local-search-for-csps) works on complete assignments

## Search
- State: partial assignment
- Action: extends the assignment, adding a value
- Tree would have $d^n$ leaves, thanks to commutability

## Variable and Value Ordering
### Variable Ordering
- Static
- Random choice
- Minimum-Remaining-Value (MRV)
	- choose the variable with the fewest legal moves
	- Aka fail-first, or most constrained value
	- can perform orders of magnitude better than static or random selection
- Degree heuristic
	- for when all variables have the same MRV
	- selecting variable with the largest number of constrants
	- used as tiebreaker in MRV
### Value Ordering
- Least-Constraining-Value
	- Prefer values that rule out the fewest choices in neighbors
	- e.g. in the coloring problem, if we can pick again an already used color, it would be better (unused colors remain usable by others)

## Interleaving Search and Inference
### Forward Checking
- whenever a variable X is assigned
- for every variable Y connected to X by a constraint
- delete from Y's domain any value inconsistent with the value of X
e.g in map-coloring problem
![](../attachments/cleanshot-2025-11-09-at-1532562x.png)

### Maintaining Arc Consistency (MAC)
Same as forward checking, but looking further ahead.

Effectively, after assigning a value to X, we call [AC-3](/reasoning-and-problem-solving/algorithms/ac-3), starting with all the constraints on variable X in the queue.


## Intelligent Backtracking
### Chronological Backtracking
- the one in [Backtracking Search](/reasoning-and-problem-solving/algorithms/backtracking-search)
- most recent decision point is revisited

### Backjumping
- considers conflict-sets (i.e. assignments that restrict current variable)
- jumps to the most recent variable in the conflict set
- not useful if using forward-checking or MAC (you either do them or this)

### Conflict-Directed Backtracking
- uses a more complete definition of conflict sets
- this includes, when backjumping, adding to the conflict set of the destination variable the conflict set of the one that failed
conf(Xi) <- conf(Xi) U conf(Xj) - {Xi}
- We remove $X_i$, as the variable itself can't be in its own conflict set

## Constraint Learning
- Process of identifying "no-good" variable/value combinations
- no-goods are used for forward-checking (as a new type of constraint) or by backjumpting (before the no-good is set)

## Structure of Problems
Structure of the constraint graph can help find solutions quickly
### Independent Subproblems
- e.g. Tasmania in the Australia coloring example
- given that the cost of solving a CSP was $O(d^n)$, we effectively are reducing n.
### Directional Arc Consistency (DAC)
- constraint graph is a tree
	- any two variables are connected by only one path
- can be solved in linear time to the number of variables
- use a topological sort of the variables (start with root, children always after parent)

There are different ways to reduce a graph to a tree

### Cutset Conditioning
- assign a value to a variable, such that remaining CSP becomes a tree
- iterate over possible assignments, until we find one

### Tree Decomposition
- Transform the graph into a tree, where each node consists of a set of variables
- Finding the decomposition is an NP-hard problem

