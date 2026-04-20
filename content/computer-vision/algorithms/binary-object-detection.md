---
title: Binary Object Detection
---

## Overview

Binary object detection identifies and labels connected regions (objects) in binary images.

## Two Main Algorithms

1. **Region Growing** (flood-fill based)
2. **Sequence Labeling** (two-pass algorithm)

---

## 1. Region Growing Algorithm

### Concept

Start from an unlabeled pixel and "grow" the region by adding connected neighbors with the same value.

### Connectivity Types

- **4-connectivity**: Up, Down, Left, Right neighbors
- **8-connectivity**: All 8 surrounding pixels

### Pseudocode

```
Algorithm RegionGrowing(binary_image, connectivity=4)
Input:
    - binary_image: M × N binary image (0 = background, 1 = foreground)
    - connectivity: 4 or 8

Output:
    - labeled_image: M × N array with unique labels for each object
    - num_objects: number of distinct objects

1. M, N ← binary_image.shape
2. labeled_image ← ZEROS(M, N)
3. current_label ← 0

4. FOR y = 0 TO M-1 DO:
5.     FOR x = 0 TO N-1 DO:
6.
7.         // Found unlabeled foreground pixel
8.         IF binary_image[y, x] == 1 AND labeled_image[y, x] == 0 THEN:
9.
10.            current_label ← current_label + 1
11.
12.            // Initialize queue with seed pixel
13.            queue ← [(x, y)]
14.            labeled_image[y, x] ← current_label
15.
16.            // Grow region
17.            WHILE queue NOT EMPTY DO:
18.                (cx, cy) ← DEQUEUE(queue)
19.
20.                // Check neighbors based on connectivity
21.                IF connectivity == 4 THEN:
22.                    neighbors ← [
23.                        (cx+1, cy), (cx-1, cy),
24.                        (cx, cy+1), (cx, cy-1)
24.                    ]
25.                ELSE:  // connectivity == 8
26.                    neighbors ← [
27.                        (cx+1, cy), (cx-1, cy),
28.                        (cx, cy+1), (cx, cy-1),
29.                        (cx+1, cy+1), (cx+1, cy-1),
30.                        (cx-1, cy+1), (cx-1, cy-1)
31.                    ]
32.                END IF
33.
34.                // Check each neighbor
35.                FOR (nx, ny) IN neighbors DO:
36.                    IF nx >= 0 AND nx < N AND ny >= 0 AND ny < M THEN:
37.                        IF binary_image[ny, nx] == 1 AND
38.                           labeled_image[ny, nx] == 0 THEN:
39.                            labeled_image[ny, nx] ← current_label
40.                            ENQUEUE(queue, (nx, ny))
41.                        END IF
42.                    END IF
43.                END FOR
44.            END WHILE
45.        END IF
46.    END FOR
47. END FOR

48. num_objects ← current_label
49. RETURN (labeled_image, num_objects)
```

---

## 2. Sequence Labeling Algorithm (Two-Pass)

### Concept

Scan image twice:

1. **First pass**: Assign provisional labels and record equivalences
2. **Second pass**: Resolve equivalences and assign final labels

### Pseudocode

