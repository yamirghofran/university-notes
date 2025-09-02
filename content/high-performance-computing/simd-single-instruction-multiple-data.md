---
title: SIMD (Single Instruction, Multiple Data)
---

A single instruction is applied to multiple data points simultaneously.

e.g. for increasing the brightness of an image, the instruction "increase brightness by 10%" is applied to multiple data points (the pixels) simultaneously.

This is a form of **data parallelism** and is highly efficient for tasks with regular repetitive operations on large datasets.

Modern CPUs and GPUs have specialized SIMD instruction sets (like SSE and AVX) to perform these **vector operations**.