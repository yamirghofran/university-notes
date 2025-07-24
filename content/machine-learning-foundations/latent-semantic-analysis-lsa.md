---
title: Latent Semantic Analysis (LSA)
---

**LSA** is a technique that analyzes relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms. It uses a mathematical technique called [Singular Value Decomposition (SVD)](/machine-learning-foundations/singular-value-decomposition-svd) to reduce the dimensionality of the term-document matrix while preserving the similarity structure among documents.

## How it Works
1. **Term-Document Matrix Construction:**
   - Create a matrix where each row represents a unique word and each column represents a document.
   - The entries in the matrix can be raw counts, term frequency (TF), or term frequency-inverse document frequency (TF-IDF) values.
2. **Singular Value Decomposition (SVD):**
   - Apply SVD to the term-document matrix to decompose it into three matrices: $U$, $\Sigma$, and $V^T$.
   - $U$ represents the term-topic matrix.
   - $\Sigma$ is a diagonal matrix of singular values.
   - $V^T$ represents the document-topic matrix.
3. **Dimensionality Reduction:**
   - Reduce the number of dimensions by keeping only the top $k$ singular values and their corresponding vectors in $U$ and $V^T$.
   - This results in a lower-dimensional approximation of the original term-document matrix.
4. **Topic Interpretation:**
   - The reduced matrices can be used to identify topics and the relationships between terms and documents.
## Advantages
- Effective in capturing synonymy and polysemy.
- Reduces noise and redundancy in the data.
## Limitations
- The resulting topics are not easily interpretable.
- Assumes a linear relationship between terms and documents.
## Comparison with [LDA](/machine-learning-foundations/latent-dirichlet-allocation-lda)
- LSA is based on linear algebra and dimensionality reduction, while LDA is based on probabilistic modeling.
- LSA is simpler and faster but less interpretable, whereas LDA provides more interpretable topics but is computationally more demanding.
- LSA can handle synonymy and polysemy to some extent, but LDA explicitly models the generative process of documents, making it more robust in capturing the underlying topic structure.
