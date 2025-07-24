---
title: Training and Holdout Datasets
---

ML algorithms should make accurate predictions based on unknown data, i.e. data on which the model has not been trained.

We divide a dataset into three subsets: **training, validation, and test**.

## Training Set
Largest portion of the available data, used to produce (learn) the model. These are the data 'known' by the model.

## Holdout Sets
The remaining portion of the available data, usually divided into validation and test sets of similar size and not used to train the model.

### Validation Set
Used to select the learning algorithm and find the best configuration value for that model (called [Hyperparameter](/machine-learning-foundations/parameters-and-hyperparameters)).

### Training Set
Used to test the model before delivery.