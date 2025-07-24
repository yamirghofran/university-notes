---
title: Systematic Circuit Analysis
---


# Mesh Analysis
Leverage the linear characteristics of the elements to get equations that are linear combinations of the solutions obtained. 
1. Identify meshes in the circuit and assign then a mesh current (unknowns). 
2. Apply KVL as many times as unknowns are. 
3. Once the system of eq.s is solved, the net current in each branch will be the sum of mesh currents flowing through that branch.
asdfhjh jsadhfkjadh. jjh hh  
hello youssefffffffffffffffffffffffff
**Draw the mesh current you're considering in exams**. Not real currents.
![[Screenshot 2024-02-29 at 13.21.00.png]]

Voltage gain: negative. Voltage drop, positive.
Have to declare your direction of positive for each mesh.
$$\text{(mesh1) }I_1R_3 + (I_1-I_3)R_4 - V_a + (I_1 - I_2) R_2 = 0$$
$$\text{(mesh2)  }I_2R_1+(I_2-I_1)R_2+V_a+(I_2-I_3)R_5=0$$
$$\text{(mesh3)  }(I_3-I_2)R_5+(I_3-I_1)R_4+I_3R_6=0$$
The current flowing through $R_2$ would be $I_1-I_2$

- The number of independent equations satisfy `meshes = branches - nodes + 1`

plus to minus (voltage drop) therefore add
minus to plus (voltage gain) therefore subtract