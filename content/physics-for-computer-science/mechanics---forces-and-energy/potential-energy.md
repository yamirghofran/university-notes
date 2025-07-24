---
title: Potential Energy
---

- [Conservative Forces](/physics-for-computer-science/mechanics---forces-and-energy/conservative-forces)
We hence define the potential energy in each case as

| Gravitational potential energy                                                          | Elastic potential energy                                                        |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| $U_{\text {grav }}=m g y$                                                               | $U_{\mathrm{el}}=\frac{1}{2} k x^{2}$                                           |
| $W_{\text {grav }}=U_{\text {grav, } 1}-U_{\text {grav, } 2}=-\Delta U_{\text {grav }}$ | $W_{\mathrm{el}}=U_{\mathrm{el}, 1}-U_{\mathrm{el}, 2}=-\Delta U_{\mathrm{el}}$ |
| Potential energy increases as the body moves up                                         | Potential energy increases as the spring is stretched or compressed             |
| ![[Pasted image 20240306140057.png]]                                                    | ![[Pasted image 20240306140105.png]]                                            |

Remarks:
- Potential energy can be interpreted as a measure of the possibility for work to be done.
- Same units as work and kinetic energy.
- Gravitational potential energy is a shared property between the body and the earth

## Gradient force

A more systematic/mathematical way to define potential energy is when a force can be written as the gradient of another scalar function

$$\vec F=-\vec{\nabla} U=-\left(\frac{\partial U}{\partial x} \hat{\imath}+\frac{\partial U}{\partial y} \hat{\jmath}+\frac{\partial U}{\partial z} \hat{k}\right)$$

Then

$$W=\int \vec F\cdot d\vec r=\int -\vec{\nabla} U\cdot d\vec r=-\int dU=U_1-U_2$$

Hence we conclude

- any minimum in a potential-energy curve is a stable equilibrium position. Conversely, any maximum in a potential-energy curve is an unstable equilibrium position.
- a [conservative force](/physics-for-computer-science/mechanics---forces-and-energy/conservative-forces) always acts to push the system toward lower potential energy.


## Energy Diagrams
![[Pasted image 20240306140151.png]]