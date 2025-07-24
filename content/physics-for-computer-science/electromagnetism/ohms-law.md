---
title: Ohm's Law
---

Once the conduction is established, what is the relation between the current density and the electric field causing such current density? The Ohm's law tells us that the relation is linear
$$ \vec E=\rho \vec J$$
*Remarks*
- Good approximation for metals. A material that obeys Ohm's law is called Ohmic. Many are non-Ohmic (like diodes)
- $\rho$ is called **resistivity**, measured in $(\mathrm{V} / \mathrm{m}) /\left(\mathrm{A} / \mathrm{m}^{2}\right)=\mathrm{V} \cdot \mathrm{m} / \mathrm{A}=\Omega \cdot\mathrm{m}$. It characterizes the intrinsic resistance to a electric current. Same symbol as volume density charge, do not confuse them!!!
- The reciprocal of resistivity is **conductivity**.
- Poor electrical conductors (ceramics, plastics) are normally poor thermal conductors as well, as particles are nor free to transport any form of energy. 
![[Pasted image 20240306171835.png]]
## Resistance
Ohm's law can be re-expressed in a more convenient form. Let's assume the conductor is a long wire of length $L$ and cross-section area $A$. Let $V$ potential difference between the extremes of the wire, and $I$ the current flowing within. As $\vec J$ and $\vec E$ are constant and parallel along the wire, we can write $I=JA$ and $V=EL$, hence $$ V=\frac{\rho L}{A} I=RI$$
*Properties*

- $R=V/I$ is called **resistance**, measured in Ohms ($\Omega=V/A$). Unlike the resistivity, it is not an intrinsic quantity of the material as it also depends on the **geometry**.
- Typical values in circuits $\Omega$, kilohms, $k\Omega=10^{3}\Omega$, megaohms $M\Omega=10^{6}\Omega$
- Resistance varies with temperature, the simples model is linear $R(T)\approx R_{0}\left[1+\alpha\left(T-T_{0}\right)\right]$.
- A circuit component made to have a specific value of resistance is called a **resistor**. 

In practice, real resistors of different values are used to limit the current in a certain part of the circuit.
![[Pasted image 20240306171842.png]]

[https://youtu.be/HsLLq6Rm5tU](https://youtu.be/HsLLq6Rm5tU)

