---
title: Local Search
---

In local search, we relax previous constraints:
- We won't worry about the path, but the state
- We will explore continuous instead of discrete states
- We will remove the assumption about determinism
- We will remove the assumption of observability

In local search, we use algorithms that
- don't keep track of the paths or reaches states.
- might not be systematic
- use little memory
- can find reasonable solutions in large or infinite spaces
- useful for **optimization problems** (best state based on objective function)
![](../attachments/cleanshot-2025-11-04-at-1420482x.png)