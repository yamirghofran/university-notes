---
title: Data Bias
---

Bias in data is an inconsistency with the phenomenon that data represents. 

# Types of Bias
## Selection Bias
Selection bias is the tendency to skew your choice of data sources to those that are easily available, convenient, and/or cost-effective. 

## Self-Selection Bias
Self-selection bias is a form of selection bias where you get the data from sources that "volunteered" to provide it. Most poll data has this type of bias.

## Omitted Variable Bias
Omitted variable bias happens when your [featurized](/machine-learning-foundations/feature-engineering) data doesn't have a feature necessary for accurate prediction.

e.g. if your churn prediction model doesn't know that a competitor has started to offer the same service for a lower price.

## Sponsorship/Funding Bias
E.g. a news agency is sponsored by a video-game company so they won't say bad things about it. If you're training a model on the news articles, your model will be suboptimal.

## Sampling Bias
Sampling bias (also known as [distribution shift](/machine-learning-foundations/distribution-shift)) occurs when the distribution of examples used for training doesn't reflect the distribution of the inputs the model will receive in production.

## Prejudice / Stereotype Bias
Prejudice / Stereotype Bias is often observed in data obtained from historical sources, such as books or photo archives, or from online activity such as social media, online forums, and comments to online publications.

## Systematic Value Distortion
Systematic value distortion is bias usually occurring with the device making measurements or observations. This results in a machine learning model making suboptimal predictions when deployed in the production environment.

## Experimenter Bias
Experimenter bias is the tendency to search for, interpret, favor, or recall information in a way that affirms one's prior beliefs of hypotheses. In ML often translates to the dataset being obtained from the answers to a survey given by a particular person, one example per person.

## Labeling Bias
Labeling bias happens when [Labels](/machine-learning-foundations/feature-vector) are assigned to unlabeled examples by a biased process or person.

# Ways to Avoid Bias
Question everything.