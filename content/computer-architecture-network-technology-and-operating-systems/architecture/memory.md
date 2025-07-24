---
title: Memory
---

# Types of Memory
## By Physical Nature
### Semiconductor (Solid State)
![](../attachments/cleanshot-2025-01-19-at-2133212x.png)
### Magnetic
![](../attachments/cleanshot-2025-01-19-at-2133342x.png)
### Optic
- CDs
vacuum (obsolete)
![](../attachments/cleanshot-2025-01-19-at-2133452x.png)
## By Access to Data capability
### Random
Each byte can be accessed independent no matter which byte has been accessed before. e.g. RAM.
### Sequential
Bytes must be accessed in order. Accessing bytes that are not sequential has a high penalty in recovery time.
- magnetic hard disks
- magnetic tapes
- DVDs
## By Their Retention Time
### Volatile
- Static ([SRAM](/computer-architecture-network-technology-and-operating-systems/architecture/sram)) flip-flops, quick and expensive
- Dynamic ([DRAM](/computer-architecture-network-technology-and-operating-systems/architecture/dram)) caps, slow and cheap
### Non-volatile
- Flash
- cdrom
- magnetic disks
# Memory Configurations
## Single Channel
- One RAM module connected to one memory controller channel
- Single data path between RAM and CPU
- Lower theoretical bandwidth

![](../attachments/cleanshot-2025-01-19-at-2202582x.png)
## Dual Channel
- 2 RAM modules connected to two memory controller channels
- 2 parallel data paths between RAM and CPU
- Double the theoretical bandwidth compared to single channel
- Both modules work together simultaneously.
![](../attachments/cleanshot-2025-01-19-at-2203032x.png)


## Memory Address Maps
Memory maps in microcontrollers are used to organize the different types of memory available in a microcontroller. Different address blocks are used to map different kinds of
memory (i.e. volatile or non-volatile) and also [peripherals](/computer-architecture-network-technology-and-operating-systems/architecture/peripherals).

Memory-mapped [peripherals](/computer-architecture-network-technology-and-operating-systems/architecture/peripherals) are controlled writing and reading values to specific regions of the address space.

To use memory-mapped peripherals, the programmer must know the memory map of the microcontroller. The memory map is a diagram that shows the location of each memory-mapped peripheral in the microcontroller's memory space.
![](../attachments/cleanshot-2025-01-31-at-1011312x.png)

## Memory Hierarchy
Since fast memory is expensive, a memory hierarchy is organized into several levels. Each level is smaller, faster and more expensive per byte than the next lower level, which is farther from the processor. The goal is to provide a memory system with cost per byte almost as low as the cheapest level of memory and speed almost as fast as the fastest level.

![](../attachments/cleanshot-2025-01-31-at-1018512x.png)
## Memory Protection Schemes
**Paging**
The most popular is adding protection restrictions to each page of virtual memory.

Fixed-sized pages, typically 4kb or 8kb long, are mapped from the virtual address space into physical address space via a **page table**.

Since only the [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) can update the page table, the paging mechanism provides total access protection.

---
- Types of memory
	- By physical nature
		- Solid-state (semiconductor)
		- Magnetic
		- Optic
	- By access pattern
		- Random
		- Sequential
	- By duration
		- Volatile
			- SRAM
			- DRAM
		- Non-volatile
			- Flash
			- CDRom
- Memory configurations
	- Single channel
	- Dual channel
- Memory address maps
- Memory hierarchy
- Memory protection schemes
	- Paging
		- Page table