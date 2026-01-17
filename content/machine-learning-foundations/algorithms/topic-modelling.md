---
title: Topic Modelling
---

A family of techniques that uses unlabeled data, typically in the form of natural language text documents. The model learns to represent a document as a vector of topics. 

e.g. in a collection of news articles, the five major topics could be sports, politics, entertainment, finance, and technology. Then each document could be represented as a five-dimensional feature vector, one dimension per topic. [0.04, 0.5, 0.1, 0.3, 0.06]

Topic modeling algorithms, such as [Latent Semantic Analysis (LSA)](/machine-learning-foundations/algorithms/latent-semantic-analysis-lsa) and [Latent Dirichlet Allocation (LDA)](/machine-learning-foundations/algorithms/latent-dirichlet-allocation-lda), learn by analyzing the unlabeled documents. These two algorithms produce similar outputs, but are based on different mathematical models. LSA uses [Singular Value Decomposition (SVD)](/machine-learning-foundations/algorithms/singular-value-decomposition-svd) of the word-to-document matrix (constructed using a binary [Bag of Words](/machine-learning-foundations/feature-engineering/bag-of-words) or TF-IDF). LDA uses a hierarchical **Bayesian model**, in which each document is a **mixture** of several topics, and each word's presence is attributable to one of the topics.