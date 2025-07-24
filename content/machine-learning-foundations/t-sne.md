---
title: t-SNE
---

t-Distributed Stochastic Neighbor Embedding (t-SNE) is a popular technique for dimensionality reduction and visualization of high-dimensional data. It is particularly effective at preserving local structures and revealing the underlying patterns in the data. Here's a detailed explanation of t-SNE:

## Key Concepts

1. **Dimensionality Reduction**: t-SNE reduces the dimensionality of data, typically from high dimensions to 2 or 3, for visualization purposes.
2. **Probabilistic Model**: t-SNE uses a probabilistic model to measure similarities between data points in both the high-dimensional and low-dimensional spaces.
3. **Kullback-Leibler Divergence**: The algorithm minimizes the divergence between the high-dimensional and low-dimensional distributions to preserve local structures.
4. **t-Distribution**: t-SNE uses a t-distribution in the low-dimensional space to model the similarities, which helps in preserving both local and global structures.

## Mathematical Formulation

Given a dataset $\mathbf{X}$ with $n$ samples and $d$ features, the steps to perform t-SNE are as follows:

1. **High-Dimensional Similarities**: Compute the pairwise similarities $p_{j|i}$ between data points in the high-dimensional space using a Gaussian kernel. $$p_{j|i} = \frac{\exp(-\|\mathbf{x}_i - \mathbf{x}_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-\|\mathbf{x}_i - \mathbf{x}_k\|^2 / 2\sigma_i^2)}$$ where $\sigma_i$ is the variance of the Gaussian centered on data point $\mathbf{x}_i$.
2. **Symmetrize Similarities**: Symmetrize the similarities to obtain $p_{ij}$. $$p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$$
3. **Low-Dimensional Similarities**: Compute the pairwise similarities $q_{ij}$ in the low-dimensional space using a t-distribution. $$q_{ij} = \frac{(1 + \|\mathbf{y}_i - \mathbf{y}_j\|^2)^{-1}}{\sum_{k \neq l} (1 + \|\mathbf{y}_k - \mathbf{y}_l\|^2)^{-1}}$$ where $\mathbf{y}_i$ and $\mathbf{y}_j$ are the low-dimensional representations of data points $\mathbf{x}_i$ and $\mathbf{x}_j$.
4. **Kullback-Leibler Divergence**: Minimize the Kullback-Leibler (KL) divergence between the high-dimensional and low-dimensional distributions. $$\text{KL}(P \| Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$
5. **Gradient Descent**: Use gradient descent to minimize the KL divergence and update the low-dimensional representations $\mathbf{y}_i$.

## Advantages

- **Local Structure Preservation**: t-SNE excels at preserving local structures and revealing fine-grained patterns in the data.
- **Visualization**: t-SNE is particularly effective for visualizing high-dimensional data in 2D or 3D.
- **Non-linear Relationships**: t-SNE can capture non-linear relationships in the data, making it more robust than linear dimensionality reduction techniques like PCA.
- **Interpretability**: The low-dimensional embeddings produced by t-SNE can reveal meaningful clusters and patterns in the data.

## Disadvantages

- **Computational Complexity**: t-SNE is computationally intensive, especially for large datasets, as it involves pairwise distance calculations.
- **Global Structure**: t-SNE may not preserve global structures as well as local structures, leading to potential distortions in the low-dimensional representation.
- **Parameter Sensitivity**: The performance of t-SNE can be sensitive to the choice of parameters, such as the perplexity (which controls the effective number of neighbors) and the learning rate.
- **Non-deterministic**: The results of t-SNE can vary between runs due to the stochastic nature of the optimization process.

## Applications

t-SNE is widely used in various fields, including:

- **Bioinformatics**: Visualizing gene expression data and identifying cell types in single-cell RNA sequencing data.
- **Image Processing**: Visualizing high-dimensional image features for tasks like image clustering and classification.
- **Natural Language Processing**: Visualizing text data for topic modeling and sentiment analysis.
- **Anomaly Detection**: Identifying outliers and anomalies in high-dimensional data.
- **Customer Segmentation**: Clustering and visualizing customer data for market research and targeted marketing.

## Example

Consider a dataset of gene expression data with 1,000 features (genes) and 100 samples. t-SNE can be used to reduce the dimensionality of this data to 2D for visualization. By plotting the data in the 2D space, clusters of similar gene expression profiles can be easily identified and analyzed.

## Conclusion

t-Distributed Stochastic Neighbor Embedding is a powerful technique for visualizing high-dimensional data by preserving local structures. Its ability to reveal fine-grained patterns and clusters makes it a valuable tool in many data analysis and machine learning applications. However, its computational complexity and sensitivity to parameters should be considered when applying it to large or complex datasets.
