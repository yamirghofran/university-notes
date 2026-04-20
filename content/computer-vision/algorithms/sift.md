---
title: SIFT Detection and Description
---

## Overview

SIFT (Scale-Invariant Feature Transform) detects and describes local features that are invariant to:

- Scale changes
- Rotation
- Illumination changes
- Partially invariant to viewpoint changes

---

## Part 1: SIFT Keypoint Detection

### Scale Space Construction

Build a Gaussian pyramid with multiple octaves and scales per octave.

```
Algorithm BuildGaussianPyramid(image, num_octaves, scales_per_octave, sigma_0)
Input:
    - image: input grayscale image
    - num_octaves: number of octaves (typically 4)
    - scales_per_octave: scales per octave (typically 3-5)
    - sigma_0: initial sigma (typically 1.6)

Output:
    - gaussian_pyramid: list of octaves, each containing blurred images

1. pyramid ← EMPTY_LIST
2. k ← 2^(1/scales_per_octave)    // Scale factor between levels

3. FOR octave = 0 TO num_octaves-1 DO:
4.     octave_images ← EMPTY_LIST
5.
6.     // Downsample for new octave (except first)
7.     IF octave > 0 THEN:
8.         image ← DOWNSAMPLE(pyramid[octave-1][scales_per_octave-1], factor=2)
9.     END IF
10.
11.    // Create scales within octave
12.    FOR s = 0 TO scales_per_octave+2 DO:    // Extra scales for DoG
13.        sigma ← sigma_0 × k^s
14.        blurred ← GAUSSIAN_FILTER(image, sigma)
15.        APPEND(octave_images, blurred)
16.    END FOR
17.
18.    APPEND(pyramid, octave_images)
19. END FOR

20. RETURN pyramid
```

### Difference of Gaussian (DoG) Pyramid

Approximates Laplacian of Gaussian efficiently:

$$\text{DoG}(x, y, \sigma) = G(x, y, k\sigma) - G(x, y, \sigma) \approx (k-1)\sigma^2 \nabla^2 G$$

```
Algorithm BuildDoGPyramid(gaussian_pyramid)
Input:
    - gaussian_pyramid: from previous step

Output:
    - dog_pyramid: Difference of Gaussian pyramid

1. dog_pyramid ← EMPTY_LIST

2. FOR each octave IN gaussian_pyramid DO:
3.     dog_octave ← EMPTY_LIST
4.
5.     FOR i = 0 TO LENGTH(octave)-2 DO:
6.         dog ← octave[i+1] - octave[i]    // Simple subtraction
7.         APPEND(dog_octave, dog)
8.     END FOR
9.
10.    APPEND(dog_pyramid, dog_octave)
11. END FOR

12. RETURN dog_pyramid
```

### Extrema Detection (Keypoint Localization)

Find local extrema in 3D (scale-space):

```
Algorithm DetectExtrema(dog_pyramid, contrast_threshold)
Input:
    - dog_pyramid: DoG pyramid
    - contrast_threshold: minimum DoG value (typically 0.03-0.04)

Output:
    - keypoints: list of (x, y, octave, scale, sigma)

1. keypoints ← EMPTY_LIST

2. FOR each octave_idx, octave IN dog_pyramid DO:
3.     // Check middle scales only (need neighbors above and below)
4.     FOR s = 1 TO LENGTH(octave)-2 DO:
5.         dog_current ← octave[s]
6.         dog_above ← octave[s+1]
7.         dog_below ← octave[s-1]
8.
9.         rows, cols ← dog_current.shape
10.
11.        FOR y = 1 TO rows-2 DO:
12.            FOR x = 1 TO cols-2 DO:
13.                value ← dog_current[y, x]
14.
15.                // Skip low contrast points
16.                IF ABS(value) < contrast_threshold THEN:
17.                    CONTINUE
18.                END IF
19.
20.                // Get 3×3×3 neighborhood
21.                neighborhood ← [
22.                    dog_below[y-1:y+2, x-1:x+2],
23.                    dog_current[y-1:y+2, x-1:x+2],
24.                    dog_above[y-1:y+2, x-1:x+2]
25.                ]
26.
27.                // Check if local extremum
28.                IF value > MAX(neighborhood) OR value < MIN(neighborhood) THEN:
29.                    // Refine location (sub-pixel accuracy)
30.                    (x_refined, y_refined, sigma) ← REFINE_LOCATION(
31.                        octave, s, x, y
32.                    )
33.
34.                    IF NOT ON_EDGE(dog_current, x, y) THEN:
35.                        APPEND(keypoints, (x_refined, y_refined,
35.                                           octave_idx, s, sigma))
36.                    END IF
37.                END IF
38.            END FOR
39.        END FOR
40.    END FOR
41. END FOR

42. RETURN keypoints
```

