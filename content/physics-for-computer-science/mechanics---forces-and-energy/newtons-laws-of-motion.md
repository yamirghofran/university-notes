---
title: Newton's Laws of Motion
---

# Newton's First Law
**A body on which no net force is applied moves with constant velocity and zero acceleration.**

Only the net force is what matters. For example, no force at all is the same as two opposing forces acting on the same body (not to confuse with two opposing forces acting on two bodies!).

$$\sum F=\vec{F}_{1}+\vec{F}_{2}=\vec{F}_{1}+\left(-\vec{F}_{1}\right)=\vec 0$$

The tendency of a body to keep moving once it is set in motion is called **inertia**.
## Inertial frame of reference
The First law can be seen as a definition of a particular frame of reference. Essentially, the First law states that there exists a frame of reference in which a body does not require a force to remain in mo tion. This is an inertial frame of reference, in which the First law applies.

For instance, the frame inside an accelerating car is not a inertial frame.

In many situations we can safely assume that the earth is a good approximation to an inertial frame.

Pseudo forces or fictitious forces due to a non-inertial rotating frame:
- centrifugal force
- Coriolis force
- Euler force

![[Pasted image 20240306134653.png]]Centrifugal Forces

![[Pasted image 20240306134711.png]]Coriolis Forces
# Newton's Second Law
When an net external force is applied to a body, the body accelerates in the same direction as the force and proportional to it. The proportionality constant is the body inertial mass.
$$\vec F_{net}=\sum \vec{F}=m \vec{a}$$
Mass characterizes the inertial properties of a body. It turns out that the inertial mass coincides with the gravitational mass. We therefore do not distinguish between these two masses. Ultimately, the mass of a body is related to the number of particles it contains.

The SI unit of mass is the kilogram. Forces are measured in newtons $1 \mathrm{N}=1 \mathrm{kg} \cdot \mathrm{m} / \mathrm{s}^{2}$
![[Pasted image 20240306134805.png]]
![[Pasted image 20240306134811.png]]
Remarks:
- Newton's second law refers to external forces, which are those exerted on the body by other bodies (the environment of the body). A body cannot alter its own motion by means of inner forces: traditionally stated as 'you cannot lift yourself by pulling up your belt'.
- Newton's second law is valid only in inertial frames of reference, like the first law. Does it mean we cannot use it in non-inertial frames? Yes we can! but including also pseudoforces.
- Newton's law represents a fundamental basis to think causality in contrast to mere correlations.
## Common forces
* **Weight ($\vec w$)**. This is the force exerted by the Earth near the surface, which can be approximated as a **constant force**. Then we may write  ($\vec w=m\vec g$), where $\vec g$ is the constant acceleration caused by the force. $g=9.8 \mathrm{kg} \cdot \mathrm{m} / \mathrm{s}^{2}$
* **Elastic force** (springs, rubber-bands...). This is the force caused by a spring that wants to return to its natural length $l$. $\vec F=-k(\vec x-\vec l)$ ($k$ is the elastic constant).
* **Friction**. which is proportional to the normal force $\vec F_{fric}=\mu \vec N$.
* **Centrifugal force**. A pseudo force that directed radially outwards the rotation axis. The module is $F_{cf}=m\omega^2 r$, where $\omega$ is the angular velocity ($\vec\omega=\vec v\times\vec r$)
* **Fluid resistance**. $\vec F=-k\vec v$

## Variable mass

The previous statement of the Newton's second law is valid only when the mass remains constant while the force acts. There are many situations when this is not the case, like an accelerating rocket.

By introducing the linear momentum $\vec p=m\vec v$, the statement is modified as

$$\vec F_{net}=\frac{d\vec p}{dt}$$
# Newton's Third Law
**If body A exerts a force on body B (an "action”), then body B exerts a force on body A (a “reaction”) of equal magnitude and opposite direction.**

$$\vec{{F}}_{A \text { on } B}=-\vec{{F}}_{B \text { on } A}$$

Forces come in pairs ( action–reaction pair), but they act on different bodies!

![[Pasted image 20240306135027.png]]

Many times, the reaction is negligible when the mass A is much bigger than mass B, so only action matters. This happens, for instance, when we neglect the movement of the Earth caused by the attraction of an object.

## Conservation of linear momentum

The third law can be seen as a consequence of the conservation of linear momentum in a system composed of many particles. Say we have an isolated system $A$, composed of two subsystems $S_1$ and $S_2$

![[Pasted image 20240306135051.png]]

Newton's second law on A: $\vec F_{net\text { on } A}=\vec 0=m_{S_1}\vec a_1+m_{S_2}\vec a_2$.
But applying again Newton's law on $S_1$ and $S_2$, we conclude that $m_{S_1}\vec a_1=\vec{{F}}_{B \text { on } A}$ and $m_{S_2}\vec a_2=\vec{F}_{A \text { on } B}$, hence $\vec{{F}}_{A \text { on } B}=-\vec{{F}}_{B \text { on } A}$

This is a good example to start thinking in terms of layers of abstraction!