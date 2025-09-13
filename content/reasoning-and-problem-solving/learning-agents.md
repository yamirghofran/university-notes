---
title: Learning Agents
weight: 4
---

Early on, it became clear that agents needed to learn:
- Describing all possible situations is not feasible
- Environments might change or be unknown

Turing was already describing learning agents in 1950
![](../attachments/cleanshot-2025-09-13-at-1308212x.png)

## Conceptual Components
- **Learning element**
	- responsible for making improvements
	- Improvements can be made in all parts of the model previously described
- **Performance element**
	- responsible for selecting actions
	- Usually designed first, aﬀects the design of the learning element
- **Critic**
	- provides feedback to the learning element
	- Uses an external performance standard to measure current performance
- **Problem generator**
	- suggesting new actions
	- Sometimes actions will be taken to gather information, rather than do the known good thing