---
title: Cosine Similarity
---

Given two vectors $a = (a_1, a_2, \ldots, a_n)$ and $b = (b_1, b_2, \ldots, b_n)$, the cosine similarity is defined as:
$$

\cos \theta = \frac{a \cdot b}{\|a\| \|b\|}
$$


where:
- $a \cdot b$ is the dot product of $a$ and $b$
- $\|a\|$ and $\|b\|$ are the magnitudes (or [norm](/matrices-and-linear-transformations/vector-norm-or-length)) of $a$ and $b$, respectively.
## Interpretation
The cosine similarity measures the cosine of the angle between the two vectors. The value of $\cos \theta$ ranges from -1 to 1, where:
- $\cos \theta = 1$ means the vectors are identical (i.e., the angle between them is 0°)
- $\cos \theta = -1$ means the vectors are opposite (i.e., the angle between them is 180°)
- $\cos \theta = 0$ means the vectors are orthogonal (i.e., the angle between them is 90°)
## Properties
- Cosine similarity is a measure of similarity, not distance.
- It is sensitive to the direction of the vectors, not their magnitude.
- It is often used in text analysis, information retrieval, and recommender systems.
## Example
Suppose we have two vectors:
- $a = (1, 2, 3)$
- $b = (4, 5, 6)$
The [Dot Product](/matrices-and-linear-transformations/dot-product) of $a$ and $b$ is:
$$

a \cdot b = (1 \cdot 4) + (2 \cdot 5) + (3 \cdot 6) = 4 + 10 + 18 = 32
$$


The magnitudes of $a$ and $b$ are:
$$

\|a\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}
$$


$$

\|b\| = \sqrt{4^2 + 5^2 + 6^2} = \sqrt{77}
$$


The cosine similarity is:
$$

\cos \theta = \frac{32}{\sqrt{14} \cdot \sqrt{77}} \approx 0.97
$$


This means that the vectors $a$ and $b$ are very similar, with an angle of approximately 14° between them.
## Applications
Cosine similarity is widely used in:
- Text analysis and information retrieval
- Recommender systems
- Image and video analysis
- Natural language processing
- Machine learning and data mining