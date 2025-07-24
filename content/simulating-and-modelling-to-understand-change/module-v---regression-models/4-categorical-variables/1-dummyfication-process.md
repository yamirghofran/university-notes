---
title: 1. Dummyfication Process
---


We have already seen how to work with:
- SIMPLE LINEAR REGRESSION → One quantitative response or dependent variable and one quantitative independent variable (also called explanatory or predictor).
- MULTIPLE LINEAR REGRESSION → One quantitative response or dependent variable and more than one quantitative independent variable (also called explanatory or predictor)
- MULTIPLE LINEAR REGRESSION → One quantitative response or dependent variable and several quantitative and qualitative independent variables.

Multiple-regression models can also be written to include qualitative (or categorical) independent variables. **Qualitative variables, unlike quantitative variables, cannot be measured on a numerical scale. Therefore, we must code the values of the qualitative variable (called levels) as numbers before we can fit the model.**

These coded qualitative variables are called dummy (or indicator) variables, since the numbers assigned to the various levels are arbitrarily selected. For example, if we want to include gender in our model as a predictor we first have to ‘dummify’ the variable:
- Gender: qualitative variable with two categories; female (level A) and male (level B).
- Gender = x (dummy variable)

![](../attachments/screenshot-2024-05-11-at-202216.png)

![](../attachments/screenshot-2024-05-11-at-202227.png)

Therefore, if we want to follow the logic of regression modeling, we can create a model that relates E(y) to a qualitative independent variable with two levels or values as you see in the slide. Note that this case could be analyzed through ANOVA.

In this example **we hypothesize a model that relates the mean of the variable y to an independent qualitative variable x (in this case gender)**. As a result of the dummyfication of the gender variable, we will obtain two models, i.e. two distinct lines describing the relationship between the two variables.

One model for each value of the qualitative variable.

If we want to dummify a factor with more categories we have to create more dummy variables. Always use a number of dummy variables that is one less than the number of levels of the qualitative variable. Thus, for a qualitative variable with k levels, use k - 1 dummy variables.

Civil Status: qualitative variable with four categories; married, single, divorced and widowed. Civil Status = x1, x2, x3 (three dummies)

- x1 → 1 if married, 0 if not
- x2 → 1 if single, 0 if not
- x3 → 1 if divorced, 0 if not
- x1, x2 and x3 = 0 if widowed (base level)

![](../attachments/screenshot-2024-05-11-at-202527.png)

![](../attachments/screenshot-2024-05-11-at-202551.png)

Now imagine that you want to build a model with, for example, two quantitative and two qualitative independent variables. Imagine a model in which you are going to try to relate salary (y) to age and height (quantitative) but also gender and civil status (qualitative).

The number of combinations and resulting models is enormous! A model that has so many combinations needs many dummy variables and will return a model for each combination of the values of the qualitative variables.

Luckily you know how to write code so you don't have to worry about all this. But you will have to understand how to interpret the slopes.

Imagine that you want to create a model to predict the annual salary of the first jobs of young Americans who have recently graduated from college.

To do this, you obtain a data sample with information on three variables: Early Career Pay (dependent, quantitative), Public or Private University (factor) and Reputation Score of the University (quantitative).

## Interpretation of beta estimates of each category
We expect the value of E(y) to increase or decrease by (the value of the beta estimator i) if we use (the factor level i) compared to if we use (the factor level chosen as the base level), holding all other independent variables constant.

![](../attachments/screenshot-2024-05-11-at-202700.png)

![](../attachments/screenshot-2024-05-11-at-202713.png)

We expect the mean value of Early Career Pay to increase by $4617.3 if the students come from a Private University compared to those coming from a Public University, holding all other independent variables constant.