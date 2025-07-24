---
title: 4. Forward and Backward Selection
---

These are the two approaches to selecting predictor variables and creating the final model:

- **Forward selection**: we **start with a null model without predictive variables and add variables one by one**. A variable that,when added to the model, results in a lower residual error, a smaller sum of the squared errors, will be the first to be added to the model. If the p-value for the variable is small enough and the value of adj R2 goes up, then the predictor variable will be included in the model. We will do successive steps with these rules.
- **Backward selection**: we **start with a model that has all possible predictor variables added and discard one by one**. If the p-value of a predictor variable is large enough, and the value of the adjusted R2 does not decrease significantly when it is removed or even increases, this predictor variable will be removed.

There are many statistical programs that automate these two approaches and Python, in particular, offers several libraries that implement these selection methods forward and backward automatically and we may see some of them. **But for today's use case I want you to compare all the options and select the best combination of predictor variables manually using backward or forward selection.**