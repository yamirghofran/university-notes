---
title: Shader
---

A small program that can be installed on and runs on the Graphics Processing Unit ([GPU](/computer-architecture-network-technology-and-operating-systems/architecture/gpu)) to calculate and define the visual appearance of 2D or 3D graphics in a computer system. Shaders are a crucial component of the graphics pipeline and play a key role in determining the final image that is displayed on the screen.

- **Vertex Shader**: A vertex shader is responsible for transforming 3D vertices into screen space. It takes the vertex data as input, applies transformations, and outputs the transformed vertex.
- **Fragment Shader** (also known as Pixel Shader): A fragment shader is responsible for calculating the final color of a pixel. It takes the output from the vertex shader as input and outputs the final color of the pixel.

- Vertex and fragment operation specified in small (macro) [Assembly](/computer-architecture-network-technology-and-operating-systems/architecture/assembly) language.
- User-specified mapping of input data to operations.
- Limited ability to use intermediated computed values to index input data.

![](../attachments/cleanshot-2025-02-08-at-1844062x.png)