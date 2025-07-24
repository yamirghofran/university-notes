---
title: 5. Model Predictions
---

We have already said that **our logistic regression model aims to classify whether a case will present an event (1) or not (0)**.

This means that **we are going to use our model to predict whether an observation is a success or a failure in terms of the variable y (dichotomous)**.

This classification is done by calculation of the **p**:

![](../attachments/screenshot-2024-05-12-at-124100.png)


Luckily, we don’t have to use any formulas to get the p from the expected log(odds) of our model because Python already does that so **we just have to take the fitted values using our model.**

`logit_model.predict(nba['gp'])`
![](../attachments/screenshot-2024-05-12-at-124145.png)

# Classifying Observations: Cutoff Points

Now then... how do we classify a case as success or failure based on the expected probability?

To do this, we must choose a **cutoff point**, that is, from what probability it is considered a success. As you will understand, the choice of the cutoff point is crucial when assessing how well the model fits.

In our example, we will start considering 0.5 as a good cutoff point. That is, players with a expected probability higher or equal than 0.5 will be classified as successes, and the rest as failures. In Python you can do it like this:

`nba["predictions"] = (predicted_probabilities > 0.5).astype(int)`

In this way, you will create a new column in your dataset where you classify the observations as 0 or 1 based on the cutoff point and the fitted values of the model. Now you can view your dataset in Python and compare the columns of predictions with those of actual values of y.

![](../attachments/screenshot-2024-05-12-at-124306.png)

There we have our predictions.
Now...what would happen if we change the cutoff point? Is 0.5 the optimal? How effective is our model? Can we improve it?

# Confusion Matrix
In logistic regression, a **confusion matrix is a table that is used to evaluate the performance of a classification model**. It is a two-dimensional table that shows the number of correct and incorrect predictions of the model, arranged in four categories or cells.

The four categories or cells in a confusion matrix for a binary classification problem are:

- **True Positive (TP)**: the model predicted a positive outcome, and it was actually positive.
- **False Positive (FP)**: the model predicted a positive outcome, but it was actually negative.
- **True Negative (TN)**: the model predicted a negative outcome, and it was actually negative.
- **False Negative (FN)**: the model predicted a negative outcome, but it was actually positive.

Obviously, our interest is to maximize the True Positive and True Negative, and minimize the False Negative and False Positive.

These four pieces of data are summarized in the following four categories:

- Number of real positives: TP + FN
- Number of actual negatives: TN + FP
- Number of correct predictions: TP + TN
- Number of incorrect predictions: FP + FN

![](../attachments/screenshot-2024-05-12-at-124429.png)

## Sensitivity (True Positive)
The true positive ratio (TPR) or model **sensitivity as the proportion of predictions that have been positive relative to those that the model had as positive:** 
- TPR = TP/(TP+FN)
## Specificity (True Negative)
The true negative ratio (TNR) or model **specificity as the proportion of predictions that have been negative relative to those that the model had as negatives:**
- TNR = TN/(TN+FP)

## Confusion Matrix in Python
To create the confusion matrix in Python and thus be able to see the number of cases in which our prediction has been good, using the cutoff point of 0.5, we will work with pandas to compute the metrics.

```python
conf_matrix = pd.crosstab(nba['target_5yrs'], nba["predictions"],
rownames=['Actual'], colnames=['Predicted'])
conf_matrix

```

![](../attachments/screenshot-2024-05-12-at-125131.png)

## Confusion Matrix Metrics

- **Accuracy**: it is the general evaluation. It evaluates the **number of TP and TN as a function of the total number of observations.**
- **Sensitivity**: It focuses on the TPs. **Rate of TPs in relation to the total number of positives.**
- **Specificity**: It focuses on TNs. **Rate of TN in relation to the total number of negatives.**

## Interpretation in our example
According to the **accuracy** metric, in general, our model is somewhat poor: **0.68** (in practice we will want an accuracy higher than 0.8 as a rule of thumb, and an accuracy near 0.5 means that our model is not different than randomness).

If we put the focus on **sensitivity, we can see that the rate of true positives is higher: 0.82**. On the other hand, if we focus on **specificity, we see that the true negative rate is much lower: 0.47.**

This interpretation will allow us to find the flaws in our model.

With this information, we can try to **change the cutoff point to improve the sensitivity or specificity of our model depending on our objective**. We will use **ROC curves** for doing this.

Here, our role as analysts is important since we have to decide whether to give more importance to hit positives or to hit negatives, i.e. to improve the sensitivity or the specificity of our model.

# ROC Curve

A model that is 100% correct would be 100% sensitive and 100% specific, but this never happens, and that is why ROC curve exists. This curve **gives us the ratio of true positives (sensitivity) on the vertical axis and the ratio of false positives (1-specificity) on the horizontal axis**. In this way we can visualize how increasing the sensitivity, specificity will decrease.

![](../attachments/screenshot-2024-05-12-at-125836.png)

**The more the curve fits to the upper left edge, the better the prediction of the model** as we will be able to maintain high sensitivity and specificity.

**The closer you get to the diagonal the worse the performance of the model** as we will be predicting 50% for each category.

We call the area below the ROC curve the **AUC index**.

## ROC Curve and AUC Index

ROC is a probability curve and **AUC represents the degree or measure of separability**. It tells how much the model is capable of distinguishing between classes. The higher the AUC, the better the model is at predicting 0 classes as 0 and 1 classes as 1.


This graph will help us **visually make the cut-off point decision for the model**. That is, from what value between 0 and 1 we will decide that the prediction is a positive value.
- The closer to 1 we will have a higher sensitivity and lower specificity (1-specificity is higher), so our model will predict positive values well.
- The closer we are to 0, the more specificity (1-specificity is lower) and less sensitivity, so our model will predict negative values well.

## ROC Curve in Python
```python

from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(nba['target_5yrs'],
predicted_probabilities)
roc_auc = auc(fpr, tpr)

```

![](../attachments/screenshot-2024-05-12-at-130105.png)

It means that there is a 74% chance that the model will be able to distinguish between a positive and a negative case.

# AUC Index

An excellent model has AUC near to the 1 which means it has a good measure of separability. A poor model has an AUC near 0 which means it has the worst measure of separability. In fact, it means it is reciprocating the result. It is predicting 0s as 1s and 1s as 0s. And when AUC is 0.5, it means the model has no class separation capacity whatsoever.

This is an ideal situation. When two curves don’t overlap at all means model has an ideal measure of separability. It is perfectly able to distinguish between positive class and negative class.


![](../attachments/screenshot-2024-05-12-at-130154.png)

When two distributions overlap, we introduce type 1 and type 2 errors. Depending upon the threshold, we can minimize or maximize them. When AUC is 0.7, it means there is a 70% chance that the model will be able to distinguish between positive class and negative class.

![](../attachments/screenshot-2024-05-12-at-130210.png)


This is the worst situation. When AUC is approximately 0.5, the model has no discrimination capacity to distinguish between positive class and negative class.

![](../attachments/screenshot-2024-05-12-at-130224.png)

When AUC is approximately 0, the model is actually reciprocating the classes. It means the model is predicting a negative class as a positive class and vice versa.

![](../attachments/screenshot-2024-05-12-at-130241.png)

# Optimizing Cutoff Point
For optimizing the cutoff point, there is not a specific function we can use in statsmodels or sklearn, so we will create the code for doing this, maximizing the sensitivity and the specificity for finding the best threshold:

![](../attachments/screenshot-2024-05-12-at-130303.png)

We can now use this cutoff point for computing the previous confusion matrix and its metrics:

![](../attachments/screenshot-2024-05-12-at-130316.png)