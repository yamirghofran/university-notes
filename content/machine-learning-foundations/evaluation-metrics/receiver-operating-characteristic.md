---
title: Receiver Operating Characteristic
---

The ROC (Receiver Operating Characteristic) curve is a graphical representation used to evaluate the performance of a **binary classification** model. It can only be used with classifiers that return a score (or a probability) of prediction. 
![](/machine-learning-foundations/attachments/pasted-image-20250204123842.png)

- **True Positive Rate (TPR) or Sensitivity (Y-axis)**: This is the proportion of actual positive cases that are correctly identified by the model. It is calculated as: $$\text{TPR} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$
- **False Positive Rate (FPR) (X-axis)**: This is the proportion of actual negative cases that are incorrectly identified as positive by the model. It is calculated as: $$\text{FPR} = \frac{\text{False Positives}}{\text{False Positives} + \text{True Negatives}}$$

## Interpretation

- **ROC Curve Shape**: The ROC curve plots the TPR against the FPR at various threshold settings. A model that performs perfectly would have a ROC curve that passes through the top-left corner (TPR = 1, FPR = 0). A model that performs no better than random chance would have a ROC curve that is a diagonal line from the bottom-left to the top-right (TPR = FPR).
- **Area Under the Curve ([AUC-ROC](/machine-learning-foundations/evaluation-metrics/auc-roc))**: The AUC-ROC is a single scalar value that summarizes the performance of the model. It represents the probability that a randomly chosen positive instance is ranked higher than a randomly chosen negative instance. An AUC of 1 indicates perfect performance, while an AUC of 0.5 indicates performance no better than random chance.

## Example

Imagine you have a binary classifier for detecting spam emails:

- **True Positives (TP)**: Emails correctly identified as spam.
- **False Positives (FP)**: Emails incorrectly identified as spam (but are actually not spam).
- **True Negatives (TN)**: Emails correctly identified as not spam.
- **False Negatives (FN)**: Emails incorrectly identified as not spam (but are actually spam). The ROC curve helps visualize the trade-off between the TPR and FPR at different threshold levels, providing a comprehensive view of the model's performance across all possible classification thresholds.