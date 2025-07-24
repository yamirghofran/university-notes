---
title: Feature Engineering
---

Transforming raw data into tidy data ([Raw and Tidy Data](/machine-learning-foundations/raw-and-tidy-data)), i.e. into a [feature vector](/machine-learning-foundations/feature-vector).
Fundamental part of ML Engineering.

Algorithm-specific formatting of feature vectors. e.g. transforming categorical attributes into numerical features with certain [properties](/machine-learning-foundations/properties-of-good-features) .

Feature engineering is a process of first conceptually and then programmatically transforming a raw example into a [Feature Vector](/machine-learning-foundations/feature-vector). It consists of conceptualizing a feature and then writing the programming code that would transform the entire raw example, with potentially some help of some indirect data, into a feature.

For feature engineering with text, you can use feature engineering techniques like [One-Hot Encoding](/machine-learning-foundations/one-hot-encoding) and [bag of words](/machine-learning-foundations/bag-of-words).

There are other **encoding** techniques as well:
- [Mean Encoding](/machine-learning-foundations/mean-encoding)
- [Feature Hashing](/machine-learning-foundations/feature-hashing)
- [Topic Modelling](/machine-learning-foundations/topic-modelling)

## Feature Concatenation
Records/examples can have multiple parts, each transformed by an encoder into a (sub)feature.

We can concatenate those features into a single feature (order does not matter).
We can concatenate all the (sub)features. Choose the same order for each record.

Note: useful because each (sub)feature can have a different dimensionality.

## Best Practices
-  **Start simple:** try features that require little coding time/computing resources.
-  **Reuse old non-ML algorithms:** use their output as a feature of the new ML one!
-  **Reduce cardinality:** categorical feature with many values help to train different      modes for a model (e.g., country, zipcode). If we do not need 'modes':
  - [Feature hashing](/machine-learning-foundations/feature-hashing): Slide 21, Lecture 4.
  - Group similar values: e.g., Group states into regions if states are not needed to solve the problem.
  - Group the long tail: e.g., group infrequent values under 'other'.
  - Remove the feature: (almost) all values are unique.
  - Careful! Reducing cardinality is tricky: e.g., we might inadvertently destroy the information that would allow the model to distinguish one “Springfield” from another!
-  **Use counts with caution:** counts tend to change over time, outdating the model. E.g., number of calls per mobile customer increasing with the subscription time.
-  **Select features only when necessary:** reasons to do it:
  - We need an explainable model; thus, we keep only the most significant predictors.
  - We have not enough computing resources, e.g., RAM, drive space, etc.
  - We do not have time to experiment and/or rebuild the model in production.
  - We expect a significant [distribution shift](/machine-learning-foundations/distribution-shift) between two model trainings.
-  **Test the code carefully:**
  - Unit tests for all automated feature extractors.
  - Test each feature for speed and memory consumption in the deployment environment.
  - Test for external dependencies, i.e., DB, remote APIs, etc.
  - Rerun all the tests in the production environment.
  - Don’t fail silently.
-  **Keep code, model, and data in sync:** [version](/machine-learning-foundations/storing-data) must be the same.
-  **Isolate feature extraction code:** it can be debugged and tested.
-  **Log the production feature values:** useful for dev, debugging, testing.
---
- [Storing and Documenting Features](/machine-learning-foundations/storing-and-documenting-features)
- [Synthesizing Features](/machine-learning-foundations/synthesizing-features)
- [Feature Selection](/machine-learning-foundations/feature-selection)
