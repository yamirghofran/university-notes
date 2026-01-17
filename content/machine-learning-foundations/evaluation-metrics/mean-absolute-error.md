---
title: Mean Absolute Error
---

A measure of the average **absolute difference** between actual and predicted values in regression analysis.
$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$
-  ${y_i}$: observed value
-  ${\hat{y}_i}$: predicted value
-  ${n}$: number of observations

## Purpose
Quantifies prediction accuracy; lower values indicate better performance.

## Properties
-  Non-negative: MAE is always zero or positive.
-  Less sensitive to outliers compared to MSE.
---
## Related to
- [MSE](/machine-learning-foundations/evaluation-metrics/mean-squared-error)