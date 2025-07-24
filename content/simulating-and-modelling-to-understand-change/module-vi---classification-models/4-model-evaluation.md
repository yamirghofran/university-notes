---
title: 4. Model Evaluation
---

# Evaluation Metrics

As you can see in the summary of a logistic regression model that you have made with Logit(), in addition to the coefficients, there may be other metrics that help us understand how effective the model is and compare it with others.

- The **Null deviance**
- The **Residual deviance**
- The **AIC** →  reports the model mismatch, so we expect it to be small to get a good fit. By itself, we will not know if the AIC is large or small, so we will use it to compare with other models.


![](../attachments/screenshot-2024-05-12-at-123438.png)

# Accuracy
## Standard Error / RSE

In linear regression, we use the RSE metric to estimate where we expect 95% of the observed values of y to fall. The problem is that **this metric is based on the error distribution of a linear model being normal**, and this **does not apply in a logistic regression model whose response variable follows a Bernoulli distribution (0 or 1)**, where the probability of success is a function of the predictors.


# Adequacy
![](../attachments/screenshot-2024-05-12-at-123538.png)

## z test vs t test
In linear regression we use the t-test to assess the significance of individual variables. However, **in the case of logistic regression, we use the Wald statistic to assess the significance of the independent variables**. Instead of simple beta, exponential beta is used in logistic regression as the independent coefficient. Exponential beta provides an odd ratio for the dependent variable based on the independent variables. **This essentially is a probability of an event occurring vs. not occurring.**


## Wald test vs z test
**In the summary of the logistic regression you will see that instead of using a t-test a z-test is used. This z-test is actually a Wald test**. The Wald test is a test that uses the z-distribution but it is a specific test for the Maximum likelihood method.

In short, the Wald test is a test that uses the z-distribution to test whether the beta parameters are different from 0 and, therefore, serves to check whether the variable y has a real relationship with the variable associated with that beta.

**The test follows the same logic as the linear regression test but is adapted to the discrete nature of the variable y and to the new method we have used to estimate the betas (ML).**

## Interpretation

Therefore, as in linear regression, we must pay attention to the p-value of this test to see if the predictor variables of the model have a real relationship with the response variable.

Thus, **we want a significant p-value**, preferably less than any reasonable value of alpha. If the pvalue is not significant, perhaps the predictor variable associated with that beta is not related to y and, therefore, is not useful and should be removed from the model.

# Usefulness

## $R^2$ doesn't apply in Logistic Regression

R-squared for nonlinear models it is an **invalid goodness-of-fit statistic** for this type of model. R2 relates to the proportion of the sample variability around E(y) explained by the relationship between y and x.

To calculate this proportion, the **error measures of a linear model are used** (Least Squares), **which do not apply in a nonlinear model** (logistic regression, Maximum Likelihood), so that R2 is no longer a reliable metric.

Imagine a logistic regression model. Now, how would you get the difference between the expected value and the actual value?

## Akaike Information Criteria (AIC)

However, the **AIC is a good indicator of goodness of fit and is still valid for logistic regression**. Therefore, it is still useful for comparing models.

Recall that the **AIC is an estimate of the information lost when a given model is used to represent the process that generates the data**, so the model with the lowest AIC will be the one that loses the least information and, therefore, the best in this sense.

**We will use this metric and the Wald test to select the model variables.**

## Confusion Matrix and ROC Curve
If we cannot measure the accuracy of the model nor can we use the R2 to see how useful it is, what do we do to see if the model is effective?

In logistic regression we use the **Confusion Matrix and the ROC** Curve for this.

First, let's see how we use the model to make predictions since we will have to work with an important concept that will arise from how we **classify the fitted value** of an observation: the **cutoff point**.
