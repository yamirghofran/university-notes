---
title: Data Noise
---

Noise in data is a corruption of examples.

- Images can be blurry or incomplete. 
- Text can lose formatting, which makes some words concatenated or split.
- Audio data can have noise in the background.
- Poll answers can be incomplete or have missing attributes.

If [tidy data](/machine-learning-foundations/raw-and-tidy-data) has missing attributes, [Data Imputation](/machine-learning-foundations/data-imputation) techniques can help fill in those missing values.

Blurred images can be de-blurred using specific image de-blurring algorithms, though deep machine learning models like [neural networks](/machine-learning-foundations/neural-networks) can learn to de-blur if needed.

Noise in audio data can also be algorithmically suppressed.

Noise is more of a problem in small datasets because the presence of noise can lead to **overfitting**: the algorithm may learn to model the noise contained in the training data.

In big data, on the other hand, noise, if randomly applied to each example independently of other examples in the dataset, is typically "averaged out" over multiple examples. It can bring a [regularization](/machine-learning-foundations/regularization) effect as it prevents the learning algorithm from relying too much on a small subset of input [features](/machine-learning-foundations/feature-vector).