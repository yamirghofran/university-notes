---
title: Belief State
---

The belief state (b) is the agent's knowledge or summary of its current situation, serving as the basis for decision-making.

It's a probability distribution over all possible physical states (S) the environment could be in, given the agent's complete history of past actions and observations.

Since the actual state s is unknown, search algorithms operate in the **belief space (B)**, where each state in the search space is a belief state b.

The belief state is **dynamically updated** using Bayes' rule whenever the agent takes an action (a) and receives a new observation (o).

The belief state is a **sufficient statistic** for the entire observation-action history: it contains all the information necessary for optimal future action selection.