### Edge Response Elimination

Reject points on edges using Hessian ratio:

```
Function ON_EDGE(dog_image, x, y, threshold=10)
Input:
    - dog_image: DoG image at current scale
    - x, y: pixel coordinates
    - threshold: edge threshold (typically 10)

Output:
    - is_edge: boolean

1. // Compute second derivatives (Hessian)
2. D_xx ← dog_image[y, x+1] - 2×dog_image[y, x] + dog_image[y, x-1]
3. D_yy ← dog_image[y+1, x] - 2×dog_image[y, x] + dog_image[y-1, x]
4. D_xy ← (dog_image[y+1, x+1] - dog_image[y+1, x-1] -
5.          dog_image[y-1, x+1] + dog_image[y-1, x-1]) / 4

6. // Harris measure on Hessian
7. trace ← D_xx + D_yy
8. det ← D_xx × D_yy - D_xy²

9. // Edge if ratio of eigenvalues is large
10. IF det <= 0 THEN:
11.     RETURN TRUE    // On edge or unstable
12. END IF
13.
14. ratio ← trace² / det
15.
16. IF ratio > (threshold + 1)² / threshold THEN:
17.     RETURN TRUE    // On edge
18. END IF

19. RETURN FALSE
```

---

## Part 2: SIFT Descriptor Computation

### Orientation Assignment (Rotation Invariance)

```
Algorithm AssignOrientation(image, keypoint, num_bins=36)
Input:
    - image: Gaussian blurred image at keypoint scale
    - keypoint: (x, y, octave, scale, sigma)
    - num_bins: number of orientation histogram bins

Output:
    - orientations: list of dominant orientations

1. (x, y, octave, scale, sigma) ← keypoint
2.
3. // Compute gradients in region around keypoint
4. region_size ← ROUND(3 × 1.5 × sigma)
5.
6. histogram ← ZEROS(num_bins)
7. bin_width ← 2π / num_bins

8. FOR dy = -region_size TO region_size DO:
9.     FOR dx = -region_size TO region_size DO:
10.
11.        // Compute gradient
12.        gx ← image[y+dy, x+dx+1] - image[y+dy, x+dx-1]
13.        gy ← image[y+dy+1, x+dx] - image[y+dy-1, x+dx]
14.
15.        magnitude ← SQRT(gx² + gy²)
16.        orientation ← ATAN2(gy, gx)    // -π to π
17.
18.        // Gaussian weight by distance from center
19.        weight ← EXP(-(dx² + dy²) / (2 × (1.5 × sigma)²))
19.
20.        // Add to histogram
21.        bin ← FLOOR((orientation + π) / bin_width) mod num_bins
22.        histogram[bin] += weight × magnitude
23.    END FOR
24. END FOR

25. // Smooth histogram
26. histogram ← SMOOTH_CIRCULAR(histogram)

27. // Find dominant orientation(s)
28. max_val ← MAX(histogram)
29. threshold ← 0.8 × max_val
30.
31. orientations ← EMPTY_LIST
32. FOR bin = 0 TO num_bins-1 DO:
33.     IF histogram[bin] >= threshold THEN:
34.         // Parabolic interpolation for accuracy
35.         angle ← (bin + 0.5) × bin_width - π
36.         APPEND(orientations, angle)
37.     END IF
38. END FOR

39. RETURN orientations
```

### Descriptor Computation

