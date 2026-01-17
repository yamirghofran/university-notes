---
title: Latent Dirichlet Allocation (LDA)
---

**LDA** is a generative probabilistic model that assumes each document is a mixture of a small number of topics and that each word in the document is attributable to one of the document's topics. It uses Dirichlet priors for the document-topic and topic-word distributions.

## How it works
1. **Initialization:**
   - Choose the number of topics $k$.
   - Initialize topic distributions for each document and word distributions for each topic.

2. **Iterative Process:**
   - For each document, randomly assign each word to one of the $k$ topics.
   - Iteratively update the topic assignments for each word based on:
     - The prevalence of topics in the document.
     - The prevalence of words in the topic.

3. **Convergence:**
   - The process continues until the topic assignments stabilize, meaning that further iterations do not significantly change the topic distributions.

4. **Topic Interpretation:**
   - After convergence, each document is represented as a distribution over topics.
   - Each topic is represented as a distribution over words.
## Advantages
- Produces interpretable topics
- Captures the probabilistic nature of topic distributions
## Limitations
- Requires number of topics to be specified in advance.
- Computationally intensive for large datasets

## Comparison with [LSA](/machine-learning-foundations/algorithms/latent-semantic-analysis-lsa)
- LSA is based on linear algebra and dimensionality reduction, while LDA is based on probabilistic modeling.
- LSA is simpler and faster but less interpretable, whereas LDA provides more interpretable topics but is computationally more demanding.
- LSA can handle synonymy and polysemy to some extent, but LDA explicitly models the generative process of documents, making it more robust in capturing the underlying topic structure.

