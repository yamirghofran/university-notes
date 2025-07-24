---
title: Self-Inductance
---

The [Magnetic Flux](/physics-for-computer-science/electromagnetism/magnetic-flux) through an isolated circuit (the flux produced by the circuit itself) depends on the geometry of the circuit and the current. Hence, for a stationary and rigid circuit the change in the flux is due to changes in current. We can then write

$$\frac{d \Phi}{d t}=\frac{d \Phi}{d I} \frac{d I}{d t}$$

We define the self-inductance (or simply inductance) $L$
$$L=\frac{d \Phi}{d I}$$
[Faraday's Law](/physics-for-computer-science/electromagnetism/faradays-law) can then be expressed as
$$\mathcal{E}=-L \frac{d I}{d t}$$

*Properties*
- When the circuit lies in a linear magnetic medium (like vacuum), the flux linearly depends on the current, according to the Biot-Savart law. Therefore, the self-inductance is simply the proportionality constant between current and flux
$$L=\frac{\Phi}{I}$$
- For coil with N turns and current $i$ in each loop, $L=\frac{N\Phi}{i}$. As the flux in turn depends on $N$, the self-inductance is proportional to $N^2$.
- the SI unit of self-inductance is the henry (H) in honor of the American physicist Joseph Henry (1797–1878). $1 \mathrm{H}=1 \mathrm{Wb} / \mathrm{A}=1 \mathrm{V} \cdot \mathrm{s} / \mathrm{A}=1 \Omega \cdot \mathrm{s}=1 \mathrm{J} / \mathrm{A}^{2}$. Analogously to the farad, the henry is a rather large unit of mutual inductance. Typical values of mutual inductance lies in the range of millihenry ($mH$) or microhenry ($\mu H$).
- **The self-induced emf in a circuit opposes any change in the current in that circuit.**

## Example: Toroidal Solenoid
![[Pasted image 20240306214543.png]]
Applying Ampere's circuital law, it's straightforward to derive the self-inductance of a toroidal solenoid of radius $R$ and cross-sectional area $A$. We assume a ferromagnetic core of magnetic permeability $\mu$

$$L=\frac{N \Phi_{B}}{i}=\frac{\mu N^{2} A}{2 \pi R}$$