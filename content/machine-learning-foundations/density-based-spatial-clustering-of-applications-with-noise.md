---
title: Density-Based Spatial Clustering of Applications with Noise
---

Density-Based Spatial Clustering of Applications with Noise (DBSCAN) is a popular clustering algorithm used in data mining and machine learning. It is particularly effective for identifying clusters of varying shapes and sizes in a dataset, and it can also handle [Data Noise](/machine-learning-foundations/data-noise) ([Outliers](/machine-learning-foundations/outliers)) effectively. Here's a detailed explanation of DBSCAN:

## Key Concepts

1. **Density**: DBSCAN defines clusters as areas of high density separated by areas of low density. The density is determined by two main parameters:
	- **EPS (ε)**: The maximum distance between two points for them to be considered as in the same neighborhood.
	- **MinPts**: The minimum number of points required to form a dense region (or cluster).
2. **Core Points**: A point is a core point if it has at least MinPts neighbors within a distance of EPS.
3. **Border Points**: A point is a border point if it has fewer than MinPts neighbors within EPS but is in the neighborhood of a core point.
4. **Noise Points**: Points that are neither core points nor border points are considered noise.

## Algorithm Steps

1. **Initialization**: Start with an arbitrary point that has not been visited.
2. **Neighborhood Query**: Retrieve all points within EPS distance from the current point.
3. **Core Point Check**: If the current point is a core point (i.e., it has at least MinPts neighbors), create a new cluster with this point as the first point.
4. **Cluster Expansion**:
	- For each neighboring point, if it has not been visited, mark it as visited and retrieve its neighbors.
	- If a neighboring point is a core point, add its neighbors to the cluster.
	- Repeat the process until all reachable points have been added to the cluster.
5. **Noise Identification**: If the current point is not a core point and is not reachable from any core point, it is labeled as noise.
6. **Repeat**: Repeat the process for all unvisited points until all points have been processed.

## Advantages

- **No Need for Predefined Number of Clusters**: Unlike algorithms like K-Means, DBSCAN does not require the number of clusters to be specified in advance.
- **Handles Noise**: DBSCAN can effectively identify and separate noise points from clusters.
- **Flexible Shape**: It can find clusters of arbitrary shape, not just spherical or convex shapes.

## Disadvantages

- **Parameter Sensitivity**: The performance of DBSCAN is highly dependent on the choice of EPS and MinPts. Incorrect values can lead to poor clustering results.
- **Memory Usage**: For large datasets, DBSCAN can be memory-intensive due to the need to store and process neighborhood information.
- **Scalability**: The algorithm can be computationally expensive for very large datasets, although optimizations and variants exist to mitigate this.

## Applications

DBSCAN is widely used in various fields, including:

- **Image Segmentation**: Identifying objects or regions in images.
- **Anomaly Detection**: Detecting outliers in data, such as fraud detection in financial transactions.
- **Geospatial Analysis**: Clustering spatial data points, such as customer locations.
- **Bioinformatics**: Clustering gene expression data or protein structures.

## Example

Consider a dataset of 2D points. DBSCAN can be used to cluster these points based on their density. By setting appropriate values for EPS and MinPts, the algorithm will identify dense regions (clusters) and separate them from sparse regions (noise).
