---
title: L2 Regularization (Ridge)
---

$$
\min_{w^{(1)}, w^{(2)}, b} \left[ C \times \left( (w^{(1)})^2 + (w^{(2)})^2 \right) + \frac{1}{N} \times \sum_{i=1}^{N} (f_i - y_i)^2 \right]
$$

-   L1 regularization produces a sparse model (assuming the value of hyperparameter \(C\) is large enough), i.e., a model where most of its parameters equal exactly zero.
-   L1 implicitly performs feature selection by deciding which features are essential for prediction and which are not.
-   L1 is a good choice when we want to increase model explainability.
-   L2 is a good choice to **maximize the model performance on the holdout data**.
-   In the literature, L1 = lasso; L2 = ridge regularization.
