---
title: Inter-Process Communication
---

Mechanisms and protocols used to allow [Process](/computer-architecture-network-technology-and-operating-systems/operating-systems/process)es to exchange data and synchronize their actions.
## Data Exchange
IPC allows processes to exchange data.
This can be as simple as a signal to indicate an event or as complex as transferring large amounts of data via shared memory or message queues.

## Synchronization
Beyond data exchange, IPC mechanisms often play a crucial role in synchronizing the execution of multiple processes. This ensures that processes operate in a coordinated manner, adhering to dependencies and execution order requirements.

## Why
- Concurrency Management
- Resource Sharing
- Modularity and Scalibility
- Distributed Systems
- Efficiency and Performance

## Tools and Components
- [Pipes](/computer-architecture-network-technology-and-operating-systems/operating-systems/pipes)
	- Anonymous pipes
	- Named pipes (FIFOs)
- [Signals](/computer-architecture-network-technology-and-operating-systems/operating-systems/signals)
- [Message Queues](/computer-architecture-network-technology-and-operating-systems/operating-systems/message-queues)
- Semaphores
- [Shared Memory](/computer-architecture-network-technology-and-operating-systems/operating-systems/shared-memory)
- [Sockets](/computer-architecture-network-technology-and-operating-systems/operating-systems/sockets)
- [Memory-Mapped Files](/computer-architecture-network-technology-and-operating-systems/operating-systems/memory-mapped-files)
