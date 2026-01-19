---
title: Recurrent Neural Networks
---

- For sequential data, connections form a loop to keep memory of past inputs
- Use: speech recognition, time-series forecasting, machine translation, chatbots.
- Data flow: loops allow information to persist across different time steps, making it suitable for sequence learning.
- Structure: Input layer → Recurrent hidden layers (with memory state) → Output.
- Activation function: Tanh/ReLU in hidden layers, Softmax for sequence classification.
- Loss function: Cross-entropy loss for classification, MSE for regression tasks.
- Learning: Uses gradient descent and backpropagation through time (BPTT) to update weights.
- Pros: Can handle sequential data, remembers previous inputs, good for time-dependent tasks.
- Cons: Suffers from vanishing gradients, struggles with long-term dependencies, slow training.
## Example Architecture
![](/machine-learning-foundations/attachments/cleanshot-2025-03-02-at-2244002x.png)
- RNNs have loops to feed back information from previous steps into the network.
- RNNs remember prior inputs, ideal for tasks where context is important

## Hyperparameters
- Embedding dimensionality of words
- Size of memory (dimensionality of memory vector)

## RNNs Unrolled
![](/machine-learning-foundations/attachments/cleanshot-2025-03-15-at-1352592x.png)
- Once unrolled, RNNs become chains of repeating units, often called "cells".
- RNNs take one input at a time and update an internal memory called hidden state.
 $$h_t = f(W_x X_t + W_h h_{t-1} + b)$$
-  $h_t$ = Hidden state at time step $t$ (memory)
-  $X_t$ = Input at time step $t$
-  $W_x$ = Weights for input $X_t$
-  $W_h$ = Weights for the hidden state (previous memory)
-  $b$ = bias
-  $f$ = Activation function (usually $\tanh$ or ReLU)

- Each cell is a "mini-network" that processes sequential data step-by-step with a set of neurons that apply transformations over time.
- `tanh` (hyperbolic tangent) is the activation function used after the sum product of current and past weights/inputs.
- `softmax` is one of the activation functions used for the output layer.
- Note: an RNN can produce an output (i.e. prediction) at each iteration and/or pass the hidden state to the next cycle without an output.
## RNN Patterns
![](/machine-learning-foundations/attachments/cleanshot-2025-03-15-at-1358072x.png)
- **Vector to Sequence** (one to many)
	- e.g. image captioning, input an image and get the caption one word at a time.
- **Sequence to Vector** (many to one)
	- e.g. spam classifier, reads in all email one word at a time and returns a spam/no-spam single token.
- **Encoder-Decoder** (many to many)
	- e.g. translation, gets a sentence in and then gets a translated out.
- **Sequence to Sequence** (many to many)
	- e.g. price forecasting, reads in a time series of stock volume/technical indicators and returns a price prediction for each input at time t.
## RNN Text Example
- Dataset
	- "I love machine learning"
	- "Deep learning is very difficult"
	- "Learning models "
- FNNs took the whole sentence as a single vector; **RNNs process each word sequentially**.
- Instead of [Bag of Words](/machine-learning-foundations/feature-engineering/bag-of-words) (which ignores order), we represent each sentence as a sequence of word indices, i.e. each sentence is a sequence of numbers.
![](/machine-learning-foundations/attachments/cleanshot-2025-03-15-at-1406292x.png)

- Instead of using BoW, we use **word embeddings**:
	- Convert each word into a dense vector of real numbers.
	- Capture relationships between words, e.g. "love" and "like" are similar.
- Each word index is mapped to a pre-trained or trainable embedding vector. This is done using an embedding layer in neural networks.
- Converted the sentence to an embedding matrix, i.e. sequence of dense vectors:
	- $[0.5, 0.2, 0.1, 0.8], [0.9, 0.1, 0.7, 0.4], [0.3, 0.8, 0.5, 0.6], [0.6, 0.7, 0.3, 0.9]$
	![](/machine-learning-foundations/attachments/cleanshot-2025-03-15-at-1418512x.png)
- We pass each element of the sequence to the RNN, one element at each time $t$.
- The RNN updates the hidden state $h$ at each time $t$, holding the entire sentence into the last hidden variable.
- Execution processes of "I love machine learning":
	-  $t_1 \rightarrow [0.5, 0.2, 0.1, 0.8] \rightarrow h_1 = f(W_x X_1 + W_h h_0) \rightarrow$
	-  $t_2 \rightarrow [0.9, 0.1, 0.7, 0.4] \rightarrow h_2 = f(W_x X_2 + W_h h_1) \rightarrow$
	-  $t_3 \rightarrow [0.3, 0.8, 0.5, 0.6] \rightarrow h_3 = f(W_x X_3 + W_h h_2) \rightarrow$
	-  $t_4 \rightarrow [0.6, 0.7, 0.3, 0.9] \rightarrow h_4 = f(W_x X_4 + W_h h_3).$
