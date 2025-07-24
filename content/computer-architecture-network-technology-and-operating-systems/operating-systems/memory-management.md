---
title: Memory Management
---

Key objectives: Relocation, protections, sharing, logical organization, physical organization.

- efficiency
- speed
- multitasking
- stability
- security
- virtual memory
- resource sharing
- allocation and deallocation
- memory mapping

Virtual memory basically uses storage as memory. Not used in realtime systems to keep maximum speed.

## Memory Allocation Strategies

**Fixed Partitioning**
- sizes for partitioning (fragments) are all the same.
- Higher speed and extremely efficient. Maximum speed possible. You don't wan't fragments.
- When you have multiple instances of the same program.
**Dynamic Partitioning**
- fragments have different sizes

![](../attachments/cleanshot-2025-02-21-at-1128122x.png)

![](../attachments/cleanshot-2025-02-21-at-1128212x.png)

(internal vs external fragmentation)?
[Paging](/computer-architecture-network-technology-and-operating-systems/operating-systems/paging) and [segmentation](/computer-architecture-network-technology-and-operating-systems/operating-systems/segmentation) are solutions to fragmentation.