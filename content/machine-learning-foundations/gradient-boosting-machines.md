---
title: Gradient Boosting Machines
---

 z[Ensemble Methods](/machine-learning-foundations/ensemble-methods) that build models by combining multiple weak learners (typically [Decision Tree](/machine-learning-foundations/decision-tree)s) to create a strong predictive model (e.g. [Random Forest](/machine-learning-foundations/random-forest)).
- XGBoost
- LightGBM
- CatBoost

## How it works
- Minimize a **loss function** (e.g. [MSE](/machine-learning-foundations/mean-squared-error), log loss) using [Gradient Descent](/machine-learning-foundations/gradient-descent) and iteratively improve the model.
1. **Initialization**: Simple model to predict mean value ( #ml/regression ) or uniform probabilities #ml/classification .
2. **Compute residuals**: difference between observed values and model predictions (residuals).
3. **Fit a weak learner**: train it to predict the residuals from the previous step.
4. **Update the model**: Add the predictions from the weak learner to the model, scaled by a **learning rate**.
5. **Iterate**: until matching a stopping criterion (e.g. num. iterations, no improvement in performance).
## Preconditions
- [Hyperparameter](/machine-learning-foundations/parameters-and-hyperparameters) tuning (learning rate)
- [Regularization](/machine-learning-foundations/regularization) (prevent overfitting)
## Evaluation
- Classification
	- [Accuracy](/machine-learning-foundations/accuracy)
	- [Precision](/machine-learning-foundations/precision)
	- [Recall](/machine-learning-foundations/recall)
	- F-1 Score
	- [AUC-ROC](/machine-learning-foundations/auc-roc)
- Regression
	- [MSE](/machine-learning-foundations/mean-squared-error)
	- [MAE](/machine-learning-foundations/mean-absolute-error)
	- [[Y2Q2/Machine Learning Foundations/R-squared|R-squared]]
## Advantages
- High predictive accuracy
- Handles non-linear relationships
## Limitations
- Computationally expensive
- Sensitive to ?