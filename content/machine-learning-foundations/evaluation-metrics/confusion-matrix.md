---
title: Confusion Matrix
---

A confusion matrix is a table that describes the performance of a classification model on a set of test data for which the true values are known. It allows you to see how well your classification model is performing by comparing the predicted classes against the actual classes.

## Structure

A confusion matrix for a binary classification problem (two classes) is typically a 2x2 table, while for a multi-class classification problem, it is an $N \times N$ table, where $N$ is the number of classes.

## Components

For a binary classification problem, the confusion matrix has the following components:

- **True Positives (TP)**: The number of instances where the model correctly predicted the positive class.
- **True Negatives (TN)**: The number of instances where the model correctly predicted the negative class.
- **False Positives (FP) or Type I errors**: The number of instances where the model incorrectly predicted the positive class (i.e., predicted positive when the actual class was negative).
- **False Negatives (FN) or Type II errors**: The number of instances where the model incorrectly predicted the negative class (i.e., predicted negative when the actual class was positive).

## Example for Binary Classification

Suppose you have a binary classification problem with classes "Positive" and "Negative". The confusion matrix might look like this:

|                   | Predicted Positive | Predicted Negative |
|-------------------|-------------------|-------------------|
| Actual Positive   | TP = 50           | FN = 10           |
| Actual Negative   | FP = 5            | TN = 35           |

### Components for Multi-Class Classification
For a multi-class classification problem with \( N \) classes, the confusion matrix will have \( N \) rows and \( N \) columns. Each cell in the matrix represents the number of instances where the actual class is \( i \) and the predicted class is \( j \).

### Example for Multi-Class Classification
Suppose you have a multi-class classification problem with three classes: "Cat", "Dog", and "Bird". The confusion matrix might look like this:

|               | Predicted Cat | Predicted Dog | Predicted Bird |
|---------------|---------------|--------------|---------------|
| Actual Cat    | 40            | 5            | 5             |
| Actual Dog    | 3             | 45           | 2             |
| Actual Bird   | 2             | 1            | 47            |


## Metrics Derived from Confusion Matrix

Several important metrics can be derived from the confusion matrix:

1. **[Accuracy](/machine-learning-foundations/evaluation-metrics/accuracy)**: $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
2. **[Precision](/machine-learning-foundations/evaluation-metrics/precision)**: $$\text{Precision} = \frac{TP}{TP + FP}$$
3. **[Recall](/machine-learning-foundations/evaluation-metrics/recall) (Sensitivity or True Positive Rate)**: $$\text{Recall} = \frac{TP}{TP + FN}$$
4. **Specificity (True Negative Rate)**: $$\text{Specificity} = \frac{TN}{TN + FP}$$
5. **F1 Score**: $$\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
6. **False Positive Rate**: $$\text{False Positive Rate} = \frac{FP}{FP + TN}$$
7. **False Negative Rate**: $$\text{False Negative Rate} = \frac{FN}{FN + TP}$$
## Interpretation

- **Diagonal Elements**: The diagonal elements of the confusion matrix (TP and TN for binary classification) represent the number of correct predictions.
- **Off-Diagonal Elements**: The off-diagonal elements represent the number of incorrect predictions.
- **Balance of Classes**: The confusion matrix helps in understanding the balance of classes and the performance of the model on each class.

## Advantages

- **Comprehensive View**: Provides a comprehensive view of the performance of a classification model.
- **Detailed Insights**: Allows for detailed insights into the types of errors being made by the model.

## Limitations

- **Complexity**: Can become complex and difficult to interpret for multi-class problems with many classes.
- **Interpretation**: Requires a good understanding of the classification problem and the specific context to interpret the results correctly. In summary, a confusion matrix is a powerful tool for evaluating the performance of classification models. It provides a detailed breakdown of correct and incorrect predictions, allowing for a comprehensive analysis of model performance and identification of areas for improvement.
