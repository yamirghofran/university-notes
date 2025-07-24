---
title: Decision Tree
---

The decision tree algorithm is a [supervised](/machine-learning-foundations/supervised-learning) machine learning method used for both #ml/classification and #ml/regression tasks. It works by recursively splitting the dataset into subsets based on [Feature](/machine-learning-foundations/feature-vector) values, creating a tree-like structure of decisions. Each internal node represents a decision based on a feature, each branch represents the outcome of that decision, and each leaf node represents a final prediction (class label or continuous value).
![](../attachments/cleanshot-2025-02-01-at-1038212x.png)
## How it works
1. **Input Data:**
   - A dataset with labeled examples (for classification) or continuous target values (for regression).
   - Each example is represented as a set of features.
2. **Tree Construction:**
   - The algorithm starts at the root node and recursively splits the data into subsets based on feature values.
   - The goal is to create splits that maximize the homogeneity (**purity**) of the resulting subsets.
3. **Splitting Criteria:**
   - The choice of feature and split point is determined by a splitting criterion:
     - For #ml/classification:
       - [Gini Index](/machine-learning-foundations/gini-index)
       - [Entropy](/machine-learning-foundations/entropy)
       - [Information Gain](/machine-learning-foundations/information-gain)
     - For #ml/regression :
       - **Variance Reduction**: Splits are chosen to minimize the variance of the target variable in the resulting subsets.
4. **Stopping Conditions:**
   - The recursion stops when one of the following conditions is met:
     - All samples in a node belong to the same class (for classification).
     - The target values in a node are sufficiently homogeneous (for regression).
     - A predefined maximum depth is reached.
     - Further splits do not improve the model significantly (based on a threshold).
5. **Leaf Nodes:**
   - For #ml/classification : the leaf node predicts the majority class of the samples in that node.
   - For #ml/regression: The leaf node predicts the average (or median) target values of the samples in that node.

## Evaluation
- [Accuracy](/machine-learning-foundations/accuracy)
- [Mean Squared Error](/machine-learning-foundations/mean-squared-error)
## Advantages
-  Easy to interpret and visualize (white-box model).
-  Handles both numerical and categorical data.
-  Requires little data preprocessing (e.g., no need for [feature scaling](/machine-learning-foundations/feature-scaling)).
-  Robust to outliers.
## Disadvantages
-  Prone to overfitting, especially with deep trees without pruning.
-  Can be unstable; small changes in the data may lead to different trees.
-  Biased toward features with more levels or categories.
-  May not perform well on datasets with complex relationships (e.g., XOR problems).

## Popular Decision Tree Algorithms
1. **ID3 (Iterative Dichotomiser 3):**
   - Uses [information gain](/machine-learning-foundations/information-gain) for splitting.
   - Handles categorical features only.
2. **C4.5:**
   - An extension of ID3 that handles both categorical and numerical features.
   - Uses information gain ratio to reduce bias toward features with many levels.
3. **CART (Classification and Regression Trees):**
   - Uses [Gini](/machine-learning-foundations/gini-index) impurity for classification and variance reduction for regression.
   - Supports binary splits only.
4. [Random Forest](/machine-learning-foundations/random-forest)
   - An [ensemble method](/machine-learning-foundations/ensemble-methods) that builds multiple decision trees and combines their predictions to improve accuracy and reduce overfitting.
5. **Gradient Boosted Trees:**
   - Builds trees sequentially, with each tree correcting the errors of the previous one.
## Applications
-  Customer segmentation
-  Fraud detection
-  Medical diagnosis
-  Predictive modeling
-  Natural language processing (e.g., parsing sentences)
