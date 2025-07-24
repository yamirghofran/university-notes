---
title: Neural Networks
---

## Introduction
- Training data containing examples of input-output pairs of the function to be learned.
- Artificial neural networks are popular machine learning techniques inspired by the mechanism of biological organisms.
- Computation units are metaphorically referred to as "neurons".
- Neurons are **linked** to one another, and each **input** to a neuron is **adjusted by a weight**, which influences the function calculated by that neuron.
- Neural Networks propagate the computed values from the input neurons to the output neuron(s), using the weights as intermediate parameters.
- **Learning occurs by changing the weights connecting the neurons.**
![](../attachments/cleanshot-2025-03-02-at-2211592x.png)
## How Neural Networks Learn
- Training data pairs are fed into the neural network, which uses the input representations to make predictions about the output labels.
- Training data provide feedback on the correctness of the weights, depending on how well the predicted output matches the annotated output label of the input.
- **Weights between neurons are adjusted in response to prediction errors.**
- Weights are changed carefully in a **mathematically justified way** so as to **reduce the error in computation** on that example.
- The goal of **changing the weights** is to **modify the computed function to make the predictions more accurate** in future iterations.
- By successively adjusting the weights between neurons **over many input/output pairs**, the Neural Network's function is refined over time to make more accurate predictions.
- e.g. if the NN is trained with many different images of bananas, it will eventually be able to properly recognize a banana in an image it has not seen before.
## Why Neural Networks Can Be Good Learners
- Neural Networks are computational graphs of basic ML models (metaphorically called neurons) connected in particular ways.
- Each basic ML model is a computing unit based on least-squares/[Logistic Regression](/machine-learning-foundations/logistic-regression).
- By combining multiple units, we increase the power of the model to learn more complicated functions of the data than those learned by the basic models.
- Neural Networks power depends on:
	- The way these units are combined (i.e. the **architecture** of a NN) affects the architecture's power and requires the analyst's understanding and insight.
	- Sufficient training data is necessary to learn more weights (i.e. the number of iterations or epochs) in these expanded computations graphs.
## Single Computational Layer - The Perceptron
- Dataset $(\overline{X}, y)$ where $\overline{X} = [x_1, \ldots, x_d]$ contains $d$ feature variables and $y \in \{-1, +1\}$ the observed value of the binary class value.
- Observed value: label, i.e., the target value we need to predict.
- As with all the ML models, we train the perceptron to predict $y$, and then use it to predict unobserved $y$ from $X$.
- Architecture of the perceptron:
	- **Input nodes**: contain $d$ nodes, each transmitting a feature $x$
	- **Edges**: have weights $\overline{W} = [w_1 \ldots w_d]$
	- **Output node**: computes the linear function $\overline{W} \cdot \overline{X} = \sum_{i=1}^d w_i x_i$
	- **Activation function**: maps the result to $[-1, +1]$ or $[0, 1]$, introducing non-linearity
	- **Loss function**: smoothened least-squares regression function
- Binary classification: $\hat{y} = \text{sign}\{\overline{W} \cdot \overline{X}\} = \text{sign}\left\{\sum_{j=1}^d w_j x_j\right\}$
$$
\text{sign}(y) =
\begin{cases}
+1, & \text{if } y \geq 0 \\
- 1, & \text{if } y < 0
\end{cases}
$$
## Neural Network Architectures
The architecture of a Neural Network refers to its structure, including the number of layers, types of connections, and activation functions.

Neural Networks are categorized based on connectivity, data flow, and purpose.

Types of Neural Network Architectures:
- [Feedforward Neural Networks](/machine-learning-foundations/feedforward-neural-networks): Data flow in one direction.
- [Convolutional Neural Networks](/machine-learning-foundations/convolutional-neural-networks): Uses convolutional/pooling layers.
- [Recurrent Neural Networks](/machine-learning-foundations/recurrent-neural-networks): Maintains a memory of previous inputs.
- [Long short-term memory](/machine-learning-foundations/long-short-term-memory) and gated recurrent units (GRU): Upgraded RNNs.
- [Transformers](/machine-learning-foundations/transformers): Capture long-range dependencies.
- Neural Architecture Search (NAS) Models: Optimize network structure.
- (unsupervised) generative adversarial networks (GANs): two competing NNs.
- (unsupervised) autoencoders: encode/decode data.
- Capsule networks: alternative to [CNN](/machine-learning-foundations/convolutional-neural-networks)s, retain positional relationships between features.
- Hybrid: CNN+RNN, Transformer+CNN, Autoencoder+GAN
- Kolmogorov-Arnold Networks (KANs), Physics-constrained neural networks... and more.