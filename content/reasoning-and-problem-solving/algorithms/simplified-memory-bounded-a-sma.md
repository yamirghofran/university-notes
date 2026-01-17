---
title: Simplified Memory-Bounded A* (SMA*)
---

- Works like A* while there is memory
- When it can't add more:
	- Drops the worst f(n) node
	- Backtracks the f(n) value to its parent
- Complete if solution is reachable (give the limited memory)
- Optimal if optimal is reachable, best reachable otherwise
- Other details:
	- When all have same f(n), drops the oldest one
	- On some problems, can suﬀer from going back and forth between branches