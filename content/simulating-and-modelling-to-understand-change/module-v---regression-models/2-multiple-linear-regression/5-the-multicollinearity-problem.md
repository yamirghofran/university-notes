---
title: 5. The Multicollinearity Problem
---

**Multicollinearity refers to the correlation between predictor variables in the model**. It is a very common problem in multiple linear regression models.

Obviously, when there is a correlation between the variable we want to predict and the predictors we don’t have any problem, but **when there is a significant relationship between the predictor variables this can cause problems in the model**.

Multicollinearity exists whenever an independent variable is highly correlated with one or more of the other independent variables in a multiple regression equation.

Multicollinearity is a problem because it undermines the statistical significance of an independent variable.

Although multicollinearity does not affect the regression estimates, it makes them vague, imprecise, and unreliable. Thus, it can be hard to determine how the independent variables influence the dependent variable individually. This inflates the standard errors of some or all of the regression coefficients.

For variables that are highly related we would need to study them more deeply, and decide which of the two is more convenient to include in the model because it offers us a better result at a global level. We are never going to include two variables that have a high correlation between them.

To decide which variable we are going to leave in the model we are going to use the VIF (Variance Inflation Factor) test.

This method measures the increase in variability in an estimated coefficient of a particular variable due to the high correlation between two or more of the predictor variables.

**The inflation factor of the variance needs to be calculated for each and every one of the variables, and if the value is too high for a particular variable, this predictor has to be removed from the model.**

Some libraries calculate it automatically. To do this we will estimate a multiple regression model using as a dependent variable the variable that gives us problems and as independent the rest of predictor variables.

![](../attachments/screenshot-2024-05-11-at-195828.png)

The VIF is interpreted as follows:

- If VIF = 1 the variables have no correlation, there is no collinearity problem.
- If 1 < VIF < 5 the variables are moderately correlated with other predictor variables but can be part of the model
- If 5 < VIF we have a collinearity problem because the variable is highly correlated with the other variables of the model and we must eliminate it.

In today’s use case, you will have to do this calculation for all the variables in the model.
- Newspaper ~ TV+Radio
- Radio ~ TV+Newspaper
- TV ~ Newspaper+Radio

We will use the variance_inflation_factor method from statsmodels as follows:
![](../attachments/screenshot-2024-05-11-at-195945.png)

In the use case, you will have to do all these calculations and interpret the VIF indicators with the rules mentioned above in order to obtain useful conclusions for the selection of predictor variables.