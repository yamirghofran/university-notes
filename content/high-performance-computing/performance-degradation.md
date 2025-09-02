---
title: Performance Degradation
---

[Peak performance](/high-performance-computing/peak-performance) - observe [sustained performance](/high-performance-computing/sustained-performance) = **SLOW**

## Starvation
Absence of work: not enough parallelism by user application to keep all the system resources busy, or there is enough work but it is not distributed evenly (load-balanced).

## Latency
The time it takes for information to travel from one part of a system to another.
- local memory access
- execution pipeline
- network requests
- etc.

## Overhead
The amount of additional work beyond the required amount to perform the computation
- task scheduling
- synchronization of parallelism
- support communication
- etc.

## Waiting
Waiting for shared resources due to contention of access degrades performance. Two or more requests at the same time to the same resource.