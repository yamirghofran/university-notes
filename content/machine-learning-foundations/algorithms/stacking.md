---
title: Stacking
---

- Ensemble learning is training an ensemble model, which is a combination of several base models, each individually performing worse than the ensemble model.
- Train an ensemble of weak models, e.g., random forest and gradient boosting.
- Combining multiple weak models can create a strong ensemble because when multiple uncorrelated models agree, they are likely to agree on the correct outcome.
- Uncorrelated: use different features and/or different types of weak models. Same models with different hyperparameter tuning are unlikely to be strong.
- Three ways to combine weakly correlated models into an ensemble model:
	- Averaging: for regression or score-based classification. Averaging all models' predictions about input $x$.
	- Majority vote: for classification. Returning the majority class among all models' predictions about input $x$.
	- **Model stacking**: trains a strong model by inputting the outputs of other strong models.

![](/machine-learning-foundations/attachments/cleanshot-2025-05-04-at-1246502x.png)
- Combine classifiers $f_{1}, f_{2}$, and $f_{3}$, to train a metamodel
- All f predict the same set of classes.
- Create a synthetic dataset from the predictions of $\mathrm{f}_{1-3}$.
- Train the metamodel on the synthetic dataset.
## Training
- Use different machine learning algorithms and models,
- Weakly correlate base models by randomly sampling the features of the training dataset.
- The same learning algorithm can produce sufficiently uncorrelated models when trained with very different hyperparameter values.
## Evaluation & Tuning
- Ensure the meta-model combines base model outputs effectively, without overfitting
- Use k-fold cross-validation: how well a model generalizes to an independent dataset.
- Recap: split the dataset into k roughly equal parts (folds) and use one fold as the validation set and the others as the training set. Average the performance across all k folds.
- Prevent data leakage by using only out-of-fold predictions to train the meta-model
- Evaluate the full stack: it should outperform individual base models on the validation set.
- Tune base model hyperparameters independently, then train the metamodel on out-of-fold predictions.
- Tune the whole stack jointly via nested cross-validation (computationally expensive).

## Data Leakage
- Create the synthetic training set for the stacked model, following a process similar to the one for cross-validation.
- First, split all training data into $>10$ blocks. The more blocks the better, but the process of training the model will be slower.
- Temporarily exclude one block from the training data, and train the base models on the remaining blocks.
- Then use the models to make predictions on the excluded block.
- Obtain the predictions, and build the synthetic training examples for the excluded block by using the predictions from the base models.