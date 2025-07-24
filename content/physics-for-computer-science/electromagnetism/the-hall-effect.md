---
title: The Hall Effect
---

  Let's apply a magnetic field on a conductor in the form of a flat strip.

| ![[Pasted image 20240306210041.png]] | ![[Pasted image 20240306210046.png]] |
| ------------------------------------ | ------------------------------------ |

1. The magnetic field deviates the trajectory of electrons causing accumulation at one of the edges of the strip, leaving an excess positive charge at the opposite edge.
2. Accumulation continues until the resulting transverse electrostatic field is large enough to counteract the external magnetic field.
3. The final electric field implies there exists a potential difference between the opposite edges of the strip (distance $d$), called the **Hall voltage** or **Hall emf**.

Consider figure b), a positive charge $e$ moving along the positive x-axis ($v_{\mathrm{d}}>0$). The magnetic field is along positive y ($B_{y}>0$), while the electrostatic field is along negative x ($E_{z}<0$).

$$e E_{z}+e v_{\mathrm{d}} B_{y}=0$$
$$J_{x}=n e v_{\mathrm{d}}$$,

Consider figure a), a negative charge $-e$ moving along the negative x-axis ($v_{\mathrm{d}}<0$). The magnetic field is along negative y ($B_{y}<0$), while the electrostatic field is along positive x ($E_{z}<0$).

$$-e E_{z}-e v_{\mathrm{d}} B_{y}=0$$
$$J_{x}=-n e v_{\mathrm{d}}$$,

Both situations can be summarized as follows

$$q E_{z}+q v_{\mathrm{d}} B_{y}=0$$
$$J_{x}=n q v_{\mathrm{d}}$$

Then

$$n q=\frac{-J_{x} B_{y}}{E_{z}}=\frac{-J_{x} B_{y} d}{V_{ab}}$$

*Remarks*
* The sign of the Hall voltage crucially depends on the sign of the charge carriers: $V_{ab}>0$ for electrons.
* Discovered by the American physicist Edwin Hall in 1879

[https://youtu.be/wpAA3qeOYiI](https://youtu.be/wpAA3qeOYiI "Share link") - Hall Effect
[https://youtu.be/42qNfPOYlR8](https://youtu.be/42qNfPOYlR8) - Hall Effect sensors for Arduino
