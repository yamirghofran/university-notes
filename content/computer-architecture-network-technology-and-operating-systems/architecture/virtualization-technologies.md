---
title: Virtualization Technologies
---

[Containers](/computer-architecture-network-technology-and-operating-systems/architecture/containers) and virtual machines (VMs) are two different technologies used for running applications.

**Containers** are lightweight and isolated silos for running an application on the host operating system. They build on top of the host operating system's **kernel** and contain only apps and some lightweight operating system APIs and services that runs in user mode 1.

VMs run a complete [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system), including **its own kernel**, on top of a **hypervisor**, which abstracts the underlying hardware resources.

![](../attachments/cleanshot-2025-01-19-at-2243282x.png)

## Virtual Machines
Hypervisors
- Microsoft Hyper-V
- Linux KVM
- VMware
- XenCenter
- VirtualBox
![](../attachments/cleanshot-2025-01-19-at-2245172x.png)

## Hardware Assisted Virtualization
Intel VT or AMD-V
- Faster control transference between hosts and guests
- Network optimization
- Input/Output ports reservation
- [DMA](/computer-architecture-network-technology-and-operating-systems/architecture/direct-memory-access-dma) re-assignation
- [Interrupt](/computer-architecture-network-technology-and-operating-systems/architecture/interrupt) Re-assignation