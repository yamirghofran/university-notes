---
title: Supervised Learning
---

Use datasets composed of **labeled data** to perform operations like #ml/classification and #ml/regression .

## Preconditions
1. Obtain a labeled dataset
2. split the dataset into [Training and Holdout Datasets](/machine-learning-foundations/data/training-and-holdout-datasets)
3. Ensure that records in the validation and test datasets are statistically similar and independent.
4. [Data Imputation](/machine-learning-foundations/data/data-imputation) and [Feature Engineering](/machine-learning-foundations/feature-engineering/feature-engineering)
5. Convert all examples into numerical feature vectors
6. Select a performance metric that returns a single number.
7. We have a [Baseline](/machine-learning-foundations/evaluation-metrics/baseline)

## Main Algorithms
- [Linear Regression](/machine-learning-foundations/algorithms/linear-regression)
- [Logistic Regression](/machine-learning-foundations/algorithms/logistic-regression)
- [Decision Tree](/machine-learning-foundations/algorithms/decision-tree)s
- [Random Forest](/machine-learning-foundations/algorithms/random-forest)s
- [Support Vector Machines](/machine-learning-foundations/algorithms/support-vector-machines) (SVM)
- [k-Nearest Neighbors](/machine-learning-foundations/algorithms/k-nearest-neighbors) (KNN)
- [Naive Bayes](/machine-learning-foundations/algorithms/naive-bayes)
- [Gradient Boosting Machines](/machine-learning-foundations/algorithms/gradient-boosting-machines)
- [SGD](/machine-learning-foundations/deep-learning/stochastic-gradient-descent) Regressor/Classifier
## Examples
- Handwritten Digit Recognition
- Spam Detection
- Customer Segmentation
- Personalized Treatment
- Credit Scoring
- Churn Prediction
- Object Detection
- Sentiment Analysis.
- Fraud Detection.
- Learn Detection.

## Limitations
- Needs significant amount of labeled data: time-consuming and expensive.
- Training data must represent real-world scenarios and avoid [biases](/machine-learning-foundations/data/data-bias).

## Classification
Predicts the category the data belongs to.
e.g. spam detection, churn prediction, sentiment analysis, dog breed detection.

## Regression
Predicts a numerical value based on previously observed data. e.g. house price prediction, stock price prediction, height-weight prediction.

## Other Problems
Under specific conditions, supervised ML can solve problems beyond classification and regression.

- Ranking problems
- Metric learning
- Time-series forecasting
- Anomaly detection
- Structured prediction
- Imitation learning