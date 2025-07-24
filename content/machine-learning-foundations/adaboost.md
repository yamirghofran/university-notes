---
title: AdaBoost
---

AdaBoost (Adaptive Boosting) is a popular ensemble learning algorithm that combines multiple weak models to create a strong predictive model. It was first introduced by Yoav Freund and Robert Schapire in 1996.

## Key Concepts
-  **Weak Models**: A weak model is a simple model that is only slightly better than random guessing. In AdaBoost, weak models are typically decision trees or decision stumps (a decision tree with only one level).
-  **Weighted Voting**: Each weak model is assigned a weight based on its performance. The final prediction is made by taking a weighted vote of all the weak models.
-  **Adaptive Learning**: AdaBoost is an adaptive algorithm, meaning that it adjusts the weights of the training data based on the performance of the previous models.

## How AdaBoost Works
The AdaBoost algorithm works as follows:
1. **Initialize Weights**: Assign equal weights to all training data points.
2. **Train Weak Model**: Train a weak model on the weighted training data.
3. **Calculate Error**: Calculate the error of the weak model on the weighted training data.
4. **Update Weights**: Update the weights of the training data based on the error of the weak model. The weights of the misclassified data points are increased, while the weights of the correctly classified data points are decreased.
5. **Repeat**: Repeat steps 2-4 for a specified number of iterations or until a stopping criterion is met.
6. **Final Prediction**: Make the final prediction by taking a weighted vote of all the weak models.

## AdaBoost Algorithm
The AdaBoost algorithm can be formalized as follows:

-  **Input**:
  - Training data: $(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)$
  - Number of iterations: $T$
-  **Initialize**:
  - Weights: $w_i = \frac{1}{n}$ for $i = 1, 2, ..., n$
-  **For** $t = 1, 2, ..., T$:
  - Train a weak model $h_t$ on the weighted training data
  - Calculate the error of the weak model: $\epsilon_t = \frac{\sum_{i=1}^n w_i \cdot \mathbb{I}(h_t(x_i) \neq y_i)}{\sum_{i=1}^n w_i}$
  - Calculate the weight of the weak model: $\alpha_t = \frac{1}{2} \cdot \ln\left(\frac{1 - \epsilon_t}{\epsilon_t}\right)$
  - Update the weights: $w_i = w_i \cdot \exp(-\alpha_t \cdot \mathbb{I}(h_t(x_i) = y_i))$ for $i = 1, 2, ..., n$
  - Normalize the weights: $w_i = \frac{w_i}{\sum_{j=1}^n w_j}$ for $i = 1, 2, ..., n$
-  **Output**:
  - Final prediction: $H(x) = \text{sign}\left(\sum_{t=1}^T \alpha_t \cdot h_t(x)\right)$

## Example
Suppose we have a binary classification problem with two features: $x_1$ and $x_2$. We want to classify points as either positive or negative. We use AdaBoost with decision stumps as the weak models.

|  | $x_1$ | $x_2$ | $y$ |
| --- | --- | --- | --- |
| 1  | 1    | 1    | 1   |
| 2  | 1    | 2    | 1   |
| 3  | 2    | 1    | -1  |
| 4  | 2    | 2    | -1  |

We initialize the weights as follows:

|  | $w$ |
| --- | --- |
| 1  | 0.25 |
| 2  | 0.25 |
| 3  | 0.25 |
| 4  | 0.25 |

We train the first weak model, which is a decision stump that splits on $x_1$. The error of the weak model is $\epsilon_1 = 0.5$. We update the weights as follows:

|  | $w$ |
| --- | --- |
| 1  | 0.25 |
| 2  | 0.25 |
| 3  | 0.5  |
| 4  | 0.5  |

We normalize the weights and repeat the process for a specified number of iterations. The final prediction is made by taking a weighted vote of all the weak models.

## Advantages
AdaBoost has several advantages, including:

-  **Handling high-dimensional data**: AdaBoost can handle high-dimensional data with a large number of features.
-  **Robustness to outliers**: AdaBoost is robust to outliers and noisy data.
-  **Handling missing values**: AdaBoost can handle missing values in the data.

## Limitations
-  **Computational complexity**: AdaBoost can be computationally expensive, especially for large datasets.
-  **Overfitting**: AdaBoost can suffer from overfitting, especially when the number of iterations is large.

## Real-World Applications
AdaBoost has been widely used in many real-world applications, including:

-  **Face detection**: AdaBoost has been used for face detection in images.
-  **Text classification**: AdaBoost has been used for text classification, such as spam vs. non-spam emails.
-  **Recommendation systems**: AdaBoost has been used in recommendation systems to predict user preferences.

