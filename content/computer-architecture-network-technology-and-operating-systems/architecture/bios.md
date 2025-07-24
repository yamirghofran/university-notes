---
title: BIOS
---

**BIOS** (Basic Input/Output System) is the firmware that controls and configures the basic hardware settings of a computer, such as the time, date, and boot order. It is typically stored in a non-volatile memory chip on the motherboard and is responsible for:
- Initializing hardware components
- Configuring boot settings
- Providing low-level input/output operations
- Offering a setup interface for users to configure settings.

The BIOS or [UEFI](/computer-architecture-network-technology-and-operating-systems/architecture/uefi) is burned into flash [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) on the motherboard. 
At startup it will look for a bootable drive and load an [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader) from the drive.

At that point it turns control over to the operating system’s bootloader which takes care of loading your [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system). Once the operating system is up and running, you can just point and click to load and run any program you want.


1. The BIOS performs a **power-on self-test** (POST) to check if all the hardware components are working properly.
2. The BIOS loads the **[Interrupt](/computer-architecture-network-technology-and-operating-systems/architecture/interrupt) handlers and device drivers**, It provides a set of [Low-level Routine](/computer-architecture-network-technology-and-operating-systems/architecture/low-level-routine) that the [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) uses to interface with different hardware devices, such as the keyboard, screen, and serial and parallel ports.
3. The BIOS displays the system settings and determines which **devices are bootable**.
4. The BIOS **loads the [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader)** from the bootable device, which is typically the hard disk or a USB drive. The bootloader is a small program that resides in the Master Boot Record (MBR) of the bootable device. It is responsible for loading the kernel of the operating system into [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) and transferring control to it. The bootloader also provides a menu of boot options if multiple operating systems are installed on the same device
5. **The bootloader loads the kernel** of the operating system into memory.
6. The kernel initializes the system processes and device drivers.
![](../attachments/cleanshot-2025-02-03-at-0959312x.png)
