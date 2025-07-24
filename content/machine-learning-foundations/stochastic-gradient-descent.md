---
title: Stochastic Gradient Descent
---

Optimization algorithm used to minimize a [loss function](/machine-learning-foundations/loss-function) by iteratively updating model parameters.
## How it works
- Linear model that uses stochastic gradient descent to optimize a regression or classification [Loss Function](/machine-learning-foundations/loss-function) (e.g. [MSE](/machine-learning-foundations/mean-squared-error), Huber loss, epsilon-insensitive loss)
- Minimize a loss function by iteratively updating the model [Parameter](/machine-learning-foundations/parameters-and-hyperparameters)s in the direction of the negative gradient of the loss function ([Gradient Descent](/machine-learning-foundations/gradient-descent))
- Use a subset of data for each update, introducing randomness, which helps escape local minima and find better solutions in [non-convex optimization problems](/machine-learning-foundations/non-convex-optimization-problems).
- Parameters ($\theta$) updating rule: $\theta = \theta - \eta \cdot \nabla L(\theta)$.
## Preconditions
- Learning rate [Hyperparameter](/machine-learning-foundations/parameters-and-hyperparameters) tuning
- [Feature Scaling](/machine-learning-foundations/feature-scaling)
## Evaluation
- Regressor
	- [MSE](/machine-learning-foundations/mean-squared-error)
	- [MAE](/machine-learning-foundations/mean-absolute-error)
	- [R Squared](/machine-learning-foundations/r-squared)
- Classifier
	- [Accuracy](/machine-learning-foundations/accuracy)
	- [Precision](/machine-learning-foundations/precision)
	- [Recall](/machine-learning-foundations/recall)
	- F-1 Score
	- [AUC-ROC](/machine-learning-foundations/auc-roc)
## Advantages
- Scalable
- Supports various classification paradigms
- Supports high-dimensional and sparse data
## Limitations
