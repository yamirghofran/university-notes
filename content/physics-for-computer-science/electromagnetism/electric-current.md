---
title: Electric Current
---

An electric current is simply a motion of electric charge in space, thus one could define it as a local variation of charge $Q(\vec x)$ in time.
$$I=\frac{d Q}{d t}$$
Intuitively, the charge in a certain region of space increases when there is current **flowing in** (so $dQ/dt>0$)

Alternatively, we could say that electric current is a **net flow of charge**. Mathematically,  we define the current as the net charge flowing through a cross-sectional area per unit time. 

| ![[Pasted image 20240306171413.png]] | $d Q=q\left(n A v_{\mathrm{d}} d t\right)$ |
| ------------------------------------ | ------------------------------------------ |
Hence, $$I=\frac{d Q}{d t}=n q v_{\mathrm{d}} A$$
* $n$: concentration of particles per unit volume ($m^{-3}$)
* $v_{\mathrm{d}}$: velocity of the particles ($m/s$) 
* $A$ cross-sectional area ($m^2$)
* $q$ charge of a single particle.


*Remarks*
- Current is not a vector quantity, but a **scalar** quantity. 
- The SI unit of current is the **ampere**, in honor of André Marie Ampère (1775–1836), defined as one coulomb per second $1 \mathrm{A}=1 \mathrm{C} / \mathrm{s}$
- When the charge is constrained to follow a conducting path, it is called an **electric circuit**. In a circuit, current is always along the length of the wire, regardless of its shape.
- Electric currents move **energy** in space.  Electric circuits are therefore useful to transport energy in a controlled fashion.
- Electric currents are everywhere: computers, biological nervous systems, global atmospheric electrical circuit...
- In normal DC circuits, currents are of the order of milliamperes ($1mA=10^{-3}A)$ or ($1\mu A=10^{-6}A)$. Currents for engines, machinery, etc, in the ampere range. Current in computer circuits, in the range of nanoamperes ($1nA=10^{-9}A)$ or picoamperes ($1pA=10^{-12}A)$.
-  A conductor may contain different kinds of moving charged particles with different signs (electrons, positive ions, holes...), but all of the **add up** to the net current.
- Current is not used up or along the circuit, but energy is!


## Vector Current Density
Knowing what the current is, alternative ways to define the vector current density are $$\vec{J}=n q \vec v_{\mathrm{d}}$$
$$|\vec J||=\frac{I}{A}$$
$$I=\int_{S} \vec{J} \cdot \vec{n} d S$$
*Properties*
- Current density is a **vector**! even though the current is a scalar. 
- SI unit is $A/m^2$
- Its direction indicates the **conventional** flow of charge, and its magnitude the current per unit surface.
- Bearing in mind the expression for the electric flux, current would be like the flux for the current density.

## Model of Metallic Conduction
Free electrons move randomly in a conductor, like a **gas** made of electrons, travelling at $\approx 10^6m/s$. Nonetheless, there is no net flow of charge in any direction.

Now suppose we establish a constant field $\vec E$ inside the conductor, so the electrons will experience a constant force $\vec F=q\vec E$. In free space, this force would cause that particles to describe a uniformly accelerated linear motion; however, electrons frequently collide with the positive ions of the conductor. In each collision the direction randomly changes, but there is also a very slow net motion or drift, described by the **drift velocity**  $\vec v_{\mathrm{d}}$ on the order of $\approx 10^{-4}m/s$. In a circuit, the electric field (which travels at the speed of light) is established along the circuit almost immediately, that's why electrons start to move all along the wire at very nearly the same time. The electric force then does a work on the moving charges. Part of the kinetic energy is transferred to the conductor through collisions, causing ions in the conductor to vibrate (perceived as the conductor heating up). 

![[Pasted image 20240306171626.png]]

- if q is positive $\vec v_{\mathrm{d}}$ lies in the same direction as $\vec E$
- if q is negative $\vec v_{\mathrm{d}}$ is in the opposite direction as $\vec E$
- In both cases $\vec{J}$ shares direction with  $\vec E$

[https://youtu.be/8Posj4WMo0o](https://youtu.be/8Posj4WMo0o "Share link")

