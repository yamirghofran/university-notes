---
title: Bias-Variance Tradeoff
---

[Hypterparameter Tuning](/machine-learning-foundations/hyperparameters/hypterparameter-tuning) controls two tradeoffs: [Precision-Recall Tradeoff](/machine-learning-foundations/evaluation-metrics/precision-recall-tradeoff) and the Bias-Variance  tradeoff.

In practice, by trying to reduce variance, you increase bias, and vice versa. i.e. reducing [Overfitting](/machine-learning-foundations/evaluation-metrics/overfitting) leads to [Underfitting](/machine-learning-foundations/evaluation-metrics/underfitting), and the other way around.

The most important factor is **model complexity**.

A sufficiently complex model will learn to memorize all training examples and their labels and, thus, will not make prediction errors when applied to the training data. It will have low bias. However, a model relying on memorization will not be able to correctly predict labels of previously unseen data. It will have high variance.

![](/machine-learning-foundations/attachments/cleanshot-2025-02-08-at-1938582x.png)

The "zone of solutions" is where both bias and variance are low. Once in this zone, you can do [Hypterparameter Tuning](/machine-learning-foundations/hyperparameters/hypterparameter-tuning) to reach the needed [Precision-Recall Tradeoff](/machine-learning-foundations/evaluation-metrics/precision-recall-tradeoff), or opimize another [Model Performance Metrics](/machine-learning-foundations/evaluation-metrics/model-performance-metrics) appropriate for your problem.

## How to reach zone of solutions
- Move to the right by increasing the complexity of the model, and , by doing so, reducing its bias.
- Move to the left by [regularizing](/machine-learning-foundations/regularization/regularization) the model to reduce variance by making the model simpler.

### Increasing Complexity
- In Shallow models like [Linear Regression](/machine-learning-foundations/algorithms/linear-regression), you can increase complexity by switching to a higher-order polynomial regression.
- In a [Decision Tree](/machine-learning-foundations/algorithms/decision-tree), increase the depth of the tree.
- In a [SVM](/machine-learning-foundations/algorithms/support-vector-machines), use polynomial or RBF kernels instead of linear kernel.
- In a [Neural Network](/machine-learning-foundations/deep-learning/neural-networks), increase its size: number of units per layer, and number of layers.