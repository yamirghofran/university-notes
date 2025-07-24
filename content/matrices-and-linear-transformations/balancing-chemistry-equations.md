---
title: Balancing Chemistry Equations
---

## Rules
A balanced chemical equation is an algebraic representation that shows the relative number of molecules (or moles) of each substance involved in a reaction. Ensure the same number of atoms for each element on both sides of the equation, as required by the law of conservation of mass.
$$
\text{NH}_3 + \text{O}_2 \rightarrow \text{N}_2 + \text{H}_2\text{O}
$$

## To solve it
1. Assign variables to represent the coefficients of each substance.
2. Write one equation for each element, ensuring the total number of atoms is the same on both sides.
3. Solve the equations to find the values of the variables.
4. Adjust to the smallest whole-number integer combination of variables to represent the reaction.

## Example 1
Find balanced chemical equation for this reaction

$$
\text{H}_2 + \text{O}_2 \rightarrow \text{H}_2\text{O}
$$

### Solution:

$$
x\text{H}_2 + y\text{O}_2 \rightarrow z\text{H}_2\text{O} \quad x, y, z \text{ unknowns} \in \mathbb{Z} \quad \min(\text{combination}(x, y, z))
$$

**Hydrogen**: \(2x = 2z\)  
**Oxygen**: \(2y = z\)

$$
\begin{cases} 
2x - 2z = 0 \\ 
2y - z = 0 
\end{cases}
$$

$$
\begin{pmatrix} 
2 & 0 & -2 \\ 
0 & 2 & -1 
\end{pmatrix}
\begin{pmatrix} 
x \\ 
y \\ 
z 
\end{pmatrix}
=
\begin{pmatrix} 
0 \\ 
0 
\end{pmatrix}
$$

Using RREF:

$$
\begin{pmatrix} 
2 & 0 & -2 & | & 0 \\ 
0 & 2 & -1 & | & 0 
\end{pmatrix}
\rightarrow
\begin{pmatrix} 
1 & 0 & -1 & | & 0 \\ 
0 & 1 & -\frac{1}{2} & | & 0 
\end{pmatrix}
$$

$$
x - z = 0 \quad \Rightarrow \quad x = z
$$

$$
y - \frac{1}{2}z = 0 \quad \Rightarrow \quad y = \frac{1}{2}z
$$

Solutions: $((x, y, z) = (z, \frac{1}{2}z, z) = (c, \frac{1}{2}c, c) \rightarrow \min(x, y, z) = (2, 1, 2))$

$$
\boxed{2\text{H}_2 + \text{O}_2 \rightarrow 2\text{H}_2\text{O}}
$$
## Example 2

Combustion of ammonia in oxygen produces nitrogen and water. Find balanced chemical equation for this reaction.

$$
\text{NH}_3 + \text{O}_2 \rightarrow \text{N}_2 + \text{H}_2\text{O}
$$
$$
w\text{NH}_3 + x\text{O}_2 \rightarrow y\text{N}_2 + z\text{H}_2\text{O}
$$

**Nitrogen**: $(w = 2y)$
**Oxygen**: $(2x = z)$
**Hydrogen**: $(3w = 2z)$

Equations:

$$
\begin{cases} 
w - 2y = 0 \\ 
2x - z = 0 \\ 
3w - 2z = 0 
\end{cases}
$$

Matrix form:

$$
\begin{pmatrix} 
1 & 0 & -2 & 0 & | & 0 \\ 
0 & 2 & 0 & -1 & | & 0 \\ 
0 & 0 & 6 & -2 & | & 0 
\end{pmatrix}
\rightarrow
\begin{pmatrix} 
1 & 0 & 0 & -\frac{2}{3} & | & 0 \\ 
0 & 2 & 0 & -1 & | & 0 \\ 
0 & 0 & 6 & -2 & | & 0 
\end{pmatrix}
\rightarrow
\begin{pmatrix} 
1 & 0 & 0 & -\frac{2}{3} & | & 0 \\ 
0 & 1 & 0 & -\frac{1}{2} & | & 0 \\ 
0 & 0 & 1 & -\frac{1}{3} & | & 0 
\end{pmatrix}
$$

Solutions:

$$
(w, x, y, z) = \left(\frac{2}{3}z, \frac{1}{2}z, \frac{1}{3}z, z\right) = \left(\frac{2}{3}c, \frac{1}{2}c, \frac{1}{3}c, c\right), \quad c \in \mathbb{R}
$$

Minimum integer combination:

$$
(w, x, y, z) = (4, 3, 2, 6)
$$

Balanced equation:

$$
\boxed{4\text{NH}_3 + 3\text{O}_2 \rightarrow 2\text{N}_2 + 6\text{H}_2\text{O}}
$$