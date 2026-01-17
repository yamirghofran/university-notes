---
title: Adaptive Synthetic Sampling Method (ADASYN)
---

ADASYN is an extension of [SMOTE](/machine-learning-foundations/data/synthetic-minority-oversampling-technique-smote) that adaptively generates synthetic samples for the minority class, focusing on harder-to-learn examples.

## How it works
- Calculates the density distribution of the minority class.
- Generates more synthetic samples for minority class instances that are harder to classify (i.e., closer to the decision boundary).
- Uses a weighted distribution to emphasize underrepresented regions.

## Advantages
- Reduces bias introduced by class imbalance.
- Improves learning for difficult minority class samples.
## Limitations
- Computationally more expensive than SMOTE.
- May still generate noisy samples if the dataset has outliers.