---
title: Mean Squared Error
---

A measure of the average squared difference between actual and predicted values in regression analysis.
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
- $y_i$: observed value
- $\hat{y}_i$: predicted value
- $n$: number of observations

Baseline: the mean model predicts the average of the training data labels and is the best model when no information about the target variable can be learned from the features.
## Purpose
Quantifies prediction accuracy; lower values indicate better performance.
## Properties
- Non-negative: MSE is always zero or positive.
- Penalizes large errors more due to squaring differences.
## Limitations
- Sensitive to [outliers](/machine-learning-foundations/outliers), as larger errors have a greater impact on the MSE.
- Units are squared units of the target variable, which may not be interpretable.
## Use Cases
Evaluating model fit and comparing different
models; often used alongside other metrics like RMSE (Root Mean Squared Error) for interpretability.

--- 
## Related to 
- [MAE](/machine-learning-foundations/mean-absolute-error)