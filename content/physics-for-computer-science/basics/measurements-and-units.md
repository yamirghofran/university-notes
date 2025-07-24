---
title: Measurements and Units
---

# Physical Quantities
Part of the scientific method is to measure the system we want study. The result of these measurements are numbers. A number or collection of numbers used to describe a physical phenomenon is a **physical quantity**, such as the temperature of a gas, the current in a circuit, or the electric force exerted by a charge. 

When only one number is required, the quantity is a **scalar**. Other vectors require a direction in space to be determined, like forces or velocities, and these are called **vectors**. Other quantities require even more directions, and these are called **tensors** (represented by matrices or arrays). All these have a geometric interpretation, so they follow certain transformation rules when we change our coordinates. Let's bear in mind that we describe the same physical reality regardless of the framework we use, so there has to be a consistency between different descriptions.

# Units
To measure a quantity, we compare it with some reference standard. This standard defines a **unit** of the quantity. Any physical quantity requires at least a number (magnitude) and a unit. **One must always specify the unit used**. For example, kelvins for temperature, amperes for current, and newtons for electric force.

Some physical quantities are considered fundamental, and so they are simply defined through the way we measure them. There are seven of this sort of quantities, with their respective fundamental units. The rest are defined by combinations of these fundamental magnitudes. The fundamental units must not change over time, and they can be replicated by independent observers. The most common system of these units is the International System, or SI (Système International).

| Quantity            | SI unit       |
| ------------------- | ------------- |
| length              | meter(m)      |
| mass                | kilogram (kg) |
| time                | second (s)    |
| electric current    | ampere (A)    |
| temperature         | kelvin (K)    |
| amount of substance | mole (mol)    |
| luminous intensity  | candela (cd)  |

In practice we need to resort to smaller or greater units than the standard ones, and so we introduce a prefix.

| Multiple or Submultiple | Prefix | Symbol |
|-------------------------|--------|--------|
| $10^{18}$               | exa    | E      |
| $10^{15}$               | peta   | P      |
| $10^{12}$               | tera   | T      |
| $10^{9}$                | giga   | G      |
| $10^{6}$                | mega   | M      |
| $10^{3}$                | kilo   | k      |
| $10^{2}$                | hecto  | h      |
| $10^{1}$                | deca   | da     |
| $10^{-1}$               | deci   | d      |
| $10^{-2}$               | centi  | c      |
| $10^{-3}$               | milli  | m      |
| $10^{-6}$               | micro  | μ      |
| $10^{-9}$               | nano   | n      |
| $10^{-12}$              | pico   | p      |
| $10^{-15}$              | femto  | f      |
| $10^{-18}$              | atto   | a      |
An equation must always be dimensionally consistent, which means that both sides of the equation must have the same units (or in an abstract way, the same dimensions).

For example,
$$d\vec r=\vec v dt$$

The l.h.s is measured in meters and the r.h.s is the product $m/s\times s=m$.

# Scientific Notation
It is customary to express the magnitude using the **scientific notation**
For example, the speed of light is
$$c=299792458 m/s\approx 3.00\times 10^8 m/s$$
Even if we don't know exact figures, it is useful to estimate or remember **order of magnitudes**, which corresponds to the power-of-10 exponent. Example, what is the order of magnitude of radio-wave frequencies?

# Uncertainties and Significant Figures
Any measurement is subjected to different sources of uncertainty due to:
- instrument precision
- calibration errors (systematic errors)
- statistical errors (the result of random influences)
Let's say we buy a resistor of $100\Omega$ with $2\%$ tolerance. This means,
$$R=(100\pm 2)\Omega$$
We have 3 **significant figures**. It would not make any sense to write
$$R=(100.4\pm 2)\Omega$$
# Precision vs. Accuracy
Finally, it's relevant to make a distinction between precision and accuracy of a measurement
![[Pasted image 20240306132223.png]]
