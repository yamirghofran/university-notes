---
title: Microprocessor
---

# Types
## 8086 (First x86)
1. **Instruction Register and Decoder**: These components fetch, decode, and execute instructions. The instruction register holds the current instruction, while the decoder interprets it.

2. **Control Logic**: Manages control signals for executing instructions, coordinating the microprocessor's operations.

3. **General Purpose Registers**:

▪ **AH, AL, BH, BL, CH, CL, DH, DL**: These are 8-bit registers that can be combined into 16-bit registers (AX, BX, CX, DX) for various operations.

▪ **SP (Stack Pointer)**: Points to the top of the stack in memory, used for subroutine and interrupt handling.

▪ **BP (Base Pointer)**: Primarily used for accessing parameters in stack frames.

▪ **SI (Source Index) and DI (Destination Index)**: Used for indexed addressing and string operations.

4. **Arithmetic Logic Unit (ALU)**: Performs arithmetic and logic operations, interacting with the registers and temporary registers.

5. **Temporary Registers (TEMP)**: Hold intermediate data during operations, assisting the ALU.

6. **Internal Data Bus**: A 16-bit bus for data transfer within the microprocessor.

7. **Address Bus**: A 16-bit bus used to address memory locations.

8. **Buffers**: Facilitate data transfer between internal components and external peripherals or memory.
## RISC-V
![](../attachments/cleanshot-2025-01-12-at-0841292x.png)

1. **Instruction Register and Pre-Decoder**: The instruction register holds the current instruction. The pre-decoder prepares instructions for decoding by breaking them down into simpler parts.

2. **Decode and Optimize**: This stage interprets the instruction and optimizes it for efficient execution. The branch predictor helps determine the flow of control, improving pipeline efficiency.

3. **Control Logic**: Manages control signals for executing instructions, coordinating the processor's operations.

4. **Registers**:

▪ **32 Integer Registers**: General-purpose registers used for arithmetic, logic, and data manipulation.

▪ **32 Floating Point Registers**: Used for floating-point operations, enhancing computational capabilities.

5. **Arithmetic Logic Unit (ALU)**: Performs arithmetic and logic operations, interacting with the integer and floating-point registers.

6. **Floating Point Unit (FP Unit)**: Dedicated to handling floating-point calculations, improving performance for complex mathematical operations.

7. **Load/Store Unit**: Manages data transfer between memory and registers, adhering to the load/store architecture principle.

8. **Data Registers**: Temporary storage for data being processed or transferred.

9. **Internal Data Bus**: A 32-bit bus for data transfer within the processor.

10. **Address Bus**: A 32-bit bus used to address memory locations.

11. **Buffers**: Facilitate data transfer between internal components and external peripherals or memory.

![](../attachments/cleanshot-2025-01-12-at-0843242x.png)
## Z80
Used in calculators.

The Z80 architecture is a microprocessor architecture with several key components illustrated in the diagram:

1. **Instruction Register and Decoder**: These components fetch, decode, and execute instructions. The instruction register holds the current instruction, while the decoder interprets it.

2. **Control Logic**: Manages control signals for executing instructions, coordinating the processor's operations.

3. **Registers**:

▪ **General Purpose Registers**: B, C, D, E, H, L and their alternate pairs B', C', D', E', H', L'. These are used for various data operations and can be paired for 16-bit operations.

▪ **IX and IY**: Index registers used for advanced addressing modes.

▪ **A and A' (Accumulator)**: Used for arithmetic and logic operations.

▪ **F and F' (Flags)**: Store the status of operations (zero, carry, etc.).

4. **Program Counter (PC)**: A 16-bit register that holds the address of the next instruction to be executed.

5. **Stack Pointer (SP)**: Points to the current top of the stack in memory, used for subroutine and interrupt handling.

6. **Multiplexers (MUX)**: Allow selection between different data sources for processing.

7. **Arithmetic Logic Unit (ALU)**: Performs arithmetic and logic operations, interacting with the accumulator and other registers.

8. **Temporary Register (TEMP)**: Holds intermediate data during operations, assisting the ALU.

9. **Internal Data Bus**: An 8-bit bus for data transfer within the microprocessor.

10. **Address Bus**: A 16-bit bus used to address memory locations.

11. **Buffers**: Facilitate data transfer between internal components and external peripherals or memory.
![](../attachments/cleanshot-2025-01-12-at-0836162x.png)
## AVR
Arduino

![](../attachments/cleanshot-2025-01-12-at-0836342x.png)

1. **Instruction Register and Decoder**: These components fetch, decode, and execute instructions. The instruction register holds the current instruction, and the decoder interprets it.

2. **Control Logic**: Manages control signals for executing instructions, coordinating the microcontroller's operations.

3. **32 General Purpose Registers**: These registers are used for data manipulation and storage. They allow for efficient data handling and quick access during operations.

4. **Program Counter (PC)**: A 16-bit register that holds the address of the next instruction to be executed, enabling sequential instruction fetching.

5. **Stack Pointer (SP)**: Points to the current top of the stack in memory, used for subroutine and interrupt handling.

6. **Index Registers (IX, IY)**: Used for addressing and accessing data within memory, aiding in complex data operations.

7. **Arithmetic Logic Unit (ALU)**: Performs arithmetic and logic operations, interacting with the general-purpose registers and accumulators.

8. **Accumulator (ACU)**: Used in conjunction with the ALU for arithmetic and logic operations, holding intermediate results.

9. **Multiplexer (MUX)**: Allows selection between different data sources for processing.

10. **Internal Data Bus**: An 8-bit bus for data transfer within the microcontroller.

11. **Address Bus**: A 16-bit bus used to address memory locations.

12. **Buffers**: Facilitate data transfer between internal components and external peripherals or memory.
## 8051
The 8051 architecture is a microcontroller architecture that includes several key components, as illustrated in the diagram:

1. **Instruction Register and Decoder**: These components are responsible for fetching, decoding, and executing instructions. The instruction register holds the current instruction, while the decoder interprets it.

2. **Control Logic**: Manages the control signals for the execution of instructions, coordinating the operation of the processor.

3. **Program Counter (PC)**: A 16-bit register that holds the address of the next instruction to be executed, enabling sequential instruction fetching.

4. **Data Pointer (DPRTR, DPH, DPL)**: A 16-bit register used to store memory addresses, often for indirect addressing in data transfer operations.

5. **Accumulator (ACU) and Register A**: The accumulator is an 8-bit register used for arithmetic and logic operations. It is a key part of the Arithmetic Logic Unit (ALU).

6. **Arithmetic Logic Unit (ALU)**: Performs arithmetic and logic operations. It interacts with the accumulator and other registers to process data.

7. **Temporary Register (TEMP)**: Holds intermediate data during operations, assisting the ALU in calculations.

8. **Internal Data Bus**: An 8-bit bus used for data transfer within the microcontroller.

9. **Address Bus**: A 16-bit bus used to address memory locations.

10. **Buffers**: Facilitate data transfer between the internal components and external peripherals or memory.

![](../attachments/cleanshot-2025-01-12-at-0834392x.png)

## IA64 (Itanium)
![](../attachments/cleanshot-2025-01-12-at-0843462x.png)