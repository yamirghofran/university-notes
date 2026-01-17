---
title: Backpropagation
---

Backpropagation, short for "backward propagation of errors," is a fundamental algorithm used in training artificial neural networks. It is the process by which the network adjusts its internal parameters (weights and biases) to minimize the error in its predictions. Here's a step-by-step explanation of how backpropagation works:

## 1. Forward Pass

- **Input**: The process begins with an input signal that propagates through the network layer by layer.
- **Activation**: Each neuron in a layer computes a weighted sum of its inputs, adds a bias term, and applies an activation function to produce an output.
- **Output**: The final output of the network is compared to the desired output (target) to calculate the error.

## 2. Error Calculation

- **Loss Function**: The error is quantified using a loss function, such as Mean Squared Error (MSE) for regression tasks or Cross-Entropy Loss for classification tasks.
- **Output Error**: The error at the output layer is calculated as the difference between the predicted output and the actual target.

## 3. Backward Pass

- **Gradient Calculation**: The error is propagated backward through the network. This involves calculating the gradient of the loss function with respect to each weight and bias in the network.
- **Output Layer**: The gradient of the loss with respect to the output layer's activations is computed.
- **Hidden Layers**: The gradient is then propagated backward through each hidden layer, using the chain rule of calculus to compute the gradient of the loss with respect to the weights and biases of each neuron.

## 4. Weight and Bias Update

- **Gradient Descent**: The weights and biases are updated in the direction that reduces the error. This is typically done using an optimization algorithm like Stochastic Gradient Descent (SGD), Adam, or RMSprop.
- **Weight Update**: Each weight is updated by subtracting the product of the learning rate and the gradient of the loss with respect to that weight.
- **Bias Update**: Similarly, each bias is updated by subtracting the product of the learning rate and the gradient of the loss with respect to that bias.

## 5. Iteration

- **Epoch**: The forward and backward passes are repeated for many iterations (epochs) over the training dataset. With each iteration, the network's parameters are adjusted to minimize the overall error.

## Mathematical Formulation

- **Forward Pass**: For a neuron $j$ in layer $l$, $$z_j^{(l)} = \sum_i w_{ji}^{(l)} a_i^{(l-1)} + b_j^{(l)}$$ $$a_j^{(l)} = \sigma(z_j^{(l)})$$ where $w_{ji}^{(l)}$ are the weights, $b_j^{(l)}$ is the bias, $a_i^{(l-1)}$ is the activation from the previous layer, and $\sigma$ is the activation function.
- **Backward Pass**: The gradient of the loss $L$ with respect to a weight $w_{ji}^{(l)}$ is given by: $$\frac{\partial L}{\partial w_{ji}^{(l)}} = \frac{\partial L}{\partial z_j^{(l)}} \frac{\partial z_j^{(l)}}{\partial w_{ji}^{(l)}}$$ where $\frac{\partial L}{\partial z_j^{(l)}}$ is the error term for neuron $j$ in layer $l$, and $\frac{\partial z_j^{(l)}}{\partial w_{ji}^{(l)}} = a_i^{(l-1)}$.

## Importance

Backpropagation is crucial for training deep neural networks because it provides an efficient way to compute the gradients of the loss function with respect to the network's parameters. This efficiency allows for the training of networks with many layers and parameters, enabling the development of complex models for various applications.
