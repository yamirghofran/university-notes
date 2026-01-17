---
title: Predictive Power
---

The ability of a model to accurately predict outcomes or target variables based on input [Feature](/machine-learning-foundations/feature-engineering/feature-vector)s. It is a measure of how well a model generalizes to unseen data and captures the underlying patterns in the dataset. High predictive power means the model can make reliable predictions, while low predictive power indicates poor performance.

## Factors affecting predictive power
1. **Quality of Data:**
   - Clean, relevant, and well-preprocessed data improves predictive power. [missing values](/machine-learning-foundations/data/dealing-with-missing-attributes), [noise](/machine-learning-foundations/data/data-noise), and irrelevant features can degrade performance.
2. **Feature Selection and Engineering:**
   - [Selecting the most relevant features](/machine-learning-foundations/feature-engineering/feature-selection) and creating new meaningful features ([Feature Engineering](/machine-learning-foundations/feature-engineering/feature-engineering)) can significantly enhance predictive power.
3. **Model Choice:**
   - Different algorithms have different strengths and weaknesses. Choosing the right model for the problem is crucial for achieving high predictive power.
4. **Hyperparameter Tuning:**
   - Optimizing [Hyperparameter](/machine-learning-foundations/introduction/parameters-and-hyperparameters)s (e.g., learning rate, regularization strength) can improve a model's predictive power.
5. **Training Data Size:**
   - More data often leads to better predictive power, as the model can learn more robust patterns.
6. **[Bias-Variance Tradeoff](/machine-learning-foundations/hyperparameters/bias-variance-tradeoff):**
   - Balancing bias (error due to overly simplistic assumptions) and variance (error due to sensitivity to small fluctuations in the training set) is key to maximizing predictive power.


## Evaluating Predictive Power
### For #ml/classification  Problems:
-  **Accuracy**: Percentage of correctly predicted instances.
-  **Precision**: Proportion of true positives among predicted positives.
-  **Recall (Sensitivity)**: Proportion of true positives among actual positives.
-  **F1-Score**: Harmonic mean of precision and recall.
-  **ROC-AUC**: Area under the receiver operating characteristic curve, which measures the tradeoff between true positive rate and false positive rate.

### For #ml/regression  Problems:
-  **Mean Squared Error (MSE)**: Average squared difference between predicted and actual values.
-  **Root Mean Squared Error (RMSE)**: Square root of MSE, in the same units as the target variable.
-  **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual values.
-  **R-squared ($R^2$)**: Proportion of variance in the target variable explained by the model.
