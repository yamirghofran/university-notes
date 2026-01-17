---
title: Naive Bayes
---

## What it does
- Based on [[Baye's Theorem]]
- It assumes that features are conditionally independent given the class label.
- Simplifies computation and often performs well in practice, despite the naive assumption.
$$
P(C|X) = \frac{P(X|C) \cdot P(C)}{P(X)}
$$

-  **$P(C|X)$**: Posterior probability (probability of the class given the features).
-  **$P(X|C)$**: Likelihood (probability of the features given the class).
-  **$P(C)$**: Prior probability (probability of the class occurring).
-  **$P(X)$**: Evidence (probability of the features).

## How it works
- 3 types
	- Gaussian (continuous data)
	- Multinomial (discrete data)
	- Bernoulli (binary)
- If a [Feature](/machine-learning-foundations/feature-engineering/feature-vector) value doesn't appear in the training data for a class, it results in zero probability for that class (can be addressed using [Laplace Smoothing](/machine-learning-foundations/regularization/laplace-smoothing))
- Calculates posterior probabilities.
## Preconditions
- Conditional independence rarely holds in the real world.
- Requires minimal training data and has few parameters to tune.
## Evaluation
- Performance can degrade when features are highly correlated.
- [Accuracy](/machine-learning-foundations/evaluation-metrics/accuracy)
- [Precision](/machine-learning-foundations/evaluation-metrics/precision)
- [Recall](/machine-learning-foundations/evaluation-metrics/recall)
- F-1 Score
- [AUC-ROC](/machine-learning-foundations/evaluation-metrics/auc-roc)
## Advantages
- Fast and efficient
- Simple to implement
- Performs well with small data
- Handles high-dimensional data
## Limitations
- Assumes independence of features
- Struggles with zero probabilities