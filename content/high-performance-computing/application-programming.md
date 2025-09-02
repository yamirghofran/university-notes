---
title: Application Programming
---

- How to use it: programming interfaces (languages, libraries, tools,...)
- Programming languages for HPC focus on **performance**.
	- Parallel tasks and synchronization between them (sharing & allocating resources)
	- Most used: Fortran, C, C++, Python.
- Granularity of parallel work:
- **Fine-grained parallelism** is emphasized in multi-threaded shared-memory system programming interfaces such as [OpenMP](/high-performance-computing/openmp) and Cilk++.
- **Medium- to coarse-grained parallelism**, as reflected by highly scaled massively parallel processors (MPPs) and clusters, is primarily represented by communicating sequential processes such as the message-passing-interface ([MPI](/high-performance-computing/mpi))
- **Very coarse-grained** workloads with **no interactivity**, sometimes referred to as "embarrassingly parallel" or "job-stream" workflow.

## Key differences between programming for HPC vs conventional computers
- **Parallelism**
	- Single Computer: Limited parallelism, often using multi-threading.
	- Supercomputing: Heavy parallel programming across thousands of processors using MPI and OpenMP.
- **Resource Management**
	- Single Computer: Simple, managed by the OS within a single machine's limits.
	- Supercomputing: Complex, involving multiple nodes, explicit memory distribution, and load balancing.
- **Problem Types**
	- Single Computer: Suitable for small-scale, less resource-intensive problems.
	- Supercomputing: Designed for large-scale, complex problems requiring vast computational power.
- **Development Tools**
	- Single Computer: Standard tools and libraries.
	- Supercomputing: Specialized tools and libraries like MPI, OpenMP, CUDA, and performance analysis tools.