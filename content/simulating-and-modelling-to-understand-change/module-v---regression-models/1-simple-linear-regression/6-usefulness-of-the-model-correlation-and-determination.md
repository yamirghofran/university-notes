---
title: 6. Usefulness of the Model. Correlation and Determination
---

Sometimes we can fit a model that is adequate because we have enough evidence to indicate that the true slope is not zero, i.e., the independent variable (x) and the dependent variable (y) have a linear (straight) relationship, but, even if this relationship exists, it may be very weak. **When the relationship is very weak we may want to use another independent variable (if we have that information) to try to explain the behavior of the dependent variable.**

Therefore, **the model we propose will be more useful the stronger the relationship between these two variables.**

In this section we will answer these two questions to determine how useful our model is:

- How strong is the relationship between y and x? **Correlation coefficient (r)**
- How much does the information provided by x contribute to describing or predicting y? **Coefficient of determination ($r^2$)**

## Correlation coefficient (r)

Answers "According to our sample, how strong is the linear relationship between two variables"?

- The correlation coefficient measures the degree of association between the independent variable (x) and the dependent variable (y).
- The possible values of this coefficient range from -1 to 1, depending on the strength and direction of the relationship between the two variables.
- CAUTION: this coefficient does not indicate a cause-effect relationship.
- If the correlation between x and y is weak, we may want to find another independent variable (x) if we want to get good results in the prediction of the dependent variable (y).

![](../attachments/screenshot-2024-05-11-at-134548.png)![](../attachments/screenshot-2024-05-11-at-134557.png)

It seems that the information given by the correlation between two variables is the same as that obtained by making inferences about the true slope 𝜷1 .
It is true that both metrics give us information about whether the relationship exists and the direction of the relationship, but:
- The correlation coefficient **(r) is a value we get from the sample, so we need to make inferences about the true slope 𝜷1 to describe the REAL relationship** that exists between the two variables.
- The value of the true slope **𝜷1 does not indicate the strength of the relationship between the two variables**, that’s why **we use r**.
![](../attachments/screenshot-2024-05-11-at-134723.png)

Strong when $r \geq 0.7$

## Coefficient of determination ($r^2$)

Another way to measure the usefulness of a linear model is to **measure the contribution of x in predicting y**. To accomplish this, we calculate how much the errors of prediction of y were reduced by using the information provided by x (as compared to the errors we would obtain if we used only the mean of y to predict the value of new observations)

$r^2$ represents the proportion of the total sample variability around ȳ that is explained by the linear relationship between x and y.

![](../attachments/screenshot-2024-05-11-at-134912.png)

Note that **$r^2$ is always between 0 and 1 because r is between -1 and +1**. Thus, an $r^2$ of .60 indicates that **the variation of the y values about their predicted values has been reduced 60% by the use of the least squares equation ŷ, instead of ȳ, to predict y.**

![](../attachments/screenshot-2024-05-11-at-135040.png)

# Calculating and Interpreting Usefulness of the Model
![](../attachments/screenshot-2024-05-11-at-135128.png)

$r^2$: 81.67% of the sample variation in reaction time (y) can be 'explained' by using the percent of drug in the blood (x) in a straight-line model.

r: According to our sample data, there is a correlation of 0.904 (very high) between the percentage of drug in blood (x) and the reaction time (y). This indicates that there is a strong positive relationship between the two variables in our sample (DOES NOT IMPLY CAUSATION).

Conclusion: the percentage of drug in blood (x) seems to be a good predictor of reaction time (y).