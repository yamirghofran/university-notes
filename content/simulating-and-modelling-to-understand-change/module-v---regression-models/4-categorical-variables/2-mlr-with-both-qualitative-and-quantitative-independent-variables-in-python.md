---
title: 2. MLR with both qualitative and quantitative independent variables in Python
---

In a dataset, we can find two cases. For example:

- The qualitative variable Gender is a column with values "Male" or "Female".
- The qualitative variable Gender is a column with values 0 or 1. In this case, the values are coded in the dataset, i.e. 0 equals "Male" and 1 equals "Female" (or the other way around). In this case the variable is still qualitative even if its values are numbers.

The dummyfication process is done automatically in pandas using the `get_dummies` function.


Dataset info: The dataset contains statistics about the sales of a product (in thousands of units) in 200 different markets, together with the money spent on TV advertising , the money spent on Radio advertising, the money spent on Newspaper advertising in each of these markets (all of them measured in thousands of dollars), the type of Ad used (qualitative with 4 levels; AdType1, AdType2, AdType3 and AdType4), the Season in which the campaign was done (qualitative with 3 levels; Summer, Christmas and Standard) and the Country in which the campaign was done (qualitative with 2 levels; 0 (Spain) and 1 (Foreign Country))

In this example, your company has given you some more information, since, in addition to the money invested in advertising on TV, Radio and Newspaper, it wants to know the effect of the Season, the type of ad and the country to improve the sales volume.
Having this information may allow us to build a better and more powerful model to predict sales volume.

## Create Dummy Variables
We can use the `get_dummies` function to easily transform those variables into something our models can understand.

![](../attachments/screenshot-2024-05-11-at-220011.png)

Build a Multiple Linear Regression model is much easier dividing the dataset in predictors and target variables, but in this case we will use a model formula to identify all the different terms:

model_formula = ‘dependent variable ~ independent variable 1 + independent variable 2 +...+ independent variable k’

```python
model_formula = ‘Sales ~ TV + Radio + Newspaper + AdType_AdType2 + AdType_AdType3 +AdType_AdType4 + Season_Standard + Season_Summer + Country_1’
model = smf.ols(formula=model_formula, data=sales_data).fit()
```

![](../attachments/screenshot-2024-05-11-at-221619.png)

## Interpreting $\beta$ Estimates of the Qualitative Variables

We expect the value of E(y) to increase or decrease by (the value of the beta estimator i) if we use (the factor level i) compared to if we use (the factor level chosen as the base level), holding all other independent variables constant. Some examples:

Estimate 𝜷4→ We expect the the average sales volume to decrease by 2.7 (2706 units) if we use the Ad Type 2 instead of the Ad Type 1, holding all other independent variables constant.

Estimate 𝜷9→ We expect the the average sales volume to decrease by 0.039 (39 units) if the campaign is done in a Foreign Country instead of Spain, holding all other independent variables constant.

Estimate 𝜷7→ We expect the the average sales volume to decrease by 1.498 (1498 units) if the campaign is done in spring or autumn (Standard) instead of Christmas or close (winter), holding all other independent variables constant.

## Evaluate the Model
![](../attachments/screenshot-2024-05-11-at-221719.png)

![](../attachments/screenshot-2024-05-11-at-221734.png)

### Interpreting Key Metrics

**Adj. r2** → 94.2% of the sample variation in Sales volume (y) can be explained by using Season, AdType, money spent on TV advertising, on Radio advertising, on Newspaper and Country as predictors.

**s or RSE** → We expect most (95%) of the observed sales volume(y) to lie within ±2.484 (± 2484 units) of their respective predicted values (ŷ - 2.484, ŷ + 2.484) .

**p value f test for the slopes** → Since the p value (3.49e-114) is smaller than any reasonable value of alpha, we reject the H0 that all the slopes are equal to zero. That means that, at least one independent variable is useful for predictin se they are linearly related.

We expect the value of E(y) to increase or decrease by (the value of the beta estimator i) if we use (the factor level i) compared to if we use (the factor level chosen as the base level), holding all other independent variables constant. Some examples:

Estimate 𝜷4→ We expect the the average sales volume to decrease by 2.7 (2706 units) if we use the Ad Type 2 instead of the Ad Type 1, holding all other independent variables constant..

Estimate 𝜷9→ We expect the the average sales volume to decrease by 0.039 (39 units) if the campaign is done in a Foreign Country instead of Spain, holding all other independent variables constant..

Estimate 𝜷7→ We expect the the average sales volume to decrease by 1.498 (1498 units) if the campaign is done in spring or autumn (Standard) instead of Christmas or close (winter), holding all other independent variables constant.

## Use the `predict()` function
Imagine that your company wants to predict a range of the sales volume of a product that it will obtain in a campaign in which it will invest $20000 in TV advertising (TV = 20), $30000 in Radio (Radio = 30) and $2000 in Newspaper (Newspaper = 2).

This campaign will be launched at Christmas(Season = ‘Christmas’) to the public in Spain (Country = ‘0’) and the type 3 ad will be used (AdType = ‘AdType3’). At 95% confidence, what interval of sales volume (y) do you estimate to obtain if this campaign is launched to one of the 200 markets in the sample?

![](../attachments/screenshot-2024-05-11-at-221855.png)