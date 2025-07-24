---
title: Interrupt
---

Signals emitted by hardware or software when a process or an event needs **immediate** attention.

They alert the [Processor](/computer-architecture-network-technology-and-operating-systems/architecture/microprocessor) to execute a high-priority process requiring suspension of the current working process.

Interrupts are used in computer systems to handle events that require immediate attention, such as input/output (I/O) operations with [Peripherals](/computer-architecture-network-technology-and-operating-systems/architecture/peripherals), hardware errors, and software exceptions.
![](../attachments/cleanshot-2025-01-23-at-1930352x.png)
ISR: Interrupt Service Routine
## Interrupts Priority
Interrupt priority is a mechanism that decides the order in which interrupts are serviced by the CPU when multiple interrupts occur simultaneously.
- **Simultaneous**: several interrupts processed in parallel.
- **Nested**: a high priority can interrupt  a low priority interrupt
- **Queued**: processed in order according to their priority when the current interrupt finishes.
- **Inhibited**: while processing an interrupt other interrupts are ignored

## Interrupt Vector Table
Processors use an interrupt vector table to store the addresses of interrupt service routines (ISRs).

The vector table consists of 32/64-bit vector entries that store the address of the instruction where the cpu will jump when/if the interrupt is raised.

![](../attachments/cleanshot-2025-01-23-at-1935042x.png)

## Interrupt Demo
![](../attachments/cleanshot-2025-01-23-at-1935252x.png)

---
- Interrupt priority
	- Simultaneous
	- Nested
	- Queued
	- Inhibited
- Interrupt Vector Table