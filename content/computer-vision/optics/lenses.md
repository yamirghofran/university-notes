---
title: Lenses
weight: 1
---

All rays coming from a given object point get mapped to a single point in the image providing the object is at "focus".
- it captures much more light → good
- objects out of focus get blurred → bad

Lenses, like [Pinhole cameras](/computer-vision/optics/the-pinhole-camera), perform [perspective projection](https://grokipedia.com/page/3D_projection#perspective-projection).

## Snell's Law
Lenses are made of glass or plastic with refraction indexes much larger than air (~1).

![Slide2-Image Formation, p.21](../attachments/slide2-image-formation-p21-a0183a69.png)
[3B1B Video on Refraction Index](https://www.youtube.com/watch?v=KTzGBJPuJwM)

## Thin Conex Lens
Here's how a thin convex lens focuses multiple rays coming from a point in the object on a single point mapped in the image (resulting in a sharp bright image at the focused area).
![Slide2-Image Formation, p.22](../attachments/slide2-image-formation-p22-87bb57e9.png)
Tradeoff: the detector has to be at the exact right focal distance f, and if not, it will be blurry.

The equation that determines the ideal distance is:
![Slide2-Image Formation, p.22](../attachments/slide2-image-formation-p22-07d4cec5.png)

## Magnification in Lenses
[Magnification](/computer-vision/optics/magnification) is defined in the same manner as before: $$m = \frac{h_i}{h_o} = \frac{i}{o}$$
![Slide2-Image Formation, p.23](../attachments/slide2-image-formation-p23-4cb6a491.png)

See [[Slide2-Image Formation.pdf#page=25|proof]] here.

### Magnification in Two Lenses
When applying magnification in two lenses, their magnification factors get multiplied.$$m = m_1 \cdot m_2 = \frac{i_1}{o_1} \cdot \frac{i_2}{o_2}$$
![Slide2-Image Formation, p.26](../attachments/slide2-image-formation-p26-8ebce558.png)

## Focus in Lenses

> Aperture: diameter of the lense $D = f/N$ (could be defined by the F-number (N))

A point being in focus means that all rays hit the detector at a single point.
Out of focus means they hit detector at multiple points. (one single point will be mapped to a blurry circle)

There's a "plane of focus" and points not mapped one-to-one on it will be represented by a disk.

![Slide2-Image Formation, p.30](../attachments/slide2-image-formation-p30-fa6fa883.png)

The formula for calculating the blur circle diameter is:
![Slide2-Image Formation, p.30](../attachments/slide2-image-formation-p30-b9232c31.png)

Small apertures tend to behave like a pinhole (less light, less blur). In order to focus a defocused image, we can:
1. Move the object to the object plane
2. Move the image plane
3. Move the lens
4. Change the aperture
![Slide2-Image Formation, p.33](../attachments/slide2-image-formation-p33-984bef6d.png)