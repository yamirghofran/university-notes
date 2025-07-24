---
title: GPU
---

Initially used for graphics processing, but with the advent of **CUDA architecture**, they can now be used for general-purpose computing as well.

CUDA is an extension of C/C++ programming that provides parallel programmers with a small set of capabilities to parallelize functions, loops, and recursions. 

In contrast to prior APIs like Direct3D and OpenGL, which required advanced skills in graphics programming by using CUDA, GPUs can be treated as an array of CPUs where parallel computations can be made.


![](../attachments/cleanshot-2025-01-12-at-0801512x.png)

The architecture of a GPU is designed to handle parallel processing of large amounts of data.

GPUs have a large number of cores that work together to perform complex calculations.

The cores are organized into groups called streaming multiprocessors (SM) which are responsible for executing instructions in parallel.

Each streaming multiprocessor has its own set of registers and shared memory, which allows it to perform calculations independently of other SMs.

The [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory) hierarchy of a GPU is also designed to optimize parallel processing. GPUs have a large amount of memory that is divided into different levels of [Cache](/computer-architecture-network-technology-and-operating-systems/architecture/cache).

![](../attachments/cleanshot-2025-02-08-at-1833552x.png)
## Old GPUs
![](../attachments/cleanshot-2025-02-08-at-1834362x.png)
- Programmable [Shader](/computer-architecture-network-technology-and-operating-systems/architecture/shader)s
- General Purpose [GPU](/computer-architecture-network-technology-and-operating-systems/architecture/gpu) (GPGPU)
	A new programming model:
	- PhD in computer graphics required.
	- Financial companies started hiring game programmers.
	- [GPU](/computer-architecture-network-technology-and-operating-systems/architecture/gpu) as processor.

## Mobile GPU
- Adreno
	-  developed by Qualcomm for use in their Snapdragon SoCs 2.
- Mali
	- developed by ARM Holdings for use in their SoCs 2.
- PowerVR
	- developed by Imagination technologies.
![](../attachments/cleanshot-2025-02-08-at-1848502x.png)

![](../attachments/cleanshot-2025-02-08-at-1852512x.png)
