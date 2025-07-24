---
title: Faraday's Law
---

Faraday's law states that **a changing [Magnetic Flux](/physics-for-computer-science/electromagnetism/magnetic-flux) induces an [Electromotive Force (emf)](/physics-for-computer-science/electromagnetism/electromotive-force-emf)**. Namely, the induced emf in a closed loop equals the negative rate of change of magnetic flux through the loop.
$$\mathcal{E}=-\frac{d \Phi_{B}}{d t}=-\frac{d}{dt}\int \vec{{B}} \cdot d \vec{A}=-\frac{d}{dt}\int B d A \cos \phi$$
Generalization of a coil with N turns,

$$\mathcal{E}=-N \frac{d \Phi_{B}}{d t}$$

- Only a **dynamic flux** produces an emf, not a static flux.
- A dynamic flux is **not necessarily** produced by a dynamic magnetic field. The vector area $\vec A$ could also vary in time!
- Why the negative sign? It gives right the **direction** of the induced current.
- Experimental law that summarizes the experiments of Michael Faraday and Joseph Henry in the beginning of the XIX century.
- This law is at the heart of any electric generating station, which converts other forms of energy into electric energy(gravitational energy at hydroelectric plants, chemical energy in a coal-fired plant, or nuclear energy in a nuclear power plant) 

[https://youtu.be/Hh58afwzHfA](https://youtu.be/Hh58afwzHfA "Share link")

## How to find the direction of the emf
1. Fix direction of vector area $\vec A$.
2. In combination with the magnetic field, determine the sign of the magnetic flux (through the dot product $\vec{B} \cdot d \vec{A}$)
3. Determine the sign of the induced emf or current using Faraday's law: when the flux increases, the induced emf or current decreases and vice versa.
4. Finally, use the right-hand rule to determine the direction of the induced emf or current. For a positive emf, it is in thee same direction as your curled fingers, and negative otherwise.

![[Pasted image 20240306212202.png]]

## Induced Electric Field
We can understand the emf induced in a moving conductor based on Lorentz forces, but what drives the charges around the circuit when the conductor is still and there is only a changing magnetic flux?

Let us re-express Faraday's law using the definition of an emf
$$\oint_{C} \vec{E} \cdot d \vec{l}=-\frac{d}{d t} \int_{S} \vec{B} \cdot \vec{n} d A$$
There has to be **an induced electric field in the conductor caused by a changing magnetic flux**!

Remarks:
- Contrary to what we study for a static fields, this electric field does not fulfill $\oint_{C} \vec{E} \cdot d \vec{l}=0$, hence it is **not conservative** and the concept of potential is meaningless! Only when $\frac{d \Phi_{B}}{d t}=0$ we recover a conservative field $\vec E$. Nonetheless, **the definition $\vec F=q\vec E$ is always correct**.