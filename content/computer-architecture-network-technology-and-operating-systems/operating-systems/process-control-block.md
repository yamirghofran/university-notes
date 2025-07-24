---
title: Process Control Block
---

The data structure used by an [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) (OS) to manage and control the execution of [Process](/computer-architecture-network-technology-and-operating-systems/operating-systems/process)es.
![](../attachments/cleanshot-2025-02-21-at-1537582x.png)
- Pointer
- Process state
- Process number
- Program counter
- Register
- Memory limits
- Open files list

```C
/* Simplified representation of the task_struct structure in Linux kernel */
struct task_struct {
volatile long state; // Process state (e.g., TASK_RUNNING, TASK_STOPPED)
struct thread_info *thread_info;
struct exec_domain *exec_domain; // Execution domain information (deprecated)
struct mm_struct *mm; // Memory management information (address space)
struct fs_struct *fs; // Filesystem information
struct files_struct *files; // File descriptor table
struct signal_struct *signal; // Signal handlers and signals pending
struct sighand_struct *sighand; // Signal handling information
...
/* Various other fields */
...
};
```