Note: the **size of the hidden state h is a hyperparameter** chosen based on the size of the input and the amount of "memory" we want to give to the RNNs.

-  Assume $h$ is a vector of size 8, each time step >0 compute a matrix like:

$$
h_2 = \tanh \left( 
\begin{bmatrix}
w_{1,1} & w_{1,2} & w_{1,3} & w_{1,4} \\
w_{2,1} & w_{2,2} & w_{2,3} & w_{2,4} \\
\vdots & \vdots & \vdots & \vdots \\
w_{8,1} & w_{8,2} & w_{8,3} & w_{8,4} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
x_{2,1} \\
x_{2,2} \\
x_{2,3} \\
x_{2,4} \\
\end{bmatrix}
+
\begin{bmatrix}
u_{1,1} & u_{1,2} & \cdots & u_{1,8} \\
u_{2,1} & u_{2,2} & \cdots & u_{2,8} \\
\vdots & \vdots & \ddots & \vdots \\
u_{8,1} & u_{8,2} & \cdots & u_{8,8} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
h_{1,1} \\
h_{1,2} \\
\vdots \\
h_{1,8} \\
\end{bmatrix}
+
\begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_8 \\
\end{bmatrix}
\right)
$$

-  1st Matrix ($W_X$): transforms the 2nd word from embedding space to hidden space.
-  2nd Matrix ($W_H$): transforms the previous hidden state into the current hidden state.
-  $\tanh$ applies to the resulting 8D vector that stores memory from $h_0$ and $h_1$.

- We take the final hidden state $h_4$ and pass it through a fully connected layer to predict sentiment:
	-   $y = \text{Softmax}(W_o h_4 + b_o)$
	-   $h_4$: final hidden state (memory of the sentence)
	-   $W_o$, $b_o$: weight matrix of the output layer and bias vector of the output layer
	-   Softmax converts outputs into probabilities for positive, neutral, or negative
- We need a fully connected output layer because the hidden state $h_4$ is not in the correct format for classification.
- $W_o$ and $b_o$ map $h_4$ to a probability distribution over possible sentiment classes.

$$
\begin{bmatrix}
y_{\text{Positive}} \\
y_{\text{Neutral}} \\
y_{\text{Negative}}
\end{bmatrix}
=
\text{Softmax} \left(
\begin{bmatrix}
w_{o,11} & w_{o,12} & \cdots & w_{o,1h} \\
w_{o,21} & w_{o,22} & \cdots & w_{o,2h} \\
w_{o,31} & w_{o,32} & \cdots & w_{o,3h}
\end{bmatrix}
\cdot
\begin{bmatrix}
h_{T,1} \\
h_{T,2} \\
\vdots \\
h_{T,h}
\end{bmatrix}
+
\begin{bmatrix}
b_{o,1} \\
b_{o,2} \\
b_{o,3}
\end{bmatrix}
\right)
$$
- The output of that matrix is
	- Positive: 89.1%
	- Neutral: 10.7%
	- Negative: 0.2%

- This concludes the **forward pass** of the RNN.
- During training, we implement a **backpropagation through time (BPTT)**
	- Compute the loss, comparing the resulting three classes probabilities to the true classes.
	- Compute the gradients backward through time.
	- Update weights $W_o$, $W_X$, $W_h$ by applying gradient descent.

## Problems with RNN
- Vanishing and exploding gradients that make long-term dependencies hard to learn.
- Slow training due to their sequential architecture, e.g. 100 words = 100 steps.
- Short-term memory due to finite size of hidden states.
- Bias towards recent inputs due to gradients decay as they backpropagate.

- RNNs update weights with BPTT, compute the gradient of the loss with respect to parameters using the chain rule.
$$
\frac{\partial L}{\partial W_h} = \sum_{t} \frac{\partial L}{\partial h_t} \cdot \frac{\partial h_t}{\partial h_{t-1}} \cdots \frac{\partial h_1}{\partial W_h}
$$
-  Repeatedly multiplying gradients by the weight matrix.
  - Eigenvalues < 1: weights shrink to near-zero (vanish);
  - Eigenvalues > 1: weights grow uncontrollably (explode)

-  Vanishing gradients:
  - Earlier time steps don’t impact learning, i.e., long-term dependencies are forgotten.
  - E.g., "not" in "I do not like this movie" could be forgotten.

-  Exploding gradients:
  - Weights become too large, getting NaN errors that stop the model from converging.
  - Loss fluctuates widely, and the model might memorize noise instead of patterns.
