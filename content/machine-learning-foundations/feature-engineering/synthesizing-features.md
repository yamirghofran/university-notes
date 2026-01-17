---
title: Synthesizing Features
---

## Feature Discretization
Discretizing a real-valued numerical feature can improve predictive accuracy with small datasets. 
Different **binning strategies** are converted back to numerical values for the ML algorithm.

## Synthesizing features from relational data
Reduce multiple tables to single features by computing statistics on data across tables.

## Synthesizing features from the data
[Clustering](/machine-learning-foundations/algorithms/clustering) is commonly used to synthesize one or more additional features.
e.g. [K-Means Clustering](/machine-learning-foundations/algorithms/k-means-clustering): 
1. Choose k
2. Apply clustering to the training data
3. Add k additional features to your feature vectors. 
Each feature is binary: 1 if the vector belongs to a cluster.

## Synthesizing features from other features
- (Deep) [Neural Networks](/machine-learning-foundations/deep-learning/neural-networks) with large amounts of data.
- Apply a simple transformation to one or a pair of existing features.
- Numerical features of the feature from [k-Nearest Neighbors](/machine-learning-foundations/algorithms/k-nearest-neighbors), found by using [[Minkowski Distances|Euclidean distance]] or [[Cosine Similarity]].
	- discretization
	- squaring
	- mean/standard deviation
- Pairs of numerical features: simple arithmetic operators
	- e.g. produce all the possible transformations for all the pairs and then select those that increase the quality of the model.