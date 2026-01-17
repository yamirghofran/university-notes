---
title: Agents
weight: 2
---

For each possible **percept sequence**, a **RATIONAL AGENT** should select an action that is expected to maximize its **[Performance](/reasoning-and-problem-solving/performance) measure**, given the evidence provided by the percept sequence and whatever **built-in [knowledge](/reasoning-and-problem-solving/knowledge-representation)** the agent has.

- Perceives [environment](/reasoning-and-problem-solving/environments)
- through sensors
- acting upon it through actuators

Sensors produce **percepts**, creating a **percept sequence**.

![](../attachments/cleanshot-2025-09-10-at-1308342x.png)
## Types of Agents
- [Simple reflex agents](/reasoning-and-problem-solving/simple-reflex-agents)
- [Model-based reflex agents](/reasoning-and-problem-solving/model-based-reflex-agents)
- [Goal-based agents](/reasoning-and-problem-solving/goal-based-agents)
- [Learning agents](/reasoning-and-problem-solving/learning-agents)
- [Utility-based Agents](/reasoning-and-problem-solving/utility-based-agents)
These are generalizations. Real agents might have characteristics of several.
Any type of agent can either be static or a learning agent.
## Sensors and Actuators
- Human
	- Sensors: eyes, ears, etc.
	- Actuators: hands, legs, etc.
- Software agent
	- Sensors: file contents, typed input, etc.
	- Actuators: writing files, playing sounds, etc.
## Agent Function
**Agent function**, mathematical map of inputs to outputs:
- Inputs
	- Built-in knowledge
	- Percept sequence
- Output
	- Next action
Agent programs (i.e. code or algorithm) is the way we would find it in practice.

## Performance Measure
Desirability of a sequence of environment states (caused by the sequence of actions of the agent)

"Do the right thing" = produce desired consequences ("consequentialism")

- From the point of view of designer (not the machine)
- Can be explicit or sometimes implicit
- Should be about the outcome, not how to achieve it
- Can be fully described, or might learn from the user