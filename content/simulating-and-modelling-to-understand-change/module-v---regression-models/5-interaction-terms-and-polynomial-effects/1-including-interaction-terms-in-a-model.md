---
title: 1. Including Interaction Terms in a Model
---

# Interaction Models
Imagine that, for some reason, you have a lot of data about students' performance in a subject. With this data, you have built a multiple linear regression model that aims to estimate **the final grades** of students in a subject (dependent variable) **using the hours of study per week** (x1) and the **quality of the teacher** (x2, measured quantitatively) as predictor variables.

You hypothesize a first order model:
- y = 𝜷0 + 𝜷1x1 + 𝜷2x2 + 𝞮
- Line of means: E(y) = 𝜷0 + 𝜷1x1 + 𝜷2x2

As you well know, the student who does not study anything, no matter how good the teacher is, generally does not pass. But, if the teacher is very good and the student has studied something, the effects of those hours of study are multiplied. That is, **the effect of the hours of study that the student spends on the final grade depends on the quality of the teacher**. In the same way, **the effect of teacher quality on the final grade will also depend on the hours of study**, since the student who studies more will benefit more from the teacher's performance if it is good.

Note that I am talking about the effect on the dependent variable, not the value of the dependent variable.

To improve your model, you decide to take that possible interaction into account and you hypothesize the following model:

- y = 𝜷0 + 𝜷1x1 + 𝜷2x2 + 𝜷3x1 x2 + 𝞮
- E(y) = 𝜷0 + 𝜷1x1 + 𝜷2x2 + 𝜷3x1 x2

If x1 and x2 interact, this means that the effect of x1 on y depends on the value of x2, and vice
versa.

If they interact with each other to affect the values of the dependent variable, a model that takes this interaction into account is more accurate than a model that does not.

![](../attachments/screenshot-2024-05-11-at-222311.png)

## An Interaction Model Relating E(y) to Two Quantitative Independent Variables
![](../attachments/screenshot-2024-05-11-at-222347.png)

where
(β1 + β3x2) represents the change in E(y) for every 1-unit increase in x1, holding x2 fixed => **Estimated slope for x1**
(β2 + β3x1) represents the change in E(y) for every 1-unit increase in x2, holding x1 fixed => **Estimated slope for x2**

### Effect of Interaction

Given: 
![](../attachments/screenshot-2024-05-11-at-222428.png)

- Without interaction term, effect of x1 on y is measured by β1
- With interaction term, effect of x1 on y is measured by β1 + β3x2
	- Effect increases as x2 increases

Consequently, an interaction model is appropriate when the linear relationship between y and one independent variable depends on the value of the other independent variable.


![](../attachments/screenshot-2024-05-11-at-222756.png)

## Interaction Models
Once interaction has been deemed important in, for example, the model **E(y) = 𝜷0 + 𝜷1x1 + 𝜷2x2 + 𝜷3x1 x2**, do not conduct t-tests on the B coefficients of the first-order terms x1 and x2.

**These terms should be kept in the model regardless of the magnitude of their associated p-values shown on the printout.**

You will probably never know a priori whether interaction exists between two independent variables; consequently, you will need to fit and test the interaction term to determine its importance.

## Include Interaction Terms in Python

To include interaction terms in a regression model, you just have to use ‘*’ or ‘:’ like this:

An Interaction model relating E(y) to two quantitative independent variables in Python:

`model_formula = ‘dependent variable ~ ind. variable 1 * ind. variable 2’`

Or

`model_formula = ‘dependent variable ~ ind. variable 1 + ind. variable 2 + ind. variable 1: ind.variable 2’`

Interaction terms can be included in any type of model, just place `*` between the two variables that you believe interact to have an effect on the dependent variable.

## Interaction Models

Consider the problem of predicting sales based on Facebook, Youtube and Newspaper advertising budget.

![](../attachments/screenshot-2024-05-11-at-223051.png)

**A model without interactions assumes that, for instance, the effect on sales of youtube advertising is independent of the effect of facebook advertising.**

This assumption might not be true. For example, spending money on facebook advertising may increase the effectiveness of youtube advertising on sales. In marketing, this is known as a synergy effect, and in statistics it is referred to as an interaction effect.

Let’s start by fitting a standard multiple regression.

![](../attachments/screenshot-2024-05-11-at-223136.png)
Newspaper variable is not significant

![](../attachments/screenshot-2024-05-11-at-223204.png)

Let’s investigate whether an interaction may be helpful in our model. We have two options for plotting interaction effects, we will see both.
Remember that in order to create a model with interaction between youtube and facebook it is sufficient to write youtube*facebook to include both the interaction and the main effects.

![](../attachments/screenshot-2024-05-11-at-223219.png)

From the summary we notice that the interaction is significant.

Note that, sometimes, it is the case that the interaction term is significant but not the main effects. **The hierarchical principle states that, if we include an interaction in a model, we should also include the main effects, even if the p-values associated with their coefficients are not significant.**

Let’s try and understand the meaning of the interaction using the two plots.

![](../attachments/screenshot-2024-05-11-at-223251.png)

For different values of Facebook advertising budget the effect of youtube advertising on sales is always in the same direction(sales increase as advertise increases), but the relationship changes since the slopes are different. When facebook advertising increases, the effect of youtube advertising is stronger.