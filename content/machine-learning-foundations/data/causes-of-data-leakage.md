---
title: Causes of Data Leakage
---

## Target is a Function of a Feature
e.g. you are building a model to predict housing prices. One of your features is the realtor commission that has a direct relationship to the house price that can be learned by the model. When using the model in production, you won't know the realtor's commission, so the model will perform poorly.

## Feature Hides the Target
![](/machine-learning-foundations/attachments/cleanshot-2025-01-18-at-1237122x.png)

## Feature From the Future
![](/machine-learning-foundations/attachments/cleanshot-2025-01-18-at-1237362x.png)

You are building a model to predict whether a person will repay their loan. One of your features is the number of late payment reminders. In production, this number will always be 0 because the loan hasn't been given yet. Therefore, your model will perform poorly.

