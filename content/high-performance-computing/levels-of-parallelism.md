---
title: Levels of Parallelism
---

## Bit-Level Parallelism
- 8-bit → 16-bit → 32-bit → 64-bit processors. More data in a single operation.

## Instruction-Level Parallelism (ILP)
Executing multiple instructions from a single program (process) at the same time, as long as the instructions are independent of each other.
Largely handled by the hardware itself.

## Task Parallelism
Distributing different tasks across multiple processors. e.g. in a weather simulation, one set of processors might model atmospheric conditions while another models ocean currents.

## Data Parallelism
The same task is performed on different subsets of a large dataset. e.g. when processing a large image, the image can be divided into sections, and each processor can apply the same filter to its assigned section.