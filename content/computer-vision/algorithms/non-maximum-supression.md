# Non-Maximum Suppression (NMS)

## Overview
NMS is a post-processing technique that removes duplicate detections by keeping only the strongest response in a local neighborhood.

## Applications
- Edge detection (Canny)
- Object detection (YOLO, Faster R-CNN)
- Corner detection
- Hough transform peak selection
- Feature detection

---

## Core Idea
When multiple detections overlap significantly and likely correspond to the same object:
1. Keep the detection with highest confidence/score
2. Suppress (remove) nearby detections with lower scores

---

## General NMS Algorithm

```
Algorithm NonMaximumSuppression(detections, scores, overlap_threshold)
Input:
    - detections: list of detections (bounding boxes, points, etc.)
    - scores: confidence score for each detection
    - overlap_threshold: maximum allowed overlap (IoU threshold, typically 0.5)

Output:
    - selected: list of indices of kept detections

// ============================================
// SORT BY SCORE
// ============================================
1. N ← LENGTH(detections)
2. indices ← ARGSORT(scores, DESCENDING)    // Highest score first

3. selected ← EMPTY_LIST
4. suppressed ← BOOLEAN_ARRAY(N, initial=FALSE)

// ============================================
// GREEDY SELECTION
// ============================================
5. FOR i = 0 TO N-1 DO:
6.     idx ← indices[i]
7.     
8.     // Skip if already suppressed
9.     IF suppressed[idx] THEN:
10.        CONTINUE
11.    END IF
12.    
13.    // Keep this detection
14.    APPEND(selected, idx)
15.    
16.    // Suppress overlapping detections
17.    FOR j = i+1 TO N-1 DO:
18.        other_idx ← indices[j]
19.        
20.        IF suppressed[other_idx] THEN:
21.            CONTINUE
22.        END IF
23.        
24.        // Compute overlap
25.        overlap ← COMPUTE_OVERLAP(detections[idx], detections[other_idx])
26.        
27.        // Suppress if overlap exceeds threshold
28.        IF overlap > overlap_threshold THEN:
29.            suppressed[other_idx] ← TRUE
30.        END IF
31.    END FOR
32. END FOR

33. RETURN selected
```

---

## NMS for Bounding Boxes (Object Detection)

### Intersection over Union (IoU)

$$\text{IoU} = \frac{\text{Area of Intersection}}{\text{Area of Union}}$$

```
Function ComputeIoU(box1, box2)
Input:
    - box1: (x1, y1, x2, y2) - top-left and bottom-right corners
    - box2: (x1, y1, x2, y2)

Output:
    - iou: Intersection over Union ratio

1. // Compute intersection
2. x_left   ← MAX(box1.x1, box2.x1)
3. y_top    ← MAX(box1.y1, box2.y1)
4. x_right  ← MIN(box1.x2, box2.x2)
5. y_bottom ← MIN(box1.y2, box2.y2)

6. IF x_right < x_left OR y_bottom < y_top THEN:
7.     RETURN 0    // No intersection
8. END IF

9. intersection_area ← (x_right - x_left) × (y_bottom - y_top)

10. // Compute union
11. box1_area ← (box1.x2 - box1.x1) × (box1.y2 - box1.y1)
12. box2_area ← (box2.x2 - box2.x1) × (box2.y2 - box2.y1)
13. union_area ← box1_area + box2_area - intersection_area

14. iou ← intersection_area / union_area
15. RETURN iou
```

### Complete NMS for Object Detection

```
Algorithm NMS_BoundingBoxes(boxes, scores, iou_threshold, max_boxes=0)
Input:
    - boxes: N × 4 array of (x1, y1, x2, y2)
    - scores: N confidence scores
    - iou_threshold: IoU threshold for suppression (typically 0.5)
    - max_boxes: maximum boxes to return (0 = unlimited)

Output:
    - kept_indices: indices of boxes to keep

1. N ← LENGTH(scores)
2. IF N == 0 THEN:
3.     RETURN []
4. END IF

5. // Sort by score descending
6. sorted_indices ← ARGSORT(scores, DESCENDING)

7. kept ← []
8. 
9. WHILE LENGTH(sorted_indices) > 0 DO:
10.    // Pick box with highest score
11.    current ← sorted_indices[0]
12.    APPEND(kept, current)
13.    
14.    IF max_boxes > 0 AND LENGTH(kept) >= max_boxes THEN:
15.        BREAK
16.    END IF
17.    
18.    // Compute IoU with remaining boxes
19.    ious ← []
20.    FOR i = 1 TO LENGTH(sorted_indices)-1 DO:
21.        other ← sorted_indices[i]
22.        iou ← ComputeIoU(boxes[current], boxes[other])
23.        APPEND(ious, iou)
24.    END FOR
25.    
26.    // Keep only boxes with IoU below threshold
27.    remaining ← []
28.    FOR i = 1 TO LENGTH(sorted_indices)-1 DO:
29.        IF ious[i-1] <= iou_threshold THEN:
30.            APPEND(remaining, sorted_indices[i])
31.        END IF
32.    END FOR
33.    
34.    sorted_indices ← remaining
35. END WHILE

36. RETURN kept
```

---

## NMS for Edge Detection (Canny)

