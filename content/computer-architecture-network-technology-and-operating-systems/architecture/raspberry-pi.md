---
title: Raspberry Pi
---

The Raspberry Pi boot process is initiated by the [GPU](/computer-architecture-network-technology-and-operating-systems/architecture/gpu) core, which is on when the device is first turned on. 

1. The GPU reads the **first-stage** [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader) from the ROM on the SoC and executes it. 
2. The first-stage [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader) reads the second-stage bootloader (bootcode.bin) from the SD card and loads it into the L2 [cache](/computer-architecture-network-technology-and-operating-systems/architecture/cache) and runs it. 
3. The second-stage bootloader enables SDRAM and reads the third-stage bootloader (loader.bin) from the SD card into RAM, and runs it. 
4. The third-stage bootloader reads the GPU firmware (start.elf). start.elf reads config.txt, cmdline.txt and kernel.img. The third-stage bootloader doesn’t do much, but it is needed to load start.elf at the top of memory (ARM uses SDRAM from address zero)

![](../attachments/cleanshot-2025-02-03-at-0956232x.png)


![](../attachments/cleanshot-2025-02-03-at-0956132x.png)
