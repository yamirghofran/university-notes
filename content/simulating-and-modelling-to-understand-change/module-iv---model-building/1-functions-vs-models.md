---
title: 1. Functions vs Models
---

A function is a mathematical concept: the relationship between an output and one or more inputs. One way to talk about a function is that you plug in the inputs and receive back the output.
For example, the formula y = 3x + 7 can be read as a function with input x and output y. Plug in a value of x and receive the output y. So, when x is 5, the output y is 22.
One way to **represent a function is with a formula, but there are other ways as well, for example graphs and tables**.

## Deterministic models
Would you be able to make a mathematical formula that relates the money you earn at a job in a day (y, in euros) to the overtime you work (x, in hours)? Suppose you have a fixed salary of 90 euros per day (standard working time) and you earn an additional 12 euros for each extra hour of work you do.
y = 90 + 12x
This is called a deterministic relationship. If we were to construct a model that hypothesize an exact relationship between variables, it would be called a deterministic model.



| ![](../attachments/screenshot-2024-03-08-at-205505.png) | ![](../attachments/screenshot-2024-03-08-at-205536.png) |
| ------------------------------------------ | ------------------------------------------ |

## Probabilistic Models
Now imagine that you have an e-commerce and you want to make a model that relates the revenue from monthly sales (y) to the monthly advertising expenses (x). Let's suppose that in the first 2 months you have earned 2.5 euros for every euro spent on advertising (each month). Do you think you can hypothesize a model that relates the revenue of a month with the money you invest in advertising in that month?
You also know that, if you don't spend money on advertising, you will earn, approximately, 300 euros per month.

y = 300 + 2.5x + 𝜺

Our probabilistic model will include both a **deterministic component** and a **random error component**.

| ![](../attachments/screenshot-2024-03-08-at-205734.png) | ![](../attachments/screenshot-2024-03-08-at-205753.png) |
| ------------------------------------------ | ------------------------------------------ |

A mathematical model is a mathematical expression of some phenomenon. Often describes relationships between variables.
A model can be a Deterministic Model (hypothesize exact relationships, with no error)
- Example: my age (y) and yours (x) → y = 10 + 1x
Or a Probabilistic Model (hypothesize two components: the Deterministic
component and the Random error)
- Example: sales volume (y) is 15 times advertising spending (x) + random error → y = 0 + 15x + ε
	- Random error may be due to factors other than advertising


![](../attachments/screenshot-2024-03-08-at-205850.png)

## Definitions

- The **response or dependent variable** is the variable whose behavior or variation you are trying to understand. On a graph, the response variable is conventionally plotted on the vertical axis.
- The **explanatory or independent variables** are the other variables that you want to use to explain the variation in the response. The previous figure shows just one explanatory variable, temperature. It’s plotted on the horizontal axis.
- **Conditioning on explanatory variables** means taking the value of the explanatory variables into account when looking at the response variables. When you looked at the gas usage for those months with a temperature near 49°, you were conditioning gas usage on temperature.
- The **model/fitted/predicted value** is the output of a function. The function (the model) has been arranged to take the explanatory variables as inputs and return as output a typical value of the response variable. That is, the model function gives the typical value of the response variable conditioning on the explanatory variables. The function shown in the previous figure is a model function. It gives the typical value of gas usage conditioned on the temperature. For instance, at 49°, the typical usage is 65 ccf. At 20°, the typical usage is much higher, about 200 ccf.
- The **residuals/errors** show how far each case is from its model value. For example, one of the cases plotted in Figure 6.2 is a month where the temperature was 13° and the gas usage was 191 ccf. When the input is 13°, the model function gives an output of 228 ccf. So, for that case, the residual is 191 - 228 = -37 ccf. Residuals are always “actual value minus model value.”

This way, **the idea of a function is fundamental** to understanding statistical models. Whether the function is represented by a formula or a graph, the function takes one or more inputs and produces an output. The output is the model value, the expected value, a “typical” or “ideal” value of the response variable at given levels of the inputs. The inputs are the values explanatory variables.

The **model function** describes how the typical value of the response variable depends on the explanatory variables. The output of the model function varies along with the explanatory variables. For instance, when temperature is low, the model value of gas usage is high. When temperature is high, the model value of gas usage is low. The idea of “depends on” is very important.

The model function describes a **relationship**. If you plug in values for the explanatory variables for a given case, you get the model value for that case. The model value is usually different from one case to another, at least so long as the values of the explanatory variables are different.
When two cases have exactly the same values of the explanatory values, they will have exactly the same model value even though the actual response value might be different for the two cases.

The **residuals** tell how each case differs from its model value. Both the model values and the residuals are important. The model values tell what’s typical or average. The residuals tell how far from typical an individual case is likely to be.

Models explain the **variation** in the response/dependent variable. Some of the variability is explained by the model, the remainder is unexplained. The model values capture the
“**deterministic**” or “explained” part of the variability of the response variable from case to
case. The residuals represent the “random” or “unexplained” part of the variability of the
response variable.