---
title: Scheduling
---

The process of allocating the [CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu) to different [Process](/computer-architecture-network-technology-and-operating-systems/operating-systems/process)es. The primary goal of scheduling is to optimize the use of system resources, ensure **fairness**, **efficiency**, and provide a responsive user experience.

**Criteria**:
- Response time
	- Time the process takes to return any data
- Throughput
	- The number of processes that complete their execution per unit time. It measures the rate at which processes are completed by the system.
- Turnaround time
	- Time the process takes to finish
- Waiting time
	-  The time a process spends waiting in the ready queue for the CPU to become available. It does not include the time spent waiting for I/O operations.

## Types of Scheduling
There are two primary types of scheduling: **Cooperative(non-preemptive)** and **Preemptive**.

### Cooperative Scheduling
- In cooperative scheduling, the [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) relies on the processes to voluntarily yield control of the CPU back to the operating system.
-  The process will continue to execute until it completes its task or yields control back to the operating system.
-  This approach is also known as non-preemptive scheduling.
-  Cooperative scheduling is simple to implement but can lead to poor system performance if a process does not yield control in a timely manner.

### Preemptive Scheduling
-  In preemptive scheduling, the [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) forcibly takes control of the [CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu) from a [Process](/computer-architecture-network-technology-and-operating-systems/operating-systems/process) after a certain time period, known as a time slice or time quantum.
-  The operating system will then allocate the CPU to another process, allowing multiple processes to execute concurrently.
-  Preemptive scheduling provides better system responsiveness and fairness, as no single process can monopolize the CPU.
-  This approach is more complex to implement than cooperative scheduling but provides better overall system performance.
![](../attachments/cleanshot-2025-02-21-at-1533552x.png)
## Scheduling Algorithms
### First-Come-First-Served (FIFO)
The process that arrives first in the ready queue is executed first. Simple, fair. No starvation
- Convoy effect (short process blocked by long process)
- Non-optimal performance
- No priority considered
![](../attachments/cleanshot-2025-02-21-at-1534342x.png)

### Last-In-First-Out Scheduling (LIFO)
Stack-like behavior. Simple and responsive.

**Disadvantages**
- Starvation
- Inefficient for most practical applications
- Poor average waiting time.
### Shortest Job First (SJF)
The process with the shortest execution time is executed first.
### Priority Scheduling
Processes are assigned a priority, and the process with the highest priority is executed first.
### Round Robin (RR)
Each process is allocated a fixed time slice, and the [CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu) is allocated to each process in a circular fashion.

Fair, responsive, and simple.

**Disadvantages**
- Context switching overhead
	- You have to copy all registers, come back, do it again.
- Time quantum sensitivity
- Average performance
Critical: Selecting optimal Time quantum to switch the context
**Disadvantages**
- Starvation
- Inefficient

### Multilevel Queue Scheduling
Multiple queues and each queue has a different priority. Each queue will have a different algorithm for scheduling.

Linux uses [Completely Fair Scheduler](/computer-architecture-network-technology-and-operating-systems/operating-systems/completely-fair-scheduler).

| Scheduling Algorithm                    | Description                                                                                                         | Advantages                            | Disadvantages                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------- |
| **First-Come-First-Served (FIFO)**      | The process that arrives first in the ready queue is executed first. Simple, fair. No starvation.                   | - Simple<br>- Fair<br>- No starvation | - Convoy effect<br>- Non-optimal performance<br>- No priority considered                     |
| **Last-In-First-Out Scheduling (LIFO)** | Stack-like behavior. Simple and responsive.                                                                         | - Simple<br>- Responsive              | - Starvation<br>- Inefficient for most practical applications<br>- Poor average waiting time |
| **Shortest Job First (SJF)**            | The process with the shortest execution time is executed first.                                                     | - Efficient for short jobs            | - Starvation for longer jobs                                                                 |
| **Priority Scheduling**                 | Processes are assigned a priority, and the process with the highest priority is executed first.                     | - Priority-based execution            | - Starvation for lower priority processes                                                    |
| **Round Robin (RR)**                    | Each process is allocated a fixed time slice, and the CPU is allocated to each process in a circular fashion.       | - Fair<br>- Responsive<br>- Simple    | - Context switching overhead<br>- Time quantum sensitivity<br>- Average performance          |
| **Multilevel Queue Scheduling**         | Multiple queues and each queue has a different priority. Each queue will have a different algorithm for scheduling. | - Flexibility in scheduling           | - Complexity<br>- Starvation for lower priority queues                                       |

## Example Use Cases
-  Cooperative scheduling is often used in embedded systems or real-time systems where predictability and simplicity are crucial.
-  Preemptive scheduling is commonly used in general-purpose operating systems, such as Windows, Linux, or macOS, where responsiveness and fairness are essential.

## Mathematical Representation
The scheduling problem can be represented mathematically using the following equation:
$$
\begin{aligned}
\text{Response Time} &= \text{Waiting Time} + \text{Execution Time} \\
&= \frac{\text{Total Execution Time}}{\text{Number of Processes}} + \text{Execution Time}
\end{aligned}
$$
where the response time is the time it takes for a process to complete, the waiting time is the time a process spends waiting for the CPU, and the execution time is the time a process spends executing on the CPU.

