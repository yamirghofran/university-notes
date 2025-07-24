---
title: 3. Best Subset Regression
---

We have come up with a model by dropping variables by ourselves. In this case it was feasible and we actually needed only one step. In the case of a large number of variables this may become infeasible to do and we need an automatic tool to give us at least a model to start with.

Suppose we have p predictors, where p is possibly large. To perform best subset selection, we fit a separate least squares regression for each possible combination of the p predictors. That is, we fit all p models that contain exactly one predictor, all models that contain exactly two predictors, and so forth.

We then look at all of the resulting models, with the goal of identifying the one that is best.

### Three-Stage Process
Step 1: Let M0 denote the null model, which contains no predictors. This model simply predicts the sample mean for each observation.
- Step 2: For k = 1, 2,..., p:
	- Fit all the models that contain k predictors;
	- Choose the best of these models and call it Mk. In this case, the best is defined as the one that has the highest R2
- Step 3: Select a single best model across M0,M1,...,Mp using the criteria of choice.

There is not a specific function in **Python** for obtaining the results of a best subset regression, so we have to create a program for performing those operations (this could be a good programming exercise if you want to try by yourselves).

In the Notebook of the session you can find a function developed for this purpose. Let’s see the results:

![](../attachments/screenshot-2024-05-11-at-225556.png)

![](../attachments/screenshot-2024-05-11-at-225609.png)

