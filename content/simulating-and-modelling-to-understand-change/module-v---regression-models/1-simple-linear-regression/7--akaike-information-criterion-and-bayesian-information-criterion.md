---
title: 7.  Akaike Information Criterion and Bayesian Information Criterion
---

# AIC and BIC
In addition, we can obtain two additional parameters that give us information on the fit of a regression model, which are the **AIC(Akaike Information Criterion)** and the **BIC (Bayesian Information Criterion)**.

These two parameters actually report the model mismatch, so **we expect them to be small** to get a good fit.

**Their use is mainly oriented to the variable selection for the model. Many professionals measure whether there is a significant change in these values to decide whether one model works better than another by introducing a new variable into the model.**

**We will use them then to compare two models.**

To get these values we simply use the AIC and BIC attributes in the model we just created:
![](../attachments/screenshot-2024-05-11-at-135516.png)