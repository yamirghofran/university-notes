---
title: Outliers
---

Outliers are examples that look dissimilar to the majority of examples from the dataset. It's up to the data analyst to define "dissimilar". Typically, dissimilarity is measured by some distance metric, such as [[Minkowski Distances|Euclidean distance]].

In practice, however, what seems to be an outlier in the original [Feature Vector](/machine-learning-foundations/feature-engineering/feature-vector) space can be a typical example in a feature vector space transformed using tools such as a **kernel function**. Feature space transformation is often explicitly done by a kernel-based model, such as [Support Vector Machines](/machine-learning-foundations/algorithms/support-vector-machines), or implicitly by a deep [Neural Network](/machine-learning-foundations/deep-learning/neural-networks).

Some algorithms are more sensitive to outliers than others.

[Shallow Learning](/machine-learning-foundations/introduction/shallow-learning) algorithms, such as **linear** or **logistic regression** and some [Ensemble Methods](/machine-learning-foundations/algorithms/ensemble-methods), such as [AdaBoost](/machine-learning-foundations/algorithms/adaboost), are particularly sensitive to outliers.

A sufficiently complex [neural network](/machine-learning-foundations/deep-learning/neural-networks) can model each outlier very well with more complexity and cost.

Excluding outliers from the training data is debatable. Deleting examples from datasets isn't considered scientifically or methodologically sound, specially in small datasets. But, if their deletion leads to a performance boost, it might be justified.

A modern approach to getting such a measure is to build an [AutoEncoder](/machine-learning-foundations/algorithms/autoencoder) and use the **reconstruction error** as the measure of (dis)similarity: the higher the reconstruction error for a given example, the more dissimilar it is to the dataset.