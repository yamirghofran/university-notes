---
title: Conditional Plan
---

aka contingency plan, policy, or strategy.

A course of action that explicitly handles the uncertainties arising from [partial observability](/reasoning-and-problem-solving/environments) and [Non-deterministic Actions](/reasoning-and-problem-solving/non-deterministic-actions).

Unlike a simple sequence of actions (a straight-line plan), a conditional plan is a structure (e.g. tree/graph) that includes conditional branches based on the observations the agent receives during execution.

It maps possible **observations** (or the resulting belief states) to subsequent actions. The plan specifies what action to take for every possible outcome of an action/observation step.

The goal of the search process is to find an **optimal conditional plan**