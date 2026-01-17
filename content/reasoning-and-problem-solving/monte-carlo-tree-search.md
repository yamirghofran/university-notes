---
title: Monte Carlo Tree Search
---

MCTS applies when:
- the branching factor is too big to go beyond a few plys
- It is difficult to define a good branching factor

This is true for games like Go.


Instead of using a heuristic evaluation function, it uses the estimated value from simulations (aka playout or rollout) of complete games (i.e. we have a true utility at the end)

Average utility is usually the same as probability of winning (or win percentage)

Choosing random moves in the simulation is not valuable: instead we use a **playing policy**.
- biases moves towards "good" moves
- they can be learned using a neural network
- or use game-specific heuristics (e.g. capture moves in chess)

### Play Policy
Very quickly decide which action to take next. Not a search to find the optimal move, but a basic to bias towards good moves.
Common to learn these policies using Neural Networks.

Example: Upper Confidence bounds applied to Trees (UCT):
![](../attachments/cleanshot-2025-11-09-at-1945502x.png)
C is a constant, we can start with sqrt(2), but trying different values is common.


## Pure Monte Carlo Search
Do N simulations from the current state of the game, and calculate the win percentage.

For some games, pure MCTS converges to the optimal play as N increases, but that is not always the case.

1. Selection: select actions starting at the root of the tree
2. Expansion: generate a new child for the selected node
3. Simulation: perform a playout
4. Back-propagaion: update the nodes all the way up the tree

The selection policy needs to balance two factors:
- Exploration of states with few playouts
- Exploitation of states that look good, to improve estimate

## Comparison with other algorithms
For a game with branching factor of 32 and average depth of 100 ply, if we can consider a billion game states:
- [Minimax](/reasoning-and-problem-solving/algorithms/minimax) will search 6 ply
- [Alpha-Beta Search](/reasoning-and-problem-solving/algorithms/alpha-beta-search) with perfect move-ordering 12 ply
- Monte-Carlo can do 10 million playouts
Which is better will depend on many things.

We can sometimes combine MCST with aspects of Minimax or Alpha-Beta, e.g. doing early termination of playouts.

MCTS works well on new games: there is no need to have knowledge about what are good strategies for the game but works poorly on games where a single move can make a very big difference, as it might not find it.

We can see MCTS as a type of reinforcement learning

