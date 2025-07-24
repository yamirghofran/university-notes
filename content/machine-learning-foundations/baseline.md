---
title: Baseline
---

Used to evaluate the performance of the ML algorithm compared to simpler/naive/trivial solutions.

A model or algorithm that provides a reference point for comparison:
- rule-based algorithm
- heuristic algorithm
- a simple statistic about training data
- another ml algorithm
- etc

## Random Prediction
Throwing a dice but be careful and look at the probability distributions
- classification: randomly picking a class from all the classes of the problem.
- regression: randomly selecting a target from all unique target values in the training data.
## Zero Rule
- classification: predict the most common class in the [Training Dataset](/machine-learning-foundations/training-and-holdout-datasets), independent of the input value.E.g., 100 records, 80 non-span, 20 spam. Baseline: 80% accuracy.
- regression: predict the sample average of the target values in the training data.
## Machine Learning
- Text classification, machine translation: [SVM](/machine-learning-foundations/support-vector-machines) with a linear kernel.
- General numerical dataset: [[Y2Q2/Machine Learning Foundations/Linear Regression|Linear Regression]] or [[Y2Q2/Machine Learning Foundations/Logistic Regression|Logistic Regression]] or [[Y2Q2/Machine Learning Foundations/k-Nearest Neighbors|kNN]] (k=5)
- Image classification: [SVM](/machine-learning-foundations/support-vector-machines) with linear kernel, convolutional [[neural network]].
## Rule-based or groups of humans
- e.g. doctors.