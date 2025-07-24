---
title: Topic Modelling
---

A family of techniques that uses unlabeled data, typically in the form of natural language text documents. The model learns to represent a document as a vector of topics.

e.g. in a collection of news articles, the five major topics could be sports, politics, entertainment, finance, and technology. Then each document could be represented as a five-dimensional feature vector, one dimension per topic. [0.04, 0.5, 0.1, 0.3, 0.06]

Topic modeling algorithms, such as [Latent Semantic Analysis (LSA)](/machine-learning-foundations/latent-semantic-analysis-lsa) and [Latent Dirichlet Allocation (LDA)](/machine-learning-foundations/latent-dirichlet-allocation-lda), learn by analyzing the unlabeled documents. These two algorithms produce similar outputs, but are based on different mathematical models. LSA uses [singular value decomposition (SVD)](/machine-learning-foundations/singular-value-decomposition-svd) of the word-to-document matrix (constructed using a binary [bag of words](/machine-learning-foundations/bag-of-words) or TF-IDF). LDA uses a hierarchical **Bayesian model**, in which each document is a **mixture** of several topics, and each word's presence is attributable to one of the topics.
