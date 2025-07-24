---
title: Work-energy Theorem
---

Let's combine [Newton's second law](/physics-for-computer-science/mechanics---forces-and-energy/newtons-laws-of-motion) with the definition of work

$$W=\int_{t_{1}}^{t_{2}} \mathbf{F} \cdot \mathbf{v} d t=m \int_{t_{1}}^{t_{2}} \mathbf{a} \cdot \mathbf{v} d t=\frac{m}{2} \int_{t_{1}}^{t_{2}} \frac{d v^{2}}{d t} d t=\frac{m}{2} \int_{v_{1}^{2}}^{v_{2}^{2}} d v^{2}=\frac{m v_{2}^{2}}{2}-\frac{m v_{1}^{2}}{2}$$

where we used the mathematical identity

$$\frac{d v^{2}}{d t}=\frac{d(\mathbf{v} \cdot \mathbf{v})}{d t}=\frac{d \mathbf{v}}{d t} \cdot \mathbf{v}+\mathbf{v} \cdot \frac{d \mathbf{v}}{d t}=2 \frac{d \mathbf{v}}{d t} \cdot \mathbf{v}=2 \mathbf{a} \cdot \mathbf{v}$$

Remarks

- The theorem informs us that a positive work increases the final speed of the particle compared to the initial speed.
- The theorem says nothing about the direction of the velocities, only changes in speed.
- Total work is a function of initial and final states of motion. It does not matter what happens in between
- As we used Newton's laws in deriving the theorem, it is valid only in an inertial frame of reference.
- The theorem is valid in general, regardless of particle trajectory or forces being constant or not. This generality comes in handy when solving certain problems that would be more difficult to solve using only Newton's law (avoiding solving differential equations for example). It is useful even for constant forces.