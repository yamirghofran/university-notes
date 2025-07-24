---
title: 1. Model Selection Criteria
---

-Today we will look more closely at various techniques to choose which predictors to include in our linear regression model.
- You have already learnt some approaches:
- Using R2 or adj R2 to compare models;
- Checking whether the parameter of a predictor is significantly different from zero;
- Check the p-value of the F-test;
- Combine these with cross-validation to avoid overfitting problems.


Two additional criteria are the so-called [ Akaike Information Criterion (AIC) and the Bayesian Information Criterion (BIC)](/simulating-and-modelling-to-understand-change/module-v---regression-models/1-simple-linear-regression/7--akaike-information-criterion-and-bayesian-information-criterion).

We will not give a formal definition of either criterion, but just the intuition on how to use them. For both AIC and BIC the best model is the one with the smallest value of the index. (Note that conversely for R2 and adj. R2 a higher values is better).

Both indexes address, just like the adj. R2 the tradeoff between goodness-of-fit and complexity of the model. They are both computed by combining two terms: one assessing how well the model fits the data (using the maximum likelihood or a transformation of the SSE); the other assessing how complex our model is.

We will illustrate the use of these indexes later on.

## An Application

Consider the swiss data set, to identify the best model for predicting Fertility on the basis of socio-economic indicators.

`data.head()`
![](../attachments/screenshot-2024-05-11-at-224951.png)

The aim is to identify which covariate are significantly useful in predicting the response.

### A disclaimer

In this example we will exclusively focus on tools for model selection. HOWEVER, this does not mean that the other fundamental steps of a statistical analysis can be skipped or overlooked. Namely:

- You should always start with an exploratory data analysis;
- The methods we discuss today do not account for possible interactions and transformations of variables. Whether these are required can be understood through exploratory analysis and modelling;
- Once you come up with a model you should always check if its assumptions are met and tenable.

## The Standard Approach
Let's start with the full model.
```python
model_1 = smf.ols(formula = "Fertility ~ Agriculture + Examination
+ Education + Catholic + Infant_Mortality",

                  data = swiss).fit()
print(model_1.summary())
```

![](../attachments/screenshot-2024-05-11-at-225132.png)
**Examination** does not seem to be significant and therefore we may want to drop it.

```python
model_2 = smf.ols(formula = "Fertility ~ Agriculture + Education +
Catholic + Infant_Mortality",

                  data = swiss).fit()
print(model_2.summary())
```

![](../attachments/screenshot-2024-05-11-at-225217.png)

**Adj. $R^2$** is basically equal to the previous model, whilst the **pvalue for the F- test** has decreased and **F** has increased.
Regarding the [ AIC and BIC](/simulating-and-modelling-to-understand-change/module-v---regression-models/1-simple-linear-regression/7--akaike-information-criterion-and-bayesian-information-criterion) we see that both had decreased in the second model.