---
title: Hierarchical Clustering
---

Hierarchical clustering is a popular [Clustering](/machine-learning-foundations/algorithms/clustering) technique used in data mining and machine learning to group similar data points into clusters. Unlike partitioning methods such as [K-Means](/machine-learning-foundations/algorithms/k-means-clustering), hierarchical clustering does not require the number of clusters to be specified in advance. Instead, it creates a hierarchy of clusters that can be visualized as a dendrogram. Here's a detailed explanation of hierarchical clustering:

## Key Concepts

1. **Dendrogram**: A tree-like diagram that represents the nested grouping of data points. The dendrogram shows the sequence of merges or splits and the distance between clusters at each level.
2. **Agglomerative Clustering**: A bottom-up approach where each data point starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.
3. **Divisive Clustering**: A top-down approach where all data points start in one cluster, and splits are performed recursively as one moves down the hierarchy.
4. **Linkage Criteria**: The method used to measure the distance between clusters. Common linkage criteria include:
	- **Single Linkage**: The minimum distance between any single point in the first cluster and any single point in the second cluster.
	- **Complete Linkage**: The maximum distance between any single point in the first cluster and any single point in the second cluster.
	- **Average Linkage**: The average distance between all points in the first cluster and all points in the second cluster.
	- **Centroid Linkage**: The distance between the centroids of the two clusters.
	- **Ward's Method**: Minimizes the variance within clusters.

## Algorithm Steps (Agglomerative)

1. **Initialization**: Start with each data point as its own cluster.
2. **Distance Matrix**: Compute the distance [[matrix]] for all pairs of data points.
3. **Merge Clusters**: Find the pair of clusters with the smallest distance according to the chosen linkage criterion and merge them into a single cluster.
4. **Update Distance Matrix**: Update the distance matrix to reflect the new cluster configuration.
5. **Repeat**: Repeat steps 3 and 4 until all data points are in a single cluster or a stopping criterion is met (e.g., a desired number of clusters).
6. **Dendrogram Construction**: Construct a dendrogram to visualize the hierarchy of clusters.

## Algorithm Steps (Divisive)

1. **Initialization**: Start with all data points in a single cluster.
2. **Split Clusters**: Find the cluster that can be split into two clusters that maximize the chosen criterion (e.g., minimize within-cluster variance).
3. **Update Clusters**: Replace the original cluster with the two new clusters.
4. **Repeat**: Repeat steps 2 and 3 until each data point is in its own cluster or a stopping criterion is met.
5. **Dendrogram Construction**: Construct a dendrogram to visualize the hierarchy of clusters.

## Advantages

- **No Need for Predefined Number of Clusters**: Hierarchical clustering does not require the number of clusters to be specified in advance.
- **Dendrogram Visualization**: The dendrogram provides a visual representation of the clustering process, making it easy to interpret the results.
- **Flexibility**: Can handle different types of data and distance metrics.
- **Deterministic**: The results are deterministic and do not depend on random initialization.

## Disadvantages

- **Computational Complexity**: Hierarchical clustering can be computationally intensive, especially for large datasets, as it requires calculating and updating the distance matrix.
- **Scalability**: The algorithm may not scale well to very large datasets due to its quadratic time complexity.
- **Sensitivity to Noise**: The algorithm can be sensitive to noise and outliers, which can affect the clustering results.
- **Lack of Reassignment**: Once a data point is assigned to a cluster, it cannot be reassigned to another cluster, which can lead to suboptimal clustering.

## Applications

Hierarchical clustering is widely used in various fields, including:

- **Bioinformatics**: Clustering gene expression data or protein structures.
- **Image Segmentation**: Grouping similar pixels or regions in an image.
- **Market Research**: Segmenting customers based on purchasing behavior.
- **Anomaly Detection**: Identifying outliers in data.
- **Document Clustering**: Grouping similar documents based on textual content.

## Example

Consider a dataset of 2D points. Agglomerative hierarchical clustering can be used to group these points into clusters. By starting with each point in its own cluster and repeatedly merging the closest pairs of clusters, the algorithm will create a hierarchy of clusters. The dendrogram will show the sequence of merges and the distance between clusters at each level, allowing for easy interpretation of the clustering results.

## Conclusion

Hierarchical clustering is a versatile and intuitive clustering technique that provides a hierarchical representation of data. Its ability to handle different types of data and distance metrics, along with the visual representation of the dendrogram, makes it a valuable tool in many data mining and machine learning applications. However, its computational complexity and sensitivity to noise should be considered when applying it to large or noisy datasets.
