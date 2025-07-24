---
title: 2. ANOVA Method
---

We already noticed that the summary function for a linear model gives us the result of the test comparing the fitted model against the one where no predictors are included.

We would obtain the same result fitting a model with no predictors and then using the command anova.

```python
model_0 = smf.ols(formula = "Fertility ~ 1", data = swiss).fit()
anova_lm(model_0, model_1)
```

![](../attachments/screenshot-2024-05-11-at-225345.png)

The same approach can be used to compare any two models that are **nested** between each other, meaning where one is a generalization of the other (i.e. it includes more predictors, it includes additional interactions and so on).

Let’s see if the models with all predictors (model) and the model where we dropped one predictor (model2) are **significantly different**.

`anova_lm(model_2, model_1)`
![](../attachments/screenshot-2024-05-11-at-225420.png)

Indeed they are not, since we noticed that the variable Examination is not useful to predict the response.
