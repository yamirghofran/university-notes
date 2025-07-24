---
title: 3. Using the residuals analysis to improve our model
---

In Python, through the ols_resid_plots() function (developed for the course), we can see all the graphs necessary to check the assumptions of the error of our model.

`ols_resid_plots(model)`

![](../attachments/screenshot-2024-05-11-at-200533.png)

## Linearity and Mean of the Error

We use the top-left plot

![](../attachments/screenshot-2024-05-11-at-200613.png)


This plot shows Residuals vs fitted values.

- To get a reliable model, **we want the red line to be as horizontal as possible and to match the dotted line**.
- The points above the dotted line are positive residuals and those below are negative, so, in order for the mean of the residuals to be equal to or close to 0, we want the residuals to be equally dispersed above and below the dotted line.
- In our case, **we can consider that the assumption is met**. Since the line is practically horizontal and we can see that the errors are not distributed following a pattern that would indicate otherwise.

![](../attachments/screenshot-2024-05-11-at-200740.png)



| In this other case we see that the residuals follow a curve pattern. This could mean that our model would improve if we used a higher order polynomial regression because to describe curved relationships we do not use a straight linear model, we use a polynomial one, and if the residuals of the polynomial model still show a curve, we increase the order of the model.                                                                                                                                  | ![](../attachments/screenshot-2024-05-11-at-200902.png) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| For example, the model in this other case is a quadratic or second order model since one variable is squared and is intended to describe a relationship between variables through a curved line. But, according to this plot, a second order does not seem sufficient so we would look to see what happens if we apply a cubic or third order model, or even a higher order model. It could also mean that we are not taking into account an interaction effect or that some outliers are influencing our model. | ![](../attachments/screenshot-2024-05-11-at-200942.png) |

## Normality of the Error

We use the top-right plot
![](../attachments/screenshot-2024-05-11-at-201056.png)

Normal QQ plot


- The Normal Q-Q plot is used to check if our residuals follow Normal distribution or not.
- **The residuals are normally distributed if the points follow the dotted line closely**
- In our case residual points follow the dotted line closely except for observation 131.
- So we can say that our model residuals have passed the test of Normality.
- This assumption is usually fulfilled except for cases of important outliers that are far away from the line, which are usually important outliers that are affecting our model negatively and should be excluded of our dataset. It seems that observation 131 is an observation that we have to keep an eye on as we might improve our model if we get rid of it.
- We will normally use an additional KS test to ensure this results.

## Homogeneity of the Variance
Scale location plot indicates spread of points across predicted values range.
![](../attachments/screenshot-2024-05-11-at-201352.png)
- This plot shows if **residuals are spread equally along the ranges of predictors. It’s good if you see a horizontal line with equally spread points**.
- In our example we can see that the line is not completely horizontal but there is no clear pattern and it seems that the errors are distributed in a similar way throughout the model.
- However, observation 131 still stands out and, as mentioned above, it may be better to remove it from our dataset.

## Recheck Outliers
We use the bottom-right plot

Is a plot that allows us to recheck the outliers in a more rigorous way than with the boxplot method we used in the exploratory phase of the project.

![](../attachments/screenshot-2024-05-11-at-201450.png)

**The Residuals vs Leverage plot**
- On this plot, outlying values are identified with their index ID in red.
- The critical value for the Cook’s distance threshold will change depending on the sample size and the influence of the outliers in the model
- In this case we can clearly see that the case 131 (index 130) is an outlier, so we could eliminate the case and run the model again to see if we improve the performance.

## Independence of the Errors

**Statistical test. Durbin Watson**
In the case of the last assumption where we talked about the independence of the errors, we do not have a plot to check if it is fulfilled. One option we can use is a **test called durbin watson whose null hypothesis is that the errors are independent and the alternative that they are dependent**. Thus, if the **pvalue** we obtain in the test is **greater than alpha**, we will fail to reject the null hypothesis and, therefore, the **assumption will be fulfilled**. However, if we obtain a very low p-value, we will reject the null hypothesis and it will mean that the errors of our model are not independent and, therefore, we should use another type of more complex model such as a time series model.

The test statistic for the Durbin-Watson test ranges between 0 and 4, where a value of 2 indicates no autocorrelation. A value of less than 2 suggests that there is positive autocorrelation in the residuals, while a value greater than 2 suggests negative autocorrelation. The closer the test statistic is to 0 or 4, the stronger the evidence for positive or negative autocorrelation, respectively.

We can also use the autocorrelation plot for visualizing the independence.

![](../attachments/screenshot-2024-05-11-at-201743.png)

![](../attachments/screenshot-2024-05-11-at-201801.png)