```
Algorithm ComputeDescriptor(image, keypoint, orientation, size=4, num_bins=8)
Input:
    - image: Gaussian blurred image at keypoint scale
    - keypoint: (x, y, octave, scale, sigma)
    - orientation: assigned dominant orientation
    - size: descriptor grid size (typically 4×4)
    - num_bins: orientation bins per cell (typically 8)

Output:
    - descriptor: 128-dimensional vector (4×4×8)

1. (x, y, _, _, sigma) ← keypoint
2. descriptor ← EMPTY_LIST
3.
4. // Rotate coordinates to align with keypoint orientation
5. cos_o ← COS(orientation)
6. sin_o ← SIN(orientation)
7.
8. // Descriptor window size
9. window_size ← 4 × size × sigma    // 4×4 cells, each 4×4 pixels
10.
11. FOR cell_y = 0 TO size-1 DO:
12.     FOR cell_x = 0 TO size-1 DO:
13.
14.         cell_histogram ← ZEROS(num_bins)
15.
16.         // Sample 4×4 region within cell
17.         FOR dy = 0 TO 3 DO:
18.             FOR dx = 0 TO 3 DO:
19.
20.                 // Sample point in image coordinates
21.                sample_x ← x + (cell_x - 1.5) × 4 × sigma + dx × sigma
22.                sample_y ← y + (cell_y - 1.5) × 4 × sigma + dy × sigma
23.
24.                // Rotate by keypoint orientation
25.                rot_x ← cos_o × (sample_x - x) - sin_o × (sample_y - y) + x
26.                rot_y ← sin_o × (sample_x - x) + cos_o × (sample_y - y) + y
27.
28.                // Compute gradient at sample point (bilinear interpolation)
28.                gx ← INTERPOLATE_GRADIENT_X(image, rot_x, rot_y)
29.                gy ← INTERPOLATE_GRADIENT_Y(image, rot_x, rot_y)
30.
31.                magnitude ← SQRT(gx² + gy²)
32.                sample_orientation ← ATAN2(gy, gx) - orientation
33.
34.                // Gaussian weight by distance from keypoint center
35.                dist_x ← (cell_x - 1.5) × 4 + dx
36.                dist_y ← (cell_y - 1.5) × 4 + dy
37.                weight ← EXP(-(dist_x² + dist_y²) / 8)
38.
39.                // Add to cell histogram with trilinear interpolation
40.                bin ← (sample_orientation + π) × num_bins / (2π)
41.                bin_low ← FLOOR(bin) mod num_bins
42.                bin_high ← CEIL(bin) mod num_bins
43.
44.                w_high ← bin - FLOOR(bin)
45.                w_low ← 1 - w_high
46.
47.                cell_histogram[bin_low] += w_low × weight × magnitude
48.                cell_histogram[bin_high] += w_high × weight × magnitude
49.            END FOR
50.        END FOR
51.
52.        APPEND(descriptor, cell_histogram)
53.    END FOR
54. END FOR

55. // Flatten to 128-dimensional vector
56. descriptor ← FLATTEN(descriptor)

57. // Normalize
58. descriptor ← descriptor / NORM(descriptor)
59.
60. // Threshold large values (illumination invariance)
61. descriptor ← MIN(descriptor, 0.2)
62.
63. // Renormalize
64. descriptor ← descriptor / NORM(descriptor)

65. RETURN descriptor
```

---

## Complete SIFT Algorithm

```
Algorithm SIFT(image)
Input:
    - image: input grayscale image

Output:
    - keypoints: list of keypoints with descriptors

1. // Step 1: Scale-space extrema detection
2. gaussian_pyramid ← BuildGaussianPyramid(image, num_octaves=4,
                                           scales_per_octave=3)
3. dog_pyramid ← BuildDoGPyramid(gaussian_pyramid)
4. keypoints ← DetectExtrema(dog_pyramid, contrast_threshold=0.03)

5. // Step 2: Keypoint localization and filtering
6. refined_keypoints ← EMPTY_LIST
7. FOR each kp IN keypoints DO:
8.     IF NOT ON_EDGE(kp) THEN:
9.         APPEND(refined_keypoints, kp)
10.    END IF
11. END FOR

12. // Step 3: Orientation assignment
13. oriented_keypoints ← EMPTY_LIST
14. FOR each kp IN refined_keypoints DO:
15.     image_at_scale ← GET_IMAGE(gaussian_pyramid, kp.octave, kp.scale)
16.     orientations ← AssignOrientation(image_at_scale, kp)
17.
18.     FOR each angle IN orientations DO:
19.         new_kp ← (kp.x, kp.y, kp.octave, kp.scale, kp.sigma, angle)
20.         APPEND(oriented_keypoints, new_kp)
21.     END FOR
22. END FOR

23. // Step 4: Descriptor computation
24. final_keypoints ← EMPTY_LIST
25. FOR each kp IN oriented_keypoints DO:
26.     image_at_scale ← GET_IMAGE(gaussian_pyramid, kp.octave, kp.scale)
27.     descriptor ← ComputeDescriptor(image_at_scale, kp, kp.orientation)
28.
29.     final_kp ← {
30.         x: kp.x,
31.         y: kp.y,
32.         scale: kp.sigma,
33.         orientation: kp.orientation,
34.         descriptor: descriptor    // 128-dim vector
35.     }
36.     APPEND(final_keypoints, final_kp)
37. END FOR

38. RETURN final_keypoints
```

---

## SIFT Descriptor Properties

| Property                | Value                                |
| ----------------------- | ------------------------------------ |
| Descriptor size         | 128 dimensions (4×4×8)               |
| Scale invariance        | Yes (via scale-space)                |
| Rotation invariance     | Yes (via orientation normalization)  |
| Illumination invariance | Yes (gradient-based + normalization) |

---

## Python Implementation

```python
import cv2

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(image, None)

# keypoints: list of KeyPoint objects (x, y, size, angle, response, octave)
# descriptors: N×128 array of SIFT descriptors

# For feature matching
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)
```
