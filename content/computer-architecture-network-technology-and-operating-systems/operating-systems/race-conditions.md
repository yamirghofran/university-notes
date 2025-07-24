---
title: Race Conditions
---

- Non-determinism
	- The outcome is unpredictable and varies with different runs of the program, even if the input remains the same.
- Concurrency
	- Race conditions arise in concurrent environments where tasks are executed in parallel.
- Shared Resources
	- Access to shared resources (like global variables, static variables, or shared hardware resources) without proper synchronization is a common cause.
- Timing Sensitivity
	- The occurrence of a race condition often depends on the sequence and timing of uncontrollable events, such as the scheduling order of threads by the [Operating System](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system)
## Common Scenarios Leading to Race Conditions
- Check-Then-Act Operations
	- If a thread checks a condition (like if a resource is available) and then acts on it (accesses the resource), the condition may change after the check but before the action, due to another concurrent thread.
- Read-Modify-Write Sequences
	- When multiple threads read a value from a shared variable, modify it, and then write it back, the final value may reflect only one of the modifications, losing the others.
- Improper use of Synchronization Primitives
	- Even with synchronization mechanisms in place (like [Mutexes](/computer-architecture-network-technology-and-operating-systems/operating-systems/mutexes) or [Semaphores](/computer-architecture-network-technology-and-operating-systems/operating-systems/semaphores)), incorrect usage can still lead to race conditions, such as forgetting to lock a mutex or incorrect ordering of lock acquisition.
## Prevention and Mitigation
- [Mutexes](/computer-architecture-network-technology-and-operating-systems/operating-systems/mutexes), locks, and condition variables
	- Use mutexes or locks to ensure that only one thread can access a critical section of code at a time.
- Atomic Operations
	- Utilize atomic operations provided my many programming languages and frameworks that ensure a sequence of operations is treated as a single, indivisible step.
- Design Strategies
	- Architectural changes, such as reducing the sharing of mutable data between threads or using immutable data structures, can inherently prevent race conditions.