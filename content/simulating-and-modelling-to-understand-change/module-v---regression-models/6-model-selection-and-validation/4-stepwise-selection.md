---
title: 4. Stepwise Selection
---

For computational reasons, best subset selection cannot be applied when the number of p predictor variables is large.

Best subset selection may also suffer from statistical problems when p is large.

The larger the search space, the higher the chance of finding models that look good on the training data, even though they might not have any predictive power on future data.

Thus an enormous search space can lead to overfitting and high variance of the coefficient estimates.


For both of these reasons, stepwise methods, which explore a far more restricted set of models, are attractive alternatives to best subset selection.

Again, there is not an algorithm in statsmodels that allow us to perform the stepwise selection. We have two options, we can do it by hand or using a different library named “mlxtend”. Both options are used in the notebook.

Next we will see how to interpret the results of the mlxtend library.

## Forward Selection
Forward stepwise selection begins with a model containing no predictors, and then adds predictors to the model, one-at-a-time,until all of the predictors are in the model. In particular, at each step the variable that gives the greatest additional improvement to the fit is added to the model.

The three-stage process of performing forward stepwise selection includes:

- Step 1: Let M0 denote the null model, which contains no predictors. This model simply predicts the sample mean for each observation.
- Step 2: For k = 0,..., p − 1:
	- Consider all p−k models that augment the predictors in Mk with one additional predictor.
	- Choose the best among these p−k models, and call it Mk+1. Here, the best is defined as having the highest R2.
- Step 3: Select a single best model across M0, M1,..., Mp using the criteria of choice.
We can perform forward stepwise using regsubsets by setting method = "forward".

```python
forward_selector = SFS(linear_regression,
                       k_features="best",
                       forward=True,
                       floating=False,
                       scoring='r2',
                       cv=0)
forward_selector.fit(predictors, target)
forward_selected_features =
list(predictors.columns[list(forward_selector.k_feature_idx_)])
print("Forward Selection: ", forward_selected_features)
```
![](../attachments/screenshot-2024-05-11-at-225850.png)


The SequentialFeatureSelector (SFS) function in the mlxtend library has several parameters that control the feature selection process. Here's a description of the parameters we have used:
- k_features: This parameter specifies the desired number of features to select or a range of features to consider. You can set it to an integer, a tuple, or "best". When set to "best", SFS will automatically select the combination of features that yields the highest score according to the scoring metric.
	- Example: k_features=3, SFS will select 3 features; k_features=(3, 5): SFS will consider all feature combinations of sizes 3, 4, and 5; k_features="best": SFS will choose the best combination of features based on the scoring metric.
- floating: This is a boolean parameter (True/False) that controls whether to enable "floating" in the stepwise process. Floating allows features to be added or removed dynamically during forward or backward selection. This can help in identifying better feature subsets, as it allows the algorithm to reconsider features that were previously added or removed. If set to True, floating is enabled, and if set to False, floating is disabled.
- scoring: This parameter specifies the scoring metric to evaluate the performance of the feature combinations. It should be a string representing a valid scikit-learn scoring metric, such as 'r2' (R-squared), 'neg_mean_squared_error' (negative mean squared error), or 'neg_mean_absolute_error' (negative mean absolute error). The scoring metric is used to determine the best feature subset, with higher scores indicating better performance.
- cv: This parameter represents the number of cross-validation folds to use when evaluating the performance of the feature combinations. Cross-validation is a technique that divides the dataset into several subsets (folds) and trains and evaluates the model on each fold, providing a more reliable estimate of the model's performance. If cv is set to an integer, that number of cross-validation folds will be used. If set to 0 or None, no cross-validation is performed, and the model is trained on the entire dataset.

## Backwards Selection
Backward stepwise selection provides an efficient alternative to best subset selection. However, unlike forward stepwise selection,it begins with the full least squares model containing all p predictors, and then iteratively removes the least useful predictor, one-at-a-time.

The three-stage process of performing backward stepwise selection 
includes: 
- Step 1: Let M0 denote the full model, which contains all p predictors.
- Step 2: For k = p, p − 1, ...1:
	- Consider all k models that contain all but one of the predictors in Mk, for a total of k - 1 predictors.
	- Choose the best among these k models, and call it Mk-1. Here, the best is defined as having the highest R2.
● Step 3: Select a single best model across M0, M1,..., Mp using the criteria of choice.

We can perform backward stepwise using regsubsets by setting method = "backward"

```python
backward_selector = SFS(linear_regression,
                        k_features="best",
                        forward=False,
                        floating=False,
                        scoring='r2',
                        cv=0)
backward_selector.fit(predictors, target)
backward_eliminated_features =
list(predictors.columns[list(backward_selector.k_feature_idx_)])
print("Backward Elimination: ", backward_eliminated_features)
```
![](../attachments/screenshot-2024-05-11-at-230200.png)

## Stepwise Selection
For this simple example forward, backward and best subset identify the same model as the best one for every number k of predictors included.

However notice that in general this is not the case:

- Different subsetting procedures (best subset vs. forward stepwise vs. backward stepwise) will likely identify different “best”models.
- Different indexes (AIC, BIC, and Adj. R2) will likely identify different “best” models.
Therefore it is important to highlight that these tools are not to be used for automatic modeling but as a starting point in situations where there are just too many covariates.