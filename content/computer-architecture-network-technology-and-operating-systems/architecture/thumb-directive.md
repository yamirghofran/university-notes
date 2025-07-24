---
title: Thumb Directive
---

The `THUMB` directive is used in ARM assembly language to switch the processor into Thumb mode. Thumb mode is an alternative instruction set for ARM processors, which uses 16-bit compressed instructions instead of the standard 32-bit ARM instructions. This can lead to more efficient use of memory and potentially increased performance, especially in memory-constrained environments.
## Purpose
-  **Code Size**: The primary advantage of Thumb mode is the reduction in code size. By using 16-bit instructions, the same functionality can be achieved with less memory usage, which is beneficial in embedded systems where memory is limited.
-  **Performance**: In some cases, using Thumb instructions can improve performance due to better cache utilization and reduced memory bandwidth requirements.
-  **Compatibility**: It allows for a mix of ARM and Thumb instructions, providing flexibility in optimizing both performance and code size.
## Usage
-  **Switching Modes**: The `THUMB` directive is used in assembly code to indicate that the following instructions should be assembled in Thumb mode. When the processor is switched to Thumb state, it executes Thumb instructions.
-  **Interworking**: ARM processors that support both ARM and Thumb instruction sets can switch between the two modes. This is called "interworking," and it allows developers to use the strengths of both instruction sets within the same application.
## Example
Here is a simple example of how the `THUMB` directive might be used in ARM assembly:

```assembly
AREA MyCode, CODE, READONLY
ENTRY
THUMB
MOV R0, #1      ; Move 1 into register R0
ADD R0, R0, #2  ; Add 2 to the value in R0
BX LR           ; Return from subroutine
```
