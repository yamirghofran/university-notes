---
title: A Brief History of Supercomputing
---


# A Brief History of Supercomputing

## Epoch I—Automated Calculators Through Mechanical Technologies

### Timeline & Key Developments
- **10,000 years ago**: Tally sticks - earliest known counting devices
- **2400 BCE**: Abacus - first systematic calculation tool
- **200 BCE**: Chinese Suanpan - advanced abacus design
  - Artificial representation and storage of numbers
  - Introduction of the concept of process

### Mechanical Calculators
- **1642**: Pascaline - Blaise Pascal's mechanical calculator
- **1851**: Arithmometer - Thomas de Colmar
  - Performed division, addition, subtraction
  - Early "ALU" or "arithmetic logic unit"

### Control & Data Storage
- **1801**: Joseph Jacquard weaving loom
  - Control through storage of commands via punch cards
- **1890**: Tabulator (US Census)
  - Punch cards for data processing
  - IBM origins (originally the Tabulating Machine Company)

### Programmable Machines
- **1834**: Babbage Analytical Engine
  - Combined ALU + punch cards
  - First programmable mechanical computer
- **1938**: Konrad Zuse - First programmable electromechanical computer
- **1944**: IBM Harvard Mark I
  - Arithmetic function units
  - Sequence control through stored instructions
  - Intermediate data storage and I/O
  - Performance: 1 instruction per second (IPS)

## Epoch II—von Neumann Architecture in Vacuum Tubes
- **Boolean logic**: George Boole (1848)
  - Framework for complex digital logic functions
  - Basic Boolean operations (AND, OR, NOT)
- **Binary arithmetic**: Claude Shannon (1937)
  - Derived the basic unit of information: the "bit" (binary digit)
  - Foundation for binary arithmetic
- **Computability**: Alan Turing (1936)
  - Turing machine model of computation
  - "Turing equivalent" = general purpose computing
- **von Neumann Architecture**: Stored-program digital computing
  - Basis for almost all CPU designs to this day

### Technology: Vacuum Tubes
- Thomas Edison discovered vacuum tubes by accident (1880)
- Enabled electronic digital computing

### World War II Developments
- **Eckert and Mauchly (US)**: ENIAC for ballistics calculations
- **Turing (UK)**: Colossus for code breaking

### Post-War Commercial Systems
- **MIT Whirlwind**
- **IBM 704**
- **IAS**
- **UNIVAC I**
- **LEO 1 (UK)**: First commercially produced computer
  - Based on EDSAC: 600 IPS
- **IBM 701**: First IBM scientific computer
- **IBM 650**: First mass-produced commercial machine (mid-1950s)
  - Performance: 4 KIPS

### Performance Characteristics
- Performance directly function of CPU clock rate and parallel bit processing

## Epoch III—Instruction-Level Parallelism

### Technology Breakthrough
- **1947**: Transistor invented at Bell Laboratories
  - Alternative to vacuum tube
  - First using germanium, then silicon

### Transistor-Based Systems
- **TX-0**: First transistorized computer (Lincoln Laboratories)
- **IBM 1401** (1959)
- **DEC PDP-1** (1960) - Beginning of minicomputer era
- Both based on TX-0 design

### System Design Evolution
- Printed circuit boards and modules
- Higher abstraction: logical gates (Boolean functions) and latches (single-bit storage)
- Business applications: long-term data storage and I/O devices
- Scientific applications: floating-point operations optimization

### First True Supercomputer
- **CDC 6600** (Seymour Cray)
  - **1 Megaflops**
  - **Instruction-level parallelism (ILP)**: 10 separate logic gates overlapping operations

## Epoch IV—Vector Processing and Integration

### Technology: Integrated Circuits (late 1960s)
- Pushed improvements in size, speed, power, and cost

### Vector Processing
- **Cray-1** (1976, Seymour Cray)
  - **136 megaflops**
  - 80 MHz clock rate
  - Vector pipelined processing for ultralightweight parallelism
- **Pipelining**: divides function into successive subfunctions
  - Less time per subfunction
  - Simultaneous operation on different data
- **Vector processing**: vector register (vector of single registers)
  - Multiple parallel memory accesses

## Epoch V—Single-Instruction Multiple Data Array

### Technology Advances
- Higher functionality chips at lower size, cost, and power
- Microprocessor & dynamic random access memory (DRAM) advances
- **8-bit microprocessors**: Intel, Motorola, Zilog

### SIMD Architecture
- **Single-Instruction Multiple Data (SIMD)**
- All processors perform same operation simultaneously
- Each processor works on dedicated data block
- **Thinking Machine CM-2**: Example of SIMD-array architecture

## Epoch VI—Communicating Sequential Processors and Very Large Scale Integration

### Technology: VLSI (Very Large Scale Integration)
- Billions of transistors on single semiconductor die
- **4-bit and 8-bit** (1970s) and **16-bit** (1980s) microprocessors for PCs

