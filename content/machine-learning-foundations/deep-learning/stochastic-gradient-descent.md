---
title: Stochastic Gradient Descent
---

Optimization algorithm used to minimize a [Loss Function](/machine-learning-foundations/loss-function) by iteratively updating model parameters.
## How it works
- Linear model that uses stochastic gradient descent to optimize a regression or classification [Loss Function](/machine-learning-foundations/loss-function) (e.g. [MSE](/machine-learning-foundations/evaluation-metrics/mean-squared-error), Huber loss, epsilon-insensitive loss)
- Minimize a loss function by iteratively updating the model [Parameter](/machine-learning-foundations/introduction/parameters-and-hyperparameters)s in the direction of the negative gradient of the loss function ([Gradient Descent](/machine-learning-foundations/deep-learning/gradient-descent))
- Use a subset of data for each update, introducing randomness, which helps escape local minima and find better solutions in [Non-convex Optimization Problems](/machine-learning-foundations/deep-learning/non-convex-optimization-problems).
- Parameters ($\theta$) updating rule: $\theta = \theta - \eta \cdot \nabla L(\theta)$.
## Preconditions
- Learning rate [Hyperparameter](/machine-learning-foundations/introduction/parameters-and-hyperparameters) tuning
- [Feature Scaling](/machine-learning-foundations/feature-engineering/feature-scaling)
## Evaluation
- Regressor
	- [MSE](/machine-learning-foundations/evaluation-metrics/mean-squared-error)
	- [MAE](/machine-learning-foundations/evaluation-metrics/mean-absolute-error)
	- [R-squared](/machine-learning-foundations/evaluation-metrics/r-squared)
- Classifier
	- [Accuracy](/machine-learning-foundations/evaluation-metrics/accuracy)
	- [Precision](/machine-learning-foundations/evaluation-metrics/precision)
	- [Recall](/machine-learning-foundations/evaluation-metrics/recall)
	- F-1 Score
	- [AUC-ROC](/machine-learning-foundations/evaluation-metrics/auc-roc)
## Advantages
- Scalable
- Supports various classification paradigms
- Supports high-dimensional and sparse data
## Limitations
