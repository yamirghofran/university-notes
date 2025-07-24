---
title: Stack
---

The stack is a region of data memory that is set aside by the programmer specifically for the main purpose of storing the [microprocessor](/computer-architecture-network-technology-and-operating-systems/architecture/microprocessor)'s state information when it branches to a subroutine. A stack is a last-in, first-out memory structure.
![](../attachments/cleanshot-2025-01-23-at-1941392x.png)
The stack segment is used for managing:
- local variables
- function arguments
- control information such as return addresses.
![](../attachments/cleanshot-2025-01-23-at-1938212x.png)
[Stack Pointer](/computer-architecture-network-technology-and-operating-systems/architecture/registers) stores the address of the last element added to the stack.
![](../attachments/cleanshot-2025-01-19-at-2232262x.png)
## Push 
Decrements the value of the stack pointer and inserts value at that position.
## Pop
Read the value pointed by SP and increments the stack pointer.