### Market Evolution
- **PCs**: Lower-cost personal use
- **Workstations**: Higher-cost industrial-grade purposes

### Parallel Processing Systems
- **Research systems**:
  - Caltech Cosmic Cube
  - MIT Concert
  - IBM RP2
  - Intel Touchstone Delta

### Commercial Massive Parallel Processors (MPPs)
- **1990s**: First commercial MPPs
- **Features**:
  - Custom networks
  - Distributed-memory hardware
  - Message-passing methods
  - Synchronization primitives
- **Examples**:
  - Intel Touchstone Paragon (1994)
  - Thinking Machines Corporation CM-5 (1992)
  - IBM SP-2

### Commodity Clusters
- **HPC assembled from standard cluster "PC" nodes**
- **Economy of scale** vs custom-designed MPPs
- **Examples**:
  - UC Berkeley Network of Workstations (NOWs)
  - NASA Beowulf Project
- **Dominant technologies**: x86 processor, Ethernet networks, Linux OS, MPI
- **TOP500 dominance**

## Epoch VII—Multicore Petaflops

### Architecture
- **Multicore sockets + GPUs + hybrid programming methods**
- Performance based on number of cores employed
- **Programming challenge**: Programming models struggling to catch up
- **Dynamic adaptive computing**: New runtime system software and programming interfaces

## Neodigital Age and Beyond Moore's Law

### End of Moore's Law
- Chip density and peak performance approaching limits
- Feature size approaching nanoscale (~5 nm)

### Future Technologies
- **Quantum computing**
  - Exploits quantum mechanics physics
  - Same circuits perform many actions simultaneously
- **Neuromorphic architectures**
  - Brain-inspired structures
  - Pattern matching, searching, machine learning

## Recap: Supercomputer Evolution

### Architecture Paradigms by Era

#### 1940 – 1950: First Computers are Supercomputers
- **Characteristics**: Specialized, very expensive
- **Focus**: First generation computing

#### 1960 – 1980: General Purpose Computers Appear
- **Characteristics**: Still special machines for complex problems
- **Focus**: Supercomputing (High Performance Computing - HPC)
- **Applications**: Floating operations (linear algebra)
- **Technology**: Special purpose (fast vector processors, parallel architectures)
- **Scale**: Only few machines produced

#### 1990 – 2000: Integration of Standard Processors
- **Architecture**: Many "computers" connected through fast network
- **Memory model**: Distributed memory → MPI
- **Systems**: Both proprietary MPPs and Cluster Computing

#### 2010 – : Heterogeneous Cluster Systems
- **Technology**: Accelerator technologies (GPU, many-core)
- **Architecture**: Hybrid systems combining different processing units

## Different Epochs of Supercomputing - Summary Table

| Characteristic / Epoch      | Epoch I—Automated Calculators | Epoch II—von Neumann Architecture | Epoch III—Instruction-Level Parallelism | Epoch IV—Vector Processing | Epoch V—SIMD Array               |
| --------------------------- | ----------------------------- | --------------------------------- | --------------------------------------- | -------------------------- | -------------------------------- |
| **Period**                  | Late 1800s - Early 1900s      | Mid 1900s                         | Late 1900s                              | 1970s - 1980s              | 1980s                            |
| **Technology**              | Mechanical gears & levers     | Vacuum tubes & transistors        | Microprocessors circuits                | Integrated circuits        | Array processors                 |
| **Main Use**                | Arithmetic calculations       | General-purpose computation       | Pipeline processing                     | Scientific calculations    | Graphics & parallel computations |
| **Computational Power**     | Low                           | Moderate                          | High                                    | Very high                  | Ultra high                       |
| **Key Challenges**          | Limited functionality         | Heat dissipation & size           | Balancing parallel units                | Memory & bandwidth         | Scalability                      |
| **Example Machine/Concept** | Analytical Engine (Babbage)   | ENIAC                             | Intel 8086                              | Cray-1                     | CM-1 Machine                     |

| Characteristic / Epoch  | Epoch VI—Communicating Sequential Processors | Epoch VII—Multicore Petaflops | Neodigital Age & Beyond Moore's Law   |
| ----------------------- | -------------------------------------------- | ----------------------------- | ------------------------------------- |
| **Period**              | 1990s                                        | 2000s - 2010s                 | 2010s - Present                       |
| **Technology**          | VLSI chips                                   | Multicore CPUs & GPUs         | Quantum bits, Neuromorphic            |
| **Main Use**            | Data processing & parallelism                | High-scale parallelism        | Specialized tasks, Quantum algorithms |
| **Computational Power** | Massive                                      | ExaFLOPS                      | Beyond classical computation          |
| **Key Challenges**      | Intercommunication & synchronization         | Energy & heat management      | Decoherence, stability                |
| **Example Machine**     | Intel Paragon                                | IBM Roadrunner, Titan         | IBM Q System, Google's Sycamore       |