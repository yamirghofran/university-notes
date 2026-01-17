---
title: Precision-Recall Tradeoff
---

We have to choose a balance between [Precision](/machine-learning-foundations/evaluation-metrics/precision) and [Recall](/machine-learning-foundations/evaluation-metrics/recall) because we can't have both high. Increasing one decreases the other.

- **High precision**: model is conservative in predicting positives → high False Negatives as it misses some positives.
- **High recall**: model is liberal in predicting positives → high False Positives as it misses some negatives.

## Tuning the tradeoff
- We can assign a higher weight to the examples of a specific class. e.g. [SVM](/machine-learning-foundations/algorithms/support-vector-machines) in `scikit-learn` accepts weights of classes as input.
- By tuning [Hyperparameter](/machine-learning-foundations/introduction/parameters-and-hyperparameters)s to maximize either [Precision](/machine-learning-foundations/evaluation-metrics/precision) or [Recall](/machine-learning-foundations/evaluation-metrics/recall) on the [Validation Dataset](/machine-learning-foundations/data/training-and-holdout-datasets).
- By varying the decision threshold for algorithms that return prediction scores.
### Example
We have a [Logistic Regression](/machine-learning-foundations/algorithms/logistic-regression) model or a [Decision Tree](/machine-learning-foundations/algorithms/decision-tree). We can increase precision at the cost of a lower recall: we decide that the prediction will be positive only if the score returned by the model is higher than 0.9 (instead of the default value of 0.5)

## Single Metric
To compare two or more models, we want a single value that determines the precision-recall tradeoff. 

- Optimizing and satisficing technique
	- Depending on the problem, choose either precision or recall and fix one metric to a threshold. e.g. spam classification: choose precision, fix FN threshold to 2%.
	- Generalization: threshold n-1 metrics and optimize the nth.
- [F-Score](/machine-learning-foundations/evaluation-metrics/f-score)
- Simple average, or weighted average of metrics.
- Invent our own domain-specific metric.