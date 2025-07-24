---
title: Segmentation
---

![Segment tables and address translation in segmentation](../attachments/cleanshot-2025-02-21-at-1129012x.png)

Internal. Every program has a segment. Each segment has a maximum size.

Applications use segment number, and offset. e.g. segment number 3, position 5.

Segmentation fault if program tries to access a bigger memory than segment size. Program destroyed because "illegal".

**Difference between segments and pages**

Segments variable size, pages fixed.
[pages](/computer-architecture-network-technology-and-operating-systems/operating-systems/paging) is handled by [Operating System](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) or hardware device, segmentation is handled by program.
Different fragmentation.