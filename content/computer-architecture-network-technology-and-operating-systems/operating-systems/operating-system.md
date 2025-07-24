---
title: Operating System
---

An operating system (OS) is a fundamental software component that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between users and the computer hardware, ensuring efficient and effective use of the system's resources.

## Types of Operating Systems
- Real-time
- Embedded
- Distributed
- Multiuser
- Multiprocessing
Don't assume every OS is multiuser and multiprocessing. e.g. not in microcontroller. simple unique task.

## Functions of Operating Systems
- [Process](/computer-architecture-network-technology-and-operating-systems/operating-systems/process) management
- [Memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) management
- [Filesystem](/computer-architecture-network-technology-and-operating-systems/operating-systems/filesystem) management
- Device management ([Peripherals](/computer-architecture-network-technology-and-operating-systems/architecture/peripherals))
- Security and access control

## Key Components

1. **Kernel**
   - The core part of the operating system that manages system resources and facilitates communication between hardware and software components.
   - **Monolithic Kernel**: All core functions run in kernel space (e.g., Linux).
   - **Microkernel**: Only the most essential services run in kernel space, with other services running in user space (e.g., Minix, QNX).

2. **Process Management**
   - Manages the creation, scheduling, and termination of processes.
   - **Process**: An instance of a program in execution.
   - **Thread**: The smallest unit of execution within a process.
   - **Scheduling**: Determines the order in which processes are executed (e.g., Round Robin, Priority Scheduling).

3. **Memory Management**
   - Manages the computer's memory, allocating and deallocating memory space as needed.
   - **Virtual Memory**: Allows processes to use more memory than physically available by using disk storage as an extension of RAM.
   - **Paging and Segmentation**: Techniques for managing memory allocation and deallocation.

4. **File System Management**
   - Manages the organization, storage, retrieval, and updating of files.
   - **File**: A named collection of data stored on a disk.
   - **Directory**: A structure that organizes files and other directories.
   - **File System**: The method and data structure that an operating system uses to control how data is stored and retrieved (e.g., NTFS, ext4, FAT32).

5. **Device Management**
   - Manages input/output (I/O) devices such as printers, keyboards, and storage devices.
   - **Device Drivers**: Software components that allow the operating system to communicate with hardware devices.
   - **I/O Scheduling**: Determines the order in which I/O requests are handled.

6. **Security and Access Control**
   - Ensures that only authorized users and processes can access system resources.
   - **Authentication**: Verifies the identity of users and processes.
   - **Authorization**: Determines the level of access granted to authenticated users and processes.
   - **Encryption**: Protects data by converting it into a code that can only be read by authorized users.

7. **Networking**
   - Manages network communication and protocols.
   - **TCP/IP**: The standard protocol suite for network communication.
   - **Network Services**: Services such as DNS, DHCP, and web servers.

### Functions of an Operating System

8. **Resource Allocation**
   - Allocates system resources (CPU, memory, I/O devices) to processes and users.
   - Ensures efficient and fair use of resources.

9. **Process Scheduling**
   - Determines the order in which processes are executed.
   - Balances the need for fairness, efficiency, and responsiveness.

10. **Memory Management**
   - Allocates and deallocates memory space as needed.
   - Manages virtual memory and paging.

11. **File Management**
   - Organizes and manages files and directories.
   - Provides file access and protection mechanisms.

12. **Security and Protection**
   - Protects the system and its resources from unauthorized access.
   - Ensures data integrity and confidentiality.

13. **User Interface**
   - Provides a user interface for interacting with the system (e.g., Command Line Interface (CLI), Graphical User Interface (GUI)).

## Examples of Operating Systems

-  **Windows**: Developed by Microsoft, widely used in personal computers and servers.
-  **macOS**: Developed by Apple, used in Mac computers.
-  **Linux**: An open-source operating system with various distributions (e.g., Ubuntu, Fedora, Debian).
-  **Unix**: A multi-user, multitasking operating system developed in the 1960s and 1970s.
-  **Android**: A mobile operating system based on the Linux kernel, developed by Google.