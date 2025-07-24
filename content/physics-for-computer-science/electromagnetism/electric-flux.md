---
title: Electric Flux
---

Electric flux $\Phi_{E}$ is essentially a measure of how much electric field flows though a certain surface. For a uniform electric field and a flat surface, the electric flux is

$$\Phi_{E}=|\vec E| A \cos \phi=\vec{E} \cdot \vec{A}=\vec E \cdot (A\hat n)$$

where $\phi$ is the angle between the electric field and the normal vector $\hat n$. $E\cos\phi$ is the perpendicular component of the electric field with respect to the surface. 

* A surface has two sides, so there will be two possible signs of the flux: positive when the electric field has a component along the normal, and negative otherwise. The limit case when the electric field is parallel to the surface produces a zero flux.
 

![[Pasted image 20240306143259.png]]

## General Expression
The way to generalize the previous expression to general electric fields and surfaces is to integrate the contribution of infinitesimal surfaces. Mathematically speaking, we are defining a **surface integral**.

$$\Phi_{E}=\int_S \vec E \cdot d \vec A=\int_S E \cos \phi dA$$
$$d \vec{A}=\hat{n} d A$$

- flux is a **scalar**
- This expression gives an **average** value of the perpendicular component of the electric field (multiplied by a factor: the area of the surface).
- The SI unit is $Nm^2/C$
