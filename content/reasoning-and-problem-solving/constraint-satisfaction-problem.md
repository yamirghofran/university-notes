---
title: Constraint Satisfaction Problem
---

Using a [factored representation](/reasoning-and-problem-solving/agent-representation) for each state: a set of variables, each of which has a value.

CSP search algorithms use general-purpose (rather than problem-specific) heuristics to enable the solution of complex problems.

The main idea is to eliminate large portions of the search space all at once by identifying assignments that violate the constraints.
  
A CSP is defined by:
- Variables: $(X = {X_1, \dots, X_n})$
- Domains: $(D = {D_1, \dots, D_n})$ where each $(D_i)$ lists possible values for $(X_i)$
- Constraints: ($C = {C_1, \dots, C_m}$) specifying allowed combinations of values
The task is to find a complete assignment $(A: X \to \bigcup D)$ such that every constraint is satisfied.
## Domains
Consist of allowable values for a variable:
- $D_i$ represents values for $X_i$, expressed as $\{v_1, ..., v_k\}$
- For example:
	- For a boolean Xi, Di would be {true, false}
	- For a int Xi between 0 and n, Di would be {0, 1, …, n}

Domains can be:
- Discrete or continuous
- Finite or infinite
- With linear constraints or non-linear constraints
## Constraints
Consist of a scope and relation: `<scope, rel>`
- Scope: tuple of variables that participate
- Relation (rel): defines the values that the variables can take.

- <(X1, X2), {(3,1), (3,2), (2,1)}>
- <(X1, X2), X1 > X2>

Types of Constraints:
- Unary
	- restrict the value of a single variable
- Binary
	- relates to two variables
	- Binary CSPs only include binary and unary constraints
	- N-ary constraints can always be expressed as binary constraints
- Global
	- involve an arbitrary number of variables
	- `AllDiff`
		- if m variables have n distinct values, and m > n, there is an inconsistency
		- remove singleton variables value from other variables domain
			- repeat until there are no more singleton variables
			- if there is an empty domain, there is an inconsistency
	- `Atmost` (or resource constraint)
		- `Atmost(N, X1, X2,...,Xk) → Sum(X1,...,Xk) < N`
		- We can delete the maximum value of a domain if it is not consistent with the minimum value of the others
- Preference
	- encoded as costs on an individual variable assignment

## Variables
Assignment of variables: {$X_i = v_i, X_j = v_j, …$}
- Partial assignment
	- leaves some variables unassigned
- Complete
	- all variables have a value
- Consistent (legal)
	- variable assignments don't violate any constraints
A **solution** is a consistent and complete assignment.
- Partial solution is a partial assignment that is consistent.

## Examples

###  Map Coloring
Color the map where each state is green, red, or blue, and no adjacent states are the same color.
![](../attachments/cleanshot-2025-11-09-at-1456482x.png)
![](../attachments/cleanshot-2025-11-09-at-1456572x.png)

### Job-shop Scheduling
- Schedule the assembly of a car, by fulfilling tasks
- Each task can be described as a variable, with a start time
- Task might need to happen in certain order
- Task will take some amount of time to complete
 
 Car assembly with 15 tasks:
X = {$Axle_F, Axle_B, Wheel_{RF}, Wheel_{LF}, Wheel_{RB}, Wheel_{LB}, Nuts_{RF}, Nuts_{LF}, Nuts_{RB}, Nuts_{LB}, Cap_{RF}, Cap_{LF}, Cap_{RB}, Cap_{LB}, Inspect$}


