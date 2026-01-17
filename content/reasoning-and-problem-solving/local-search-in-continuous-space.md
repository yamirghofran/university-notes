---
title: Local Search in Continuous Space
---

Different techniques to address this:
- Use variables (instead of states)
- Discretize them (i.e. increase or decrease the variables by δ)
- Empirical gradient (i.e. reduce δ over time)
- Gradient (i.e. solve the actual derivatives equation)
- Newton-Raphson to find roots

Some problems become constrained optimization problems
- variables must satisfy constraints (limits)
- Linear programming problems are one type, where inequealities for convex set
	- Time complexity polynomial on number of variables