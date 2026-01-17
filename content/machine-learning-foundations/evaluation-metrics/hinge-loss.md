---
title: Hinge Loss
---

A measure of the difference between the true labels and the predicted labels in binary classification tasks, commonly used in [Support Vector Machines](/machine-learning-foundations/algorithms/support-vector-machines) (SVMs).
$$
\text{Hinge Loss} = \frac{1}{n} \sum_{i=1}^{n} \max(0, 1 - y_i \hat{y}_i)
$$
-  ${y_i}$: true label ({+1} or {-1})
-  ${\hat{y}_i}$: predicted label

## Purpose
Measures the performance of a binary classification model; lower values indicate better performance.

## Properties
-  Non-negative: Hinge Loss is always zero or positive.
-  Encourages a large margin between classes.
