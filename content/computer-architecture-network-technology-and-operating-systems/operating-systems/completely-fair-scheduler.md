---
title: Completely Fair Scheduler
---

CFS is a **multilevel queue** scheduling but using [Cgroups](/computer-architecture-network-technology-and-operating-systems/operating-systems/cgroups) in place of multiple queues.

[Operating System](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) will save how much time a process has consumed. A process that has high priority and high access, scheduler will reduce the access after some time.

- Fair
- Proportional share scheduling
- Virtual runtime (vruntime)
	- Take into account how much time the process has accessed the CPU. After some time, it will reduce their access.
- Red-Black trees (self-balancing binary search tree) to implement vruntime
- Time slices and preemption
	- Time assigned to processes is not the same. Time slices can be different and after Linux gets back the time.
- Load balancing
	- Processes are dynamically assigned to different cores. Put unused cores on hold to not use battery.
- Tuning with `nice` values.
	- Indicate if a process is important or not as a user.
	- Use `nice` to first run a process with a priority -20 to 20.
	- `renice` used for programs already running.
	- Super user (root user) can give any value to `renice`. Other users can only reduce priority.