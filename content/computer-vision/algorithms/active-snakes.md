---
title: Active Snakes (Active Contours)
---

## Overview

Active contours (snakes) are deformable curves that evolve to fit object boundaries by minimizing an energy function.

## Key Idea

- Start with an initial curve near the object
- Evolve the curve iteratively until it "snaps" to object boundaries
- Balance between smoothness constraints and edge attraction

---

## Contour Representation

A contour is a parametric closed curve represented as a sequence of control points:

$$\mathbf{v} = \{v_i = (x_i, y_i) \mid i = 0, 1, 2, ..., n-1\}$$

Points are connected by straight line segments forming a closed loop.

---

## Energy Function

The total energy to minimize is:

$$E = E_{int}(\mathbf{v}) + E_{ext}(\mathbf{v})$$

Where:

- $E_{int}$ = Internal energy (smoothness, elasticity)
- $E_{ext}$ = External energy (edge attraction)

---

## Energy Terms

### 1. External Energy (Edge Attraction)

$$E_{ext}(\mathbf{v}) = -\sum_{i=0}^{n-1} \|\nabla G_{\sigma} * I(v_i)\|^2$$

Where:

- $I$ = input image
- $G_{\sigma}$ = Gaussian with standard deviation $\sigma$
- $\nabla$ = gradient operator
- $*$ = convolution

**Purpose**: Attracts the snake toward edges. Blurring creates a "force field" that extends the edge influence beyond the exact edge location.

**Alternative formulations**:

- $E_{ext} = -\sum_{i} \|\nabla I(v_i)\|^2$ (without blurring - weaker attraction)
- $E_{ext} = -\sum_{i} I(v_i)$ (for bright objects on dark background)

---

### 2. Internal Energy (Smoothness and Elasticity)

$$E_{int}(\mathbf{v}) = \alpha \cdot E_{elastic} + \beta \cdot E_{smooth}$$

#### Elasticity Term (First-order continuity)

Keeps points close together (prevents stretching):

$$E_{elastic} = \sum_{i=0}^{n-1} \|v_{i+1} - v_i\|^2 = \sum_{i} \left[(x_{i+1} - x_i)^2 + (y_{i+1} - y_i)^2\right]$$

#### Smoothness Term (Second-order continuity)

Prevents sharp bends (curvature minimization):

$$E_{smooth} = \sum_{i=0}^{n-1} \|(v_{i+1} - v_i) - (v_i - v_{i-1})\|^2 = \sum_{i} \left[(x_{i+1} - 2x_i + x_{i-1})^2 + (y_{i+1} - 2y_i + y_{i-1})^2\right]$$

**Parameters**:

- $\alpha$ (alpha): Controls tension/elasticity (higher = points stay closer)
- $\beta$ (beta): Controls stiffness/smoothness (higher = smoother curve)

---

## Simple Greedy Algorithm Pseudocode

```
Algorithm ActiveSnake(image, initial_contour, alpha, beta, gamma, max_iter)
Input:
    - image: input grayscale image
    - initial_contour: list of n control points [(x0,y0), (x1,y1), ..., (x_{n-1},y_{n-1})]
    - alpha: elasticity weight (tension)
    - beta: smoothness weight (stiffness)
    - gamma: step size / external energy weight
    - max_iter: maximum iterations

Output:
    - final_contour: evolved contour aligned with object boundary

// Precompute external energy (edge map)
1. blurred ← GAUSSIAN_FILTER(image, sigma)
2. gradient_x ← CONVOLVE(blurred, SOBEL_X)
3. gradient_y ← CONVOLVE(blurred, SOBEL_Y)
4. edge_map ← -(gradient_x² + gradient_y²)    // Negative for minimization

5. contour ← initial_contour
6. n ← LENGTH(contour)

7. FOR iteration = 1 TO max_iter DO:
8.     moved ← FALSE
9.
10.    // For each control point
11.    FOR i = 0 TO n-1 DO:
12.        current ← contour[i]
13.
14.        // Define neighborhood to search (e.g., 3×3 or 5×5)
15.        neighbors ← GET_NEIGHBORS(current, window_size=3)
16.
17.        best_point ← current
18.        best_energy ← INFINITY
19.
20.        // Evaluate energy for each neighbor
21.        FOR each candidate IN neighbors DO:
22.            // External energy (from precomputed edge map)
23.            E_ext ← -gamma × INTERPOLATE(edge_map, candidate)
24.
25.            // Internal energy - elasticity
26.            prev ← contour[(i-1) mod n]
27.            next ← contour[(i+1) mod n]
28.            E_elastic ← alpha × [(candidate.x - prev.x)² + (candidate.y - prev.y)² +
29.                                  (next.x - candidate.x)² + (next.y - candidate.y)²]
30.
31.            // Internal energy - smoothness
32.            prev2 ← contour[(i-2) mod n]
33.            next2 ← contour[(i+2) mod n]
34.            E_smooth ← beta × [(prev.x - 2×candidate.x + next.x)² +
35.                               (prev.y - 2×candidate.y + next.y)²]
36.
37.            // Total energy
38.            E_total ← E_ext + E_elastic + E_smooth
39.
40.            IF E_total < best_energy THEN:
41.                best_energy ← E_total
42.                best_point ← candidate
43.            END IF
44.        END FOR
45.
46.        // Move point to best position
47.        IF best_point ≠ current THEN:
48.            contour[i] ← best_point
49.            moved ← TRUE
50.        END IF
51.    END FOR
52.
53.    // Check convergence
54.    IF NOT moved THEN:
55.        BREAK    // No points moved, converged
56.    END IF
57. END FOR

58. RETURN contour
```

---

## Energy Terms Summary

| Term       | Formula                                        | Purpose             | Parameter |
| ---------- | ---------------------------------------------- | ------------------- | --------- |
| External   | $-\|\nabla G_\sigma * I\|^2$                   | Attract to edges    | $\gamma$  |
| Elasticity | $\sum \|v_{i+1} - v_i\|^2$                     | Keep points close   | $\alpha$  |
| Smoothness | $\sum \|(v_{i+1} - v_i) - (v_i - v_{i-1})\|^2$ | Prevent sharp bends | $\beta$   |

---

## Key Points

1. **Initialization**: Place initial contour near target object
2. **Convergence**: Algorithm stops when no points move or max iterations reached
3. **Trade-offs**:
   - High $\alpha$ = more compact contour
   - High $\beta$ = smoother contour
   - High $\gamma$ = stronger edge attraction
4. **Limitations**: Can get stuck in local minima, sensitive to initialization

---

## Python Implementation (skimage)

```python
from skimage.segmentation import active_contour
from skimage.filters import gaussian

# Smooth image for stable gradients
img_smooth = gaussian(image, sigma=2.0)

# Initial snake (circular)
s = np.linspace(0, 2*np.pi, 400)
cx, cy, r = 200, 150, 80
init = np.array([cy + r*np.sin(s), cx + r*np.cos(s)]).T

# Run active contour
snake = active_contour(
    img_smooth,
    init,
    alpha=0.01,    # tension
    beta=10,       # stiffness
    gamma=0.001,   # step size
    w_edge=1       # edge attraction weight
)
```
