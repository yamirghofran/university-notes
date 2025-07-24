---
title: Magnetic Field
---

As we did with the electric interaction, we shall decompose the magnetic interaction in two parts: 1) a moving charge (or current) generates a magnetic field in its surroundings and 2) another moving charge (or current) in its surroundings 'feels' the presence of the magnetic field as a force acting on it.

Let's assume a **test charge** $q$ moving at velocity $\vec B$, the magnetic force follows the **Lorentz law**, $$\vec F=q \vec v \times \vec B$$ $$\|\vec F\|=|q| \|\vec v\| \|\vec B\| sin\phi$$
Extension to a **wire** of length $l$ and current $I$, where $\vec l$ takes the direction of the the current density.
$$\vec{F}=I\vec{l} \times \vec{B}$$
*Remarks*
- Like the electric field, the magnetic field is a vector field, which associates a vector to each point in space. $\vec B(\vec r): \mathbb{R}^3\rightarrow\mathbb{R}^3$. 
- when the charge moves in the same direction as the magnetic field, the force is **zero**.
- the force is always **perpendicular** to the plane formed by the velocity and the magnetic field. Hence the **work** done by a magnetic force is **zero**. Invoking the work-energy theorem, a magnetic force **cannot change the kinetic energy** of a charge. 
- If two charges with equal magnitude and opposite sign move in the same field with the same velocity , the forces have equal magnitude but opposite direction.
- The net force in the presence of both an electric and magnetic field is the vector sum: $\vec F=q (\vec E+\vec v \times \vec B)$.
- SI units, 1 **tesla** $=1 \mathrm{T}=1 \mathrm{N} / (\mathrm{A} \cdot \mathrm{m})$. Also popular, 1 **gauss** $1 \mathrm{G}=10^{-4} \mathrm{T}$.
- As for graphical representation purposes, a dot ($\cdot$) indicates a magnetic field vector directed out of the plane, whereas a cross ($\times$) represents a vector directed into the plane.
## Right Hand rule
![[Pasted image 20240306172453.png]]

## Magnetic Field Lines
The magnetic field is graphically represented by magnetic field lines. These are curves such that their **tangent** at any point align with the magnetic field. 
![[Pasted image 20240306172525.png]]
*Properties*:
- their **spacing** represents the magnitude of the magnetic field: the closer the lines, the stronger the field.
- At any given point the magnetic field is unique, hence field lines **never intersect**.
- Magnetic field lines are not “lines of force”, this is, they do **not** point in the direction of the magnetic force on a charge.
- Magnetic field lines do have the direction that a compass needle would point at each location
[https://youtu.be/1PuL-Zh8PPk](https://youtu.be/1PuL-Zh8PPk)

## Earth's Magnetic Field
![[Pasted image 20240306172638.png]]
The magnetic field of the Earth is of the order of 1G. 1T is actually a very intense magnetic field. Magnetic resonance imaging (MRI) employs strong magnetic fields $\approx 1.5 T$.

## Elementary Sources of Magnetic Field

### Magnetic Field of a Point Charge
Magnetic field of a charge located at $\vec r_1$ moving at velocity $\vec v$
![[Pasted image 20240306172809.png]]

| circuit element at origin                                                                                  | arbitrary origin                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| $$\vec{B}(\vec r)=\frac{\mu_{0}}{4 \pi} \frac{q \vec{v} \times \hat{r}}{r^{2}}$$ $$\hat r\equiv \vec r/r$$ | $$ \vec{B}\left(\vec{r}_{2}\right)=\frac{\mu_{0}}{4 \pi} \frac{q\vec v\times\left(\vec{r}_{2}-\vec{r}_{1}\right)}{\|\vec{r}_{2}-\vec{r}_{1}\|^{3}}$$ |

- Similarly to the Coulomb field, the magnetic field is proportional to the charge q and the squared inverse of the distance $\propto 1/r^2$, but the direction is perpendicular to the plane formed by the velocity $\vec v$ and the field point $\vec r$.

### Magnetic Field of a Circuit Element
The total magnetic field created by several moving charges is the vector sum of the fields caused by the individual charges $d \vec{B}=\int d\vec B_{dQ}$. Hence it's straightforward to derive the **law of Biot and Savart**

|  circuit element at origin  |   arbitrary origin   |
|-----|-----|
|$$d \vec{B}=\frac{\mu_{0}}{4 \pi} \frac{I d \vec{l} \times \hat{r}}{r^{2}}$$ |$$d \vec{B}\left(\vec{r}_{2}\right)=\frac{\mu_{0}}{4 \pi} I_{1} \frac{d \vec{l} \times\left(\vec{r}_{2}-\vec{r}_{1}\right)}{\|\vec{r}_{2}-\vec{r}_{1}\|^{3}}$$|

with $d\vec l$ being a vector with length $dl$ in the same direction as the current density in the conductor.

Integrating over the entire circuit

$$\vec{B}\left(\vec{r}_{2}\right)=\frac{\mu_{0}}{4 \pi} I_{1} \oint_{1} \frac{d \vec{l}_{1} \times\left(\vec{r}_{2}-\vec{r}_{1}\right)}{\left|\vec{r}_{2}-\vec{r}_{1}\right|^{3}}$$
The field lines go in circles around $d\vec l$, with direction given by the right-hand side rule.

| ![[Pasted image 20240306204957.png]] | ![[Pasted image 20240306205020.png]] |
| ------------------------------------ | ------------------------------------ |
## Important Simple Cases
| long straight conducting wire          | on the axis of a circular loop                                    |
| -------------------------------------- | ----------------------------------------------------------------- |
| ![[Pasted image 20240306205053.png]]   | ![[Pasted image 20240306205059.png]]                              |
| $B_{\theta}=\frac{\mu_{0} I}{2 \pi r}$ | $B_{z}=\frac{\mu_{0} I a^{2}}{2\left(z^{2}+a^{2}\right)^{3 / 2}}$ |

Read and understand the derivation by yourself: Sears & Zemansky 28.3, 2

[https://youtu.be/bq6IhapfucE](https://youtu.be/bq6IhapfucE)

**Solenoid**: a helical winding of wire on a cylinder or toroid. When the solenoid is long compared to its cross-sectional diameter and the coils are tightly wound, the field inside the solenoid can be approximated by a uniform magnetic field, while the external field is almost negligible.

[https://youtu.be/BbmocfETTFo](https://youtu.be/BbmocfETTFo)

- Long solenoid with n turns per unit length
	![[Pasted image 20240306205221.png]]
	$$ B=\frac{\mu_{0} N I}{2\pi r}$$
- Toroidal solenoid with N turns
	![[Pasted image 20240306205301.png]]
	$$ B=\frac{\mu_{0} N I}{2\pi r}$$
