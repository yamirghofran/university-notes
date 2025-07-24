---
title: Inductors
---

An inductor is a circuit component designed to have a specific inductance. Although the [electric field](/physics-for-computer-science/electromagnetism/electrostatic-field) created by magnetic induction is non-conservative, we can still associate a voltage drop between its terminals $$V_{a b}=L \frac{d i}{d t}$$
using the convention indicated in the figure,
![[Pasted image 20240306214708.png]]

*Properties*
- They are normally built with **solenoids** or toroidal solenoids with **ferromagnetic core**. For these materials we use the corresponding magnetic permeability $\mu=\mu_r\mu_0$, which greatly amplifies the inductance.
- Unlike a resistor, **an inductor stores energy** in the induced magnetic field (analogously to a capacitor, which stores energy in the electric field)
- In a direct-current circuit, inductors are **used to keep a steady current despite any voltage fluctuations**.
- In an alternating-current circuit, inductors are used to filter current variations with high frequencies (**low-pass filters**).
- An inductor exhibits "inertia". When current decreases very rapidly in a circuit, the **back emf** increases dangerously, which may end up burning out some circuit component.

[https://youtu.be/KSylo01n5FY](https://youtu.be/KSylo01n5FY "Share link") - Inductors explainer
[https://youtu.be/KSylo01n5FY](https://youtu.be/KSylo01n5FY "Share link") - Back emf


## Magnetic Field Energy of an Inductor
To establish a current in an inductor requires certain amount of energy, employed in creating the induced magnetic field. Let's assume an ideal inductor with zero resistance, then the energy supplied to the inductor during an infinitesimal time interval $dt$ is
$$d U=Pdt=V_{ab}idt=L i d i$$
Integrating we find the total energy $$U=L \int_{0}^{I} i d i=\frac{1}{2} L I^{2}$$
Once the magnetic field is created, the inductor is charged. If the current decreases, the inductors becomes a source that supplies current to the circuit until it consumes its stored energy.

In general, one can show (beyond the scope of this course) that, for any type of inductor, the magnetic energy density $u=U/V$ (magnetic energy per unit volume) can be calculated as $$u=\frac{B^{2}}{2 \mu}$$
Taking the toroidal solenoid for a demonstration, 

$$u=\frac{U}{V}=\frac{1/2LI^2}{2\pi r A}=\frac{1}{2} \mu \frac{N^{2} I^{2}}{(2 \pi r)^{2}}=\frac{B^{2}}{2 \mu}$$