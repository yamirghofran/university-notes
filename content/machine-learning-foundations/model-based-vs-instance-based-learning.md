---
title: Model-Based vs Instance-Based Learning
---

# Model-Based Learning
Most [supervised learning](/machine-learning-foundations/supervised-learning) algorithms are model-based.

Model-based learning algorithms use the training data to create a model with [parameters](/machine-learning-foundations/parameters-and-hyperparameters) learned from the training data.

After the model is trained, it can be saved on disk while the training data can be discarded.

# Instance-Based
Instance-based learning algorithms use the whole dataset as the model.

One instance-based learning algorithm frequently used in practice is [[Y2Q2/Machine Learning Foundations/k-Nearest Neighbors]]. In classification, to predict a label for an input example, the kNN algorithm looks at the close neighborhood of the input example in the space of feature vectors an outputs the label that it saw most often in this close neighborhood.