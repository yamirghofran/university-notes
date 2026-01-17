---
title: Vacuum Problem
---

Representing the Vacuum Problem as a [Search Problem](/reasoning-and-problem-solving/search-problem) problem:

## State Space
- 2 locations A and B
- Agent's location (A or B)
- Cleanliness of each location (clean or dirty)
This leads to $2*2*2=8$ distinct states.
A state might be represented as `(Agent_Location, A_Status, B_Status)`
e.g. `(A, Dirty, Clean)`

## Initial State
e.g. `(A, Dirty, Clean)`

## Actions
Define the actions an agent can take
- Suck
- Move left
- Move right
e.g. if the agent is in state `(A, Dirty, Clean)` and it does the action `Suck`, the resulting state is `(A, Clean, Clean)`

## Goal Test
Define the codition(s) that must be met for a state to be a goal state.

## Path Cost
Define a numeric cost for each action. For the simplest problems, this is often a uniform cost of 1 per action.