---
title: Online Local Search
---

Hill-climbing and local search:
- would work because of locality, only keep one state
- but would get stuck in a local maxima, now way to move

Random walk algorithm:
- Explore the environment, selecting action at random
- Works in finite and safely explorable spaces
- Will eventually finish, but can take a long time.

Worst case scenario for random walk, time exponential with number of states:
![](../attachments/cleanshot-2025-11-04-at-1632402x.png)

Hill-climbing augmented by memory: for each state: c(s, a, s') + H(s')

Results in [Learning Real-Time A* (LRTA*)](/reasoning-and-problem-solving/algorithms/learning-real-time-a-lrta):
- Builds a map of the environment
- Chooses the apparent best of current estimates
- New actions always have h(s) (lowest possible cost): optimism under certainty


## Learning in Online Local Search
Learning the map of the environment:
- Recording the outcome of each action for a state
Learning better estimates of the cost of each state:
- Updating local rules