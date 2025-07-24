---
title: Unix Kernel
---

Core component of an operating system, responsible for managing the system's hardware and software resources.
![](../attachments/cleanshot-2025-03-13-at-1603032x.png)
## Importance
- Modularity and portability
- [Process](/computer-architecture-network-technology-and-operating-systems/operating-systems/process) management
- [Filesystem](/computer-architecture-network-technology-and-operating-systems/operating-systems/filesystem)
- [Pipes](/computer-architecture-network-technology-and-operating-systems/operating-systems/pipes) and Filters
- [Inter-Process Communication](/computer-architecture-network-technology-and-operating-systems/operating-systems/inter-process-communication) (IPC)
- Security and Permission Model
- Standard POSIX
	- Set of APIs that made operating systems be compatible.

## Kernel Architecture
Monolithic (Windows, Linux(not really), BSD, etc) vs Microkernel

Microkernell has basically nothing incorporated in the kernel (basics of memory and storage). Others are added as modules.

Monolithic has everything in it. Used more today. Advantage because of speed.

MacOS X uses a hybrid approach. Most features are monolithic, some are microkernel. MACH kernel.
![](../attachments/cleanshot-2025-03-13-at-1603502x.png)
### Components
- Virtual File System
- Memory Manager
- Process Scheduler
- Inter-Process Communication
- Network Interface

![](../attachments/cleanshot-2025-03-13-at-1604022x.png)
## Boot Process
1. BIOS/UEFI Stage
2. [Bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader) (GRUB/LILO)
3. Kernel Intialization
4. Init/Systemd process

## Kernel Modules
![](../attachments/cleanshot-2025-03-13-at-1606032x.png)
**Linux**
- lsmod
- modinfo
**Mac**
- kmutil showloaded

## System Calls
- `fork()` - create a new process
- `exec()` - execute a new program in the context of an existing process.
- `read()`, `write()` - read from and write to files and devices.
- `open()`, `close()` - to open and close file descriptors.
- `wait()` - wait for a process to change state
- `socket()` - create a socket for network communication
![](../attachments/cleanshot-2025-03-13-at-1608192x.png)

## Kernel Space vs User Space
![](../attachments/cleanshot-2025-03-13-at-1608392x.png)