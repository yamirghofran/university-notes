---
title: Adversarial Validation
---

A technique to check wether our training, validation, test, or production data come from the same distribution.
Can be applied to: [Distribution Shift](/machine-learning-foundations/distribution-shift), [Holdout Dataset](/machine-learning-foundations/training-and-holdout-datasets) split, and [Data Augmentation](/machine-learning-foundations/data-augmentation).


1. Split our original training set into **Training 1** used for adversarial analysis, and **Training 2** used later for evaluation.
2. Create a new dataset to train a classifier to distinguish between training and test data, labeling each example of Training 1 as "Training" and of Training 2 as "Testing".
3. Combine Training 1 and the original validation, test, or production Test set to create a synthetic Training Dataset.
4. Train a binary classifier to predict whether a sample is from Training or test.
5. Apply the binary classifier to Training 2. This tells us which examples in Training 2 look like they came from the test set.
E.g. when working with a test/production set, we use the samples classified as coming from the Test set by the binary classifier to evaluate generalization error.