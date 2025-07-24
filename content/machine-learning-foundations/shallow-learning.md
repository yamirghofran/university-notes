---
title: Shallow Learning
---

Learn the [parameters](/machine-learning-foundations/parameters-and-hyperparameters) of the model directly from the features of the training examples.

Traditional ML is shallow and relies on manually engineered features ([Feature Engineering](/machine-learning-foundations/feature-engineering)) and relatively simple models like linear/logistic regression, decision trees.

When compared to Deep Learning, 
- Training shallow models is computationally **cheaper**.
- Performs well on **small/medium-sized** datasets.
- Struggles with **complex patterns** and **unstructured data** (e.g. images, audio)
## Shallow Learning Strategy
1. Define a [performance metric](/machine-learning-foundations/model-performance-metrics) P and a [Baseline](/machine-learning-foundations/baseline) B.
2. Shortlist [learning algorithms](/machine-learning-foundations/selecting-the-learning-algorithm) #ml/algorithms .
3. Choose a [Hypterparameter Tuning](/machine-learning-foundations/hypterparameter-tuning) strategy T.
4. Pick a learning algorithm A.
5. Pick a combination H of hyperparameter values for algorithm A using strategy T.
6. Use the training set and train a model M using algorithm A parametrized with [Hyperparameter](/machine-learning-foundations/parameters-and-hyperparameters) values H.
7. Use the [Validation Dataset](/machine-learning-foundations/training-and-holdout-datasets) and calculate the value of metric P for model M.
8. Decide:
	- If there are still untested hyperparameter values, pick another combination H of hyperparameter values using strategy T and go back to step 6.
	- Otherwise, pick a different learning algorithm A and go back to step 5, or proceed to step 9 if there are no more learning algorithms to try.
9. Return the model for which the value of metric P is maximized.
10. Compare performace of the returned model to baseline B.