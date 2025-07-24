---
title: Work
---

Some observations
- The stronger the [[Y1Q2/Physics for Computer Science/Mechanics - Forces & Energy/Forces|force]] we have to apply to move an object (imagine heavier and heavier objects), the harder it is for us to move it.
- The greater the displacement we want to move it, the harder

These intuitions are gathered in the concept of work.
For a constant force $\vec F$ and a displacement $\Delta\vec r$, we define work $W$ as

$$W=\vec F\cdot \Delta\vec r=F\Delta r\cos\theta$$
![[Pasted image 20240306135423.png]]

Remarks
- The SI unit of work is the joule, in honor of the English physicist James Joule). $$1 \mathrm{J}=1 \mathrm{N} \cdot \mathrm{m}$$
- Work is a scalar quantity
- when one body does negative work on a second body, the second body does an equal amount of positive work on the first body in virtue of Newton's third law.
- when you lift an object, you exert an upward force that results in the object moving upwards, so the work done by this force is positive. However, the work done by the gravitational force (its weight) is negative.
- when several forces act on the object, the total work done can be calculated as the sum of each work separately, or the work done by the net force on the object.
- In many situations the work is zero even though there are forces acting on the object. This could be due to
    - The displacement is zero. Holding a weight does not perform any work on the weight even though it takes us effort (our muscle fibers do work, and so you get tired).
    - Any force acting normally with respect to direction of displacement performs no work. Noticeable examples: 1) the normal force, 2) centripetal force in a circular motion 3) magnetic force.

## General definition

To include arbitrary forces and paths, we need to extend our previous definition of work. Let's consider a force that causes an infinitesimal displacement $d\vec r$. The infinitesimal work associated to such displacement is therefore $dW=\vec F\cdot d\vec r$. In general, the force will be a function of the position of the particle along the path $\vec F=\vec F(\vec r)$. The total work is calculated by adding up all the infinitesimal contributions.

$$W=\int dW=\int \vec F(\vec r)\cdot d\vec r$$

This is called a line or path integral.
![[Pasted image 20240306135504.png]]

## Example

$$W=\int \vec F(\vec r)\cdot d\vec r=\int \vec F(\vec r)\cdot \vec v dt$$

*Calculate the work done by a constant force on the plane xy acting on a particle moving on sinusoidal in the interval $[0,2\pi]$*

$\vec F=(F_x\hat i +F_y\hat j) \text{ (N)}$
$$\vec r(t)=(t\hat i+sin(t)\hat j) \text{ m} \implies \vec v(t)=(1\hat i+cos(t)\hat j)\text{ m/s}$$

$$W=\int_0^{2\pi} (F_x\hat i +F_y\hat j)\cdot (1\hat i+cos(t)\hat j) dt=\int_0^{2\pi} (F_x+F_ycos(t))dt=F_x2\pi \text{ (J)}$$
