---
title: Multicollinearity
---

A situation in #ml/regression analysis where two or more independent variables are highly correlated, making it difficult to distinguish their individual effects on the dependent variable.
## Impact
- Inflates standard errors of coefficients.
- Leads to unreliable statistical tests (e.g., t-tests) and unstable estimates.
## Detection
- High correlation between predictors (Variance Inflation Factor, VIF > 10 is a common threshold).
- Condition Index or Eigenvalues from the correlation matrix.
## Consequences
- Difficulty in assessing the effect of each predictor.
- Potentially misleading p-values and confidence intervals.
## Solutions
- Remove or combine correlated variables.
- Use regularization techniques like Ridge Regression that can handle multicollinearity.
- [[Principal Component Analysis 1]] (PCA) to reduce dimensionality.