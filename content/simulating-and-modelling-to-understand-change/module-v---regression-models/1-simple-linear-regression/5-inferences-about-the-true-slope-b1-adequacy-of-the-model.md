---
title: 5. Inferences about the true slope B1. Adequacy of the Model
---


![](../attachments/screenshot-2024-05-11-at-132723.png)

# Inferences about the true slope $\beta_1$

In previous sections we have estimated the value of the slope from sample information, but remember that this is an estimator, not the value of the true slope 𝛃1.

**To make sure that our model is adequate we have to demonstrate statistically that the true slope 𝛃1 is not equal to 0**, because, if we are not able to do it, maybe the value of the true slope is 0 and this means that there is NOT a linear relationship (straight line) between the independent variable (x) and the dependent variable (y).


**What can we do to try to prove that a population value is not equal to zero?**

Now that we have specified the probability distribution of e and found an estimate of the variance $s^2$, we are ready to make statistical inferences about the linear model’s adequacy in predicting the response y. Suppose the reaction times are completely unrelated to the percentage of drug in the bloodstream. 

What could then be said about the values of the slope and intercept in the hypothesized probabilistic model (y = 𝛃0+ 𝛃1x + 𝜺) **if x contributes no information for the prediction of y?**

The implication is that the mean of y—that is, the deterministic part of the model E(y) = 𝛃0+ 𝛃1x—does not change as x changes. In the straight-line model, this means that the true slope, 𝛃1, is equal to 0. Therefore, to test the null hypothesis that the linear model contributes no information for the prediction of y against the alternative hypothesis that the linear model is useful in predicting y, we test
- $H_0: \beta_1 = 0$
- $H_a: \beta_1 \neq 0$

## Hypothesis test about the true slope $\beta_1$
![](../attachments/screenshot-2024-05-11-at-133128.png)
![](../attachments/screenshot-2024-05-11-at-133152.png)

![](../attachments/screenshot-2024-05-11-at-133205.png)
![](../attachments/screenshot-2024-05-11-at-133223.png)

![](../attachments/screenshot-2024-05-11-at-133306.png)

![](../attachments/screenshot-2024-05-11-at-133319.png)

### Question
- Can we reject the H0 that the true slope is equal to zero in favor of the Ha that the true slope is not equal to zero? 
	- YES, because the p-value for the two-tailed test is smaller than alpha.
- Can we reject the H0 that the true slope is equal to zero in favor of the Ha that the true slope is lower than zero? 
	- NO, because the p-value for the lower-tailed test is greater than alpha.
- Can we reject the H0 that the slpw is equal to zero in favor of the Ha that the slope is higher than zero?
	- YES, because the p-value for the upper-tailed test is smaller than alpha.
## Interpretation
- A positive slope implies that E(y) increases by the amount of $\beta_1$ for each unit increase in x.
- A negative slope implies that E(y) decreases by the amount $\beta_1$ for each unit increase in x.
- If we can't reject the H0 that the $\beta_1 = 0$, we don't have enough evidence to demonstrate that there is a linear relationship between x and y.

![](../attachments/screenshot-2024-05-11-at-133811.png)


