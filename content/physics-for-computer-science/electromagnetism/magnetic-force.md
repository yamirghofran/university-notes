---
title: Magnetic Force
---

The magnetic force is a fundamental interaction between **moving** charged particles.
The magnetic force applied on $q_1$ by $q_2$ with velocities $\vec v_1$ and $\vec v_2$ respectively is
$$\vec{F}_{1}=\frac{\mu_{0}}{4 \pi} \frac{q_1 q_{2}}{r^{2}} \vec{v}_1 \times\left(\vec{v}_{2} \times \frac{\vec{r}_{12}}{r}\right)$$
$$\vec{r}_{12}=\vec{r}_{1}-\vec{r}_{2}$$
$$r=\|\vec r_{12}\|$$
- $\frac{\mu_{0}}{4 \pi}=10^{-7} \mathrm{N} \cdot \mathrm{s}^{2} / \mathrm{C}^{2}$. 
- $\mu_0$ is the magnetic **permeability** of vacuum (universal constant). $\mu_{0} =4 \pi \times 10^{-7} \mathrm{N} \cdot \mathrm{s}^{2} / \mathrm{C}^{2}=4 \pi \times 10^{-7} \mathrm{Wb} \mathrm{A} \cdot \mathrm{m}=4 \pi \times 10^{-7} \mathrm{T} \cdot \mathrm{m} / \mathrm{A}$
- one can prove that $\vec F_1=-\vec F_2$ (Newton's third law)

Recall **cross product** of vectors![[Pasted image 20240306172152.png]]
## Magnetic Force Between Circuits
Force acting on circuit 2 caused by circuit 1

$$\mathbf{F}_{2}=\frac{\mu_{0}}{4 \pi} I_{1} I_{2} \oint_{1} \oint_{2} \frac{d \vec{l}_{2} \times\left[d \vec{l}_{1} \times\left(\vec{r}_{2}-\vec{r}_{1}\right)\right]}{\left|\vec{r}_{2}-\vec{r}_{1}\right|^{3}}$$

![[Pasted image 20240306172233.png]]
$\oint$ is the integral along the circuit (closed loop); $d \vec{l}$ is an infinitesimal length of wire, with direction given by the current density.
The previous expression simplifies when applied to two long parallel wires. The force per length of wire $L$ is simply $$\frac{F}{L}=\frac{\mu_{0} I I^{\prime}}{2 \pi r}$$
