# Canny Edge Detection

## Overview
The Canny edge detector is a multi-stage algorithm that detects edges while minimizing noise and providing good localization.

## Key Goals
1. **Low error rate**: Detect all edges with minimal false positives
2. **Good localization**: Edge points should be close to true edges
3. **Single response**: One response per edge point

---

## Pseudocode

```
Algorithm CannyEdgeDetection(image, sigma, T_low, T_high)
Input:
    - image: grayscale input image
    - sigma: standard deviation for Gaussian smoothing
    - T_low: low threshold for hysteresis
    - T_high: high threshold for hysteresis

Output:
    - edges: binary edge map

// ============================================
// STEP 1: Gaussian Smoothing (Noise Reduction)
// ============================================
1. blurred ← GAUSSIAN_FILTER(image, sigma)
   // Kernel size typically 5×5 or based on sigma

// ============================================
// STEP 2: Gradient Computation
// ============================================
2. G_x ← CONVOLVE(blurred, SOBEL_X_KERNEL)    // Horizontal gradient
3. G_y ← CONVOLVE(blurred, SOBEL_Y_KERNEL)      // Vertical gradient

4. magnitude ← SQRT(G_x² + G_y²)               // Edge strength
5. direction ← ATAN2(G_y, G_x)                  // Edge orientation (in radians)
   // Quantize to 4 directions: 0°, 45°, 90°, 135°

// ============================================
// STEP 3: Non-Maximum Suppression
// ============================================
6. nms ← ZEROS(image.shape)

7. FOR each pixel (i, j) in image DO:
8.     IF magnitude[i, j] == 0 THEN:
9.         CONTINUE
10.    
11.    // Get gradient direction (quantized to 0°, 45°, 90°, 135°)
12.    angle ← direction[i, j]
13.    
14.    // Determine neighbors to compare based on direction
15.    IF (angle >= -π/8 AND angle < π/8) OR 
16.       (angle >= 7π/8 OR angle < -7π/8) THEN:
17.        // 0° direction (horizontal edge) - compare left and right
18.        neighbors ← [magnitude[i, j-1], magnitude[i, j+1]]
19.    
20.    ELSE IF (angle >= π/8 AND angle < 3π/8) OR 
21.            (angle >= -7π/8 AND angle < -5π/8) THEN:
22.        // 45° direction - compare diagonal neighbors
23.        neighbors ← [magnitude[i-1, j+1], magnitude[i+1, j-1]]
24.    
25.    ELSE IF (angle >= 3π/8 AND angle < 5π/8) OR 
26.            (angle >= -5π/8 AND angle < -3π/8) THEN:
27.        // 90° direction (vertical edge) - compare above and below
28.        neighbors ← [magnitude[i-1, j], magnitude[i+1, j]]
29.    
30.    ELSE:
31.        // 135° direction - compare other diagonal neighbors
32.        neighbors ← [magnitude[i-1, j-1], magnitude[i+1, j+1]]
33.    
34.    // Keep pixel only if it's a local maximum
35.    IF magnitude[i, j] >= MAX(neighbors) THEN:
36.        nms[i, j] ← magnitude[i, j]
37.    ELSE:
38.        nms[i, j] ← 0    // Suppress non-maximum
39.    END IF
40. END FOR

// ============================================
// STEP 4: Double Thresholding
// ============================================
41. strong_edges ← nms > T_high
42. weak_edges   ← (nms >= T_low) AND (nms <= T_high)
43. non_edges    ← nms < T_low

44. edge_map ← ZEROS(image.shape)
45. edge_map[strong_edges] ← 255    // Strong edges = 255 (white)
46. edge_map[weak_edges]   ← 128    // Weak edges = 128 (gray, tentative)

// ============================================
// STEP 5: Edge Tracking by Hysteresis
// ============================================
47. final_edges ← strong_edges      // Start with strong edges

48. // For each weak edge pixel
49. FOR each pixel (i, j) where weak_edges[i, j] == TRUE DO:
50.     // Check 8-connected neighbors
51.     neighbors_8 ← GET_8_NEIGHBORS(edge_map, i, j)
52.     
53.     // If any neighbor is a strong edge, keep this weak edge
54.     IF MAX(neighbors_8) == 255 THEN:
55.         final_edges[i, j] ← TRUE
56.     END IF
57. END FOR

58. RETURN final_edges
```

---

## Sobel Kernels

### Sobel X (Horizontal edges)
$$
G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}
$$

### Sobel Y (Vertical edges)
$$
G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
$$

---

## Gradient Quantization for NMS

| Angle Range | Direction | Neighbors to Compare |
|-------------|-----------|-------------------|
| $[-\pi/8, \pi/8)$ or $[7\pi/8, -7\pi/8)$ | 0° (horizontal) | Left, Right |
| $[\pi/8, 3\pi/8)$ or $[-7\pi/8, -5\pi/8)$ | 45° | Top-right, Bottom-left |
| $[3\pi/8, 5\pi/8)$ or $[-5\pi/8, -3\pi/8)$ | 90° (vertical) | Top, Bottom |
| $[5\pi/8, 7\pi/8)$ or $[-3\pi/8, -\pi/8)$ | 135° | Top-left, Bottom-right |

---

## Threshold Selection Guidelines

| Ratio | Use Case |
|-------|----------|
| $T_{high} : T_{low} = 2:1$ or $3:1$ | Standard recommendation |
| Higher $T_{high}$ | Fewer edges, less noise |
| Lower $T_{high}$ | More edges, more noise |

---

## Summary of Steps

1. **Smooth**: Gaussian filter to reduce noise
2. **Gradient**: Sobel to find edge strength and direction
3. **NMS**: Keep only local maxima along gradient direction
4. **Threshold**: Classify as strong/weak/non-edge
5. **Hysteresis**: Connect weak edges to strong edges

---

## Python Implementation (OpenCV/skimage)
```python
import cv2
from skimage.feature import canny

# OpenCV
blurred = cv2.GaussianBlur(image, (5, 5), sigma)
edges_cv = cv2.Canny(blurred, T_low, T_high)

# skimage
edges = canny(image, sigma=sigma, 
              low_threshold=T_low/255, 
              high_threshold=T_high/255)
```
