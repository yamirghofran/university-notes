---
title: Electric Force
---

The electric force is a fundamental interaction between charged particles. Quantitatively, this force is determined by **Coulomb's law** (Experimental law discovered by Charles Augustin de Coulomb in the XVIII century),

$$\vec{F}_{1}=\frac{1}{4 \pi \epsilon_{0}} \frac{q_{1} q_{2}}{r_{12}^{2}} \frac{\vec{r}_{12}}{r_{12}}=\frac{1}{4 \pi \epsilon_{0}} \frac{q_{1} q_{2}}{r_{12}^{2}} \hat {r}_{12}$$
$$\vec{r}_{12}=\vec{r}_{1}-\vec{r}_{2}$$

where $q_1$,$q_2$ are **point charges**. $\mathbf{F}_{1}$ reads "force applied on $q_1$ by $q_2$".


| ![[Pasted image 20240306142138.png]] | ![[Pasted image 20240306142146.png]] |
| ------------------------------------ | ------------------------------------ |

What do we mean by a point charge? A point charge is a **model**: a charged object small enough to be considered a mathematical point in space (i.e. without internal structure).

$$\epsilon_{0}=8.854 \times 10^{-12} \mathrm{C}^{2} / \mathrm{N} \cdot \mathrm{m}^{2}$$

$$k=1 / (4 \pi \epsilon_{0})=8.987551787 \times 10^{9} \mathrm{N} \cdot \mathrm{m}^{2} / \mathrm{C}^{2} \cong 8.988 \times 10^{9} \mathrm{N} \cdot \mathrm{m}^{2} / \mathrm{C}^{2}$$

**Coulomb's constant** k is universal constant of nature. 
$\epsilon_0$ is the **vacuum permittivity**. Why do we define like that? it will simplify other formulas later on.
Some *properties*:

- Charges are supposed to be in **vacuum**. Electrically speaking, air is like vacuum.
- Magnitude of electric force is $F=k \frac{\left|q_{1} q_{2}\right|}{r^{2}}$, this is, proportional to the **squared inverse of the distance** between the charges. Experimentally tested to an accuracy of $10^{-16}$!!
- Most of everyday forces are the result of electric forces at the level of atoms and molecules, like the normal force, the tension force or the friction force.
- It obeys **Newton's third law**: the force applied on charge 1 by 2 is equal in magnitude and opposite in direction to the force applied on charge 2 by 1.
- Formally analogous to Newton's gravitation law.
- It satisfies the **superposition principle**: The net electric force applied on a charge is the __vector sum__ of all electric forces acting on it.
$$\mathbf{F}_{i}=q_{i} \sum_{j \neq i}^{N} \frac{q_{j}}{4 \pi \epsilon_{0}} \frac{\mathbf{r}_{i j}}{r_{i j}^{3}}$$

## Generalization to extensive bodies

Let us define the charge density per unit of area ($\sigma$) and the charge density per unit of volume ($\rho$) (think: are we allowed to do this? why?) to describe a **continuous** charge distributed within a volume or on a surface.

$$\rho=\lim _{\Delta V \rightarrow 0} \frac{\Delta q}{\Delta V}$$
$$\sigma=\lim _{\Delta S \rightarrow 0} \frac{\Delta q}{\Delta S}$$

Then, as a direct application of the superposition principle and the meaning of an integral, we have the force applied on charge q is


$$\vec{F}_q= \frac{q}{4 \pi \epsilon_{0}} \sum_{i=1}^{N} q_{i} \frac{\vec{r}-\vec{r}_{i}}{|\vec{r}-\vec{r}_{i}|^{3}}+\frac{q}{4 \pi \epsilon_{0}} \int_{V} \frac{\vec{r}-\vec{r}'}{|\vec{r}-\vec{r}'|^{3}} \rho\left(\vec{r}'\right) d V'\\
+\frac{q}{4 \pi \epsilon_{0}} \int_{S} \frac{\vec{r}-\vec{r}'}{|\vec{r}-\vec{r}'|^{3}} \sigma\left(\vec{r}'\right) d S'$$


$\vec{r}'$ is used to identify a point within the body.

![[Pasted image 20240306142306.png]]
