---
title: Singular Value Decomposition (SVD)
---

Singular Value Decomposition (SVD) is a fundamental mathematical technique in linear algebra used for **matrix factorization**. It decomposes a matrix into three simpler matrices, revealing the underlying structure and relationships within the data. SVD is widely used in various applications, including dimensionality reduction, data compression, noise reduction, and topic modeling (e.g., [LDA](/machine-learning-foundations/algorithms/latent-dirichlet-allocation-lda) and [LSA](/machine-learning-foundations/algorithms/latent-semantic-analysis-lsa)).

## SVD
Given a matrix $A$ of size $m \times n$ (where $m$ is the number of rows and $n$ is the number of columns), SVD factorizes $A$ into three matrices:

$$
A = U \Sigma V^T
$$

Where:

-  $U$ is an $m \times m$ orthogonal matrix (called the **left singular vectors**).
-  $\Sigma$ is an $m \times n$ diagonal matrix (called the **singular values**).
-  $V^T$ is an $n \times n$ orthogonal matrix (called the **right singular vectors**).

## Components of SVD

1. **Left Singular Vectors ($U$):**
   - The columns of $U$ are orthogonal unit vectors.
   - These vectors represent the directions of variation in the row space of $A$.

2. **Singular Values ($\Sigma$):**
   - A diagonal matrix containing non-negative values $\sigma_1, \sigma_2, \ldots, \sigma_r$, where $r$ is the rank of $A$.
   - The singular values are arranged in descending order: $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r$.
   - These values indicate the importance or "strength" of each corresponding dimension in the data.

3. **Right Singular Vectors ($V^T$):**
   - The rows of $V^T$ are orthogonal unit vectors.
   - These vectors represent the directions of variation in the column space of $A$.
## Geometric Interpretation
SVD can be thought of as a way to rotate, scale, and rotate again:

1. $V^T$ rotates the data in the original space.
2. $\Sigma$ scales the data along the new axes (singular values determine the scaling).
3. $U$ rotates the scaled data into the final space.

This process reveals the most important directions (dimensions) of variation in the data.
## Steps to Compute SVD
1. **Compute the Eigenvalues and Eigenvectors:**
   - Compute the eigenvalues and eigenvectors of $A^TA$ (for $V$) and $AA^T$ (for $U$).

2. **Sort and Select:**
   - Sort the eigenvalues in descending order and select the corresponding eigenvectors.

3. **Construct $\Sigma$:**
   - The singular values $\sigma_i$ are the square roots of the eigenvalues of $A^TA$ or $AA^T$.
   - Construct the diagonal matrix $\Sigma$ using these singular values.

4. **Assemble $U$, $\Sigma$, and $V^T$:**
   - Use the eigenvectors to form $U$ and $V$, and arrange $\Sigma$ as a diagonal matrix.
## Applications of SVD
1. **Dimensionality Reduction:**
   - By keeping only the top $k$ singular values and their corresponding vectors, SVD reduces the dimensionality of the data while preserving the most important information.
   - This is used in techniques like Principal Component Analysis (PCA) and Latent Semantic Analysis (LSA).
2. **Data Compression:**
   - SVD can approximate a matrix by retaining only the most significant singular values, reducing storage requirements.
3. **Noise Reduction:**
   - Small singular values often correspond to noise in the data. By truncating these values, SVD can filter out noise.
4. **Topic Modeling:**
   - In NLP, SVD is used in Latent Semantic Analysis (LSA) to identify relationships between terms and documents.
5. **Recommendation Systems:**
   - SVD is used in collaborative filtering to predict user preferences by decomposing user-item interaction matrices.
## Example of SVD
Consider a matrix $A$:

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
$$

After applying SVD, we get:

$$
A = U \Sigma V^T
$$
Where:
-  $U$ contains the left singular vectors.
-  $\Sigma$ contains the singular values.
-  $V^T$ contains the right singular vectors.

The singular values $\sigma_1, \sigma_2$ indicate the importance of each dimension. By keeping only the largest singular values, we can approximate $A$ with fewer dimensions.

## Advantages
- Captures underlying structure of the data.
- Provides a mathematically rigorous way to reduce dimensionality.
- Works well for sparse and dense matrices.
## Disadvantages
- Computationally expensive for large matrices.
- Requires careful selection of the number of singular values to retain.
- Interpretability of the resulting matrices can be challenging.