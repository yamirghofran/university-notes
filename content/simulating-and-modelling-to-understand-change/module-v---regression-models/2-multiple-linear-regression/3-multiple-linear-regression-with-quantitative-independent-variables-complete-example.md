---
title: 3. Multiple Linear Regression with Quantitative independent variables. Complete example
---

![](../attachments/screenshot-2024-05-11-at-194137.png)

# Data Preparation

First of all, as always, we have to give our dataset the appropriate format (in case it does not have it).

Each variable is a column whose cells are the values of the variable.
- If the variable is quantitative, it has to be of the num class. 
- If the variable is qualitative, it has to be of the class character and we have to dummify it.

In this case, all the variables we are working with are quantitative.

# Build the Model

To fit the best model we use (as in simple linear regression) the function OLS().fit(). This time we take into account more than one independent variable. We include as many independent variables as we want by adding them together.

After that, we use the summary() function to get a summary of the model results.

```python
model = sm.OLS(target, predictors).fit()
print(model.summary())
```

We can also use the formula module in statsmodels as follows:

```python
model.smf.ols('Resp ~ Size + Circ', data).fit()
print(model.summary())
```

![](../attachments/screenshot-2024-05-11-at-194532.png)

## Interpreting the beta coefficients

- $\hat{\beta_0}$ → The average value of number of responses to the ad (y) is expected to be approximately 7 (0.064, measured in hundreds) if the size of the ad is 0 square inch (x1 = 0) and the number of newspapers in circulation is 0 (x2= 0). **Nonsensical**.
- $\hat{\beta_1}$ → The number of responses to ad (y) is expected to increase by 20 (0.205, measured in hundreds) for each 1 square inch increase in ad size (x1) **holding the newspaper circulation (x2) constant**.
- $\hat{\beta_2}$ → The number of responses to the ad (y) is expected to increase by 28 for each 1 point (1000 units) increase in newspaper circulation (x2) **holding the ad size (x1) constant.**
## Evaluate the model
![](../attachments/screenshot-2024-05-11-at-194743.png)

```python
sse = model.ssr
rse = np.sqrt(model.mse_resid)
mean_error = (rse/data["Resp"].mean())*100

print("SSE:",round(model.ssr, 3))
print("RSE:",round(np.sqrt(model.mse_resid), 3))
print("Mean Error:",round(mean_error, 3))
```
![](../attachments/screenshot-2024-05-11-at-194803.png)

- Adj. r2 → 95% of the sample variation in ad responses (y) can be explained by using the ad size (x1) and the number of newspapers in circulation (x2) as predictors.
- s or RSE → We expect most (95%) of the observed ad responses (y) to lie within 2s = ±0.57 (± 57 ad responses) of their respective predicted values (ŷ - 0.577, ŷ + 0.577) .
- p value f test for the slopes → Since the p value (0.0042) is smaller than any reasonable value of alpha, we reject the H0 that all the slopes are equal to zero. That means that, at least one model term (number of newspapers in circulation or ad size) is useful for predicting y because they are linearly related.
- mean error → Since the value is 11.55, this means that we are misestimating 11.55% of the cases with our model.

Since the model seems pretty good, we can use it to make predictions. In order to do that, we first create the ‘newdata’ in Python, and then we use the get_predictions() function to get the interval we want, as we did in simple linear regression.

The New York Times wants to estimate how many responses it can get to a new ad by circulating 3000 newspapers (x2 = 3) in which the ad is 7 square inches in size (x1 = 7). Create a prediction interval to obtain this estimate.

## Use the model

![](../attachments/screenshot-2024-05-11-at-194907.png)

Therefore, for a new ad with a size of 7 square inches (x1 = 7) appearing in 3000 newspapers in circulation (x2 = 3) we estimate (at 95% confidence) that we will receive between 118 and 350 responses ((1.178, 3.501) in hundreds).


The New York Times wants to estimate the average response it can get if all of its ads are 5 square inches in size (x1 = 5) and each of them appears in 2000 newspapers in circulation (x2 = 2). Construct an interval estimation to give an answer to this question.

![](../attachments/screenshot-2024-05-11-at-195015.png)

If all the ads are 5 squares inches in size and each of them appears in 2000 newspapers in circulation, we estimate (at 95% confidence) to get between 101 and 228 responses to the ads on average ((1.01, 2.28) measured in hundreds)).

