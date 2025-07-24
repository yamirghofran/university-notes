---
title: Forces
---

A force is an interaction between bodies described mathematically by a vector and measured in Newtons (N). 

- [Newton's Laws of Motion](/physics-for-computer-science/mechanics---forces-and-energy/newtons-laws-of-motion)
- [Free Body Diagrams](/physics-for-computer-science/mechanics---forces-and-energy/free-body-diagrams)
- [Equilibrium](/physics-for-computer-science/mechanics---forces-and-energy/equilibrium)

Types:
* Contact forces. A force between bodies in contact. Interactions are modeled with a step function ($\theta(r-a)$).
    - Normal force, acting perpendicular on the surface
    - friction force, acting parallel to the surface
    - Tension force, caused by a stretched body (inner elastic forces)
* Short-range interactions. When the interaction decays exponentially with the distance ($\propto \exp{-\lambda r}$). They weaken very rapidly, so they are 'first-neighbors' interactions.
    - Nuclear forces
    - Ising model
* Long-range interactions. The interaction decays with a power law ($r^{-n}$). Forces act 'at a distance' so to speak.
    - Gravitation
    - Electromagnetic forces

## Superposition Principle

Multiple forces applied at the same point on a body have the same effect as a single force equal to the vector sum of the forces. This single force is called **net force**.

$$\vec{F}_{net}=\vec{F}_{1}+\vec{F}_{2}+\vec{F}_{3}+\cdots=\sum \vec{F}$$

$$F_{net,x}=\sum F_{x} \quad\quad F_{net,y}=\sum F_{y} \quad\quad F_{net,z}=\sum F_{z}$$
Free-body diagrams

A free-body diagram consists of the following elements:
* A representation of the body on which Newton's laws are applied.
* All the individual **external** forces acting **on** the body
* A coordinate system (conveniently chosen)
* accelerations can be included if needed as well.

When a problem involves more than one body, we can always draw a separate free-body diagram for each body
