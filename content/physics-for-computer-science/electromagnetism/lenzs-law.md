---
title: Lenz's Law
---

Lenz's law states: **the induced emf or current in a circuit opposes the change in magnetic flux**.

*Remarks*:
- It is a **qualitative law** that specifies the direction of induced current but not its module.
- It is an **alternative** (and more intuitive) way the direction of the emf compared **to Faraday's law**.
- It was formulated by the Russian scientist Emil Lenz (1804–1865) who independently from Faraday and Henry discovered it.
- Lenz's law may be seen as analogous to Newton's third law in classical mechanics.
- Lenz's law is a consequence of the **conservation of energy**.

![[Pasted image 20240306212318.png]]

### Slidewire generator revised
Applying [Faraday's Law](/physics-for-computer-science/electromagnetism/faradays-law) to the slidewire generator we derive the same expression that we derived using the Lorentz force.

<center><img src="emf.png" width="400"/></center>
$$\mathcal{E}=-\frac{d \Phi_{B}}{d t}=-B \frac{d A}{d t}=-B \frac{L v d t}{d t}=-B L v$$

The minus sign indicates that the emf is directed counterclockwise around the loop.

The induced emf produces a current around the loop of magnitude $I=\mathcal E/R=BLv/R$. As a result, the rod experiences a magnetic force $\vec F=I\vec L\times  \vec B$ opposed to the velocity (as an expression of Lenz's law). To keep a constant velocity, the applied force must compensate the magnetic force, hence

$$F=I L B=\frac{B L v}{R} L B=\frac{B^{2} L^{2} v}{R}$$

One can also check that the work done per unit time on the rod $P_{applied}=Fv$ compensates the power dissipated by the circuit $P_{dissipated}=I^2R$ (conservation of energy). 

- The slidewire generator **transforms mechanical energy into electric energy**, conserving energy in the process.

The equations

  
$$\mathcal{E} = \oint (\vec{v} \times \vec{B}) \cdot d\vec{l}$$
$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$

are actually expressions of Faraday's law. The former is more convenient formulation for moving conductors, while the latter is necessary for stationary conductors in changing magnetic fields.