---
title: Registers
---

- Small and temporary storage unit inside a computer's central processing unit ([CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu)) that holds data for immediate processing.
- Small amounts of **fast storage**.
- Some registers have specific **hardware functions**, and may be read-only or write-only.
- Computers load items from a larger [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) into registers.

Used for
- Arithmetic operations
- Bitwise operations
- Other operations
- Manipulated or tested by machine instructions.

Manipulated items are then often stored back to main memory, either by the same instruction or by a subsequent one.

Modern high-performance CPUs often have duplicates of these "architectural registers" to improve performance via register renaming, allowing parallel and speculative execution.

## Load/Store ([Risc](/computer-architecture-network-technology-and-operating-systems/architecture/instruction-set))

Memory access is limited to explicit load (move data from memory to a register) and store (move data from a register to memory) instructions.
 All arithmetic and logical operations are performed on registers.

Example: ARM, MIPS, RISC-V.

### Advantages
- **Simplicity**: Instructions are simple and uniform, making the processor easier to design and optimize.
- **Pipelining**: The uniformity of instructions allows for efficient pipelining, improving performance.
- **Energy Efficiency**: Fewer memory accesses reduce power consumption.

### Disadvantages
- **More Instructions**: Programs may require more instructions to perform the same task, as data must be explicitly loaded into registers before operations.
- **Code Size**: Programs can be larger due to the need for explicit load/store instructions.


## Register/Memory ([CISC](/computer-architecture-network-technology-and-operating-systems/architecture/instruction-set))
Instructions can directly operate on memory operands, in addition to registers.

Arithmetic and logical instructions can access memory directly, without requiring explicit load/store instructions.

Example: x86, Intel processors.

### Advantages
- **Fewer Instructions**: Programs can be more compact, as a single instruction can perform both memory access and computation.
- **Flexibility**: Direct memory access simplifies certain programming tasks.

### Disadvantages
- **Complexity**: Instructions are more complex, making the processor harder to design and optimize.
- **Inefficient Pipelining**: Variable instruction lengths and memory access times can complicate pipelining.
- **Higher Power Consumption**: Frequent memory accesses increase power usage.

## Basic Registers
- **Accumulator Registers** temporarily hold the result of arithmetic / logic operations.
- **Address Registers** temporarily hold memory addresses.
- **Data registers** temporarily hold data to later be processed.

- AF: (8-bit accumulator) A and flag bits (F) carry, zero, minus, parity/overflow, half-carry (used for BCD), and an Add/Subtract flag (usually called N) also for BCD.
- BC: 16-bit data/address register or two 8-bit registers
- DE: 16-bit data/address register or two 8-bit registers
- HL: 16-bit accumulator/address register or two 8-bit registers
- SP: stack pointer, 16 bits
- PC: program counter, 16 bits
- LR: link register.

## ARM Registers
ARM processors have 37 registers
- 30 general-purpose, 32-bit registers
	- 15 always visible: r0-r12
- SP
- LR: the Link register, aka r14, used to store the subroutine's return address.
	- when an exception occurs, the version of r14 in the exception mode is set to the address after the instruction is executed.
- The Program Counter (PC): used to determine which instruction will be executed next. The PC is referred to as an **instruction pointer** because it stores the address of the next instruction.
- The Application Program Status Register (APSR): holds copies of the [Arithmetic Logic Unit (ALU)](/computer-architecture-network-technology-and-operating-systems/architecture/arithmetic-logic-unit-alu) status flags
- Saved Program Status Registers (SPSRs), hold copies of CPSR when an exception is taken
	- the APSR flags
	- the current processor mode
	- interrupt disable flags
	- current processor state (ARM, Thumb, ThumbEE, or Jazelle)
	- execution state bits for the IT block.
## Inter Registers
![](../attachments/cleanshot-2025-01-23-at-1927352x.png)
The 8 GPRs are as follows:

-  **Accumulator register (AX).** Used in arithmetic operations. Opcodes combining constants into accumulator are 1-byte.
-  **Base register (BX).** Used as a pointer to data.
-  **Counter register (CX).** Used in shift/rotate instructions and loops.
-  **Stack Pointer register (SP).** Pointer to the top of the stack.
-  **Stack Base Pointer register (BP).** Used to point to the base of the stack.
-  **Destination Index register (DI).** Used as a pointer to a destination in stream operations.
-  **Source Index register (SI).** Used as a pointer to a source in stream operations.
-  **Data register (DX).** Used in arithmetic operations and I/O operations.
