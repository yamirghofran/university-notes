---
title: 1. Intro to Multiple Linear Regression
---

Most practical applications of regression analysis utilize models that are more complex than the simple straight-line model.

For example, a realistic probabilistic model for reaction time would include more than just the amount of a particular drug in the bloodstream. Factors such as age, a measure of visual perception, and sex of the subject are a few of the many variables that might be related to reaction time. Thus, we would want to incorporate these and other potentially important independent variables into the model in order to make accurate predictions.

Imagine that you've just been promoted to human resources manager and you think that the way each worker is paid is not fair. Therefore, you decide to create a more objective method than the one that was established. This is a good opportunity to create a multiple regression model.

The first thing you would do is consult the company's databases and collect the information you consider important when determining a worker's salary (salary would be the dependent variable y). For example, seniority in the company (x1), level of specialization (x2) and working hours (x3) of all employees. These would be our independent variables.

Then you would have to do exploratory analysis to understand how these variables behave, what type they are and how they relate to the dependent variable. This analysis allows you to hypothesize a model (or models) that can describe well the relationship between these variables. This is the first step of a multiple regression analysis.

With a multiple linear regression analysis you can use this information to estimate the salary that should be paid to each employee in a more fair way, **you can see the cases that are above or below the estimated salary (and adjust them) and you can estimate the salary of new employees.**

If this model does not work well you may have to add more variables such as the production level of the company, or, remove some of the ones you have chosen, creating, thus, new models. Then you would only have to compare the results of each model to choose the best one.

**In this topic, we are going to talk about first order multiple linear regression models. These are the simplest models, since it is basically the same as we have seen in simple linear regression, but with more independent variables.**

Probabilistic models that include more than one independent variable are called multiple regression models. The general form of these models is:

y = (𝜷0 +𝜷1x1+𝜷2x2+𝜷3x3+....+𝜷kxk) Deterministic Component + 𝜺 (Random error component)

where

- **y** → dependent (or response) variable (quantitative variable to be modeled)
- **x1, x2, x3, x4** and so on → are the independent (explanatory/ predictors) variables (quantitative variables used as predictors of y)
- **E(y) = 𝜷0 +𝜷1x1+𝜷2x2+𝜷3x3+....+𝜷kxk** → Deterministic component or line of means (error = 0)
- 𝜷0 is the intercept of the model
- 𝜷1is the slope of the line that relates **y** and **x1, 𝜷2** is the slope of the line that relates y and x2, 𝜷3 the line that relates **y and x3,...and so on**
- 𝜺 is the **random error**

As you can see, the only difference with the simple linear regression models is that there are more independent variables (x) and, therefore, more slopes, one slope for each independent variable.
This is because each of the independent variables has a linear relationship with the independent variable and, therefore, when representing the complete model, we will no longer have only one line, we will have multiple lines. Many lines that end up forming difficult to interpret visualizations, like this one (with ONLY two independent variables):

![](../attachments/screenshot-2024-05-11-at-193047.png)

In the next visualization example we are plotting two IV against the DV we have in the class notebook. We can do it independently, or using a 3D plot, but this is the maximum number of variables we can plot together. In further slides we will see that we normally plot the predicted values against the IV in order to see the performance of the model.

![](../attachments/screenshot-2024-05-11-at-193143.png)

![](../attachments/screenshot-2024-05-11-at-193159.png)
Simple Linear Regression Analysis Steps

In multiple linear regression, we will follow the same steps: Build the Model, Evaluate the Model and Use the Model.

Only some of the metrics we will use and some interpretations will change as a consequence of the fact that we will now work with more independent variables, but the process is very similar.