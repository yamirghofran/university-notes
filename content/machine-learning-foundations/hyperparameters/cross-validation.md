---
title: Cross-Validation
---

- Fix the values of the [Hyperparameter](/machine-learning-foundations/introduction/parameters-and-hyperparameters) to evaluate.
- Randomly split the training set into several subsets (folds) of the same size. Rule of thumb: 5 subsets.
- Train 5 models, each on 4 subsets, and use 1 different subset to validate each model.
- Compute value of the (pair of) hyperparameters of interest on each [Validation Dataset](/machine-learning-foundations/data/training-and-holdout-datasets) subset.
- Average the five values of the metric to get the final value.
- Generalization: in n-fold cross-validation, we train model fn on all folds, except for the n-th fold Fn