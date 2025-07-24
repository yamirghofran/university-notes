---
title: 2. Sigmoid Function and Logit Transformation
---

## From Linear Regression to Logistic Regression
In linear regression models, we used a function to predict a variable y (continuous), from the **linear combination** of other variables (continuous and/or discrete).
y = 𝜷0+ 𝜷1x + 𝜷2x + ...+ 𝜷nx + 𝜺

![](../attachments/screenshot-2024-05-11-at-233923.png)


In order to predict a (discrete) variable y (0/No, 1/Yes) from the linear combination of the independent variables, we have to transform the linear model function into what is known as a **logit model**. Therefore:
- We want to predict a variable that is categorical (dichotomous), for example: whether a disease is had or not, whether a loan is approved or not...
- Since we are talking about the occurrence or non-occurrence of an event, we have to use probability theory.
- This new alternative has to maintain one thing: that the probability is a linear combination of the independent variables. That is, a transformation of the linear model: a logit model.

![](../attachments/screenshot-2024-05-11-at-234012.png)

![](../attachments/screenshot-2024-05-11-at-234024.png)

Linear regression helps predict a numerical, continuous, unbounded variable, but not a dichotomous variable. **In a linear regression the variable y can be less than 0 and greater than 1**, and would not apply.
This forces us to look for an alternative way to **predict the event that is non-linear. This form must have a variable y that is between 0 and 1 → Probability**.

An alternative function that allows us to calculate a variable that lies between the values of 0 and 1 is the so-called **Logit** function.

![](../attachments/screenshot-2024-05-11-at-234126.png)


However, in the Logit function, the X-axis has as possible values the range of 0 and 1. Since we need these values to be on the Y-axis, it is necessary to obtain the **inverse of the Logit** function. This is known as the **Sigmoid** function.

![](../attachments/screenshot-2024-05-11-at-234202.png)

Then, starting from the logit function and calculating its inverse (sigmoid function), we could obtain the following equation, which, as we can see, fits the data points much better:

![](../attachments/screenshot-2024-05-11-at-234251.png)

However, since the model we are going to use in Python must be a linear function, a transformation must be applied so that it is equal to the linear combination of the variables. So, **the equation of the (simple) logistic regression model is**:

![](../attachments/screenshot-2024-05-11-at-234318.png)

Let’s see this step by step.
Remember that the equation of simple linear regression was given by the equation of a line that estimates the deterministic component, expressed as → E(y) = b0 + b1x
- y was a continuous variable, and the expected range of values for the variable was (-∞, +∞)
- In the case of x, this can be continuous or categorical, and the range of values can also be (-∞, +∞)
- However, when we move to logistic regression, the first difference we are going to find is that the y variable, **as a classification variable**, can no longer be continuous, but must be discrete. It will only be able to **take the values 0 and 1**.

**Problem** → To predict 0 or 1 using the same equation that we used with the linear regression is going to be practically impossible.
- To solve it we are going to look for a p value that is in a continuous range between 0 and 1 instead of working with the y value that is discrete.
- The starting point for logistic regression then will be to calculate p using the equation p = b0+ b1x.

The problem is that p i enclosed between 0 and 1, and the x variable is in the range (-∞, +∞).

What if instead of using p, we use the **odds**? We have seen that the odds could range from 0 to infinite!

● p/(1-p) = b0+ b1x  

It still does not belong to the same interval as the y variable in the linear regression, but at least

it is no longer between 0 and 1, but (0, +∞).

Problem → We have taken an additional step, but the **left side** of the equation still has the problem of being enclosed between (0, +∞), while the **right side, being a linear regression**, is enclosed from (-∞, +∞).

How can we solve it? We need to make an additional transformation to one of the two sides of the equation so that the right and left side ranges coincide.

The most standard solution is to apply the Natural logarithm to the left side, then:

● ln(p/(1-p)) = b0+ b1x

If we apply the logarithm to a number between (0, +∞), the result will be a number that goes from (-∞, +∞). With this transformation, the logarithm of any positive number goes from (-∞, +∞), the linear regression line that we already know also goes from (-∞, +∞). This transformation is known as **Logit**. This logarithm is based on e, it is a natural logarithm.

For **multiple logistic regression** we will be able to use the same transformation as for simple regression. Simply by adding more variables, we would have to enter more x and 𝛽 into the regression equation.