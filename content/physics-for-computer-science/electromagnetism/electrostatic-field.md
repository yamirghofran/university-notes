---
title: Electrostatic Field
---

A different way to think forces: a charge $q$ modifies the space around it, and other charges can sense it. We say that a charge creates a electric field $\vec{E}_0$ at point $\vec{r}$. This electric field is present at $\vec{r}$ even if there is no charge at $\vec{r}$. When we place another charge $q_0$ at $\vec{r}$ (called __test charge__), it experiences a force $\vec{F}_0$ such that $$\vec{F}_{0}=q_{0} \vec{E}_0$$
![[Pasted image 20240306142416.png]]

Mathematically, the electric field is then defined as a limit whereby the test charge goes to zero.
$$\vec{E}=\lim _{q \rightarrow 0} \frac{\vec{F}_{q}}{q}$$
The concept of field will be crucial to avoid "action-at-a-distance" force. Instead, fields that propagate in space and time (electromagnetic waves).

*Properties*:

- The electric field is a **vector field**, this is, a function $\vec E(\vec r): \mathbb{R}^3\rightarrow\mathbb{R}^3$ (like the velocity of a fluid)
- The sign of the electric field does not depend on the sign of the test charge, only on the **source charge**.
- Analogous to the gravity field $\vec{F}_{g}=m_{0} \vec{g}$ per unit of mass.
- The expression $\vec{F}_{0}=q_{0} \vec{E}_0$ is valid only for **point charges**.
- **Superposition principle** is equally valid for the electric field.
- SI units: N/C

## Electric Field Lines
An electric field line is an imaginary curve such that its tangent at any point gives the direction of the electric-filed at that point.

| ![[Pasted image 20240306142648.png]] | ![[Pasted image 20240306142643.png]] |
| ------------------------------------ | ------------------------------------ |
*Properties*:
- their **spacing** represents the magnitude of the electric field: the closer the lines, the stronger the field.
- At any given point the electric field is unique, hence field lines **never intersect**.
- A field line does **not** illustrate the trajectory of a point charge upon the electric field (except for uniform fields).

## Some Sources of Electric Field

### Electric Field of a Point Charge
As a direct consequence of Coulomb's law, we have

$$\vec{E}=\frac{1}{4 \pi \epsilon_{0}} \frac{q}{r^{2}} \hat{r}$$

|                                      |                                      |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20240306142823.png]] | ![[Pasted image 20240306142813.png]] |

It has **spherical symmetry**.

### Uniform Field
Electric field between two parallel conducting plates
$$\vec E(\vec r)=\vec E_0$$
![[Pasted image 20240306142904.png]]


### Electric Field Inside a Conductor
The electric field in a conductor is identically **zero**. _Proof by reductio ad absurdum_: Assume there exists an electrostatic field inside the conductor. Thus, there appears an electric force acting on the charges inside the conductor. As charges can move freely within the conductor, they experience a net motion and so the electric field will change. Nevertheless, we first stated that the field is static! Therefore, we conclude that the electric field must be zero at any point. (Caution: there still could be electric field in a hole inside the conductor!)

## How to calculate electric fields?

One can always rely on the superposition principle since $\vec{E}=\frac{\vec{F}}{q_{0}}=\vec{E}_{1}+\vec{E}_{2}+\vec{E}_{3}+\dots$. Thus

$$\begin{aligned}
\mathbf{E}(\mathbf{r})=& \frac{1}{4 \pi \epsilon_{0}} \sum_{i=1}^{N} q_{i} \frac{\mathbf{r}-\mathbf{r}_{i}}{\left|\mathbf{r}-\mathbf{r}_{i}\right|^{3}}+\frac{1}{4 \pi \epsilon_{0}} \int_{V} \frac{\mathbf{r}-\mathbf{r}^{\prime}}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|^{3}} \rho\left(\mathbf{r}^{\prime}\right) d v^{\prime} \\
&+\frac{1}{4 \pi \epsilon_{0}} \int_{S} \frac{\mathbf{r}-\mathbf{r}^{\prime}}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|^{3}} \sigma\left(\mathbf{r}^{\prime}\right) d a^{\prime}
\end{aligned}$$
## Important simple cases


| Charged line segment                                                                            | Ring of charge                                                                                   | Uniformly charged disk                                                                                     | Two oppositely charged infinite sheets                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![[Pasted image 20240306143044.png]]                                                            | ![[Pasted image 20240306143051.png]]                                                             | ![[Pasted image 20240306143101.png]]                                                                       | ![[Pasted image 20240306143109.png]]                                                                                                                                                                 |
| $\vec{E}=\frac{1}{4 \pi \epsilon_{0}} \frac{Q}{x \sqrt{x^{2}+a^{2}}} \hat{\boldsymbol{\imath}}$ | $\vec{E}=\frac{1}{4 \pi \epsilon_{0}} \frac{Q x}{\left(x^{2}+a^{2}\right)^{3 / 2}} \hat{\imath}$ | $\vec{E}=\frac{\sigma}{2 \epsilon_{0}}\left[1-\frac{1}{\sqrt{\left(R^{2} / z^{2}\right)+1}}\right]\hat{k}$ | $\vec{E}=\left\{\begin{array}{ll}0 & \text { above the upper sheet } \\ \frac{\sigma}{\epsilon_{0}} \hat{j} & \text { between the sheets } \\ 0 & \text { below the lower sheet }\end{array}\right.$ |
Read carefully section 21.5 from Sears and Zemansky's for detailed derivation.
