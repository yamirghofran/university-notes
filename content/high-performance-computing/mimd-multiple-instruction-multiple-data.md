---
title: MIMD (Multiple Instruction, Multiple Data)
---

In this architecture, each processor can execute different instructions on different data. This is the **most common** architecture for modern multi-core processors and supercomputers. 

MIMD allows for both task and data parallelism.

There are two main subcategories of MIMD:
- **Shared Memory MIMD**:
	- All processors have access to a common pool of memory. 
	- Communication between processors is fast and straightforward.
	- Typical multi-core laptop.
- **Distributed Memory MIMD**:
	- Each processor has its own private memory.
	- To share data, processors must explicitly send messages to each other over a network.
	- Can scale to a much larger number of processors → foundation for most large-scale supercomputers.