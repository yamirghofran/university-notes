---
title: Gradient Descent
---

Gradient descent is an optimization algorithm used to minimize the cost function in machine learning and deep learning. It is an iterative process that adjusts the parameters of the model to reduce the cost function gradually. Here's a step-by-step explanation of how gradient descent works:

## 1. **Initialize Parameters**

- Start by initializing the parameters (weights and biases) of the model with random values.

## 2. **Compute the Cost Function**

- Calculate the [Cost Function](/machine-learning-foundations/loss-function), which measures the difference between the predicted values and the actual values. Common cost functions include [Mean Squared Error](/machine-learning-foundations/mean-squared-error) (MSE) for regression tasks and [Cross-Entropy Loss](/machine-learning-foundations/cross-entropy-loss) for classification tasks.

## 3. **Compute the Gradient**
Compute the gradient of the cost function with respect to each [Parameter](/machine-learning-foundations/parameters-and-hyperparameters). The gradient indicates the direction and rate of the steepest increase in the cost function. It is typically computed using backpropagation in neural networks.

## 4. **Update Parameters**

Update the parameters by moving them in the opposite direction of the gradient. This is done using the following update rule:      $$\theta = \theta - \alpha \nabla_\theta J(\theta)$$      where:

- $\theta$ represents the parameters (weights and biases).
- $\alpha$ is the learning rate, a [Hyperparameter](/machine-learning-foundations/parameters-and-hyperparameters) that controls the step size.
- $\nabla_\theta J(\theta)$ is the gradient of the cost function with respect to the parameters.

## 5. **Repeat**

- Repeat steps 2-4 until the cost function converges to a minimum value or a maximum number of iterations is reached.

## Types of Gradient Descent

1. **Batch Gradient Descent**
- Uses the entire dataset to compute the gradient for each update. It is computationally expensive but provides a stable convergence.
2. **[Stochastic Gradient Descent](/machine-learning-foundations/stochastic-gradient-descent) (SGD)**
- Uses one sample at a time to compute the gradient and update the parameters. It is faster and more efficient but can be noisy and less stable.
3. **Mini-Batch Gradient Descent**
- A compromise between batch and stochastic gradient descent. It uses a small subset (mini-batch) of the dataset to compute the gradient and update the parameters. It balances the stability of batch gradient descent and the efficiency of stochastic gradient descent.

## Advantages of Gradient Descent

- **Simplicity**: Easy to implement and understand.
- **Efficiency**: Effective for large datasets and high-dimensional spaces.
- **Versatility**: Can be applied to a wide range of optimization problems.

## Disadvantages of Gradient Descent

- **Sensitivity to Learning Rate**: Choosing an appropriate learning rate is crucial. A very high learning rate can cause the algorithm to overshoot the minimum, while a very low learning rate can make the convergence very slow.
- **Local Minima**: Can get stuck in local minima, especially in non-convex optimization problems.
- **Saddle Points**: Can get stuck in saddle points, where the gradient is zero but it is not a minimum. Gradient descent is a fundamental algorithm in machine learning and deep learning, and understanding its principles is essential for building effective models.