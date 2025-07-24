---
title: 2. Probabilistic Models
---

y = 300 + 2.5x + ε

300+2.5x -> deterministic component
ε -> random error component

![](../attachments/screenshot-2024-04-01-at-121021.png)

## A First order (straight line) probabilistic model with a quantitative independent variable
$$y=\beta_0 + \beta_1 x + \epsilon$$
- y: Dependent or response variable (quantitative variable to be modeled)
- x: Independent or predictor variable (quantitative variable used as a predictor of y)
- $E(y)=\beta_0 + \beta_1 x$: Deterministic component or line of means (error = 0)
- $\beta_0$(beta zero): y-intercept of the line. Mean value of y when x=0. $E(y)=\beta_0 + \beta_1 (0) \to E(y)=\beta_0$
- $\beta_1$(beta one): slope of the line. The change (amount of increase or decrease) in the mean value of y for every 1-unit increase in x.
- $\epsilon$(epsilon): random error component which measures how far above or below the regression line (line of means) is from the actual observation of y. **The mean of $\epsilon$ is zero**.

A simple linear regression model contains 3 **unknown parameters**: $\beta_0$(intercept of the line), $\beta_1$(slope of the line) and the variance of the $\epsilon$ (if the line is well fitted we already know that the mean of the error is 0).

We will need to infer these parameters (or population characteristics), as always, using the information of our sample.


| Target parameters            | Estimators (from sample) |
| ---------------------------- | ------------------------ |
| $\beta_0$                    | $\hat{\beta_0}$          |
| $\beta_1$                    | $\hat{\beta_1}$          |
| $\sigma^2$ of the $\epsilon$ | $s^2$ of the $\epsilon$  |

