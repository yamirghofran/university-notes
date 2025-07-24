---
title: Starvation
---

- Priority Inversion
	- Lower-priority threads may suffer starvation because higher-priority threads continuously preempt them, preventing their execution.
- Resource Hogging
	- Some threads may hold critical resources for extended periods, or indefinitely, preventing other threads from making progress.
- Inefficient Scheduling
	- Scheduling algorithms that do not ensure fair time-sharing can lead to some threads being starved of CPU time.
## Common Scenarios
- Unfair Lock Policies
	- If a lock or synchronization mechanism does not guarantee a fair ordering of thread access (e.g. if it always favors the first thread to request access or prioritizes certain threads), then some threads may starve.
- Busy Waiting
	- Threads that continuously loop checking for a condition (busy waiting) can consume CPU resources, starving other threads.
- Improper Thread Prioritization
	- Misuse of thread priorities where lower-priority threads are perpetually postponed by the scheduler in favor of higher-priority threads, especially in systems with a significant number of high-priority threads.
## Prevention & Mitigation Strategies
- Fair Locks and Synchronization Mechanisms
	- Use locks that support fairness policies, ensuring that threads are served in the order of their requests or that every thread eventually gets a turn.
- Priority Inheritance
	- In systems with priorities, use priority inheritance mechanisms where a lower-priority thread holding a resource needed by a higher-priority thread temporarily inherits the higher priority to avoid being starved.
- Resource Allocation Limits
	- Implement limits on how long a thread can hold a resource or how often it can access it, ensuring resources are periodically freed for others
- Round-Robin or Fair Scheduling
	- Employ scheduling algorithms that ensure fair CPU time distribution among threads, preventing long-term starvation of any thread.