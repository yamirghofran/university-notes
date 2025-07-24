---
title: Good Data
---

## Informative
Good data contains enough information that can be used for modeling.

e.g. if you want to train a model that predicts whether the customer will buy a specific product, you will need to possess both the properties of the product in question and the properties of the products customers purchased in the past.
## Good Coverage
Good data has good coverage of what you want to do with the model.

e.g. if you want to use a model to classify web pages by topic and you have a thousand topics of interest, then your data has to contain examples of documents on each of the thousand topics in quantity sufficient for the algorithm to be able to learn the difference between topics.

## Reflects Real Inputs
Good data reflects real inputs that the model will see in production.

e.g. if you train your models with photos of cars in daylight, when people use it with photos of cars at night in production, it will make more mistakes.

## Unbiased
Good data is [unbiased](/machine-learning-foundations/data-bias) as possible.

## Not a Result of a [Feedback Loop](/machine-learning-foundations/feedback-loop)
Good data is not a result of the model itself. This echoes the problem of the **feedback loop**.

e.g. you can't train a model that predicts the gender of a person from their name, and then use the prediction to label a new training example.
## Consistent Labels
Inconsistency can come from several sources:
- Different people do labeling according to different criteria (or interpretations).
- The definition of some classes evolved over time. Occurs when two similar feature vectors receive two different labels.
- Misinterpretation of user's motives. e.g. user ignores news article because already seen it, not because of dis-interest.
## Big Enough
Good data is big enough to allow generalization.

## Summary
- it contains enough information that can be used for modeling
- it has good coverage of what you want to do with the model
- it reflects real inputs that the model will see in production
- it is as unbiased as possible
- it is not a result of the model itself
- it has consistent labels
- it is big enough to allow generalization
---
- [Interaction Data](/machine-learning-foundations/interaction-data)
- [Questions about Data](/machine-learning-foundations/questions-about-data)