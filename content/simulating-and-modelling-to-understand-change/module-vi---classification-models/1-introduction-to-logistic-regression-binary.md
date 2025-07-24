---
title: 1. Introduction to Logistic Regression (Binary)
---

**Linear regression** is a statistical model used to **predict continuous values of a response variable as a function of one or more predictor variables**. For example, we could build a linear regression model to predict a person's **height as a function of age, weight and gender**. In this case, the response variable (height) is continuous and can take any value within a specific range.

On the other hand, **logistic regression** is a statistical model used to **predict discrete values of a response variable as a function of one or more predictor variables**. In this case, **the response variable is binary (0 or 1) and represents the presence or absence of an event or condition**. For example, we could build a logistic regression model to predict **whether or not a person has diabetes as a function of age, weight and level of physical activity**.

Although these two types of models look different, they actually share some common features. Both models use a mathematical function that relates the predictor variables to the response variable. **In linear regression, this function is a straight line, while in logistic regression, it is a sigmoid function**.

In addition, both models use coefficients to measure the strength of the relationship between the predictor variables and the response variable.

In **linear regression, these coefficients** (slopes) represent the **change in the response variable when one of the predictor variables changes by one unit**.

In **logistic regression**, the **coefficients represent the change in the probability that the response variable equals 1 when one of the predictor variables changes by one unit**.

In order to better understand this relationship and to interpret the logistic regression coefficients appropriately, the following basic concepts must be kept in mind:
- Probability
- Odds
- Odds ratio

## Probability
**Definition**: Measure of the degree of certainty that an event may occur.
**Calculation:** Number of times the event occurs/total number of trials.
**Scale:** Number between 0 and 1. Where 0 equals an impossible event and 1 equals a certain event.

![](../attachments/screenshot-2024-05-11-at-233455.png)

I have played a card game 5 times, in which I have won 3 times and lost 2 times. According to this sample, **my probability of winning is 0.6**.

`p(win) = 3/5 = 0.6`

## Odds
**Definition**: A measure of the relative probability of an event occurring versus not occurring.
**Calculation**: ratio between the probability of the event happening/probability of it not happening.
**Scale**: ranges from 0 to infinity.

![](../attachments/screenshot-2024-05-11-at-233556.png)

I have played a card game 5 times, in which I have won 3 times and lost 2 times. According to this sample data, winning is 1.5 times more likely than losing.

![](../attachments/screenshot-2024-05-11-at-233649.png)

`odds(win) = (3⁄5)/(2⁄5) = 1.5`

## Odds Ratio
**Definition**: allows to compare the odds of an event in two groups.
**Calculation**: it is the division between the odds of event X in one group and the
odds of event X in another group. 
**Scale**: ranges from 0 to infinity.

![](../attachments/screenshot-2024-05-11-at-233740.png)

I have played a card game 5 times, in which I have won 3 times and lost 2 times.
After that, I have tried a different game and played it 5 times, in which I have won 1 time and lost 4 times.
According to this sample data, **winning in the first game is 6 times more probable than winning in the second game**.

```python
Odds (win1) = (3⁄5)/(2⁄5)= 1.5  
Odds (win2) = (1⁄5)/(4⁄5)= 0.25  
Odds ratio(win) = Odds (win1)/Odds (win2) = 6
```