---
title: Accuracy
---

The proportion of true results (both true positives and true negatives) among the total number of cases examined.
$$\text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Population}}$$
## Cost-sensitive Accuracy
Different classes have different importance.
- We assign a cost (a positive number) to both types of mistakes: False Positive and False Negative.
- We multiply the counts for FP and FN by their corresponding costs before calculating the accuracy.

## Per-class Accuracy
For imbalanced data but not for multiple very small classes.
- We calculate the accuracy of prediction for each class {1,...,C}
- We take an average of C individual accuracy measures
- e.g. spam detection: accuracy class "spam" = 23/(23+1)=0.96, accuracy class "not_spam"=556/(12+556)=0.98. Per-class accuracy=(0.96+0.98)/2=0.97.
## Use Case
Evaluates overall correctness of a #ml/classification model.
## Limitations
Can be misleading if classes are imbalanced (e.g., high accuracy with an unbalanced dataset where the majority class dominates).