---
title: Automated Planning
---

## Classical Planning
Task of finding a sequence of actions to accomplish a goal in a discrete, deterministic, static, fully observable [environment](/reasoning-and-problem-solving/environments)
- These are both the logical agent and the problem-solving agent
- Require heuristics for each domain
- Exponential large state space
**Planning Domain Definition Language (PDDL)** allows representation of actions as schemas, using a factored representation.
- State is represented as conjunction of ground atomic fluents
- Goal is just like a precondition

## Action Schemas
Captures preconditions and effects.
Effects include delete (negative) and add (positive) lists

```
Action(Slide(t, s1 , s2 )),
	PRECOND: On(t, s1 )∧Tile(t)∧Blank(s2 )∧Adjacent(s1 ,s2 ), 
	EFFECT: On(t, s2 )∧Blank(s1 )∧¬On(t, s1 )∧¬Blank(s2 ))
```

## Algorithms for Classical Planning
- Can apply the same search algorithms we already studied
	- Forward or backward search
- Can apply logical inference to find the solution
- These problems can also be solved by applying other representations
	- Situation calculus applies [First Order Logic](/reasoning-and-problem-solving/first-order-logic)
	- [Constraint Satisfaction Problem](/reasoning-and-problem-solving/constraint-satisfaction-problem)s can be used to encode the problem

## Hierarchical Planning
- Hierarchical decomposition is at the core of efforts to manage complexity
	- At each level of the hierarchy, the function is reduced to a small number of activities
- **Hierarchical Task Networks (HTN)** are used as a representation
	- Actions are now referred to as "primitive actions"
- **High-level Actions (HLA)** represent the actions that can be refined into a sequence of actions, each being another HLA or a primitive action
	- Definition is recursive
	- HLA with only primitive actions is called an "implementation"
- A high-level plan achieves the goal from a given state if at least one of its implementations achives the goal from that state.
- [Hierarchical Search](/reasoning-and-problem-solving/algorithms/hierarchical-search)

## Other Topics
- Heuristics for planning (effective strategies as we can relax contraints), including domain-independent pruning and state abstraction
- Searching for abstract solutions
- Planning and acting in non-deterministic domains
- Times, schedules, and resources
- Analysis of planning approaches