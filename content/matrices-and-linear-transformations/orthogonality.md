---
title: Orthogonality
---

# Orthogonal Vectors
Two vectors are **orthogonal** if angle between vectors is 90 degrees.
![](../attachments/cleanshot-2025-03-25-at-1128342x.png)
## Example
![](../attachments/cleanshot-2025-03-25-at-1128512x.png)
## Exercise
- Find a vector $\mathbf{u}$ (no zero vector) where $\text{Angle} (\mathbf{u}, \mathbf{v}) = 90^\circ$ and $\mathbf{v} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$.
	- ![](../attachments/cleanshot-2025-03-25-at-1130112x.png)
# Orthogonal Subspaces
Subspace S is orthogonal to subspace T ($T = S^\perp$), means every vector in S is orthogonal in T.
![](../attachments/cleanshot-2025-03-25-at-1133092x.png)
Orthogonality is impossible when dim(S) + dim(T) > dim(whole space)
![](../attachments/cleanshot-2025-03-25-at-1135342x.png)
# Orthogonal Matrix
A matrix orthogonal with [Orthonormal](/matrices-and-linear-transformations/orthonormal-vectors) columns is assigned special letter Q.

$$Q^T Q = \begin{pmatrix} \vdots & \mathbf{q}_1^T & \vdots \\ \vdots & \mathbf{q}_n^T & \vdots \end{pmatrix} \begin{pmatrix} \vert & & \vert \\ \mathbf{q}_1 & \cdots & \mathbf{q}_n \\ \vert & & \vert \end{pmatrix} = I$$
If Q is square matrix $Q^T Q = I$ tells us that $Q^T=Q^{-1}$

## Example
![](../attachments/cleanshot-2025-03-25-at-1221072x.png)
![](../attachments/cleanshot-2025-03-25-at-1221192x.png)

