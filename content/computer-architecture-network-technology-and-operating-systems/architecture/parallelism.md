---
title: Parallelism
---

# Instruction Level Parallelism
## Approaches to Exploit Parallelism
### Hardware-Based Techniques
-  **Pipeline**: Executes different stages of the execution process in parallel.
-  **Branch Prediction and Speculation**: CPU performs tasks that might not be needed to optimize execution flow.
-  **Dynamic Scheduling**: Rearranges instruction execution to reduce stalls.
### Software-Based Techniques
-  **Loop Unrolling**: Substitutes loops with repetitions to utilize instruction and data-level parallelism.
-  **Others**: Additional compiler optimizations to find parallelism at compile time.
# Data Level Parallelism
Three variations of SIMD
- Vector architectures
- Multimedia SIMD instruction set extensions
- Graphics processing units ([GPU](/computer-architecture-network-technology-and-operating-systems/architecture/gpu))

![](../attachments/cleanshot-2025-01-31-at-1026112x.png)![](../attachments/cleanshot-2025-01-31-at-1026222x.png)
# Thread Level Parallelism
- [Thread](/computer-architecture-network-technology-and-operating-systems/operating-systems/thread)
- [Process](/computer-architecture-network-technology-and-operating-systems/operating-systems/process)
![](../attachments/cleanshot-2025-01-31-at-1026472x.png)
# Simultaneous Multithreading (SMT)
![](../attachments/cleanshot-2025-01-31-at-1027272x.png)

# Multi-processing
![](../attachments/cleanshot-2025-01-31-at-1027542x.png)