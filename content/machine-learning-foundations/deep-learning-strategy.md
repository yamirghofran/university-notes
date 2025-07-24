---
title: Deep Learning Strategy
---

Assume we are building a model from scratch, based on a chosen architecture.

1. Define a performance metric **P**.
2. Define the [Cost Function](/machine-learning-foundations/loss-function) **C**.
3. Pick a parameter-initialization strategy **W**.
4. Pick a cost-function optimization algorithm **A**.
5. Choose a [Hypterparameter Tuning](/machine-learning-foundations/hypterparameter-tuning) strategy **T**.
6. Pick a combination **H** of hyperparameter values using the tuning strategy T.
7. Initialize model **M** parameters using strategy W.
8. Train M, using algorithm A, parametrized with hyperparameters H, to optimize cost function C.
9. If there are still untested hyperparameter values, pick another combination H of hyperparameter values using strategy T, and repeat step 7 and 8.
10. Return the model for which the metric P was optimized.

We choose P, C, W, A, and T depending on data characteristics, model complexity, and training dynamics.

| #   | Step                                  | Examples                                            |
| --- | ------------------------------------- | --------------------------------------------------- |
| 1   | Performance metric (P)                | - Accuracy (classification)                         |
|     |                                       | - AUC-ROC (binary classification)                   |
|     |                                       | - F1-score (imbalanced data)                        |
|     |                                       | - MSE / RMSE (regression)                           |
| 2   | Cost/loss function (C)                | - Cross-entropy loss (classification)               |
|     |                                       | - Mean Squared Error (MSE) (regression)             |
|     |                                       | - Categorical cross-entropy (multiclass)            |
| 3   | Parameter initialization strategy (W) | - Xavier (Glorot) Initialization (tanh activations) |
|     |                                       | - He Initialization (ReLU activations)              |
|     |                                       | - Random Uniform / Normal (can be unstable)         |
| 4   | Optimization algorithm (A)            | - Stochastic Gradient Descent (SGD)                 |
|     |                                       | - Adam                                              |
|     |                                       | - RMSProp                                           |
|     |                                       | - Adagrad                                           |
| 5   | Hyperparameter tuning strategy (T)    | - Grid Search                                       |
|     |                                       | - Random Search                                     |
|     |                                       | - Bayesian Optimization                             |
|     |                                       | - Hyperband                                         |
|     |                                       | - Manual Tuning                                     |


### Performance Metric (P)
- Measures how good the model is , i.e. we want to maximize this.
- We define a metric that would allow comparing the performance of two models on the holdout data and select the better of the two.
### Cost Function (C)
- Measures how bad the model is during training, i.e. we want to minimize this.
- Define what our learning algorithm will optimize to train a model.
- Regression: MSE
- Classification:
	- Categorical Cross-Entropy for multiclass classification
	- Binary Cross-Entropy for binary and multi-label classification.
### Parameter Initialization Strategy (W)
- Decides how the model starts learning. Influences learning speed and stability.
### Optimization Algorithm (A)
- Determines how weights get updated after computing loss gradients.
### Hyperparameter tuning strategy (T)
- Find best hyperparameters, e.g. learning rate, batch size, architecture depth.
- Neural networks start with unknown weights/bias, updated by training.
- Initialization gives a starting point for optimization (gradient descent).
- Good initialization: faster convergence, stable gradients (avoiding vanishing/exploding) and better model performance.
- Bad initialization:
	- All weights $=0$ or 1: no learning because of gradients collapse or identical updates.
	- Too large weights: exploding gradients; too small weights: vanishing gradients.
	- Common initialization strategies: random normal, random uniform, Xavier, He.
- PyTorch:
	- `nn.init.xavier_uniform_(model.layer.weight)`
	- `nn.init.kaiming_uniform_(layer.weight, nonlinearity='relu')`
	- `nn.init.zeros_(layer.bias) \# Bias often initialized to zero`
- Training and validation cycle:
	- If performance does not improve, we can pick a different combination of hyperparameters and build a different model.
	- We will continue to test different values of hyperparameters until there are no more values to test.
	- Then we keep the best model among those we trained in the process.
	- If the performance of the best model is still not satisfactory, we try a different network architecture, add more labeled data, or try transfer learning.
- Hyperparameter space:
	- Hyperparameter values strongly affect the properties of a trained NN.
	- Hyperparameter tuning is time and resource intensive.
	- We must decide which hyperparameters are important enough to spend the time on.
- While there is no definitive answer. While training:
	- Start with default values and then change them (e.g., see the 'cards' in Lecture 16 + PyTorch)
	- Observe to which parameters the model is more sensitive
- Tuning hyperparameters, as opposed to using the default value
- Tuning the hyperparameters to which the model is sensitive.
- Table shows approximate sensitivity of a model to some hyperparameters.

| Hyperparameter | Sensitivity |
| :-- | :-- |
| Learning rate | High |
| Learning rate schedule | High |
| Loss function | High |
| Units per layer | High |
| Parameter initialization strategy | Medium |
| Number of layers | Medium |
| Layer properties | Medium |
| Degree of regularization | Medium |
| Choice of optimizer | Low |
| Optimizer properties | Low |
| Size of minibatch | Low |
| Choice of non-linearity | Low |
## Common Configurations
### Classification
- Performance Metric (P)
	- Accuracy for balanced dataset
	- F1-score for imbalanced dataset
- Cost/loss function (C)
	- Cross-entropy for multiclass or multilabel classification
- Parameter Initialization Strategy (W)
	- Xavier when using tanh as the activation function.
	- He when using ReLU as the activation function
- Optimization Algorithm (A)
	- Adam with adaptive learning rate and handles sparse gradients well
	- Stochastic gradient descent (SGD) strong generalization, stability for large datasets
- Hyperparameter tuning strategy (T)
	- Random Search over learning rate, dropout rate, embedding dimension, layers
	- Bayesian
### Regression
- Performance Metric (P)
	- Root Mean Squared Error (RMSE) for data without large errors and outliers.
	- Mean Absolute Error (MAE) for data with outliers and large errors
- Cost/loss function (C)
	- Mean Squared Error (MSE) penalizes large errors, i.e. very sensitive to outliers
	- Huber Loss combines MSE and MAE to lower sensitivity to outliers.
- Parameter Initialization Strategy (W)
	- He initialization when using ReLU as the activation function
- Optimization Algorithm (A)
	- RMSProp with time-series, RNNs, and sequential data but needs tuning
	- Adam general purpose default choice for tabular data, images, text; robust and stable.
- Hyperparameter tuning strategy (T)
	- Grid Search

### Imbalanced Classification
- Performance Metric (P)
	- F1
	- AUC
- Cost/loss function (C)
	- Weighted cross-entropy
- Parameter Initialization Strategy (W)
	- Xavier
- Optimization Algorithm (A)
	- AdamW
- Hyperparameter tuning strategy (T)
	- Bayesian Optimization
### Time Series Forecasting
- Performance Metric (P)
	- RMSE
	- MAE
- Cost/loss function (C)
	- MSE
- Parameter Initialization Strategy (W)
	- He
- Optimization Algorithm (A)
	- RMSProp
- Hyperparameter tuning strategy (T)
	- Grid Search
### Image Tasks (CNNs)
- Performance Metric (P)
	- Accuracy
- Cost/loss function (C)
	- Cross-Entropy
- Parameter Initialization Strategy (W)
	- He
- Optimization Algorithm (A)
	- SGD + Momentum
- Hyperparameter tuning strategy (T)
	- Hyperband