```
Algorithm NMS_Edges(gradient_magnitude, gradient_direction)
Input:
    - gradient_magnitude: edge strength at each pixel
    - gradient_direction: edge orientation (in radians)

Output:
    - nms_edges: thinned edge map

1. rows, cols ← gradient_magnitude.shape
2. nms_edges ← ZEROS(rows, cols)

3. FOR y = 1 TO rows-2 DO:
4.     FOR x = 1 TO cols-2 DO:
5.         
6.         current_mag ← gradient_magnitude[y, x]
7.         angle ← gradient_direction[y, x]
8.         
9.         // Skip if no edge
10.        IF current_mag == 0 THEN:
11.            CONTINUE
12.        END IF
13.        
14.        // Quantize angle to 4 directions
15.        angle_deg ← DEGREES(angle)
16.        
17.        IF (-22.5 <= angle_deg < 22.5) OR (157.5 <= angle_deg) OR (angle_deg < -157.5) THEN:
18.            // 0° - horizontal edge, compare left and right
19.            neighbors ← [gradient_magnitude[y, x-1], 
20.                         gradient_magnitude[y, x+1]]
21.                         
22.        ELSE IF (22.5 <= angle_deg < 67.5) OR (-157.5 <= angle_deg < -112.5) THEN:
23.            // 45° - diagonal, compare top-right and bottom-left
24.            neighbors ← [gradient_magnitude[y-1, x+1], 
25.                         gradient_magnitude[y+1, x-1]]
26.                         
27.        ELSE IF (67.5 <= angle_deg < 112.5) OR (-112.5 <= angle_deg < -67.5) THEN:
28.            // 90° - vertical edge, compare top and bottom
29.            neighbors ← [gradient_magnitude[y-1, x], 
30.                         gradient_magnitude[y+1, x]]
31.                         
32.        ELSE:
33.            // 135° - other diagonal, compare top-left and bottom-right
34.            neighbors ← [gradient_magnitude[y-1, x-1], 
35.                         gradient_magnitude[y+1, x+1]]
36.        END IF
37.        
38.        // Keep only if local maximum
39.        IF current_mag >= MAX(neighbors) THEN:
40.            nms_edges[y, x] ← current_mag
41.        ELSE:
42.            nms_edges[y, x] ← 0    // Suppress
43.        END IF
44.    END FOR
45. END FOR

46. RETURN nms_edges
```

---

## Soft-NMS (Improved Version)

Instead of hard suppression, decay scores based on overlap:

```
Algorithm SoftNMS(boxes, scores, sigma=0.5, method="gaussian")
Input:
    - boxes: N × 4 array
    - scores: N confidence scores
    - sigma: parameter for Gaussian decay
    - method: "linear", "gaussian", or "hard"

Output:
    - updated_scores: modified scores

1. N ← LENGTH(scores)
2. indices ← ARGSORT(scores, DESCENDING)

3. FOR i = 0 TO N-1 DO:
4.     max_idx ← indices[i]
5.     
6.     FOR j = i+1 TO N-1 DO:
7.         idx ← indices[j]
8.         iou ← ComputeIoU(boxes[max_idx], boxes[idx])
9.         
10.        // Decay score based on overlap
11.        SWITCH method:
12.            CASE "linear":
13.                IF iou > threshold THEN:
14.                    scores[idx] ← scores[idx] × (1 - iou)
15.                END IF
16.                
17.            CASE "gaussian":
18.                scores[idx] ← scores[idx] × EXP(-iou² / sigma)
19.                
20.            CASE "hard":
21.                IF iou > threshold THEN:
22.                    scores[idx] ← 0
23.                END IF
24.    END FOR
25. END FOR

26. // Filter by updated scores
27. kept ← [i FOR i, s IN ENUMERATE(scores) IF s > threshold]
28. RETURN kept
```

---

## Summary Table

| Application | Overlap Measure | Threshold | Notes |
|-------------|-----------------|-----------|-------|
| Canny edges | Gradient comparison | Local max | Along gradient direction |
| Object detection | IoU | 0.5 | Class-aware or class-agnostic |
| Hough transform | Distance in parameter space | Varies | Peak detection |
| Corner detection | Euclidean distance | 10-20 pixels | Distance-based |

---

## Python Implementation
```python
import numpy as np

def nms_boxes(boxes, scores, iou_threshold=0.5):
    """
    boxes: (N, 4) array of [x1, y1, x2, y2]
    scores: (N,) array of confidence scores
    """
    # Sort by score
    indices = np.argsort(scores)[::-1]
    
    keep = []
    while len(indices) > 0:
        # Pick box with highest score
        current = indices[0]
        keep.append(current)
        
        if len(indices) == 1:
            break
        
        # Compute IoU with remaining boxes
        ious = compute_iou(boxes[current], boxes[indices[1:]])
        
        # Keep boxes with IoU below threshold
        mask = ious <= iou_threshold
        indices = indices[1:][mask]
    
    return keep

def compute_iou(box1, boxes):
    """Compute IoU between one box and multiple boxes."""
    x1 = np.maximum(box1[0], boxes[:, 0])
    y1 = np.maximum(box1[1], boxes[:, 1])
    x2 = np.minimum(box1[2], boxes[:, 2])
    y2 = np.minimum(box1[3], boxes[:, 3])
    
    intersection = np.maximum(0, x2 - x1) * np.maximum(0, y2 - y1)
    
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    union = area1 + area2 - intersection
    
    return intersection / union

# OpenCV NMS
import cv2
indices = cv2.dnn.NMSBoxes(boxes, scores, 
                           score_threshold=0.5,
                           nms_threshold=0.4)
```
