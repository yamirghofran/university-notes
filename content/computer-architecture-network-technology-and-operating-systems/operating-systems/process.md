---
title: Process
---

A process is an independent program in execution with its own memory space. It is the smallest unit of work that can be scheduled by the operating system.
-   **Memory**: Processes have separate [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) spaces. Each process has its own address space, which means they do not share data directly. [Inter-process communication](/computer-architecture-network-technology-and-operating-systems/operating-systems/inter-process-communication) (IPC) mechanisms are needed to share data between processes.
-   **Overhead**: Creating and managing processes involves more overhead compared to threads due to the need for separate memory management.
-   **Isolation**: Processes are isolated from each other, which enhances stability and security. If one process crashes, it does not affect others.
-   **Context Switching**: Context switching between processes is generally more expensive as it involves switching memory maps and other resources.
### Use Cases
-   **Processes** are preferred when tasks need to be isolated for security or stability reasons, or when tasks are highly independent and do not need to share data frequently.

## Anatomy of a Process
- PID (process id)
- PPID (parent process id)
- Environment
- CWD (Current Working Directory)
- UID (user id) and GID (group id)
- Priority and [Scheduling](/computer-architecture-network-technology-and-operating-systems/operating-systems/scheduling)
- File Descriptors 
- Memory Management Information
- State (stage in the lifecycle)
- Signal Handling (the method of change of state of a process)

## Process Creation
- `fork()`
	- Creates a clone of the current process. Used a lot in concurrent programming. No parameters.
- `exec()`
	- Create completely different process. Needs a parameter of the program to run in the process.
## Process Hierarchy
### Init Process
First process and starts forking and exec-ing new processes.
![](../attachments/cleanshot-2025-02-21-at-1532182x.png)

Current substitute is systemd. Embedded uses busybox.

### Root Process
Same as init process. Usually PID 1.

Macos: kernel_task (0)
launchd (1)

![](../attachments/cleanshot-2025-02-21-at-1533072x.png)



---
- [Thread](/computer-architecture-network-technology-and-operating-systems/operating-systems/thread)