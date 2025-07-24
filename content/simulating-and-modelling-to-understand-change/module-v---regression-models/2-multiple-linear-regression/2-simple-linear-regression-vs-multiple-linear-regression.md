---
title: 2. Simple Linear Regression vs Multiple Linear Regression
---


When fitting the model we will also use the Least Squares Method to get the least squares line. The difference is that now we estimate more parameters, since we have a slope for each independent variable we use.

![](../attachments/screenshot-2024-05-11-at-193324.png)

In Python you just have to use the summary() function and get the summary of the model and you will obtain all the estimates, like in simple linear regression.

![](../attachments/screenshot-2024-05-11-at-193341.png)

## Interpretations
![](../attachments/screenshot-2024-05-11-at-193402.png)

## Evaluate the model
When evaluating the model we will also measure its accuracy (error variability), adequacy and usefulness.

![](../attachments/screenshot-2024-05-11-at-193430.png)

Note*: In the f test, we test -> 
![](../attachments/screenshot-2024-05-11-at-193504.png)

The problem with R-squared is that it will either stay the same or increase with addition of more variables, even if they do not have any relationship with the output variables. This is where “Adjusted R square” comes to help. Adjusted R-square penalizes you for adding variables which do not improve your existing model.

Hence, if you are building Linear regression on multiple variable, it is always suggested that you **use Adjusted R-squared to judge goodness of model**. In case you only have one input variable, R-square and Adjusted R squared would be exactly same.

Typically, the more non-significant variables you add into the model, the gap in R-squared and Adjusted R-squared increases.

![](../attachments/screenshot-2024-05-11-at-193801.png)

![](../attachments/screenshot-2024-05-11-at-193814.png)

## Interpretations

- **Adjusted $r^2$**: 100 (adj. r2) of the sample variation in y can be explained by using the independent variables used as predictors.
- **s or RSE**: We expect most (95%) of the observed y values to lie within 2s of their respective predicted values.
- p-value f test for the slopes: If the p-value is smaller than alpha, we reject the H0 that all the slopes are equal to zero. That means that, at least one model term is useful for predicting y because they are linearly related.
Note*: In the f test, we test -> 
![](../attachments/screenshot-2024-05-11-at-193504.png)

## Use the Model
In the same way as in simple linear regression, we will use a prediction interval to estimate a new individual value of y at a given value of x1, x2, x3, x4, ...xk; and we will use a estimation interval to estimate the mean value of all new values of y at a given value of x1, x2, x3, x4, ...xk.

In order to do that, we first create the ‘newdata’ in Python, and then we use the `get_prediction() `function to get the interval we want.