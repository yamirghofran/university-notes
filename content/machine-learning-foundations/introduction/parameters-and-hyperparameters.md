---
title: Parameters and Hyperparameters
---

# Hyperparameters
Inputs of ML algorithms that influence the performance of the model.
They're not part of the [Training Dataset](/machine-learning-foundations/data/training-and-holdout-datasets) and cannot be learned from them.
- [Hypterparameter Tuning](/machine-learning-foundations/hyperparameters/hypterparameter-tuning)

e.g.
- Maximum depth of the tree in the [Decision Tree](/machine-learning-foundations/algorithms/decision-tree) learning algorithm
- Misclassification penalty in [Support Vector Machines](/machine-learning-foundations/algorithms/support-vector-machines).
- `k` in the [kNN](/machine-learning-foundations/algorithms/k-nearest-neighbors) algorithm
- Target dimensionality in [Dimensionality Reduction](/machine-learning-foundations/feature-engineering/dimensionality-reduction).

# Parameters
Variables that define the model trained by the learning algorithm.

Parameters are directly modified by the learning algorithm based on the training data.
The goal of learning is to find such values of parameters that make the model optimal in a certain sense.

e.g.
- `w` and `b` in the equation of linear regression `y = wx + b`