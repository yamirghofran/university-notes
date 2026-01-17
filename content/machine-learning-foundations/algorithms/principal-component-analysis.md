---
title: Principal Component Analysis
---

Principal Component Analysis (PCA) is a widely used technique in machine learning and statistics for [Dimensionality Reduction](/machine-learning-foundations/feature-engineering/dimensionality-reduction) while preserving as much variability (information) as possible. It is particularly useful for visualizing high-dimensional data and for preprocessing data before applying other machine learning algorithms. Here's a detailed explanation of PCA:

## How PCA Works

1. **Standardization**:
- Before applying PCA, it is often necessary to standardize the data to have a mean of 0 and a standard deviation of 1. This ensures that each feature contributes equally to the analysis.
- Formula for standardization: $$z = \frac{x - \mu}{\sigma}$$ where $x$ is the original data, $\mu$ is the mean, and $\sigma$ is the standard deviation.
2. **Covariance Matrix**:
- Compute the covariance matrix of the standardized data. The covariance matrix summarizes the pairwise covariances between the features.
- Formula for the covariance matrix: $$\text{Cov}(X) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})(X_i - \bar{X})^T$$ where $X$ is the data matrix, $\bar{X}$ is the mean vector, and $n$ is the number of samples.
1. **Eigen decomposition**:
- Perform eigen decomposition on the covariance matrix to obtain eigenvalues and eigenvectors. The eigenvalues represent the amount of variance captured by each principal component, and the eigenvectors represent the directions of the principal components.
- Formula for eigen decomposition: $$\text{Cov}(X) v = \lambda v$$ where $\lambda$ is an eigenvalue and $v$ is the corresponding eigenvector.
2. **Sorting Eigenvalues**:
- Sort the eigenvalues in descending order and select the top $k$ eigenvalues. The corresponding eigenvectors form the principal components.
- The number $k$ is chosen based on the desired amount of variance to be preserved.
3. **Projection**:
- Project the original data onto the new feature space defined by the top $k$ eigenvectors. This results in the reduced-dimensional data.
- Formula for projection: $$X_{\text{reduced}} = X W$$ where $W$ is the matrix of top $k$ eigenvectors.

## Key Concepts

- **Principal Components**: The new features obtained after dimensionality reduction. The first principal component captures the most variance in the data, the second principal component captures the second most variance, and so on.
- **Variance Explained**: The proportion of the total variance in the data that is captured by each principal component. It is useful for determining the number of principal components to retain.
- **Scatter Plot**: A plot of the data in the new feature space defined by the principal components. It is useful for visualizing the structure of the data.

## Advantages of PCA

- **Dimensionality Reduction**: Reduces the number of features while retaining most of the variance in the data.
- **Noise Reduction**: Helps in removing noise and irrelevant information by focusing on the most important features.
- **Visualization**: Enables visualization of high-dimensional data by projecting it onto 2D or 3D space.
- **Improved Performance**: Can improve the performance of machine learning algorithms by reducing overfitting and computational costs.

## Disadvantages of PCA

- **Linear Assumption**: Assumes that the data is linearly separable, which may not always be the case.
- **Interpretability**: The principal components are linear combinations of the original features, which can make them difficult to interpret.
- **Variance vs. Information**: Focuses on maximizing variance, which may not always correspond to maximizing information.

## Applications of PCA

- **Image Compression**: Reduces the dimensionality of image data while preserving important features.
- **Face Recognition**: Used for dimensionality reduction and feature extraction in face recognition systems.
- **Gene Expression Data Analysis**: Helps in identifying patterns and reducing noise in high-dimensional gene expression data.
- **Preprocessing**: Used as a preprocessing step for other machine learning algorithms to improve performance.

## Example

Suppose we have a dataset with 5 features and we want to reduce it to 2 features using PCA. Here are the steps:

4. Standardize the data.
5. Compute the covariance matrix.
6. Perform eigen decomposition to obtain eigenvalues and eigenvectors.
7. Sort the eigenvalues and select the top 2 eigenvectors.
8. Project the original data onto the new feature space defined by the top 2 eigenvectors. The resulting data will have 2 features that capture the most variance in the original data. PCA is a powerful and widely used technique for dimensionality reduction and data visualization. It helps in simplifying models, reducing computational costs, and improving the interpretability of the data.