```
Algorithm SequenceLabeling(binary_image, connectivity=4)
Input:
    - binary_image: M × N binary image (0 = background, 1 = foreground)
    - connectivity: 4 or 8

Output:
    - labeled_image: M × N array with unique labels
    - num_objects: number of distinct objects

// ============================================
// FIRST PASS: Provisional labeling
// ============================================
1. M, N ← binary_image.shape
2. labeled_image ← ZEROS(M, N)
3. next_label ← 1
4. equivalence_table ← EMPTY_MAP    // label → equivalent_label

5. FOR y = 0 TO M-1 DO:              // Raster scan (top to bottom)
6.     FOR x = 0 TO N-1 DO:          // Left to right
7.
8.         IF binary_image[y, x] == 0 THEN:
9.             CONTINUE                // Background pixel
10.        END IF
11.
12.        // Get already processed neighbors
13.        IF connectivity == 4 THEN:
14.            neighbors ← GET_4_NEIGHBORS(labeled_image, x, y)
15.        ELSE:
16.            neighbors ← GET_8_NEIGHBORS(labeled_image, x, y)
17.        END IF
18.
19.        // Remove background (0) from neighbors
20.        neighbor_labels ← [n FOR n IN neighbors IF n > 0]
21.
22.        IF LENGTH(neighbor_labels) == 0 THEN:
23.            // No labeled neighbors - new object
24.            labeled_image[y, x] ← next_label
25.            next_label ← next_label + 1
26.
27.        ELSE IF ALL_EQUAL(neighbor_labels) THEN:
28.            // All neighbors have same label
29.            labeled_image[y, x] ← neighbor_labels[0]
30.
31.        ELSE:
32.            // Different labels - merge equivalence
33.            min_label ← MIN(neighbor_labels)
34.            labeled_image[y, x] ← min_label
35.
36.            // Record equivalences
37.            FOR each label IN neighbor_labels DO:
38.                IF label != min_label THEN:
39.                    ADD_EQUIVALENCE(equivalence_table, label, min_label)
40.                END IF
41.            END FOR
42.        END IF
43.    END FOR
44. END FOR

// ============================================
// RESOLVE EQUIVALENCES (Union-Find)
// ============================================
45. FUNCTION FIND(label):
46.     WHILE equivalence_table[label] EXISTS AND
47.           equivalence_table[label] != label DO:
48.         label ← equivalence_table[label]
49.     END WHILE
50.     RETURN label
51.
52. FUNCTION UNION(label1, label2):
53.     root1 ← FIND(label1)
54.     root2 ← FIND(label2)
55.     IF root1 != root2 THEN:
56.         equivalence_table[root2] ← root1
57.     END IF

// Flatten equivalence table
58. FOR each label IN equivalence_table.keys() DO:
59.     equivalence_table[label] ← FIND(label)
60. END FOR

// ============================================
// SECOND PASS: Relabel with final labels
// ============================================
61. label_mapping ← EMPTY_MAP
62. final_label ← 1

63. FOR y = 0 TO M-1 DO:
64.     FOR x = 0 TO N-1 DO:
65.         IF labeled_image[y, x] > 0 THEN:
66.             old_label ← labeled_image[y, x]
67.
68.             // Get equivalent (minimum) label
69.             IF old_label IN equivalence_table THEN:
70.                 equiv_label ← equivalence_table[old_label]
71.             ELSE:
72.                 equiv_label ← old_label
73.             END IF
74.
75.             // Map to consecutive final labels
76.             IF equiv_label NOT IN label_mapping THEN:
77.                 label_mapping[equiv_label] ← final_label
78.                 final_label ← final_label + 1
79.             END IF
80.
81.             labeled_image[y, x] ← label_mapping[equiv_label]
82.         END IF
83.     END FOR
84. END FOR

85. num_objects ← final_label - 1
86. RETURN (labeled_image, num_objects)
```

### First Pass Labeling Rules (4-connectivity)

| D   | B   | A   | C   | Action                                         |
| --- | --- | --- | --- | ---------------------------------------------- |
| X   | X   | 0   | X   | A = background (0)                             |
| 0   | 0   | 0   | 1   | A = label(C)                                   |
| 0   | 0   | 1   | 0   | A = label(B)                                   |
| 0   | 0   | 1   | 1   | A = label(B) or label(C) (same)                |
| 0   | 1   | 1   | 0   | A = label(B)                                   |
| 0   | 1   | 1   | 1   | A = label(B)                                   |
| 1   | 0   | 1   | 0   | A = label(D)                                   |
| 1   | 0   | 1   | 1   | A = label(C), record equivalence(B,C)          |
| 1   | 1   | 1   | 0   | A = label(B) or label(D) (same)                |
| 1   | 1   | 1   | 1   | A = label(B), record equivalences if different |

Where:

- A = current pixel being labeled
- B = neighbor above (x, y-1)
- C = neighbor left (x-1, y)
- D = neighbor diagonal (x-1, y-1) - for 8-connectivity

---

## Comparison

| Aspect         | Region Growing          | Sequence Labeling   |
| -------------- | ----------------------- | ------------------- |
| Memory         | Queue can grow large    | Fixed memory        |
| Speed          | Slower (random access)  | Faster (sequential) |
| Implementation | Simpler                 | More complex        |
| Best for       | Small number of objects | Large images        |

---

## Python Implementation

```python
import cv2
import numpy as np
from skimage.measure import label

# OpenCV
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    binary_img, connectivity=8  # or 4
)

# skimage
labels_sk = label(binary_img, connectivity=2)  # 1=4-C, 2=8-C

# Get region properties
from skimage.measure import regionprops
props = regionprops(labels)
for prop in props:
    area = prop.area
    centroid = prop.centroid
    bbox = prop.bbox
```
