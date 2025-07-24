---
title: Electric Work
---

When an electric force $\vec{\mathbf{F}}$ acts on a particle moving from a to b, the **work** done **by the force** is a **line integral**
$$W_{a \rightarrow b}=\int_{a}^{b} \overrightarrow{\mathbf{F}} \cdot {d \vec{l}}=\int_{a}^{b} F \cos \phi d l$$
where $d \vec{l}$ is an infinitesimal displacement along the particle’s path and $\phi$ is the angle between $\vec{\mathbf{F}}$ and $d\vec{\mathbf{l}}$.

(Recall that **electric power** is then $P=\frac{dW}{dt}$)

When a charged particle moves in an electric field, the field exerts a force
that can do work on the particle.This work can always be expressed in terms of
electric **potential energy** (see next section).

Combining the general expression with the definition of the potential, $$W_{a \rightarrow b}=\int_{a}^{b} \overrightarrow{\mathbf{F}} \cdot {d \vec{l}}=\int_{a}^{b} F \cos \phi d l=-q\int_{a}^{b} \nabla V(\mathbf{r}) \cdot {d \vec{l}}=U_{a}-U_{b}=-\left(U_{b}-U_{a}\right)=-\Delta U$$
Conclusion: electric force is **conservative**: it only depends on the difference between the initial and final points.

## Special Cases

#### Work in a uniform electric field

$$W_{a \rightarrow b}=F d=q_{0} E d$$

#### Work in spherical field

$$W_{a \rightarrow b}=\int_{r_{a}}^{r_{b}} F_{r} d r=\int_{r_{a}}^{r_{b}} \frac{1}{4 \pi \epsilon_{0}} \frac{q q_{0}}{r^{2}} d r=\frac{q q_{0}}{4 \pi \epsilon_{0}}\left(\frac{1}{r_{a}}-\frac{1}{r_{b}}\right)$$



