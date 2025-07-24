---
title: Low-level Routine
---

Low-level routines in computer architecture refer to operations that interact directly with the hardware. These routines are typically written in [assembly](/computer-architecture-network-technology-and-operating-systems/architecture/assembly) language and are crucial for managing hardware resources efficiently.

## Key Concepts:


**BIOS Services**:
- [BIOS](/computer-architecture-network-technology-and-operating-systems/architecture/bios) is firmware that initializes and manages data flow between the computer's [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) and attached devices like hard disks, video cards, and keyboards.
- It provides a set of low-level routines that software can use to perform hardware-related tasks without needing to interact directly with the hardware.

**Interrupts**:
- BIOS functions are often accessed via software [Interrupt](/computer-architecture-network-technology-and-operating-systems/architecture/interrupt)s (e.g., `INT 0x10` for video services).

**Registers**:
- Assembly instructions use [CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu) registers to pass parameters to BIOS functions. For example, `AH` and `AL` are [registers](/computer-architecture-network-technology-and-operating-systems/architecture/registers) used to specify function numbers and parameters.

**Video Functions**:
- Examples include setting up the cursor, getting cursor position, displaying characters, and getting video mode. These are accessed via `INT 0x10`.

**Hardware Detection**:
- Functions like `INT 0x11` are used for detecting hardware components.

**Memory Functions**:
- These routines help in determining [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) size and configuration, accessed via interrupts like `INT 0x12` and `INT 0x15`.

**Other Functions**:
- Include tasks like reading keyboard input, which can be done through `INT 0x16`.

## Example Explained:

The assembly code snippet on the slide: 
```assembly
mov ah, 0x0e   ; function number = 0Eh : Display Character mov al, '!'    ; AL = code of character to display int 0x10       ; call INT 10h, BIOS video service
```

- **`mov ah, 0x0e`**: Sets the `AH` register to `0x0E`, specifying the function to display a character.
- **`mov al, '!'`**: Loads the `AL` register with the ASCII code for the character `!`.
- **`int 0x10`**: Triggers the BIOS video service interrupt to execute the display character function. These low-level routines are essential for bootstrapping the system and providing basic input/output operations before the operating system takes over.
