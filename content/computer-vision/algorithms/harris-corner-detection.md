# Harris Corner Detector

## Overview
The Harris corner detector identifies corners by analyzing the gradient structure in a local window. A corner is where the gradient changes abruptly in multiple directions.

## Key Insight
- **Flat region**: Gradients are small in all directions
- **Edge**: Gradients are large in one direction, small in perpendicular direction
- **Corner**: Gradients are large in multiple directions

---

## Mathematical Foundation

### Structure Tensor (Second Moment Matrix)

For each pixel, compute in a local window:

$$M = \sum_{(x,y) \in W} w(x,y) \begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix} = \begin{bmatrix} \mu_{20} & \mu_{11} \\ \mu_{11} & \mu_{02} \end{bmatrix}$$

Where:
- $I_x, I_y$ = image gradients in x and y directions
- $w(x,y)$ = window function (Gaussian weighting)
- $W$ = local window (typically 3×3 to 7×7)

### Eigenvalue Analysis

Let $\lambda_1, \lambda_2$ be eigenvalues of $M$ (with $\lambda_1 \geq \lambda_2$):

| Region | $\lambda_1$ | $\lambda_2$ | Response |
|--------|-------------|-------------|----------|
| Flat | Small | Small | No corner |
| Edge | Large | Small | No corner |
| Corner | Large | Large | Corner detected |

---

## Harris Response Function

Instead of explicit eigenvalue computation, use:

$$R = \det(M) - k \cdot \text{trace}^2(M)$$

Where:
- $\det(M) = \lambda_1 \lambda_2 = \mu_{20}\mu_{02} - \mu_{11}^2$
- $\text{trace}(M) = \lambda_1 + \lambda_2 = \mu_{20} + \mu_{02}$
- $k$ = empirical constant (typically 0.04 to 0.06)

**Interpretation**:
- $R > 0$: Corner
- $R < 0$: Edge
- $|R|$ small: Flat region

---

## Complete Pseudocode

```
Algorithm HarrisCornerDetector(image, k, threshold, window_size, min_distance)
Input:
    - image: grayscale input image
    - k: Harris detector sensitivity (typically 0.04-0.06)
    - threshold: minimum R value to consider (e.g., 0.01 * max(R))
    - window_size: size of Gaussian window (e.g., 3 or 5)
    - min_distance: minimum distance between corners (for NMS)

Output:
    - corners: list of (x, y) coordinates of detected corners

// ============================================
// STEP 1: Compute Gradients
// ============================================
1. I_x ← CONVOLVE(image, SOBEL_X_KERNEL)     // Horizontal gradient
2. I_y ← CONVOLVE(image, SOBEL_Y_KERNEL)       // Vertical gradient

// ============================================
// STEP 2: Compute Products of Gradients
// ============================================
3. I_x2 ← I_x × I_x                           // Element-wise square
4. I_y2 ← I_y × I_y
5. I_xy ← I_x × I_y

// ============================================
// STEP 3: Gaussian Weighting (Windowing)
// ============================================
6. // Apply Gaussian filter to each component
7. S_x2 ← GAUSSIAN_FILTER(I_x2, sigma, window_size)
8. S_y2 ← GAUSSIAN_FILTER(I_y2, sigma, window_size)
9. S_xy ← GAUSSIAN_FILTER(I_xy, sigma, window_size)

// ============================================
// STEP 4: Compute Harris Response
// ============================================
10. R ← ZEROS(image.shape)

11. FOR each pixel (x, y) in image DO:
12.     // Structure tensor components at this pixel
13.     μ_20 ← S_x2[y, x]
14.     μ_02 ← S_y2[y, x]
15.     μ_11 ← S_xy[y, x]
16.     
17.     // Determinant and trace
18.     det_M ← μ_20 × μ_02 - μ_11²
19.     trace_M ← μ_20 + μ_02
20.     
21.     // Harris response
22.     R[y, x] ← det_M - k × trace_M²
23. END FOR

// ============================================
// STEP 5: Thresholding
// ============================================
24. // Find local maxima above threshold
25. corners ← EMPTY_LIST

26. FOR y = 1 TO rows-2 DO:                    // Avoid boundaries
27.     FOR x = 1 TO cols-2 DO:
28.         
29.         // Check if above threshold
30.         IF R[y, x] > threshold THEN:
31.             
32.             // Check if local maximum (3×3 neighborhood)
33.             neighborhood ← R[y-1:y+2, x-1:x+2]
34.             IF R[y, x] == MAX(neighborhood) THEN:
35.                 APPEND(corners, (x, y, R[y, x]))
36.             END IF
37.         END IF
38.     END FOR
39. END FOR

// ============================================
// STEP 6: Non-Maximum Suppression (by distance)
// ============================================
40. // Sort by response strength (descending)
41. SORT(corners, BY=response, DESCENDING)

42. final_corners ← EMPTY_LIST

43. FOR each candidate IN corners DO:
44.     (cx, cy, response) ← candidate
45.     
46.     // Check distance to already selected corners
47.     too_close ← FALSE
48.     FOR each selected IN final_corners DO:
49.         (sx, sy, _) ← selected
50.         dist ← SQRT((cx - sx)² + (cy - sy)²)
51.         IF dist < min_distance THEN:
52.             too_close ← TRUE
53.             BREAK
54.         END IF
55.     END FOR
56.     
57.     IF NOT too_close THEN:
58.         APPEND(final_corners, candidate)
59.     END IF
60. END FOR

61. RETURN final_corners
```

---

## Alternative: Shi-Tomasi Corner Detector

Uses minimum eigenvalue directly:

$$R = \min(\lambda_1, \lambda_2)$$

More accurate but computationally more expensive.

---

## Properties

| Property | Status |
|----------|--------|
| Rotation invariance | Yes (eigenvalues invariant to rotation) |
| Scale invariance | No (fixed window size) |
| Illumination invariance | Partial (gradients are differences) |
| Noise sensitivity | Yes (requires Gaussian smoothing) |

---

## Python Implementation
```python
import cv2
import numpy as np

# Harris corners
corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold and mark corners
corner_image = image.copy()
corner_image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Or using goodFeaturesToTrack (Shi-Tomasi)
corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, 
                                  qualityLevel=0.01, 
                                  minDistance=10)
```

---

## Comparison: Harris vs. Shi-Tomasi

| Aspect | Harris | Shi-Tomasi |
|--------|--------|------------|
| Response | $\det - k \cdot \text{trace}^2$ | $\min(\lambda_1, \lambda_2)$ |
| Speed | Faster | Slower (needs eigenvalues) |
| Quality | Good | Better |
| Parameter | k (empirical) | qualityLevel |
