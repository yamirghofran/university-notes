---
title: Peripheral Component Interconnect (PCI) Bus
---

It is a high-speed **serial connection** that operates more like a **network** than a bus.

The PCI bus is a **32-bit** bus and has 32 lines to transmit data. At the beginning of a transaction, the bus is used to specify a 32-bit address. Once the address is specified, many data cycles can go through. The address is not re-transmitted but is auto-incremented at each data cycle.

The PCI bus has some shortcomings, such as a fixed width of 32 bits and the ability to handle only 5 devices at a time. A new protocol called **PCI Express** (PCle) eliminates many of these shortcomings, provides more bandwidth, and is compatible with existing [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system)s.