---
title: Feature Scaling
---

Bringing all features to the same/similar ranges of values or distributions.

Multiple experiments demonstrated that learning algorithms applied to scaled features might produce a better model.

Not guaranteed to have a positive impact on the quality of the model, but considered **best practice**. e.g. necessary for [L1-Regularization (Lasso Regression)](/machine-learning-foundations/regularization/l1-regularization-lasso-regression), can increase the training speed of deep neural networks.

Assures no individual feature dominates, especially in the initial iterations of gradient descent or other iterative optimization algorithms.

Reduces the risk of numerical overflow, a problem computers encounter when working with very small or very large numbers.

## Types of Scaling
- [[Y2Q2/Machine Learning Foundations/Feature Engineering/Normalization|Normalization]]
- [Standardization](/machine-learning-foundations/feature-engineering/standardization)

## When/how to use Normalization and Standardization
Applying simple mathematical transformations to the feature values prior to applying a scaling technique (e.g. logarithm, square, or square root) may help obtain a distribution as close as possible to a normal distribution.

Weak rule of thumb?
- Normalization tends to work better for uniformly distributed data.
- Standardization tends to work best for normally distributed data.
but data is rarely distributed following a perfect curve.

If we have the time and resources, we try and test both.
Feature scaling is usually beneficial to most learning algorithms.