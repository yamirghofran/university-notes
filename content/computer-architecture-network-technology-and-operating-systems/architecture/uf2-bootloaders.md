---
title: UF2 Bootloaders
---

A good example of an advanced [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader) is the UF2 bootloader used on CircuitPython capable boards. A UF2 bootloader is a way of **programming microcontrollers**. 

Originally developed by Microsoft, it allows a microcontroller to enumerate as a mass storage device over USB (i.e. a USB drive). You can then drag-and-drop code onto the drive, and UF2 will **re-program the microcontroller** with your code.

This bootloader can work like an Arduino and accept **serial uploads** via the USB connection. Or it can **emulate a disk drive** that lets you copy Python programs to it. 

An on-board RGB LED is used to provide diagnostic feedback in the form of steady or flashing patterns in different colors to indicate the state of the bootloading process.

![](../attachments/cleanshot-2025-02-03-at-0952192x.png)