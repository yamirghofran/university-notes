---
title: L1-Regularization (Lasso Regression)
---

- **Regularizing a model**: modify the objective function by adding a **penalizing term** whose value is higher when the model is more complex.
  $$
  \min_{w^{(1)}, w^{(2)}, b} \left[ C \times \left( |w^{(1)}| + |w^{(2)}| \right) + \frac{1}{N} \times \sum_{i=1}^{N} (f_i - y_i)^2 \right]
  $$
- Where $C$ is a hyperparameter that controls the importance of regularization.
- $C = 0$: standard non-regularized linear regression model.
- $C$ = high value: the learning algorithm tries to set most $w^{(\cdot)}$ to $\approx 0$ to minimize the objective. The model becomes very simple and likely undefined.
- **Goal**: find a value of the hyperparameter $C$ that doesn’t increase the bias too much but reduces the [variance](/machine-learning-foundations/hyperparameters/bias-variance-tradeoff) to a level appropriate to the given problem.
