---
title: Mutual Inductance
---

So far we have considered isolated circuits. Let us now assume a collection of n circuits. The magnetic flux crossing the ith circuit is simply the sum of the contributions of all circuits (including itself).
$$\Phi_{i}=\Phi_{i 1}+\Phi_{i 2}+\cdots+\Phi_{i i}+\cdots+\Phi_{i n}=\sum_{j=1}^{n} \Phi_{i j}$$
where $\Phi_{i 1}$ symbolizes the flux crossing the ith circuit due to circuit 1 and so on. The induced emf is then
$$\mathcal{E}_{i}=-\frac{d \Phi_{i}}{d t}=-\left\{\frac{d \Phi_{i 1}}{d t}+\cdots+\frac{d \Phi_{i i}}{d t}+\cdots+\frac{d \Phi_{i n}}{d t}\right\}=-\sum_{j=1}^{n} \frac{d \Phi_{i j}}{d t}$$
If each of these circuits is stationary and rigid, the only changes in $\Phi_{ij}$ are due to the changes in the currents. Hence
$$\frac{d \Phi_{i j}}{d t}=\frac{d \Phi_{i j}}{d I_{j}} \frac{d I_{j}}{d t}$$
We define the mutual inductance $M_{ij}$
$$M_{i j}=\frac{d \Phi_{i j}}{d I_{j}}\:\:(i\neq j)$$
All in all, a changing current in a coil induces an emf in an adjacent coil, and the mutual inductance describes their coupling.

*Properties*:
- When the magnetic medium is **linear** (like vacuum), the mutual inductance is constant and current-independent, given by $$M_{ij}=\frac{\Phi_{i j}}{I_j}$$
- Mutual inductance is symmetric $M_{ij}=M_{ji}$
- SI units is the henry (same as self-inductance)
- Be careful: a steady current in one coil does not induce any current in a neighboring coil.
- Mutual inductance may become a severe nuisance in complex circuits, as variations in current in one circuit induce **unwanted emfs** in neighboring circuits. A good multi-circuit design tries to minimize their mutual inductance. 

*Applications*:
- A **transformer** is used in AC circuits to raise or lower voltages. The output voltage is determined by the mutual inductance.
- **Wireless charger**: for example, a electric toothbrush is charged thanks to a mutual inductance between the base, which contains a coil supplied with AC current from a wall socket, and a coil inside the toothbrush that is connected to a rechargeable battery.


## Example: long solenoid surronded by a coil
![[Pasted image 20240306215149.png]]
$$M=\frac{N_{2} \Phi_{B 2}}{i_{1}}=\frac{N_{2} B_{1} A}{i_{1}}=\frac{N_{2}}{i_{1}} \left(\frac{\mu_{0} N_{1} i_{1}}{l}\right) A=\frac{\mu_{0} A N_{1} N_{2}}{l}$$

