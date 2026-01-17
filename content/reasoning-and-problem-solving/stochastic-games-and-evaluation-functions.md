---
title: Stochastic Games and Evaluation Functions
---

Stochastic games include a random element (e.g. dice). Backgammon is a classic example:
![](../attachments/cleanshot-2025-11-09-at-1948342x.png)

In addition to MAX and MIN nodes, we will include "chance nodes":
- Branching from each chance node represented the possible roles
- Each branch will have a probability
![](../attachments/cleanshot-2025-11-10-at-1328312x.png)
"expectiminimax value" : expected value (the average over all the possible outcomes of the chance nodes) instead of the minimax value.

![](../attachments/cleanshot-2025-11-10-at-1329192x.png)

Cut-off in stochastic games works the same way as in [minimax games](/reasoning-and-problem-solving/two-player-zero-sum-games), with an evaluation function. But, in stochastic games, the evaluation function must return values that are a positive linear transformation of the probability of winning.
- This is a good property in all games of chance.

Time complexity will now depend on:
- branching factor (b)
- maximum depth (m)
- but also on the possible dice-rolls (n)
$O(b^mn^m)$

For backgammon: n = 21, b ~= 20 (but can be much higher for doubles), then we only realistically get to a 3 or 4 ply.

We can use alpha-beta pruning, without looking at all nodes, if we can bound the possible values of the game (instead of using +/- infinite)

Some of the techniques we looked at before will also work with these games:
- Monte Carlo Tree Search
- Forward Pruning