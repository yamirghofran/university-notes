---
title: Components of HPC Systems
---

Difference of HPC vs a conventional computer:
- organization, interconnectivity, and scale of the component resources.
- ability of the supporting software to manage the operation of the system at that scale.

- **Scale**: degree of physical and logical parallelism.
- APIs and algorithms that exploit and permit application parallelism and simultaneous operations.
![](../attachments/cleanshot-2025-09-02-at-0916592x.png)
- **OS** manages all aspects of the machine
- **Compilers** that translate application programs to machine-readable binary code.
- **File systems** that present a logical abstraction of mass storage and organize the data on mass storage devices.
- **Software drivers** of the I/O devices by which the computer communicates with the external world and users.
- **tools** that make user environments.


The most important component is a **Balance** between components. 
Components selected/tuned to fit user needs

Analogy with living being:
- **Skeleton**: mechanics (chassis, rack, etc.)
- **Heart**: Processor providing compute performance
- **Brain**: Memory / Storage
	- With many layers (caches, DRAM, SSD, HD, Tape)
- **Nerve system**: Network
	- Often more than one (MPI, Administration, I/O)
- **Consciousness**: Software
	- Including various middleware layers (node management, process management, MPI, etc.)
	- Open Source.