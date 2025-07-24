---
title: Peripherals
---

Peripherals are connected to the [CPU](/computer-architecture-network-technology-and-operating-systems/architecture/cpu) through the [data bus](/computer-architecture-network-technology-and-operating-systems/architecture/buses) in a similar way as the [memory](/computer-architecture-network-technology-and-operating-systems/architecture/memory).
Writing in certain memory addresses can result in altering the peripheral behavior.
Reading allows to use the information provided by the peripheral.

## Peripherals Interaction
- **On-chip**
	- Implemented inside the same silicon chip as the CPU
	- e.g. timers, pwm, ADC, Serial
- **Off-chip**
	- Connected externally to the [address/data buses](/computer-architecture-network-technology-and-operating-systems/architecture/buses)
	- e.g. Network interfaces, Graphics accelerators

## Examples
- GPIO controllers
	- General Purpose Input and Output controllers are used to control the pins that are coming out of the microcontroller.
- Timers
	- Timing is a crucial part of any embedded system, and timers are used to control the blinking rate of LEDs or to generate precise delays.
- Pulse Width Modulation (PWM) controllers
	- PWM controllers are used to control the speed of motors, the brightness of LEDs, and the frequency of audio signals 1.
- Digital to Analog Converters (DAC)
	- Used to convert digital signals to analog signals.
- Analog to Digital Converters (ADC)
	- Used to convert analog signals to digital signals.
- Serial Communication Controllers
	- These controllers are used to communicate with other devices using serial communication protocols such as UART, SPI, I2C, and

Ethernet.
- [Direct Memory Access (DMA)](/computer-architecture-network-technology-and-operating-systems/architecture/direct-memory-access-dma)
	- DMA Controllers are used to transfer data between memory and peripherals without the intervention of the microprocessor 1.
---
- [Peripheral Component Interconnect (PCI) Bus](/computer-architecture-network-technology-and-operating-systems/architecture/peripheral-component-interconnect-pci-bus)

