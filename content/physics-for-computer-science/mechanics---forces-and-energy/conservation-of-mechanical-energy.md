---
title: Conservation of Mechanical Energy
---

We have been able to calculate the total [Work](/physics-for-computer-science/mechanics---forces-and-energy/work) done by a force in two ways, by means of the [Work-energy Theorem](/physics-for-computer-science/mechanics---forces-and-energy/work-energy-theorem), and by the concept of [[Y1Q2/Physics for Computer Science/Mechanics - Forces & Energy/Potential Energy|Potential Energy]]. Let's equate both expressions
$$\Delta K=-\Delta U\implies K_2-K_1=U_1-U_2\implies K_1+U_1=K_2+U_2\implies E_1=E_2$$
The sum of kinetic energy and potential energy is **called mechanical energy**. The previous expression expresses the conservation  of mechanical energy $E$ in a system on which only conservative forces act.

When several conservative forces act all together, the total potential energy is simply the sum of each of the potential energies. For example $U=U_{\text {grav }}+U_{\text {el }}$.

The conservation of mechanical energy essentially tells us that movement, as an action or potential action, remains constant in an isolated system. The system stores potential movement in the form of [[Y1Q2/Physics for Computer Science/Mechanics - Forces & Energy/Potential Energy|Potential Energy]] and converts this energy in actual movement or [Kinetic Energy](/physics-for-computer-science/mechanics---forces-and-energy/kinetic-energy). The process is completely reversible between these two kinds of energies.

- Energy is measured in joules, same as work
- The kilowatt-hour is the usual commercial unit of electrical energy. The kilowatt-hour is a unit of work or energy, not power. $$1 \mathrm{kW} \cdot \mathrm{h}=\left(10^{3} \mathrm{J} / \mathrm{s}\right)(3600 \mathrm{s})=3.6 \times 10^{6} \mathrm{J}=3.6 \mathrm{MJ}$$
## Conservation of energy with non-conservative forces

In conservative systems, work is reversible between kinetic energy and potential energies. Energy stored in the system can later be withdrawn with no loss. In the presence of non-conservative forces this is no longer true, and energy is lost or gained.

Examples of dissipative forces leading to energy loss
- friction force. When the direction of the motion reverses, so does the friction force, hence it does negative work in both directions. There is no potential energy associated.
- fluid resistance is neither conservative for the same reasons.

There are also non-conservative forces that increase the mechanical energy, like the non-reversible chemical reactions

We must take into account the work done by these non-conservative forces to write

$$K_{1}+U_{1}+W_{\text {nc }}=K_{2}+U_{2}$$