---
title: Imbalanced Data
---

**Class imbalance** is the problem of very uneven distribution of labels in the training data. It can significantly affect the performance of the model, independently of the chosen learning algorithm.
 
e.g. if you have a classifier to distinguish between genuine and fraudulent e-commerce transactions, your data will have much more genuine transactions than fraudulent ones. If the **loss** in the **cost function** is the same for both types of mistakes, the model will make more mistakes (misclassify) on the minority (fraudulent) transactions.

Rule of thumb is 50-50. Slight imbalance like 60-40 is ok.

Extreme imbalance like 90-10 with equally weighted errors may not be effective and would need modification.

## Methods to mitigate class imbalance in Datasets
- [Oversampling](/machine-learning-foundations/data/oversampling)
- [Undersampling](/machine-learning-foundations/data/undersampling)
- hybrid strategies
	- e.g. [[ADASYN]] + [Tomek Links](/machine-learning-foundations/data/tomek-links)
## Methods to mitigate class imbalance in Training
- [Class Weighting](/machine-learning-foundations/data/class-weighting)
- [Ensemble of Resampled Datasets](/machine-learning-foundations/algorithms/ensemble-of-resampled-datasets)
- Other methods
	- If we use stochastic gradient descent, we can address class imbalance in 2 ways:
		- We can have different learning rates for different classes: a lower value for the majority class examples, and a higher value otherwise.
		- We can make several consecutive updates of the model parameters, each time we encounter an example of a minority class.
- Performance is measured using adapted performance metrics, e.g. per-class accuracy and Cohen's kappa statistic.