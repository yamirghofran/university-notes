---
title: Properties of Good Features
---

## High Predictive Power
- How much does it influence the prediction? ([Predictive Power](/machine-learning-foundations/predictive-power))
- e.g. is marital status a good predictor of cancer? is it of the likelihood of crashing a car?
## Fast Computability
e.g. learning/inference time
- Training
	- the sparser, the less information, the more difficult to train
- Inference
	- trade-off between time to inference and quality of inference. The better, the longer.
## Reliability
Can we trust that we will get the value of a feature (e.g. API answer)? Can we trust that value?
## Un-correlatedness
Highly correlated features affect model performance. Small changes in input data may affect many variables and, thus, the model's overall performance.
## Unitary, easy to understand and maintain
The feature represents a certain, simple to understand and to explain quantity. e.g. weight, length, width, and color.