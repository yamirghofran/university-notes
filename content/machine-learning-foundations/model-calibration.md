---
title: Model Calibration
---

## Performance vs Calibration
Modern ML models output more than just the class label. Often, models calculate probability scores, with the label being a thresholded decision.
Consider a model that classifies emails as spam (1) or not spam (0).
The model actually outputs a number between 0 and 1. e.g. P(spam | features) = 0.93 i.e. the model is 93% confident this is spam.
With a threshold of 0.5, the model computes 0.93, which is greater than 0.5, and returns 1, indicating that the email is spam.
The "prediction" is merely the argmax (or a threshold) applied to a probability distribution, which represents the actual output of many classifiers.

## Model Calibration
How trustworthy are the probabilities outputted by an ML model?

Consider use cases in which ML is used for decision-making:
- medical diagnosis, financial risk assessment, autonomous driving, unmanned aerial vehicles, legal/judicial applications and disaster prediction.
- We use the model's output in further probabilistic computations, e.g. cost-sensitive decisions, downstream classifiers, simulations.

Calibration is about the reliability of predicted probabilities. How well do the model's predicted probabilities reflect the actual probabilities?
For a probability score of 0.70, how often is the model actually right, i.e. is the model actually correct about 70% of the time?
In a well-calibrated model, confidence ≈ reality.


- High performance, but poor calibration: our model correctly classifies many cases, but its probability scores are off (e.g. overconfident or under-confident)
- Good calibration but low performance: our model probability scores reflect real-world likelihoods, but the model is not good at separating classes.

## Example of Model Performance and Callibration
- Hypothetical binary classifier that tries to detect if an email is spam or not.
- We have a test set of 1000 emails, and the model gives the following outputs.

| Probability Score Bin | # Predictions | # Correct Predictions |
|-----------------------|---------------|-----------------------|
| 0.9 – 1.0             | 200           | 160                   |
| 0.7 – 0.8             | 300           | 180                   |
| 0.5 – 0.6             | 300           | 150                   |
| 0.3 – 0.4             | 100           | 40                    |
| 0.1 – 0.2             | 100           | 70                    |
- We now calculate performance and calibration.
- Performance (accuracy):
	- Total predictions = 1000
	- Total correct predictions = 160 + 180 + 150 + 40 + 70 = 600
	- Accuracy = 600 / 1000 = 60%
Calibration Check (Reliability):
- We evaluate how well the predicted probabilities match the actual outcomes.

| Probability Score Bin | Avg Probability Score | Accuracy         | Calibration Gap |
| --------------------- | --------------------- | ---------------- | --------------- |
| 0.9 – 1.0             | 0.95                  | 160 / 200 = 0.80 | −15%            |
| 0.7 – 0.8             | 0.75                  | 180 / 300 = 0.60 | −15%            |
| 0.5 – 0.6             | 0.55                  | 150 / 300 = 0.50 | −5%             |
| 0.3 – 0.4             | 0.35                  | 40 / 100 = 0.40  | +5%             |
| 0.1 – 0.2             | 0.15                  | 70 / 100 = 0.70  | +55% (!)        |
- The model is **overconfident** in the top bins: scores 95% confidence, but it's right 80% of the times.
- The model is **underconfident** in the lowest bin: scores 15% confidence, but it's righ 70% of the time.
- Even if the accuracy is okay, the predicted confidence scores are misleading.
- This is dangerous if we are using probabilities to make threshold-based decisions:
	- e.g. "send for human review if confidence is <70%"
	- Much worse, a doctor using an AI tool that says, "There's a 98% chance this requires surgery", but it's wrong 30% of the time when it says that
	- That's high performance but poor calibration. It would have been preferable if the model said "70%" if that's the actual likelihood. That helps the doctor make informed decisions.
- In the real world, not all errors are equal, and being sure of a wrong decision can be disastrous.

## Reliability Curves
![](../attachments/cleanshot-2025-05-07-at-0936292x.png)
- Classification problem
- Allows seeing how well the model is calibrated.
- **X-axis**: binned predicted probability
- **Y-axis**: actual observed outcomes
- **Diagonal line**: perfect calibration, i.e. the predicted probabilities match the observed frequencies exactly.
### Cases
- Curve is above the diagonal
	- The model is **underconfident** (predictions are lower than true frequency)
