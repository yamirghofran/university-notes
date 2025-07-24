---
title: Data Leakage
---

Data leakage, also called **target leakage**, is a problem affecting several stages of the machine learning life-cycle, from data collection to model evaluation.
![](../attachments/cleanshot-2025-01-15-at-1951402x.png)

Data leakage in [supervised learning](/machine-learning-foundations/supervised-learning) is the unintentional introduction of information about the target that should not be made available. We call it "**contamination**". Training on contaminated data leads to overly optimistic expectations about the model performance.

Three most frequent [Causes of Data Leakage](/machine-learning-foundations/causes-of-data-leakage) that can happen during data collection and preparation:
- Target being a a function of a feature
- Feature hiding the target
- Feature coming from the future
