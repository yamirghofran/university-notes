---
title: Precision-Recall Tradeoff
---

We have to choose a balance between [Precision](/machine-learning-foundations/precision) and [Recall](/machine-learning-foundations/recall) because we can't have both high. Increasing one decreases the other.

- **High precision**: model is conservative in predicting positives → high False Negatives as it misses some positives.
- **High recall**: model is liberal in predicting positives → high False Positives as it misses some negatives.

## Tuning the tradeoff
- We can assign a higher weight to the examples of a specific class. e.g. [SVM](/machine-learning-foundations/support-vector-machines) in `scikit-learn` accepts weights of classes as input.
- By tuning [Hyperparameter](/machine-learning-foundations/parameters-and-hyperparameters)s to maximize either [Precision](/machine-learning-foundations/precision) or [Recall](/machine-learning-foundations/recall) on the [Validation Dataset](/machine-learning-foundations/training-and-holdout-datasets).
- By varying the decision threshold for algorithms that return prediction scores.
### Example
We have a [logistic regression](/machine-learning-foundations/logistic-regression) model or a [decision tree](/machine-learning-foundations/decision-tree). We can increase precision at the cost of a lower recall: we decide that the prediction will be positive only if the score returned by the model is higher than 0.9 (instead of the default value of 0.5)

## Single Metric
To compare two or more models, we want a single value that determines the precision-recall tradeoff. 

- Optimizing and satisficing technique
	- Depending on the problem, choose either precision or recall and fix one metric to a threshold. e.g. spam classification: choose precision, fix FN threshold to 2%.
	- Generalization: threshold n-1 metrics and optimize the nth.
- [F-score](/machine-learning-foundations/f-score)
- Simple average, or weighted average of metrics.
- Invent our own domain-specific metric.