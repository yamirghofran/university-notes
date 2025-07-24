---
title: Linear Regression
---

## What it does
- Fits a linear relationship between input [Feature](/machine-learning-foundations/feature-vector)s and the **target variable**.
- **Linear relationship** occurs when the change in the target variable (dependent variable) is pr oportional to the change in an input feature (independent variable).
## How it Works
It minimizes the sum of squared residuals ([[3. Fitting the Model - Least Squares Approach|least squares]])
$$ SSR = \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2 $$
## Preconditions
- Assumes linearity and [homoscedasticity](/machine-learning-foundations/homoscedasticity)
- No [multicollinearity](/machine-learning-foundations/multicollinearity)
## Evaluation
- **$R^2$** [[Y2Q2/Machine Learning Foundations/R-squared|R-squared]]
- [Mean Squared Error](/machine-learning-foundations/mean-squared-error) (MSE)
## Advantages
- Simple
- Interpretable
## Limitations
- Limited to linear relationships
- Sensitive to [outliers](/machine-learning-foundations/outliers)