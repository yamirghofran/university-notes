---
title: Inference in CSPs
---

CSP algorithms will need to choose between:
- a new **variable assignment** (effectively equivalent to search)
- **constraint propagation** (reducing the number of legal values)

Constraint propagation focuses on **local consistency**, and can be seen as propagating via the constraining graph.

## Node Consistency
A single variable is node-consistent if all the values in the variable's domain satisfy the variables unary constraints

A graph is node-consistent if every variable in the graph is node-consistent

Making a graph node-consistent can be established before starting to solve


## Arc Consistency
$X_i$ is arc-consistent with respect to $X_j$ if for every value in $D_i$ there is some value $D_j$ that satisfies <$X_i$, $X_j$>

## Path Consistency

## K-consistency
- Node consistency is 1-consistency, Arc consistency is 2-consistency, etc.
- A CSP is strongly k-consistent if it is k-consistent and also (k-1)-consistent, (k-2)-consistent, ..., 1-consistent.

In a CSP with n nodes, and strong n-consistency, finding a solution is $O(n^2d)$ but finding n-consistency is exponential on n, and CSPs in the general case are NP-complete. We usually won't do that.

## Bounds Propagation
For some problems, instead of sets, we use lower and upper bounds:
- $D_k = [X_L, X_U]$

A CSP is bounds-consistent if
- For every variable X
- and for both the lower and upper-bounded values of X
- there exists some value Y that satisfies the constraints between X and Y
- for every Y