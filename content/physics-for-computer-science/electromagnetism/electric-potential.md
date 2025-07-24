---
title: Electric Potential
---

The inverse squared dependency of the electric force is crucial, as it allows as to write the electric field as the **gradient** a scalar field: the **electric potential** $V$ (also frequently denoted by $\varphi$)

$$\vec{E}(\vec{r}) = -\nabla V(\vec{r})$$
This equation thus implies $$V_{a}-V_{b}=\int_{a}^{b} \vec E \cdot \vec{d l}=\int_{a}^{b} E \cos \phi d l$$
*Properties*
- minus sign for convenience 
- Since the electric field satisfies the **superposition principle**, and being nabla a linear operator, the electric potential fulfills superposition.

$$V=V_1+V_2+V_3+\dots$$

- the SI unit is one **volt**  (1V) in honor of Alessandro Volta.
- Alternative SI unit for electric field: volt per meter $1 \mathrm{V} / \mathrm{m}=1 \mathrm{N} / \mathrm{C}$
- In circuits, a difference in potential from one point to another is often called **voltage**.

## Calculating Electric Potentials
The potential of a point charge located at $\vec{r}'$ is simply
$$V(\vec{r})=\frac{1}{4 \pi \epsilon_{0}} \frac{q_{1}}{|\vec{r}-\vec{r}'|}$$

Invoking the superposition principle, any potential can be calculated as sum (integral) of contributions.

$$
V(\vec{r})= \frac{1}{4 \pi \epsilon_{0}} \sum_{i=1}^{N} \frac{q_{i}}{|\vec{r}-\vec{r}_{i}|}+\frac{1}{4 \pi \epsilon_{0}} \int_{V} \frac{\rho\left(\vec{r}^{\prime}\right)}{|\vec{r}-\vec{r}^{\prime}|} d V^{\prime}\\
+\frac{1}{4 \pi \epsilon_{0}} \int_{S} \frac{\sigma\left(\vec{r}^{\prime}\right)}{|\vec{r}-\vec{r}^{\prime}|} d S^{\prime}$$

## Simple Cases
| Charged cylinder                                       | Charged ring                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------- |
| ![[Pasted image 20240306143852.png]]                   | ![[Pasted image 20240306143859.png]]                          |
| $V=\frac{\lambda}{2 \pi \epsilon_{0}} \ln \frac{R}{r}$ | $V=\frac{1}{4 \pi \epsilon_{0}} \frac{Q}{\sqrt{x^{2}+a^{2}}}$ |

Read and understand the derivation by yourself: Sears & Zemansky examples 23.10, 23.11

## Equipotential Lines
A equipotential surface is an imaginary surface such that the electric potential $V$ is **constant** over it.

*Examples*
![[Pasted image 20240306143941.png]]

*Properties*:
* Field lines and equipotential surfaces are always **perpendicular** to each other.
* $E$ doesn't have to be constant over an equipotential surface.
* The larger the electric field, the closer the equipotential surfaces are.
* The surface of a **conductor** *in equilibrium* is always an equipotential surface. Actually, all the volume is equipotential. 
    * This follows from the fact that **the electric field is always perpendicular to the surface of a conductor**.