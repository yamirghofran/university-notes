---
title: Directive vs Instruction
---

## Directive
-  **Definition**: A directive is a statement in a program that provides guidance or instructions to the compiler or assembler. It is not executed at runtime but helps in the compilation or assembly process.
-  **Purpose**: Directives are used to control the assembly process, define constants, allocate storage, and manage sections of code.
-  **Examples**: 
  - In assembly language, directives like `.data` and `.text` define data and code sections, respectively.
  - In C/C++, preprocessor directives such as `#include`, `#define`, and `#ifdef` are used to include files, define macros, and conditionally compile code.
## Instruction
-  **Definition**: An instruction is a command executed by the CPU. It is part of the machine code that performs operations on data, such as arithmetic, logic, control, and data movement.
-  **Purpose**: Instructions are used to perform tasks and operations on data during program execution. They are the fundamental operations that the CPU understands and executes.
-  **Examples**: 
  - In assembly language, instructions like `MOV`, `ADD`, `SUB`, and `JMP` are used to move data, perform arithmetic, and control the flow of execution.
## Key Differences
-  **Execution**: Directives are not executed at runtime; they guide the compilation or assembly process. Instructions are executed by the CPU during runtime.
-  **Function**: Directives manage how the program is translated into machine code, while instructions perform operations on data during program execution.
-  **Context**: Directives are often specific to the programming language or assembler being used, whereas instructions are specific to the CPU architecture.
