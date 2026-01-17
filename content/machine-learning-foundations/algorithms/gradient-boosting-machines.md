---
title: Gradient Boosting Machines
---

 [Ensemble Methods](/machine-learning-foundations/algorithms/ensemble-methods) that build models by combining multiple weak learners (typically [Decision Tree](/machine-learning-foundations/algorithms/decision-tree)s) to create a strong predictive model (e.g. [Random Forest](/machine-learning-foundations/algorithms/random-forest)).
- XGBoost
- LightGBM
- CatBoost

## How it works
- Minimize a **loss function** (e.g. [MSE](/machine-learning-foundations/evaluation-metrics/mean-squared-error), log loss) using [Gradient Descent](/machine-learning-foundations/deep-learning/gradient-descent) and iteratively improve the model.
1. **Initialization**: Simple model to predict mean value ( #ml/regression ) or uniform probabilities #ml/classification .
2. **Compute residuals**: difference between observed values and model predictions (residuals).
3. **Fit a weak learner**: train it to predict the residuals from the previous step.
4. **Update the model**: Add the predictions from the weak learner to the model, scaled by a **learning rate**.
5. **Iterate**: until matching a stopping criterion (e.g. num. iterations, no improvement in performance).
## Preconditions
- [Hyperparameter](/machine-learning-foundations/introduction/parameters-and-hyperparameters) tuning (learning rate)
- [Regularization](/machine-learning-foundations/regularization/regularization) (prevent overfitting)
## Evaluation
- Classification
	- [Accuracy](/machine-learning-foundations/evaluation-metrics/accuracy)
	- [Precision](/machine-learning-foundations/evaluation-metrics/precision)
	- [Recall](/machine-learning-foundations/evaluation-metrics/recall)
	- F-1 Score
	- [AUC-ROC](/machine-learning-foundations/evaluation-metrics/auc-roc)
- Regression
	- [MSE](/machine-learning-foundations/evaluation-metrics/mean-squared-error)
	- [MAE](/machine-learning-foundations/evaluation-metrics/mean-absolute-error)
	- [R-squared](/machine-learning-foundations/evaluation-metrics/r-squared)
## Advantages
- High predictive accuracy
- Handles non-linear relationships
## Limitations
- Computationally expensive
- Sensitive to ?