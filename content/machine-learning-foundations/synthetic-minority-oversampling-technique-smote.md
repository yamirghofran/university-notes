---
title: Synthetic Minority Oversampling Technique (SMOTE)
---

SMOTE is an oversampling technique used to address class imbalance in datasets by generating synthetic samples for the minority class.

## How it works
- Selects a minority class sample and finds its k-nearest neighbors.
- Creates synthetic samples along the line segments connecting the selected sample and its neighbors.
- Introduces diversity in the minority class without direct replication.

## Advantages
- Reduces overfitting compared to random oversampling.
- Improves model performance on imbalanced datasets.

## Limitations
- Can create noisy samples if the minority class is not well-separated.
- Ignores the distribution of the majority class, potentially leading to overlapping classes.