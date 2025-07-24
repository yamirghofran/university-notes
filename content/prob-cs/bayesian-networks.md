---
title: Bayesian Networks
---
The core of the Bayesian Network (BN) representation is a directed acyclic graph (DAG) G, whose nodes are the random variables in our domain and whose edges correspond, intuitively, to direct influence of one node on another.
BNs are the gold standard for causal inference and reasoning.
Applications:
- Risk assessment and reliability of engineering systems
- Risk factors discovery in medical diagnosis
- Anomaly detection
- Environmental modeling
## Student Example
![](../attachments/bayesian-networks-1.png)
![](../attachments/bayesian-networks-2.png)
There are 48 outcomes (so 47 probabilities), but we only had to define 15 of them.
We can write the joint probability as the product of the individual nodes conditional probability tables (CPT).
$$
P(L, G, S, D, I) = P(L \mid G) P(G \mid D, I) P(S \mid I) P(I) P(D)
$$
$$
P(i^1, d^0, g^2, s^1, l^0) = P(i^1) P(d^0) P(g^2 \mid i^1, d^0) P(s^1 \mid i^1) P(l^0 \mid g^2)$$
$$
= 0.3 \cdot 0.6 \cdot 0.08 \cdot 0.8 \cdot 0.4 = 0.004608
$$
## General Rule
Consider categorical random variables $X_1, \ldots, X_n$. A **Bayesian network** (BN) model is defined by
- A directed acyclic graph (DAG) $G$ where the nodes are the random variables;
- Conditional probability tables (CPTs) for each node conditional on its parents in $G$.
The BN specifies that
$$
P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid X_{\Pi_i}),
$$
where $X_{\Pi_i}$ are the parents of $X_i$ in $G$.
