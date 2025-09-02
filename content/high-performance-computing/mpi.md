---
title: MPI
---

A model where computing nodes in a cluster do not share memory. All data sharing and interaction must be done through explicit message passing.

Applications written in MPI have run successfully on cluster computing systems with more than 100,000 nodes.

While CUDA is an effective interface with each node, most application developers need to use MPI to program at the cluster level.

The effort needed to port an application into MPI is high due to the lack of shared memory across computing nodes:
- Domain decomposition to partition the input and output data into cluster nodes.
- Calling message-sending and receiving functions to manage data exchange between nodes based on the partitioning.
CUDA, on the other hand, provides shared memory for parallel execution in the GPU. 