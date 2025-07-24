---
title: 4. Specifying the Distribution of error and Estimating its Standard Deviation
---

## The Random Error $\epsilon$
There will be some data points that will not match the
expected value of y indicated by the estimated deterministic
component of the model. Between these data points and the
expected value of y (given a value of x) there is a distance
which we have called random error.

In the best fitting line we have drawn according to our sample,
the estimated values of the slope and the intercept will always
be the same, independently of the data point (estimated
deterministic component), while the value of the error can
change for each data point (as shown in the image).

![](../attachments/screenshot-2024-04-01-at-123635.png)

Thus, the probabilistic model that tries to explain the relationship between two quantitative variables has to take into account all possible values of random error.

Therefore, **the next step is to define the distribution of the error in our model**. To do this, we will follow a series of assumptions and understand some of the information we already have.
1. The first thing we are going to assume is that **the random error ε is normally distributed**.
To define what this normal distribution looks like we have to specify the value of its mean and variance (or standard deviation): $N(\mu, \sigma^2)$

But how to get these values?

Having used the least squares method to draw the line has already given us some
information. Remember that **the best fitting line fulfills two conditions**:

- The line guarantees that the sum of the errors is approximately zero.
- It has the lowest SSE of all possible lines.

The mean error is the sum of the errors divided by the total number of
observations. If the sum of the errors is 0 (or close), **the mean of the**
**distribution of the error will be 0 (or close)**.

With this, we already know that:
1. The distribution of the error $\epsilon$ is normal.
2. The mean of the distribution of the error $\epsilon$ is 0 for all settings of the independent variable x.

What we don't know is how to estimate the variance of this distribution, which will depend on the variability of the errors (or residuals) of the data we are working with.

However, we do know that this variance has to remain constant for all values of x, otherwise we would not be able to define the distribution of the error $\epsilon$ and our model would not be valid. This property is called **homoscedasticity**.

3. The variance of the distribution of the error $\epsilon$ is constant for all values of x.


It seems reasonable to assume that **the greater the variability of the random error $\epsilon$ (which is measured by its variance $\sigma^2$), the greater will be the error in the estimation of the model parameters $\beta_0$ and $B_1$ and in the error of prediction when $\hat{y}$ is used to predict y for some value of x.**
![](../attachments/screenshot-2024-05-11-at-131848.png)

The greater the variability of the random error $\epsilon_1$ the greater will be the errors.

![](../attachments/screenshot-2024-05-11-at-131921.png)

![](../attachments/screenshot-2024-05-11-at-131936.png)

### Back to the example (drug and reaction time)

![](../attachments/screenshot-2024-05-11-at-132027.png)

### Interpretation of s, the estimated standard deviation of $\epsilon$


![](../attachments/screenshot-2024-05-11-at-132102.png)

In our example, we expect most (95%) of the observed reaction time values to lie within 2s = 1.21106 of their respective predicted values.

That is, according to our sample, we expect that 95% of the values will fall within this interval ($\hat{y} - 1.21106, \hat{y} + 1.21106$)

**So, the larger the 2s, the less accurate our model is going to be.**

You can also interpret this value comparing it with the average of the real values of y, since the result of this proportion will offer us the error percentage of our model.

```python
mean_error = (rse/data["reactime"].mean())*100
```
30.277

This means that we are mis-estimating 30.27% of the cases with our model.

## The Random error
The last assumption:

4. The values of $\epsilon$ associated with any two observed values of y are independent. That is, the value of $\epsilon$ associated with one value of y has no effect on any of the values of $\epsilon$ associated with any other y values.


![](../attachments/screenshot-2024-05-11-at-132630.png)

These assumptions make it possible for us to develop measures of reliability for the least squares estimators and to devise hypothesis tests for examining the usefulness of the least squares line.

Fortunately, the assumptions doesn’t need to hold perfectly in order for least squares estimators to be useful. The assumptions will be satisfied adequately for many applications encountered in practice.