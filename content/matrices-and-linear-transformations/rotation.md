---
title: Rotation
---

A **rotation** is a [linear transformation](/matrices-and-linear-transformations/linear-transformation) that rotates a vector or object by a certain angle around a fixed point or axis. In 2D, a rotation can be represented by a matrix:
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
where $\theta$ is the angle of rotation.
For example, rotating a vector $\begin{pmatrix} x \\ y \end{pmatrix}$ by an angle of $\theta$ counterclockwise results in:
$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}$$

