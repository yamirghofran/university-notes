---
title: Alpha-Beta Pruning
---

A technique to remove large parts of the tree that don't affect the outcome. 

Consider a node n such that the player has the option of moving to n.

If the player has a better choice either at the same level (m') or at any point higher up (m), then the player will never move to n (so it can be pruned)

![](../attachments/cleanshot-2025-11-09-at-1814512x.png)

The name "alpha/beta" comes from new MAX/MIN VALUE functions:
- MAX-VALUE(state, α, β) / MIN-VALUE(state, α, β)
- α = best value found so far along the path for MAX ("at least")
- β = best value found so far along the path for MIN ("at most")
- [Alpha-Beta Search](/reasoning-and-problem-solving/algorithms/alpha-beta-search)

## Move Ordering
Pruning is highly dependent on the order in which nodes are expanded.
If we could find the perfect ordering, time complexity would be $O(b^{m/2})$
If we randomize the order, we get roughly $O(b^{3m/4})$ for some values of b
If we understand the game (e.g. chess) and some strategies, we can take that into account
Chess can be close to 2x of the best case

### Dynamic Move Ordering Schemes
- try first the moves that worked in the past
- iterative deepening can be used to re-use past explorations
- best moves are known as "killer moves", and usually tried first ("killer move heuristic")
- transposition table, to cache heuristic value of states when we can reach them by different paths (transpositions)

## Realistic Strategies
For real games, applying any of these strategies is usually impossible, so we identify two realistic ones:
- Type A Strategy
	- considers all moves to a certain depth, and then use a heuristic evaluation function to estimate utility
- Type B Strategy
