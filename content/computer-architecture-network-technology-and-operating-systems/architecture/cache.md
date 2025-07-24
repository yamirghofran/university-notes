---
title: Cache
---

A **cache** is a small, fast memory that stores frequently accessed data or instructions. The primary purpose of a cache is to reduce the time it takes to access main memory, thereby improving system performance.

## Proximity

They're closer to the [CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu) physically. That's less distance for bits to travel. Signals in on-chip wiring actually travel quite slowly compared to the speed of light. Light goes about a foot a nanosecond in a vacuum. It can be orders of magnitude slower in on-chip interconnects.

## Capacity

Smaller capacity [RAMs](/computer-architecture-network-technology-and-operating-systems/architecture/memory) are typically faster than larger capacity RAMs, in particularly because the furthest away bit is nearer, and there's less capacitance to wrangle in bit lines within the array.

## Density

The smaller capacity allows for larger transistors, which makes for less resistance, which translates to faster charging of those bit lines. ![](../attachments/cleanshot-2025-01-12-at-0826112x.png) The first code snippet is good because it accesses the image array in **row-major** order, which is how data is stored in memory for most programming languages. This leads to better cache performance and faster execution. The second code snippet is bad because it accesses the image array in **column-major** order. This results in poor cache performance, as it jumps around in memory, leading to slower execution. ![](../attachments/cleanshot-2025-01-19-at-2219082x.png)

## L1 Cache:

- **L1d Cache (Data):** Each core has a 32KB Level 1 data cache.
- **L1i Cache (Instruction):** Each core also has a 32KB Level 1 instruction cache.

## L2 Cache:

- Each core has its own 256KB Level 2 cache.

## L3 Cache:

- The Level 3 cache is shared between the cores and is 3,072KB (or 3MB).

## Key Points:

- **Private Caches:** L1 and L2 caches are private to each core, meaning each core has its own separate L1 and L2 caches.
- **Shared Cache:** The L3 cache is shared across both cores, allowing for data to be shared between them, which can improve efficiency and performance.
- **Cache Size:** The cache sizes increase from L1 to L3, with L1 being the smallest and fastest, and L3 being larger but slower in comparison. This hierarchy is designed to optimize data access speed and efficiency, with each level of cache serving a specific role in reducing latency and improving the overall performance of the processor.

## Cache Consistency

Caching data that is only read is easy, since the copy in the cache and memory will be identical Caching writes is more difficult; for example, how can the copy in the cache and memory be kept consistent? There are 2 main strategies

## Write-through and Write-back

- A **write-through** cache updates the item in the cache and writes through to update main memory.
- A **write-back** cache only updates the copy in the cache when the block is about to be replaced, it is copied back to memory. (faster but dangerous) 
Both write strategies can use a write buffer to allow the cache to proceed as soon as the data are placed in the buffer rather than wait the full latency to write the data into memory.

## Miss Rate

A measure of the benefits of different cache organizations. Miss rate is simply the fraction of cache accesses that result in a miss. i.i. the number of accesses that miss divided by number of accesses. $$\frac{\text{number of accesses that miss}}{\text{number of accesses}}$$

---
- L1,L2,L3 cache
- Proximity, Capacity, Density
- Consistency
	- Write-through
	- Write-back
- Miss rate