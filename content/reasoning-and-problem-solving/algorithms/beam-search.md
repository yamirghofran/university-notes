---
title: Beam Search
---

- Option 1: Limit size of frontier, keep on only k best f(n) nodes
	- Will be incomplete and sub-optimal
	- Good selection of k helps make it fast, and potentially near-optimal
- Option 2: Keep all nodes with f(n') > d f(n), where f(n) is current best