- Curve is below the diagonal
	- The model is **overconfident** (predictions are higher than true frequency)
- Well-calibrated model
	- The calibration plot oscillates arount the diagonal (shown as a dotted line)
	- The closer the calibration plot is to the diagonal, the better the model is calibrated.
- Logistic regression model in the figure
	- Returns the true probabilities of the positive class
	- Calibration plot is closest to the diagonal
- Not well-callibrated
	- The calibration plot usually has a sigmoid shape
	- Shown by the support vector machine and random forest models.
## Model Calibration for Multiclass Classification
- We have one calibration plot per class in a **one-versus-rest** way.
- One-versus-rest: Transform a multiclass problem into N binary classification problems and build N binary classifiers.
- Example
	- We have three classes {1,2,3}
	- We make three copies of the original dataset
	- First copy: we replace all labels not equal to 1 with a 0
	- Second copy: we replace all labels not equal to 2 with a 0
	- Third copy: we replace all labels not equal
	- We have three binary classification problems where we want to learn to distinguish between labels 1 and 0, 2 and 0, and 3 and 0.
	- In each of the three binary classification problems, the label 0 denotes the "rest" in "one-versus-rest".

## Calibration Techniques
### Raw Scores
Raw scores are continuous values the model computes before applying a decision threshold (e.g. 0.5 for binary classification).
These scores represent the model's confidence for class membership.
Examples of raw scores:
- Logistic regression or NN: the output of the sigmoid function (probabilities betewen 0 and 1)
- Support Vector Machines (SVMs): the signed distance to the decision boundary (can be any real number, positive or negative)
- Tree-based models: the proportion of trees voting for class 1 (i.e., estimated probability)
Example with a logistic regression
- Class labels: [0,1,0,1,1]; 0 = negative class, 1 = positive class. These are discrete, categorical predictions, i.e., no nuance or uncertainty.
- Raw probability scores: [[0.3, 0.7], [0.8,0.2], [0.45,0.55]] converted via a thresholding 0.5 to class labels: [1, 0, 1]
### Assumptions
- We have a trained model that outputs a score (e.g. logistic regression, SVM, trees)
- That score may not be well-calibrated, even if it's discriminative (i.e. performs well).
- We want to adjust the raw scores into better-calibrated probabilities.
### Platt Scaling (Parametric Calibration)
- Logistic regression model fitted on top of a classifier's output scores, typically a support vector machine (SVM), but it can work with others too.
- Maps the raw outputs (e.g. decision scores) of a classifier to well-calibrated probabilities between 0 and 1.
- Many classifiers (like SVMs or boosted trees) produce scores that don't represent probabilities. For example, an SVM gives a decision score 4.2, but what does that mean?
- Platt Scaling answers this by learning a mapping from the score to a calibrated probability.
### Isotonic Regression
- Unlike Platt Scaling, which assumes that a sigmoid is the correct shape for calibration, Isotonic Regression doesn't assume any fixed functional form.
- Isotonic Regression fits a monotonic (non-decreasing) function to map the predicted scores (from a classifier) to calibrated probabilities.
- Think of it like drawing a line through a staircase: the line must always go up (or stay flat), but it can have as many steps as needed to best fit the data.
- Use when we suspect a sigmoid curve does not describe calibration errors well, and we have enough calibration data to avoid overfitting.
- Avoid it when calibration dataset is small, or we are ok with a simpler but stable approximation (we go with Platt then)

Other techniques: Temperature scaling, dirilecht calibration, spline calibration, ensemble and stacking-based calibration.

### When to use them
- According to experiments
	- Platt scaling: use when the distortion in the predicted probabilities is sigmoid-shaped.
	- Isotonic regression: can correct a wider range of distortions but more prone to overfitting.
	- Isotonic regression: performs worse than Platt scaling when data is scarce.
- Experiments with eight classification problems
	- Random forests, neural networks, and bagged decision trees are the best learning methods for predicting well-calibrated probabilities prior to calibration.
	- After calibration, the best methods are boosted trees, random forest, and SVM.