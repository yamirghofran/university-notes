---
title: Monitors
---

A monitor is a synchronization construct used in concurrent programming to manage access to shared resources and ensure mutual exclusion. It is a high-level abstraction that encapsulates data and the operations that can be performed on that data, providing a way to control access to the data and ensure thread safety.

1. **Encapsulation**: A monitor encapsulates shared data and the procedures that operate on that data. This ensures that all access to the shared data is controlled and synchronized.
2. **Mutual Exclusion**: Monitors ensure that only one thread can execute a procedure (method) within the monitor at a time. This is achieved using an implicit lock that is acquired when a thread enters a monitor and released when the thread exits the monitor.
3. **Condition Variables**: Monitors use condition variables to allow threads to wait for certain conditions to be met before proceeding. Condition variables provide a way to block a thread until a specific condition is true, and to notify other threads when the condition changes.
4. **Wait and Signal**: Monitors provide `wait` and `signal` (or `notify`) operations to manage thread synchronization. The `wait` operation releases the monitor's lock and blocks the calling thread until it is awakened by a `signal` from another thread. The `signal` operation wakes up one or more waiting threads.
5. **High-Level Abstraction**: Monitors provide a higher-level abstraction compared to lower-level synchronization primitives like mutexes and semaphores. They simplify the implementation of synchronization logic by encapsulating it within the monitor's procedures.
Monitors are commonly used in languages like Java, where they are implemented using the `synchronized` keyword and `wait`/`notify` methods. They help to manage concurrent access to shared resources, prevent race conditions, and ensure data consistency in multithreaded programs.
![](../attachments/cleanshot-2025-02-21-at-1612032x.png)