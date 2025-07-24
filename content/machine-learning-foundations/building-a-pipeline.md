---
title: Building a Pipeline
---

Sequence of transformations from the raw dataset to a model.
Every stage of a pipeline receives the previous stage's output except the first stage, which receives the training dataset as its input.
- `scikit-learn` exposes the `Pipeline` class.

![](../attachments/cleanshot-2025-02-05-at-1350302x.png)

Use **Pickle** in Python for serialization (saving) and deserialization (restoring) of objects.