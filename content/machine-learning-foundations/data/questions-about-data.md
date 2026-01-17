---
title: Questions about Data
---

# Accessible?
- Does the data already exist?
- Is it accessible (physically, contractually, ethically, or from a cost perspective)
- Copyright permissions, etc
- Is the data sensitive (private customer information, government, etc)
- Do you need to anonymize the data, e.g. remove **personally identifiable information (PII)**?
# Sizeable?
- Usually you only can guess how much data you need from experience.
- How frequently does new data get generated?
- Can you gather the necessary size of data within the time frame of the project?
- To find out how much data you might need, model the model performance based on size and see where you reach a plateau.
- [Data Augmentation](/machine-learning-foundations/data/data-augmentation)

## 2 reasons for plateau:
- Not enough [informative](/machine-learning-foundations/predictive-power) features that your algorithm can leverage to build a more performant model.
- The learning algorithm you used is incapable of training a complex enough model using the data you have.

Some rules of thumb
- 10 times the number of features (often exaggerates)
- 100 or 1000 times the number of classes (often underestimates)
- 10 times the number of trainable [parameters](/machine-learning-foundations/introduction/parameters-and-hyperparameters) (usually applied to [Neural Networks](/machine-learning-foundations/deep-learning/neural-networks))

Just because you have big data doesn't mean you should use all of it. A smaller sample can give a better performance. It's important to ensure that the sample is representative of the whole big dataset through sampling strategies like [stratified and systematic sampling](/machine-learning-foundations/data/data-sampling).
# Useable?
- Data must be [tidy](/machine-learning-foundations/data/raw-and-tidy-data)
- We have to fix missing values through [Data Imputation](/machine-learning-foundations/data/data-imputation) techniques.
- We have to handle **duplicates**.
- Data can be **expired** or out of date.
- Data can be **incomplete** or **unrepresentative** of the phenomenon. e.g. photos of animals only during daylight.
# Understandable?
- It's important to know where each data attribute came from to avoid [Data Leakage](/machine-learning-foundations/data/data-leakage) and correctly tackle the correct business problem.
# Reliable?
- Can you trust the data labels?
- Delayed/indirect data labels. 
- Data obtained through a [Feedback Loop](/machine-learning-foundations/data/feedback-loop)?