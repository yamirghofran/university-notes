---
title: Hypterparameter Tuning
---

- Not optimized by the learning algorithm itself. 
- Data analyst/ML engineer "tunes" [Hyperparameter](/machine-learning-foundations/introduction/parameters-and-hyperparameters)s by experimenting with  combinations of values, one per hyperparameter.
- Each ML model / algorithm has a unique set of hyperparameters.
- Several popular **hyperparameter tuning techniques**
	- [Grid Search](/machine-learning-foundations/hyperparameters/grid-search)
	- Random Search
	- Coarse-to-Fine Search
	- Bayesian Techniques
	- [Cross-Validation](/machine-learning-foundations/hyperparameters/cross-validation)
- Hyperparameter tuning controls two tradeoffs
	- [Precision-Recall Tradeoff](/machine-learning-foundations/evaluation-metrics/precision-recall-tradeoff)
	- [Bias-Variance Tradeoff](/machine-learning-foundations/hyperparameters/bias-variance-tradeoff)

## Grid Search
- Simplest technique. Use when possible.
- Used with a few hyperparameters and short value ranges.
- Discretize and then evaluate each pair of hyperparameters.
- Train the final model with the best pair of hyperparameter values.
### Evaluation Criteria
- Configuring a pipeline with a pair of hyperparameter values.
- Applying the pipeline to the training data and training a model
- Computing the performance metric for the model on the [Validation Dataset](/machine-learning-foundations/data/training-and-holdout-datasets).

## Random Search
- Avoids combinatorial explosion
- Provide statistical distribution for each hyperparameter (e.g uniform)
- Random sample values for those distribution.
- Set the total number of combinations we want to evaluate. (total candidates)
## Coarse-to-Fine Search
- Combination of grid search and random search
- Use a coarse random search to find the regions of high potential
- Use a fine grid search in one or more of those regions
## Bayesian Techniques
- Use past evaluation results to choose the next values to evaluate.
- Can be more efficient and faster
- Slightly better than random search, but much faster.
## Gradient-based
- Most modern ML libraries implement one or more such techniques.
- Hyperparameter tuning libraries used to tune virtually any ML algorithm.

## Cross-Validation
- Grid search and other techniques require properly sized datsets.
- Rule of thumb: 100+ records, 12+ records per each class.
- We cannot have training, validation, and test sets with smaller datasets.
- We split into training and test sets, then use [Cross-Validation](/machine-learning-foundations/hyperparameters/cross-validation) on the training set.
- Use any technique with cross-validation to find the best hyperparameter values.
- We use the best values to train the final model on the entire training set.
- We asses the final model using the test set.
**Be pragmatic**: good enough tuning, given the available time. No perfection.
## Automating Hyperparameter Optimization
- **Optuna**: Best for general ml optimization tasks, especially with pruning and Bayesian optimization
- Hyperopt: similar to Optuna but slower in large-scale parallel tuning
- Ray tune: best for deep learning and large-scale computing
- Scikit-optimize: quick small-scale optimizations
- Keras tuner: optimized for Tensorflow/Keras models.