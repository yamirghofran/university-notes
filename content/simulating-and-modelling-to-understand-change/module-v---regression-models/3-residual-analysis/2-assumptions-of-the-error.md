---
title: 2. Assumptions of the Error
---

Up until now we have discussed how to evaluate whether a fitted model is good; but before making use of a fitted model, it is wise to check that it provides an adequate description of the data.

However, if we have not examined the data, to make sure that the model and techniques we have used are appropriate, we may find at a later stage that we have reached invalid conclusions.

In this section we consider general methods for checking regression models. All of them are informal and based on graphical methods. It is helpful to begin by considering formal definitions of the assumptions we have made so far when constructing our regression
models.

1. The mean of the residuals (the mean of the errors) has to be 0 or close to 0. **Mean of the error and Linearity of the model** → the deterministic part of the model captures all the non-random structure in the data
2. The residuals/errors of the model have to follow a normal (or close to a normal) distribution. **Normality of the error**.
3. The variance of the residuals/errors must remain constant. That is, it must be homogeneous. **Homogeneity of the variance** → the scale of the variability of the errors is constant at all values of the explanatory variables
4. The residuals/errors have to be independent of each other. **Independence of the errors**.
5. **The values of the explanatory variables are recorded without error** → This last assumption is not one which we can check by examining the data; instead we have to consider the nature of the experiment. The presence of appreciable error in the explanatory variables can cause a surprising amount of difficulty in fitting and interpreting the model.

Use:

- Dataset → SALESADVMLR2. Import it and call it dataset.
- Data preparation:
    - `AdType = pd.get_dummies(dataset['AdType'])`
    - `Season = pd.get_dummies(dataset['Season'])`
    -`dataset = pd.concat([dataset, AdType, Season], axis=1)`
- Best linear model → Sales ~ TV + Radio + AdType + Season

