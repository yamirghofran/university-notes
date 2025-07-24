---
title: Concurrent Programming
---

- [Race Conditions](/computer-architecture-network-technology-and-operating-systems/operating-systems/race-conditions)
- [Deadlocks](/computer-architecture-network-technology-and-operating-systems/operating-systems/deadlocks)
- [Livelocks](/computer-architecture-network-technology-and-operating-systems/operating-systems/livelocks)
- [Starvation](/computer-architecture-network-technology-and-operating-systems/operating-systems/starvation)
---
- Process: full memory stack and register set
- Threads: lightweight "processes" share memory stack but can have independent register set (hyper-threading)
- Coroutines: Even lighter. Share memory stack and register set. Takes advantage of resource access inefficiencies. User-level execution. Cooperative.

Thread vs Coroutine: Thread handled by OS, Coroutine by program.

## Fibers
Lightweight threads that are orgnized at the user user level, not by the OS.
Context switch between fibers is managed by a scheduler (if implemented, selects the next fiber...)
Fibers don't have a concept of a scheduler. They are low-level and have their own stack.
### Use Cases
- Sequence of asynchronous I/O operations
- Concurrent asynchronous fetch operations
- Organizing response code in an event-driven program
- Low-level control, game engines

## Coroutines
- Have scheduler
- High level.
- Non-blockcing
- Efficient resource use.
### Use Cases
- Producer code that 'pushes' values (via function call) to a consumer that 'pulls' them with a function call.
- Feed values through one or more filter coroutines before those values are ultimately delivered to consumer code.
## Usage
- **Threads**: dealing with CPU-bound tasks that can truly run in parallel, taking advantage of multi-core processors.
- **Fibers**: when you need many concurrent tasks that are not CPU-bound but spend a lot of time waiting for external resources. Fibers allow you to manage these tasks in a more memory-efficient way than traditional threads
- **Coroutines**: writing asynchronous code that is easy to read and maintain, especially for I/O-bound operations that would otherwise require complex callback structures.

Why do you get so many things in the `ps` command? Because it lists not only the processes but also the threads.

`<pthread.h>` is not a kernel lib.

## User-threads vs Kernel Threads
Up to kernel 2.6, pthreads were a library-only function. MacOS still works that way (but has other capabilities)
Since that version, linux threads are scheduled with the rest of the processes.
Lightweight kernel scheduling units are sometimes called kernel-threads (not k-threads).

Pthreads are 1:1(1 thread : 1 schedulable entity)
Fibers are m:n (m thread : n schedulable)

![](../attachments/cleanshot-2025-03-13-at-1618482x.png)

## Concurrent Design Patterns Example
![](../attachments/cleanshot-2025-03-13-at-1812362x.png)

![](../attachments/cleanshot-2025-03-13-at-1812482x.png)
![](../attachments/cleanshot-2025-03-13-at-1813002x.png)
![](../attachments/cleanshot-2025-03-13-at-1813202x.png)