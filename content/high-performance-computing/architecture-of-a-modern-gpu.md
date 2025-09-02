---
title: Architecture of a Modern GPU
---

Architecture of a typical CUDA-capable GPU.

- Organized into an array of highly threaded **streaming multiprocessors** (SMs).
- Each SM has a number of streaming processors (SPs) that share control logic and an instruction cache.
- Each GPU comes with multiple gigabytes of Graphic Double Data Rate (GDDR) DRAM referred to as global memory.

GDDR DRAM differ from system DRAMs on the CPU motherboard in that they are essentially the frame buffer memory that is used for graphics.
- For graphics, they hold video images and texture information for 3d rendering.
- For computing, they function as very high bandwidth off-chip memory, with longer latency than system memory. (For parallel applications, the bandwidth makes up for the latency)
As the size of GPU memory grows, applications increasingly keep their data in the global memory and only occasionally use the [[Peripheral Component Interconnect (PCI) Bus|PCI-E]] to communicate with the CPU sysstem memory if needed.
![](../attachments/cleanshot-2025-08-25-at-0913042x.png)
