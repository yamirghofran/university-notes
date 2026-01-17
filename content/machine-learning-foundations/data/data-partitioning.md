---
title: Data Partitioning
---

To divide your data in [training and holdout sets](/machine-learning-foundations/data/training-and-holdout-datasets), the partitioning has to satisfy several conditions:

1. Split was applied to raw data
	Do the split before everything else to avoid [Data Leakage](/machine-learning-foundations/data/data-leakage)
2. Data was randomized before the split.
3. Validation and test sets follow the same distribution.
4. Leakage during the split was avoided.

A small dataset of less than a thousand examples would do best with 90% of the data used for training. In this case, we might decide not to have a distinct validation set, and instead simulate with the [Cross-Validation](/machine-learning-foundations/hyperparameters/cross-validation) technique.

## Leakage During Partitioning
**Group leakage** may occur during partitioning.

e.g. if you have brain scans of patients, and multiple scans for each patient, scans of the same patient might end up in both training and holdout sets, training on the specifics of the patient.

The solution to group leakage is **group partitioning**.