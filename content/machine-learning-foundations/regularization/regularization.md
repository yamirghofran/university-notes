---
title: Regularization
---

Regularization in machine learning is a set of techniques used to prevent [Overfitting](/machine-learning-foundations/evaluation-metrics/overfitting) (making the model less complex) by adding a penalty to the [Loss Function](/machine-learning-foundations/loss-function). Regularization helps to simplify the model and make it more robust by discouraging complex models that fit the training data too closely.
In practice, it leads to higher bias, but significantly reduces the variance.
**Model Objective Function**: the expression optimized by the learning algorithm when training the model.
**Regularizing a model**: modify the objective function by adding a **penalizing term** whose values is higher when the model is more complex.
## Example
Given a two-dimensional feature vector $x= [x^{(1)}, x^{(2)}]$, [Linear Regression](/machine-learning-foundations/algorithms/linear-regression) objective is
$$
\min_{w^{(1)}, w^{(2)}, b} \left[ \frac{1}{N} \times \sum_{i=1}^{N} (f_i - y_i)^2 \right]
$$
- $[w^{(1)}, w^{(2)}]$ = weights (coefficients for linear regression) associated with different features of the model,
- $b$ = the bias term, which allows the model to shift predictions independently of the input values.
- $f_i$ = equation of the regression line, with form: $f_i = w^{(1)}x_1 + w^{(2)}x_2 + b$
- $y_i$ = true value/ground truth for the $i$-th data point in the dataset, the label that the model is predicting.
The ML algorithm minimizes the objective, reducing $w^{(1)}/w^{(2)}$ and $b$ from the training data. The model becomes less complex if some of the parameters w are equal or close to 0. 
This apples to models other than linear regression.
## Regularization Techniques
Here are some commonly used regularization techniques:
1. [L1-Regularization (Lasso Regression)](/machine-learning-foundations/regularization/l1-regularization-lasso-regression)
2. [L2 Regularization (Ridge)](/machine-learning-foundations/regularization/l2-regularization-ridge)
## 3. Elastic Net
Elastic Net is a combination of L1 and L2 regularization. It adds both the absolute and squared values of the coefficients to the loss function, balancing the properties of L1 and L2 regularization. The loss function with Elastic Net is: $$\text{Loss} = \text{Original Loss} + \lambda_1 \sum_{i} |w_i| + \lambda_2 \sum_{i} w_i^2$$
## 4. Dropout
- Each time we " run " a training example through the network, we temporarily randomly exclude some unit (neuron) from the computation.
- The higher the percentage of units excluded, the stronger the regularization effect.
- PyTorch: dropout added inside the model architecture, but we can use L1-2 and custom.
- While simple, dropout's flexibility and regularizing effect are very effective.
## 5. Early Stopping
- Saves the preliminary model after every epoch (checkpoints).
- Assesses each checkpoint's performance on the validation set.
- After some epoch, the model can start overfitting, and the model's performance on the validation data can deteriorate (bias-variance tradeoff)
- When the validation set's performance decreases, we keep running the training for N epochs (hyperparameter, lecture 16, slide 13) and pick the best checkpoint.
## 6. Data Augmentation
- It is often used to regularize models that work with images.
- In practice, applying data augmentation often results in an increased model performance.
## 7. Batch Normalization
- Should be called batch standardization.
- Standardizes (zero mean and unit variance) the outputs of each layer before the next layer receives them as input, i.e., the activations of each layer.
- Results in faster and more stable training, as well as some regularization effect, i.e., can improve convergence.
- Generally, it is a good idea to use batch normalization.
- PyTorch:
- Fully connected layers: nn. BatchNorm1d with 2D inputs: [batch_size, features]
- Convolutional layers: nn. BatchNorm2d with 4D inputs: [batch_size, channels, height, width]
## 8. Weight Decay
Weight decay is similar to L2 regularization but is applied directly to the weights during the optimization process. It gradually reduces the magnitude of the weights, helping to prevent overfitting.
## 9. Pruning
Pruning involves removing unimportant features or weights from the model. This can be done based on the magnitude of the weights or using more sophisticated techniques like sensitivity analysis.
## 10. Noise Injection
Noise injection involves adding random noise to the input data or the model parameters during training. This helps to make the model more robust to small perturbations in the input data. Regularization techniques are essential for building robust and generalizable machine learning models. The choice of regularization method depends on the specific problem, the type of model, and the characteristics of the data.
