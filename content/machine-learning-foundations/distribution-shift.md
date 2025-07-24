---
title: Distribution Shift
---

When the distributions of the training data and test data are not the same.

## Causes
- Not enough data and/or not enough similarity between the dataset and production data.
- Data in production changes over time
	- New/outdated features and or labels
	- Consumer trends
	- Weather patterns
- e.g. lots of labeled images from the web, but our goal is to train a classifier on instagram photos.

## Types of Distribution Shift
- Covariate shift
	- Shift in values of features
- Prior probability shift
	- shift in the values of the target
- Concept drift
	- Shift in the relationship between the features and the label.

We can analytically detect that a shift has ocurred but understanding the type we are experiencing requires testing.

## Detecting Distribution Shift
### Visual Inspection
- Histograms, density plots, or boxplots of features from training and validation/test sets
- [Principal Component Analysis](/machine-learning-foundations/principal-component-analysis) or [t-SNE](/machine-learning-foundations/t-sne) projections of both datasets.
### Statistical distance metrics
Compare the distribution of features. e.g. Jensen-Shannon divergence (JSD) but there are other methods for the more statistically savvy engineers.
### Algorithmic ML
- Train a classifier to discriminate between datasets.
- Label all training data as 0 and validation data as 1.
- Train a classifier (e.g. logistic regression) to distinguish them.
- If the classifier performs much better than random guessing, a distribution shift exists.
## Identifying the Type of Distribution Shift
### Covariate Shift
- Train a classifier as described previously.
### Label Shift
- We assume that the way features are generated from labels doesn't change.
- Confusion matrix: $\hat{p}_{\text {test }}(Y)=C^{-1} \cdot p_{\text {test }}(\hat{Y})$
	- where C is the confusion matrix on the training set, and $\hat{Y}$ are predicted classes on test data
- Black Box Shift Detection (BBSD)
	- Train a classifier on the training set.
	- Use this classifier to generate soft predictions on both training and test data.
	- Compare the label distributions (e.g. histograms of predicted class probabilities) and check for significant differences that suggest label shift.
### Concept Drift
- Hardest to detect, as it often requires access to true labels Y in the test data.
- Measure performance (e.g.. accuracy, loss) of the original model on new data
	- if performance drops but covariate and label shifts are ruled out, we suspect concept shift.
- Check if misclassification patterns change in unusual ways.


--- 
- [Adversarial Validation](/machine-learning-foundations/adversarial-validation)