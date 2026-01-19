---
title: AUC-ROC
---

Area under the [ROC](/machine-learning-foundations/evaluation-metrics/receiver-operating-characteristic) curve.
Measures the ability of a model to distinguish between classes by plotting the true positive rate ([Recall](/machine-learning-foundations/evaluation-metrics/recall)) against the false positive rate (FPR) at various thresholds (imbalanced datasets).
![](/machine-learning-foundations/attachments/pasted-image-20250129144016.png)

Assesses model's ability to distinguish between classes.
- **Range**: Between 0 and 1, where 1 indicates perfect #ml/classification and 0.5 suggests no discriminative power (equivalent to random guessing).
![](/machine-learning-foundations/attachments/cleanshot-2025-02-07-at-1949132x.png)
## Advantages 
- Robust to class imbalance
- provides a comprehensive view of performance across all classification thresholds.