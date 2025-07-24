---
title: Das U-Boot
---

Das U-Boot is an open-source [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader) used in **embedded devices** to perform various low-level hardware initialization tasks and boot the device’s operating system. It is available for a number of computer architectures, including 68k, ARM, Blackfin, MicroBlaze, MIPS, Nios, SuperH, PPC, RISC-V and x86. 

U-Boot is both a **first-stage** and **second-stage** bootloader. It is loaded by the system’s ROM from a supported boot device, such as an SD card, SATA drive, NOR flash or NAND flash. U-Boot implements a subset of the [UEFI](/computer-architecture-network-technology-and-operating-systems/architecture/uefi) specification as defined in the Embedded Base Boot Requirements (EBBR) specification so binaries like GRUB or the Linux kernel can be booted via the boot manager. 

Unlike PC bootloaders which obscure or automatically choose the memory locations of the kernel and other boot data, U-Boot requires its boot commands to explicitly specify the physical [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) addresses as destinations for copying data (kernel, ramdisk, device tree, etc.) and for jumping to the kernel and as arguments for the kernel.

## U-Boot

![](../attachments/cleanshot-2025-02-03-at-0954432x.png)
