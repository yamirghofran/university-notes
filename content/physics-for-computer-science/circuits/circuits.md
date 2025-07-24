---
title: Circuits
---

- **Circuit**: a interconnection of electric devices.
- **Electric component**: characterized by voltage-current relation among terminals, called **characteristic curve**.
    - pasive
    - active
- **Terminal**:endpoint of an electric component
    - two-terminal devices: resistance, capacitor, coil...
    - tree-terminal devices: transistors, rely, some switches..
- **Connection**: ideal wire with zero resistance.
- **Node/junction**: any point on a circuit where the terminals of two or more circuit elements meet.
- **Ground**: a reference node, at which the potential is 0.
- **Branch**: any path between two nodes without nodes in between.
- **Loop**: any closed path in a circuit.
- **Mesh**: a loop that does not enclose other loops.

![[Pasted image 20240306220616.png]]
4 meshes and **3** nodes (A, B, O)

![[Pasted image 20240306220631.png]]



## Types of Circuits
- **DC current**: direction of current remains constant.
- **AC current**: current oscillates.

- **linear**: all components have linear characteristic curve. Given a linear combination of input voltages vi=Avi1+Bvi2vi=Avi1+Bvi2, the output is also a linear combination vo=Af(vi1)+Bf(vi2)v�=A�(vi1)+B�(vi2)
- **non-linear**: some components are non-linear.

**Circuit analysis**: given a circuit, calculate voltage or currents at some node or branch.

**Circuit design**: given an input-output relation, combine electronic devices fulling such requirement.