---
title: DRAM
---

Built with capacitors.

Capacitors slowly leak charge, so they need to be recharged (refreshed) periodically.
- Needs constant refreshing to maintain data (refresh every 64 milliseconds)
- Less expensive
- Higher density
- Used for main system memory
- Slower than [SRAM](/computer-architecture-network-technology-and-operating-systems/architecture/sram)

## Generations
### DDR3
- Speed 2133 MB/s
- Peak 17 GB/s

old used 1.5Volt, new uses 1.34Volts
### DDR4
- Speed 3.2 GB/s
- Peak 25,6 GB/s
### DDR 5
- Speed 6,4 GB/s
- Peak 51.2 GB/s

## Configurations
### Ranks
"2R" means Dual Rank. The module has two ranks of memory.
A rank is a set of DRAM chips that operate simultaneously. Each rank can be accessed independently.

Fewer the better → simpler memory configurations are generally more stable and have better compatibility.

### Banks
Refers to the internal organization of each DRAM chip
"x8" means each chip outputs 8 bits at a time. Common alternatives are: x4 (4 bits) or x16 (16 bits).

Fewer banks generally means better stability and compatibility.

This affects how the memory controller interacts with the RAM.

## Same Type
All chips within a memory module (across all ranks) need to be of the same type and specifications:
### Timing Consistency
- All chips must operate at the same speed.
- Same latency timings (CAS, RAS, etc)
- Same refresh requirements
### Voltage Requirements
- All chips need to use the same operating voltage
- Mixed voltage chips could cause damage or instability.
### Manufacturing/Quality Control
- Memory manufacturers typically  use identical chips from the same prodection batch
### Memory Controller Requirements
- The memory controller expects uniform behavior across all ranks.