---
title: Livelocks
---

 - Active Waiting
	- The threads involved in a livelock are not blocked; they are actively performing operations, but these operations do not contribute to the program's progress.
- Cyclic Dependencies
	- Similar to deadlocks, livelocks often involve a cycle of dependencies, but instead of being blocked, the processes or threads continually try to resolve the deadlock by changing states.
- Mutual Interference
	- The actions of each thread interfere iwth the actions of the others, preventing any from completing their tasks.
## Common Scenarios
- Polite Workers Problem
	- A scenario where two processes continually yield resources to each other to avoid deadlock. Each process tries to be "polite" by giving control to the other process, but as a result, neither can proceed.
- Incorrect Recovery Attempts
	- System designed to detect and recover from deadlocks can sometimes enter a livelock if the recovery process involves repeatedly attempting actions that are continually negated by other processes' recovery actions.
## Prevention and Mitigation Strategies
- Backoff Algorithms
	- Implementing a backoff algorithm can help by making a thread wait for a random period before retrying an operation, reducing the chance of immediately conflicting with another thread's actions.
- Prioritization of Requests
	- Assigning priorities to different threads or their requests can help ensure that at least one thread makes progress by breaking the symmetry of the situation
- Detection and Intervention
	- Monitoring the system for signs of livelock and then either manually intervening or having automated systems to break the cycle and allow progress.