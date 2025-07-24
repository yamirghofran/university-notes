---
title: Potential Energy
---

The previous scalar function U is the **electric potential energy**. 
$$U=q_0V$$
*Remarks*

- Remember: SI unit of energy is **Joule** (1 J).
- When the force does a positive work, the potential energy decreases.
- Only **a difference of potential energy** is really meaningful. We can always add up a constant. To give an absolute value, potential energy must be defined relative to some reference point where $U=0$. In circuits, this is called **ground**
- When working with atomic systems, it is useful to define another unit: a **electron volt** (1 eV); $1 \mathrm{eV}=1.602 \times 10^{-19} \mathrm{J}=e^-\times 1V$
## Reinterpreting the electric potential

The electric potential can then be interpreted as a **potential energy per unit charge**
$$V=\frac{U}{q_0}$$
and a voltage as a **work per unit charge**

$$\frac{W_{a \rightarrow b}}{q_{0}}=-\frac{\Delta U}{q_{0}}=-\left(\frac{U_{b}}{q_{0}}-\frac{U_{a}}{q_{0}}\right)=-\left(V_{b}-V_{a}\right)=V_{a}-V_{b}$$

And we find the following equivalence of units

$1 \mathrm{V}=1$ volt $=1 \mathrm{J} / \mathrm{C}=1$ joule/coulomb

## Energy in Uniform Fields
$$U=q_{0} E y$$
![[Pasted image 20240306144313.png]]

## Electric Potential Energy of Two Point Charges
By setting U to zero when two point charges $q$ and $q_0$ are infinitely far apart $r=\infty$, we have

$$U=\frac{1}{4 \pi \epsilon_{0}} \frac{q q_{0}}{r}$$

- The potential energy U given is a shared property of the two charges. In general, its a property of the charge configuration.
- The equation also holds if the test charge $q_0$ is outside a spherically symmetric charge distribution with net charge q; This is because Gauss’s law states us that the electric field outside such a distribution is the same as if all of its charge q were concentrated at its center.
- The energy of a collection of charges is the algebraic sum (energy is additive!) of each **pair** of charges.

$$U=\frac{1}{4 \pi \epsilon_{0}} \sum_{i<j} \frac{q_{i} q_{j}}{r_{i j}}$$