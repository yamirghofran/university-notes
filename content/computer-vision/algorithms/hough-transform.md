---
title: Hough Transform
---

## Overview

The Hough Transform detects parameterized shapes (lines, circles) by mapping image points to parameter space and finding peaks.

## Key Idea

- Each point in image space votes for all possible shapes that could pass through it
- Shapes are detected as peaks (accumulators) in parameter space

---

## Line Detection

### Problem with $y = mx + c$ representation

- $m$ can be infinite (vertical lines)
- Not computer-friendly

### Better Parameterization: Normal Form

$$x \cos\theta + y \sin\theta = \rho$$

Where:

- $\rho$ = perpendicular distance from origin to line
- $\theta$ = angle of perpendicular from origin to line
- Constrained: $0 \leq \theta < \pi$, $-\rho_{max} \leq \rho \leq \rho_{max}$

---

## Standard Hough Transform for Lines - Pseudocode

```
Algorithm HoughTransformLines(edges, rho_resolution, theta_resolution, threshold)
Input:
    - edges: binary edge image (output of Canny detector)
    - rho_resolution: discretization step for ρ (e.g., 1 pixel)
    - theta_resolution: discretization step for θ (e.g., 1 degree = π/180)
    - threshold: minimum votes to consider a line

Output:
    - lines: list of detected lines as (ρ, θ) pairs

// ============================================
// INITIALIZATION
// ============================================
1. rows, cols ← edges.shape
2.
3. // Calculate ρ range
4. ρ_max ← SQRT(rows² + cols²)
5. ρ_min ← -ρ_max
6.
7. // Create accumulator array
8. num_ρ ← CEIL((ρ_max - ρ_min) / rho_resolution)
9. num_θ ← CEIL(π / theta_resolution)
10. accumulator ← ZEROS(num_ρ, num_θ)

// ============================================
// VOTING
// ============================================
11. // For each edge pixel
12. FOR y = 0 TO rows-1 DO:
13.     FOR x = 0 TO cols-1 DO:
14.         IF edges[y, x] == 1 THEN:           // If edge pixel
15.
16.             // Vote for all possible θ values
17.             FOR θ_idx = 0 TO num_θ-1 DO:
18.                 θ ← θ_idx × theta_resolution
19.
20.                 // Calculate ρ for this (x, y, θ)
21.                 ρ ← x × COS(θ) + y × SIN(θ)
22.
23.                 // Quantize ρ to accumulator index
24.                 ρ_idx ← ROUND((ρ - ρ_min) / rho_resolution)
25.
25.                 // Cast vote
26.                 accumulator[ρ_idx, θ_idx] += 1
27.             END FOR
28.         END IF
29.     END FOR
30. END FOR

// ============================================
// PEAK DETECTION
// ============================================
31. lines ← EMPTY_LIST

32. FOR ρ_idx = 0 TO num_ρ-1 DO:
33.     FOR θ_idx = 0 TO num_θ-1 DO:
34.         votes ← accumulator[ρ_idx, θ_idx]
35.
36.         IF votes >= threshold THEN:
37.             // Check if local maximum (non-maximum suppression)
38.             IF IS_LOCAL_MAXIMUM(accumulator, ρ_idx, θ_idx) THEN:
39.                 ρ ← ρ_min + ρ_idx × rho_resolution
40.                 θ ← θ_idx × theta_resolution
41.                 APPEND(lines, (ρ, θ, votes))
42.             END IF
43.         END IF
44.     END FOR
45. END FOR

46. RETURN lines
```

---

## Circle Detection

### Circle Equation

$$(x - a)^2 + (y - b)^2 = r^2$$

Where $(a, b)$ is center and $r$ is radius.

### Pseudocode for Circle Detection (known radius)

```
Algorithm HoughTransformCircles(edges, radius, threshold)
Input:
    - edges: binary edge image
    - radius: expected circle radius
    - threshold: minimum votes

Output:
    - circles: list of detected centers (a, b)

1. rows, cols ← edges.shape
2. accumulator ← ZEROS(rows, cols)    // One vote per possible center

3. // For each edge pixel
4. FOR y = 0 TO rows-1 DO:
5.     FOR x = 0 TO cols-1 DO:
6.         IF edges[y, x] == 1 THEN:
7.
8.             // Vote for all possible circle centers
9.             FOR θ = 0 TO 2π WITH STEP δθ DO:
10.                a ← x - radius × COS(θ)
11.                b ← y - radius × SIN(θ)
12.
13.                // Quantize to grid
14.                a_idx ← ROUND(a)
15.                b_idx ← ROUND(b)
16.
17.                IF a_idx IN [0, cols-1] AND b_idx IN [0, rows-1] THEN:
18.                    accumulator[b_idx, a_idx] += 1
19.                END IF
20.            END FOR
21.        END IF
22.    END FOR
23. END FOR

24. // Find peaks (local maxima above threshold)
25. circles ← FIND_LOCAL_MAXIMA(accumulator, threshold)
26.
27. RETURN circles
```

---

## Generalized Hough Transform (for arbitrary shapes)

```
Algorithm GeneralizedHoughTransform(edges, template_shape, threshold)
Input:
    - edges: binary edge image
    - template_shape: R-table with reference point and edge orientations
    - threshold: minimum votes

Output:
    - detected_objects: list of (x, y, scale, rotation)

1. rows, cols ← edges.shape
2. accumulator ← ZEROS(rows, cols)

3. // Compute gradient orientation at each edge point
4. orientations ← COMPUTE_GRADIENT_ORIENTATIONS(edges)

5. // For each edge pixel
6. FOR y = 0 TO rows-1 DO:
7.     FOR x = 0 TO cols-1 DO:
8.         IF edges[y, x] == 1 THEN:
9.             φ ← orientations[y, x]           // Edge orientation
10.
11.            // Look up R-table for this orientation
12.            vectors ← R_TABLE[φ]               // Vectors to reference point
13.
14.            // Vote for reference point location
15.            FOR each r IN vectors DO:
16.                xref ← x + r.x
17.                yref ← y + r.y
18.                IF IN_BOUNDS(xref, yref) THEN:
19.                    accumulator[yref, xref] += 1
20.                END IF
21.            END FOR
22.        END IF
23.    END FOR
24. END FOR

25. RETURN FIND_PEAKS(accumulator, threshold)
```

---

## Key Parameters

| Parameter           | Description                 | Typical Values          |
| ------------------- | --------------------------- | ----------------------- |
| $\rho$ resolution   | Distance quantization       | 1-2 pixels              |
| $\theta$ resolution | Angle quantization          | 1° - 2° (π/180 to π/90) |
| Threshold           | Minimum votes for detection | Depends on image size   |

---

## Space and Time Complexity

| Shape               | Parameter Space       | Complexity                                |
| ------------------- | --------------------- | ----------------------------------------- |
| Lines               | 2D ($\rho$, $\theta$) | $O(N_{edges} \times N_\theta)$            |
| Circles (fixed r)   | 2D ($a$, $b$)         | $O(N_{edges} \times N_\theta)$            |
| Circles (unknown r) | 3D ($a$, $b$, $r$)    | $O(N_{edges} \times N_\theta \times N_r)$ |

---

## Python Implementation

```python
import cv2
import numpy as np

# Line detection
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)
# or
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180,
                        threshold=100, minLineLength=50, maxLineGap=10)

# Circle detection
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT,
                           dp=1, minDist=20,
                           param1=50, param2=30,
                           minRadius=0, maxRadius=0)
```
