---
title: Data Sampling
---

# Data Sampling Strategies
There are two main strategies: probability sampling and nonprobability sampling.

In **probability sampling**, all examples have a chance to be selected. These techniques involve randomness.

**Nonprobability sampling** is not random. To build a sample, it follows a fixed deterministic sequence of heuristic actions. This means that some examples don't have a chance of being selected, no matter how many samples you build.

We will only deal with probability sampling.
## Simple Random Sampling
Simple random sampling is the most straightforward method. 

Each example from the entire dataset is chosen purely by chance; each example has an equal chance of being selected.
**Simplicity** is the great advantage of this method, and it can be easily implemented.

A disadvantage of this method is that you may not select enough examples that would have a particular property of interest (especially in an [imbalanced dataset](/machine-learning-foundations/data/imbalanced-data)).
## Systematic Sampling
To implement **systematic sampling** (also known as **interval sampling**), you create a list containing all examples. From that list, you randomly select the first example $\mathbf{x}_{\text{start}}$ from the first $k$ elements on the list. Then, you select every $k^{\text{th}}$ item on the list starting from $\mathbf{x}_{\text{start}}$. You choose such a value of $k$ that will give you a sample of the desired size.

An advantage of the systematic sampling over the simple random sampling is that it draws examples from the whole **range of values**. However, systematic sampling is inappropriate if the list of examples has periodicity or repetitive patterns. In the latter case, the obtained sample can exhibit a bias. However, if the list of examples is randomized, then systematic sampling often results in a better sample than simple random sampling.

## Stratified Sampling
If you know about the existence of several groups (e.g., gender, location, or age) in your data, you should have examples from each of those groups in your sample. In **stratified sampling**, you first divide your dataset into groups (called strata) and then randomly select examples from each stratum, like in simple random sampling. The number of examples to select from each stratum is **proportional to the size of the stratum**.

Stratified sampling often **improves the representativeness** of the sample by reducing its bias; in the worst of cases, the resulting sample is of no less quality than the results of simple random sampling. However, to define strata, the analyst has to understand the properties of the dataset. Furthermore, it can be difficult to decide which attributes will define the strata.

If you don’t know how to best define the strata, you can use [Clustering](/machine-learning-foundations/algorithms/clustering). The only decision you have to make is how many clusters you need. This technique is also useful to choose the unlabeled examples to send for labeling to a human labeler. It often happens that we have millions of unlabeled examples, and few resources available for labeling. Choose examples carefully, so that each stratum or cluster is represented in our labeled data.

Stratified sampling is the **slowest** of the three methods due to the additional overhead of working with several independent strata. However, its potential benefit of producing a less biased sample typically outweighs its drawbacks.
