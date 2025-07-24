---
title: Capacitors
---

What is a capacitor? Essentially, two conductors separated by an insulator (or a vacuum).

In circuit diagrams a capacitor is symbolized by vertical lines representing the conductors
and the horizontal lines represent wires connected to either conductor.  

| ![[Pasted image 20240306145919.png]] | ![[Pasted image 20240306145925.png]] |
| ------------------------------------ | ------------------------------------ |

## Charging a Capacitor
Each conductor initially has zero net charge. Then a voltage transfers charge from one conductor to the other so that one has a negative charge and the other has an equal amount of positive charge. In this process, the electric field does some work to move the charges and create the potential difference between the conductors.
![[Pasted image 20240306150012.png]]
Such work must be stored somewhere. Where? in the electric field created between the conductors! An electric field stores energy, which will be important when we study electromagnetic waves.

A capacitor is therefore a device that stores electric **potential energy** but also **electric charge**.
## Capacitance
For a particular capacitor, the ratio of the charge on each conductor to the potential difference between the conductors is a constant, called the capacitance.

$$C=\frac{Q}{V_{a b}}$$
SI unit of capacitance: **farad** (F), in honor of Michael Faraday. $1 \mathrm{F}=1$ farad $=1 \mathrm{C} / \mathrm{V}=1$ coulomb/volt. $1 \mathrm{F}=1 \mathrm{C}^{2} / \mathrm{N} \cdot \mathrm{m}=1 \mathrm{C}^{2} / \mathrm{J}$

*Properties*
- The capacitance depends on the **geometry** of the capacitor and on the **insulator** between them.
- The greater the capacity, the greater the charge a capacitor accumulates for a fixed voltage. Hence, capacitance can be viewed as a measure of **how well a capacitor stores energy**. 
- One farad is a very large capacitance, as the following example shows. In many applications the most convenient units of capacitance are the microfarad $1 \mu \mathrm{F}=10^{-6} \mathrm{F}$ and picofarad $1 \mathrm{pF}=10^{-12} \mathrm{F}$

## The parallel-plate capacitor

The simplest capacitor is the parallel-plate capacitor, consisting of two parallel conducting plates, each with area A at a distance d. The separation between the plates is small compared to their dimensions, and so we shall assume that the electric .
![[Pasted image 20240306150203.png]]
The charges on the plates are uniformly distributed over their surfaces, thus by applying Gauss's law we find that $E=\frac{\sigma}{\epsilon_{0}}=\frac{Q}{\epsilon_{0} A}$. Additionally, for a uniform field we also have $V_{a b}=E d$. Combining both,

$$C=\epsilon_{0} \frac{A}{d}$$

## Other Important Types of Capacitors

| Spherical capacitor                                    | Cylindrical capacitor                                                   |
| ------------------------------------------------------ | ----------------------------------------------------------------------- |
| ![[Pasted image 20240306150250.png]]                   | ![[Pasted image 20240306150255.png]]                                    |
| $C=4 \pi \epsilon_{0} \frac{r_{a} r_{b}}{r_{b}-r_{a}}$ | $\frac{C}{L}=\frac{2 \pi \epsilon_{0}}{\ln \left(r_{b} / r_{a}\right)}$ |
See derivation on Sears-Zemansky's chapter 24.

## Potential Energy of a Capacitor
infinitesimal charge is $dW=V dq$, so $V dq=\frac{q dq}{C}$ in view of the definition of capacitance (remember, the capacitance $C$ does not change during the charging process, as it only depends on the physical characteristics of the capacitor). Thus

$$W=\int_{0}^{W} d W=\frac{1}{C} \int_{0}^{Q} q d q=\frac{Q^{2}}{2 C}$$

If we define the **potential energy** of an uncharged capacitor to be zero, then $U=W$ and

$$U=\frac{Q^{2}}{2 C}=\frac{1}{2} C V^{2}=\frac{1}{2} Q V$$
The **energy density** $u$, defined as energy per unit volume is then 

$$u=\frac{\frac{1}{2} C V^{2}}{A d}=\frac{1}{2} \epsilon_{0} E^{2}$$

## Dielectrics in Capacitors
In practice, capacitors contain dielectrics between the plates. This gives mechanical support for the whole configuration. Additionally, it increases the capacitance due to polarization: the electric field induces an opposite electric field inside the dielectric, which eventually decreases the voltage $V$ while keeping the charge $Q$ constant, thereby increasing the capacitance.

![[Pasted image 20240306150442.png]]
All our previous expressions remain the same by replacing $\epsilon_0\rightarrow\epsilon$

$$E=\sigma_{\mathrm{net}} / \epsilon_{0}=\frac{\sigma-\sigma_{\mathrm{i}}}{\epsilon_{0}}=\frac{\sigma}{\epsilon}$$
$$C=\epsilon_{r} C_{0}=\epsilon  \epsilon_{0} \frac{A}{d}=\epsilon \frac{A}{d}$$
$$u=\frac{1}{2} \epsilon E^{2}$$

## Dielectric Breakdown
No real dielectric remains an insulator for any electric field. High electric fields ionize the material, allowing conduction of charge: this is known as **dielectric breakdown**, and the magnitude of the field at which it occurs is the **dielectric strength** $E_m$. For dry air $E_m=3\times10^6 V/m$.

## Commercial Capacitors

| ![[Pasted image 20240306150611.png]] | ![[Pasted image 20240306150615.png]] |
| ------------------------------------ | ------------------------------------ |

See description of each type [here](http://www.learningaboutelectronics.com/Articles/Types-of-capacitors)

[https://youtu.be/X4EUwTwZ110](https://youtu.be/X4EUwTwZ110) - Capacitors explained.