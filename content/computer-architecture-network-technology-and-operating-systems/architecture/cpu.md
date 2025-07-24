---
title: CPU
---

## Components in a CPU
![](../attachments/cleanshot-2025-01-12-at-0808132x.png)

## Von Neumann vs Harvard
Harvard architecture used two separated memories (one for data, one for code) with different address sizes.

Von Neumann architecture uses the same memory for both data and code. 8080, z80, or Motorola 6800 use this architecture.

![](../attachments/cleanshot-2025-01-12-at-0823542x.png)

## Modern Architectures
Modern CPUs use a mixed architecture with different layers of cache memory for instructions and data and a single large memory for both.

![](../attachments/cleanshot-2025-01-12-at-0825052x.png) (several cache layers are used for data and instruction.)

![](../attachments/cleanshot-2025-01-12-at-0825392x.png)

## Fetch
The control logic fetches the instructions from the memory pointed by the instruction pointer. The instruction data is then decoded and executed by the [ALU](/computer-architecture-network-technology-and-operating-systems/architecture/arithmetic-logic-unit-alu).

## Alternative Computational Architectures
- [GPU](/computer-architecture-network-technology-and-operating-systems/architecture/gpu)
- [ASIC](/computer-architecture-network-technology-and-operating-systems/architecture/asic)
- [FPGA](/computer-architecture-network-technology-and-operating-systems/architecture/fpga)