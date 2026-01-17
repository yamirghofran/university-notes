---
title: Two-player zero-sum games
---

The problem is represented as [AND-OR Search Trees](/reasoning-and-problem-solving/and-or-search-trees).

- $S_0$: initial state
- TO-MOVE(s): player's whose turn is to move (new to games)
- ACTIONS(s): legal moves in state s
- IS-TERMINAL(s): whether the game ends at s
- UTILITY(s): value when the game ends (could be 1/0, or 1/0/0.5, etc)
We will use a common pattern of calling the player moving first MAX and the other player MIN.

![](../attachments/cleanshot-2025-11-09-at-1716102x.png)

## Optimal Decision in Games
- MAX wants to find a sequence of moves leading to a win
- MIN will act in consequence depending on MAX's move

We could generate a conditional plan (as in AND-OR search) but this requires a search tree where there is always a winning state (regardless of the other player).

AND-OR search can be generalized to a [Minimax](/reasoning-and-problem-solving/algorithms/minimax) Search (a type of [[Y3Q1/Reasoning and Problem Solving/Algorithms/DFS|DFS]])

>[!note]-
>to describe an individual move unambiguously, we sometimes use **ply**.

What action should A choose?
![](../attachments/cleanshot-2025-11-09-at-1724072x.png)
We will find the optimal strategy by working out the minimax value of each state MINIMAX(s):
- Minimax value is the utility for MAX of being in a state, assuming both players play optimally.

MINIMAX(s) = 
- UTILITY(s, MAX) if IS-TERMINAL(s)
- $\text{max}_\text{a in Actions(s)}$ MINIMAX(RESULT(s,a)) if TO-MOVE(s) = MAX
- $\text{min}_\text{a in Actions(s)}$ MINIMAX(RESULT(s,a)) if TO-MOVE(s) = MIN

Minimax decision = the action that is the optimal choice for MAX($a_1$)

>[!question]
>What if MIN is not playing optimally?

- MINIMAX will still get a result at least as good as if it did, or better
- However, there are variations that can consider probabilities of taking a risky move if MIN is not optimal (e.g. take a move that results in higher utility in most cases if MIN does not find the optimal one)

MINIMAX is not directly practical for most games:
- Time complexity $O(b^m)$
	- b is the branching factor, or number of legal moves at each state
	- m is the depth of the tree
- Space complexity can be $O(bm)$ or $O(m)$, depending on implementation
- For chess, we would need to search $10^{123}$ states 

