---
title: Support Vector Machines
---

## What it does
It finds the optimal boundary ([hyperplane](/machine-learning-foundations/hyperplane)) with the maximum margin that separates data points from different classes (i.e. classifier), ensuring robust generalization to unseen data.

## How it works
- Identifies the hyperplane that best separates data points of different classes.
- For non-linearly separable data, SVM uses a kernel trick, i.e., mathematical functions that transform data into higher dimensions, e.g. Polynomial Kernel or Radials Basis Function (RBF)

## Preconditions
- Scaled data
- Minimal noise

## Evaluation
- [Precision](/machine-learning-foundations/evaluation-metrics/precision)
- [Accuracy](/machine-learning-foundations/evaluation-metrics/accuracy)
- [Recall](/machine-learning-foundations/evaluation-metrics/recall)
- [AUC-ROC](/machine-learning-foundations/evaluation-metrics/auc-roc)
- F-1 score
- [MSE](/machine-learning-foundations/evaluation-metrics/mean-squared-error)
- [R-squared](/machine-learning-foundations/evaluation-metrics/r-squared)
## Advantages
- Effective in high dimensions
- Robust to overfitting
- Versatile
## Limitations
- Computationally complex
- Requires tuning
- Difficult to interpret
