---
title: K-Means Clustering
---

K-means clustering is a popular unsupervised machine learning algorithm used for **partitioning** a dataset into K distinct, non-overlapping clusters. The goal is to group similar data points together based on their features, such that data points within the same cluster are more similar to each other than to those in other clusters. Here's a detailed explanation of K-means clustering:

## How K-means Clustering Works:

1. **Initialization**:
- Choose the number of clusters, K.
- Randomly initialize K centroids (cluster centers) from the dataset. These centroids can be chosen randomly or using more sophisticated methods like K-means++.
2. **Assignment Step**:
- Assign each data point to the nearest centroid. The distance between a data point and a centroid is typically measured using Euclidean distance, but other distance metrics can also be used.
1. **Update Step**:
- Recalculate the centroids as the mean of all data points assigned to each cluster. This step updates the positions of the centroids to be the center of mass of the data points in their respective clusters.
2. **Convergence**:
- Repeat the assignment and update steps until the centroids no longer change significantly, or a maximum number of iterations is reached. The algorithm converges when the assignments of data points to clusters stabilize.

## Mathematical Formulation:

Given a dataset X = {x₁, x₂, ..., xₙ} with n data points and K clusters, the K-means algorithm aims to minimize the within-cluster sum of squares (WCSS), also known as the inertia: WCSS = ∑ₖ₌₁ᵏ ∑ₓᵢ∈Cₖ ‖xᵢ - μₖ‖² where:

- Cₖ is the set of points in cluster k,
- μₖ is the centroid of cluster k,
- ‖xᵢ - μₖ‖ is the Euclidean distance between a data point xᵢ and the centroid μₖ.

## Steps in Detail:

3. **Initialization**:
- Choose K (number of clusters).
- Initialize K centroids randomly or using K-means++.
4. **Assignment Step**:
- For each data point xᵢ, calculate the distance to each centroid μₖ.
- Assign xᵢ to the cluster with the nearest centroid.
5. **Update Step**:
- For each cluster k, calculate the new centroid μₖ as the mean of all data points assigned to that cluster: μₖ = (1/|Cₖ|) ∑ₓᵢ∈Cₖ xᵢ
6. **Convergence**:
- Repeat the assignment and update steps until the centroids no longer change or a maximum number of iterations is reached.

| Point | Feature1 | Feature2 |
|-------|----------|----------|
| A     | 1.0      | 2.0      |
| B     | 1.5      | 1.8      |
| C     | 5.0      | 8.0      |
| D     | 8.0      | 8.0      |
| E     | 1.0      | 0.6      |
| F     | 9.0      | 11.0     |
## Limitations
- Assumes prior knowledge of data in order to choose the appropriate $k$.
- The final clusters are very sensitive to the selection of the initial centroids
- It can produce empty clusters.
- Problems with clusters of differing sizes, densities, and non-globular shapes, and outliers.
## Example:

Suppose we have a dataset with the following points: We want to cluster these points into K = 2 clusters.

7. **Initialization**:
- Randomly initialize two centroids, say (1.0, 2.0) and (5.0, 8.0).
8. **Assignment Step**:
- Calculate the distance of each point to the centroids and assign to the nearest centroid.
9. **Update Step**:
- Recalculate the centroids based on the assigned points.
10. **Convergence**:
- Repeat the assignment and update steps until the centroids stabilize.

## Implementation in Python (using scikit-learn):

```python import numpy as np from sklearn.cluster import KMeans import matplotlib.pyplot as plt

## Sample data

data = np.array([[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]])

## Number of clusters

K = 2

## K-means clustering

kmeans = KMeans(n_clusters=K, random_state=42) kmeans.fit(data)

## Centroids

centroids = kmeans.cluster_centers_ print("Centroids:", centroids)

## Labels

labels = kmeans.labels_ print("Labels:", labels)

## Plot the results

plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis') plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X') plt.show() ```

## Considerations:

- **Choice of K**: The number of clusters, K, is a hyperparameter that needs to be chosen carefully. Techniques like the Elbow Method, Silhouette Analysis, or Gap Statistics can help determine the optimal number of clusters.
- **Initialization**: The initial placement of centroids can affect the final clustering. K-means++ is a common initialization method that improves the algorithm's performance.
- **Convergence**: K-means is sensitive to the initial placement of centroids and can converge to a local minimum. Running the algorithm multiple times with different initializations and selecting the best result can help mitigate this issue.

## Conclusion:

K-means clustering is a simple and effective algorithm for partitioning a dataset into clusters. It is widely used in various applications, including image segmentation, market segmentation, and anomaly detection. However, it has limitations, such as sensitivity to the initial placement of centroids and the assumption of spherical clusters. Despite these limitations, K-means remains a popular choice due to its simplicity and efficiency.
