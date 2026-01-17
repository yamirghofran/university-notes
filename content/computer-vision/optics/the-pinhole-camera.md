---
title: The Pinhole Camera
weight: 1
---

Simplest camera (basically just a small hole in a wall).

Pinhole cameras perform [perspective projection](https://grokipedia.com/page/3D_projection#perspective-projection).
![Slide2-Image Formation, p.3](../attachments/slide2-image-formation-p3-40a59d0b.png)
Each point in the scene gets mapped to one single point in the image.

![Slide2-Image Formation, p.4](../attachments/slide2-image-formation-p4-9acbcafe.png)
The size of the object in the image plane depends on the **focal length** and the **distance of the object to the pinhole**.

Using similar triangles, and with the image plane located at
![](../attachments/pasted-image-20260117121025.png)

A 3D straight line is also a straight line in the 2D image plane because the intersection of two planes (image plane and the plane formed by the straight line and the pinhole) is a straight line.
![Slide2-Image Formation, p.6](../attachments/slide2-image-formation-p6-72ed4f6c.png)
![Slide2-Image Formation, p.6](../attachments/slide2-image-formation-p6-ef15f578.png)

## Pinhole Size
In theory, the pinhole size sould be as small as possible because we want each point in the object be uniquely mapped to a single point in the image.
If the pinhole is too large, several rays of light for a point get through and the image gets blurry.

However, if the hole is too small, it will result in **diffraction** where the image also gets blurry.
![Slide2-Image Formation, p.16](../attachments/slide2-image-formation-p16-8e71ef2c.png)

The ideal pinhole diameter is:
![Slide2-Image Formation, p.16](../attachments/slide2-image-formation-p16-404ee59d.png)
This expression leverages the geometric blur caused by large diameters (proportional to d) with the blur caused by diffraction (proportional to $f\lambda/d$). $\lambda$ for visible light is roughly 550nm.