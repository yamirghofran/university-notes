---
title: k-Nearest Neighbors
---

#ml/algorithms
The k-nearest neighbors (KNN) algorithm is a simple, intuitive, and widely used machine learning algorithm for #ml/classification and #ml/regression tasks. It is a type of [Instance-Based](/machine-learning-foundations/model-based-vs-instance-based-learning) learning (or lazy learning), meaning it does not explicitly learn a model during training but instead stores the entire dataset and makes predictions based on similarity measures at inference time.

## How it works
1. **Input Data:**
   - A dataset with labeled examples (for classification) or continuous target values (for regression).
   - Each example is represented as a feature vector in a multidimensional space.
2. **Distance Metric:**
   - KNN relies on a distance metric to measure the similarity between data points.
   - Common distance metrics include [Minkowski Distances](/matrices-and-linear-transformations/minkowski-distances) and [Cosine Similarity](/matrices-and-linear-transformations/cosine-similarity)
3. **Choosing $k$:**
   - $k$ is a user-defined parameter representing the number of nearest neighbors to consider.
   - A small $k$ (e.g., 1) makes the algorithm sensitive to noise, while a large $k$ smooths out predictions but may include irrelevant neighbors.
4. **Prediction:**
   - For a new, unlabeled data point:
     - Calculate the distance between the new point and all points in the training dataset.
     - Identify the $k$ nearest neighbors (the $k$ points with the smallest distances).
     - For #ml/classification : Use majority voting among the $k$ neighbors to assign the class label.
     - For #ml/regression: Use the average (or weighted average) of the target values of the $k$ neighbors.
5. **Output:**
   - The predicted class (for classification) or value (for regression) for the new data point.
## Key Considerations
### **Choice of $k$:**
   - A small $k$ leads to high variance and low bias (overfitting).
   - A large $k$ leads to low variance and high bias (underfitting).
   - $k$ is often chosen using cross-validation.
### **[Feature Scaling](/machine-learning-foundations/feature-scaling):**
   - KNN is sensitive to the scale of features, so normalization or standardization is often required.
### **Computational Complexity:**
   - KNN can be computationally expensive for large datasets because it requires calculating distances for all training points during inference.
   - Optimizations like KD-trees or Ball trees can speed up neighbor searches.
### **Curse of Dimensionality:**
   - In high-dimensional spaces, distances between points become less meaningful, reducing the effectiveness of KNN.

## Advantages
- Simple to understand and implement
- Adabtable
- No training phase (lazy learning)
- Naturally handles multi-class classification
## Disadvantages
- Computationally and memory expensive for large datasets
- Sensitive to irrelevant or redundant [Feature](/machine-learning-foundations/feature-vector)s (noise).
- Requires careful tuning of k and distance metrics.
## Applications
- Image Recognition
- Recommendation systems
- Medical diagnosis
- Anomaly detection
