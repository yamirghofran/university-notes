---
title: 3. Fitting the Model - Least Squares Approach
---

To determine whether a linear relationship between x and y is plausible, it is helpful to plot the sample data in a scatterplot. You can place a ruler on the scatterplot to draw a visually fitted line (that represents the relationship between the two variables) and visually estimate the (unknown) population parameters: the intercept ($\beta_0$) and the slope ($\beta_0$).

![](../attachments/screenshot-2024-04-01-at-122254.png)

In Python, you can get a scatterplot with the plot.scatter() function. Like this:

```python
data.plot.scatter(x = "drugperc", y = "reactime", figsize = (10,8))
```

## Least Squares Method
The first condition for finding a line that fits is that the **sum of the errors is equal to 0**. We’ve find a well adjusted line if the sum of the errors (or residuals) is equal to zero.

According to the Least Squares Method, the best line is the **one whose SSE is the minimum**.

- **Sum of the errors** is the sum of the differences between the values of the sample data points (what we get) and the values we expect (using the line).
- **SSE is the sum of squared errors**. This metric is more reliable because it makes the negative errors visible (among other things).

Therefore, our mission is to obtain the equation that defines the line that best fits. Following the
Least Squares method, this line is called the Least Squares Line.

The **least squares line** $\hat{y}=\hat{\beta_0}+\hat{\beta_1}x$ is the line that has the following two properties:
1. The sum of the errors equals 0, i.e. mean error of prediction = 0.
2. The sum of squared errors (SSE) is smaller than that for any other straight-line model.

The least squares line $\hat{y}$ is the sample estimator of the deterministic component $E(y)$. That is, the least square line is the best estimator of the true line of means -> $E(y)=\beta_0+\beta_1 x$.

![](../attachments/screenshot-2024-04-01-at-123035.png)
Using LSM:
![](../attachments/screenshot-2024-04-01-at-123058.png)

![](../attachments/screenshot-2024-04-01-at-123237.png)


![](../attachments/screenshot-2024-04-01-at-123247.png)


In this step, we have defined the best-fitting straight line to be the line that minimizes
the SSE around it, and we called it the least squares line. **We should interpret the**
**least squares line only within the sampled range of the independent variable (x)**.

**We have worked with the values of the sample**. Even when the interpretations of the
estimated parameters in a simple linear regression are meaningful, we need to
remember that they are estimates based on the sample. As such, their values will
typically change in repeated sampling.