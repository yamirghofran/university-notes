---
title: Environments
weight: 3
---

Task environments: problem to which the agent is the solution

PEAS (Performance, Environment, Actuators, Sensors)

Environment includes everything that affect the agent that is not under their control (e.g. walls, steps, furniture, etc. for the vacuum cleaner)

![](../attachments/cleanshot-2025-09-10-at-1340182x.png)
## Observability

### Fully Observable
- Agent sensors give it access to the complete state of the environment.
- Only aspects that are relevant to a choice.
- e.g. Chess agent.
### Partially observable
- Noise, inaccurate or missing data
- e.g. Card game agent
### Unobservable
- Agent has no sensors at all

## Single-agent vs Multi-agent
### Single agent
- Sometimes it can be evident (e.g. solving a crossword is a single agent problem)
- Other entities are seen as agents (in the multi-agent sense) if describing the other entity would maximize its performance measure based on the first.
### Multiagents
- Competitive (only one can achieve its maximal performance)
- Cooperative (both can achieve the same maximum)
- Partiality cooperative (both can maximize performance, but with some limits)

## Determinism
### Deterministic
- Next state is completely determined by current state and action
- e.g. Chess agent
### Non-deterministic
- The majority of real world situations
- Partially observable environments appear as non-deterministic
### Stochastic
- Non-deterministic but with assigned probabilities to the possible states.

## Episodic vs Sequential
### Episodic
- Agent experience divide into single action episodes
- Next episode does not depend on past actions
### Sequential
- Agent's decision could affect all future decisions
- Much more complicated

## Static vs Dynamic
### Static
- Environment can't change while agent decides next action
- No need to worry about time
### Dynamic
- Continuously asking the agent what to do and changing
- Trading agent, Self-driving
### Semi-dynamic
If the environment does not change but performance does (e.g. can't take too long)
- e.g. Timed chess game agent

## Discrete vs Continuous
- Refers to the number of uniquely distinct states
- Can apply to time, state or both
- In some cases, if there are too many distinct states across a spectrum, the problem can be treated as continous

## Known vs Unknown
In unknown environments, there is no previous knowledge
Agent will need to learn the rules of the environment (i.e. the consequences of their actions, and how they change the state)
