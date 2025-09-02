---
title: Scaling
---

**Scalability**: ability to handle more work as size of computer or app grows.
![](../attachments/cleanshot-2025-09-02-at-0942152x.png)
## Strong Scaling
The number of processors is increased while the problem size remains constant.
- Mostly used for long-running **CPU-bound** tasks.
- Amdahl's law: the speedup is limited by the fraction of the serial part of the software that is not amenable to paralleization.

## Weak Scaling
Both the number of processors and the problem size are increased.
- Mostly used for large **memory-bound** applications where the required memory cannot be satisfied by a single node.