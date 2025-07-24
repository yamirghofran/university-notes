---
title: Booting
---

- [Bare Metal](/computer-architecture-network-technology-and-operating-systems/architecture/bare-metal)
- [Bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader)

## ARM Cortex Example
The code is written for the Cortex-M0+ processor, which is a low-power processor designed for microcontrollers.

The first four lines of the code are directives that specify the syntax, [CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu), FPU, and instruction set to be used by the assembler.
- The `.cpu` cortex-m)plus [Directive](/computer-architecture-network-technology-and-operating-systems/architecture/directive-vs-instruction) specifies that the code is intended for the Cortex-M0+ processor.
- The `.fpu` softvfp directive specifies that the code should use software floating-point emulation.
- The `.thumb` directive specifies that the code should be assembled into [Thumb](/computer-architecture-network-technology-and-operating-systems/architecture/thumb-directive) instructions.