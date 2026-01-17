---
title: Homoscedasticity
---

Assumption that the **variance of errors or residuals is constant** across all levels of an independent variable in a #ml/regression model.
## Importance
- Ensures efficient and unbiased parameter estimates using OLS.
- Maintains validity for statistical tests like t-tests and F-tests.
- Supports accurate construction of confidence intervals.
## Detection
- Visual inspection via residual plots (expect random scatter without patterns).
- Statistical tests such as Breusch-Pagan or White's test.
## Consequences of Violation
- Leads to inefficient estimates if unaddressed.
- Results in invalid hypothesis testing and confidence intervals.
## Solutions for Heteroscedasticity:
- Transformations (e.g., log transformation) to stabilize variance.
- Use robust standard errors or Weighted Least Squares (WLS).