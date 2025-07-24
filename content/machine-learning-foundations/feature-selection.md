---
title: Feature Selection
---

## Why you can't use all features
Not all features will be equally relevant for a given problem. Features present in few examples:
- Increase dimensionality: number of columns (features)/number of rows (examples)
- Increase sparsity: a lot of zeros in each example
- Increase computational cost: storage, computing time, dedicated technologies.
- Overfitting risk: fitting [noise](/machine-learning-foundations/data-noise) instead of true patterns
- Reduce model interpretability: harder to analyze and understand.
- Distance metric degradation: in high dimensions, data points tend to be equidistant, reducing the effectiveness of distance-based algorithms (e.g. [kNN](/machine-learning-foundations/k-nearest-neighbors), [clustering](/machine-learning-foundations/clustering))

## Main Techniques
- Cutting the Long Tail
	- Cut the features in the tail of the distribution of examples over features.
- [Boruta](/machine-learning-foundations/boruta)
- [L1-Regularization (Lasso Regression)](/machine-learning-foundations/l1-regularization-lasso-regression)
- Task-specific feature selection
	- Remove stop words
	- Replace uncommon words with a single label, such as RARE_WORDS
