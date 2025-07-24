---
title: C Compiler Structure
---

![](../attachments/cleanshot-2025-01-19-at-2226492x.png)
## Preprocessing
In this phase, the preprocessor reads the source code and expands it by:
- replacing the macros with their definitions
- including the header files
- removing the comments
The output of this phase is a preprocessed source code file.

## Compilation
In this phase, the compiler reads the preprocessed source code file and generates an **[assembly](/computer-architecture-network-technology-and-operating-systems/architecture/assembly) code file**. The assembly code file contains the instructions that the computer can understand.

## Assembly
In this phase, the assembler reads the [assembly](/computer-architecture-network-technology-and-operating-systems/architecture/assembly) code file and generates an **object code** file. The object code file contains the binary representation of the instructions.

## Linking
In this phase, the linker reads the object code files and combines them into **a single executable file**. The linker resolves the external references and generates the final executable file.

## Example
![](../attachments/cleanshot-2025-01-19-at-2227082x.png)