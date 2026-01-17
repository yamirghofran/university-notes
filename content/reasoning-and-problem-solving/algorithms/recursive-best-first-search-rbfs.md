---
title: Recursive Best-First Search (RBFS)
---

- Operates similar to depth-first search
- … but stops search if there is alternative path with better f(n)
- When it backtracks, it keeps the best f(n) node of the subtree
- Can require excessive node regeneration
- Optimal if h(n) is admissible
- Linear space complexity… time complexity depends on many factors