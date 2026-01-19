---
title: Feedforward Neural Networks
---

- Simplest type of artificial neural network, single/multi-layer perceptron
- **Use**: classification and regression tasks for structured data and simple features.
- **Data flow**: one direction (input → hidden layers and → output) no loops or cycles.
- **Structure**: input layer, N hidden layers, output layer.
- **Activation function**: 
	- Rectified linear unit (ReLU) for hidden layers
	- Sigmoid for binary classification
	- Softmax for multi-class classification.
- **Loss function**: 
	- MSE 
	- cross-entropy loss
- **Learning**: gradient descent + chain of calculus to optimize/compute weight updates
- **Pros**: simple implementation.
- **Cons**: not efficient for image, needs large datasets for deep architectures, can suffer from vanishing gradients without careful design.
![](/machine-learning-foundations/attachments/cleanshot-2025-03-02-at-2240252x.png)
## Execution Model
- Features are encoded, and each [Feature](/machine-learning-foundations/feature-engineering/feature-vector) is mapped to an input neuron ($X_n$)
- Each feature is mapped into a neuron of the following layer alongside a weight ($W_n$)
- Each receiving neuron performs two operations:
	- **Weighted sum:** $Z=WX+b$
	- **Activation function:** e.g. $f(z)=max(0,z)$
- This repeats for each neuron of each layer until the output layer outputs prediction $\hat{Y}$.
- Usually, hidden and output layers have different **activation functions**.
![](/machine-learning-foundations/attachments/cleanshot-2025-03-15-at-1300532x.png)
- After the model outputs $\hat{Y}$, we compare it to the true value $Y$ using a [Loss Function](/machine-learning-foundations/loss-function):
	- Binary Classification: Binary cross-entropy
	- Multi-class classification: categorical cross-entropy
	- Regression: mean squared error (MSE)
- We adjust the weights ([Backpropagation](/machine-learning-foundations/deep-learning/backpropagation)) using [Gradient Descent](/machine-learning-foundations/deep-learning/gradient-descent)
- Compute how much each weight contributed to the error.
- Adjust weights to reduce the error.
- Repeat for many iterations (epochs) until the model improves.
## Examples
- Look at how a FNN processes textual input.
- Sentiment Analysis: Classify the sentiment as positive
- Text Classification: Categorize sentences into topics (e.g. ML vs Science)
- How is input passed to the Neural Network?
- Encoding, e.g. [One-Hot Encoding](/machine-learning-foundations/feature-engineering/one-hot-encoding)
- Mapping each encoded feature to a set of neurons as large as the feature set
- Dataset
- "I love machine learning"
- "Deep learning is very difficult"
- "Learning architectures is useful"
- [Bag of Words](/machine-learning-foundations/feature-engineering/bag-of-words) encoder: 3 records, each with 10 features
- ![](/machine-learning-foundations/attachments/cleanshot-2025-03-15-at-1339252x.png)
Now that we have encoded the records, we need to map them to the neurons of the input layer to start to train the Neural Network.
- We use the hyperparameter **batch size** to decide how many records to pass to the NN at each training iteration.
**Batch Size = 1**
- We pass a single input record, e.g., $X = [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]$.
- We choose a **weight initialization method** (another hyperparameter) and get a weight vector, e.g., $W = [-0.26, -0.23, -0.25, -0.41, -1.16, 0.42, 0.36, -0.68, -0.19, -0.33]$.
- We choose a **bias initialization method** (yep, another hyperparameter) and get a bias vector, one bias value for each neuron of a layer.
- We compute the **weighted sum** ($Z = WX + b$):
	$$((-0.26*1) + (-0.23*0) + (-0.25*0) + (-0.41*0) + (-1.16*1) + (0.42*1) + (0.36*1) + (-0.68*0) + (-0.19*0) + (-0.33*0)) + b$$

**Why Bias?**
With the bias, the decision boundaries can be anywhere in the input space, not just through the origin. More flexible.

**Batch Size > 1, e.g. 3**
- We pass three input records to the NN as a matrix instead of as a vector.
$$
X = \begin{bmatrix}
1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 \\
\end{bmatrix}
$$
- Assuming a hidden layer with four neurons, we have a weighted matrix, e.g:
$$
W = \begin{bmatrix}
0.2 & 0.5 & 0.1 & 0.7 \\
0.3 & 0.8 & 0.2 & 0.6 \\
0.5 & 0.3 & 0.4 & 0.9 \\
0.6 & 0.2 & 0.5 & 0.4 \\
0.9 & 0.1 & 0.8 & 0.3 \\
0.7 & 0.4 & 0.2 & 0.1 \\
0.5 & 0.6 & 0.7 & 0.2 \\
0.3 & 0.7 & 0.9 & 0.8 \\
0.4 & 0.9 & 0.6 & 0.5 \\
0.1 & 0.2 & 0.3 & 0.7 \\
\end{bmatrix}
$$
- Compute weighted sums Z for the hidden layer $Z=XW$
$$
z = \sum_{i=1}^{n} X_i W_i + b
$$
$$
Z = \begin{bmatrix}
z_{1,1} & z_{1,2} & z_{1,3} & z_{1,4} \\
z_{2,1} & z_{2,2} & z_{2,3} & z_{2,4} \\
z_{3,1} & z_{3,2} & z_{3,3} & z_{3,4} \\
\end{bmatrix}
$$
- This is why we need GPUs/TPUs. Matrix multiplications can be efficiently parallelized across thousands of cores (e.g. GTX 4090 has 16384 CUDA cores)
	![](/machine-learning-foundations/attachments/cleanshot-2025-03-15-at-1347372x.png)
- Batch sizes vary depending on hardware, dataset size, and model type:
	- CPU: 16-32; GPU: 64-128: Server-grade GPU: 256-1024+; TPU: 512-4096

## Implementation

```
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
# Generate a synthetic dataset (binary classification)
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
# Split dataset into training (70%), validation (15%), and testing (15%) sets
X_train, X_temp, y_train, y_temp = train_test_split(
X, y, test_size=0.3, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
X_temp, y_temp, test_size=0.5, random_state=42
)
# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train) # Fit on training data and transform
X_val = scaler.transform(X_val) # Transform validation data using same scaler
X_test = scaler.transform(X_test) # Transform test data using same scaler
```

- Standardization makes feature scale uniform.
- Prevents features with larger ranges from dominating those with smaller ranges.
- NN overfits larger ranges.
- Slow/fail NN training with very different feature scales.
- Exploding/vanishing activations in deeper layers.
- Note: Fits to training set; transforms on validation and test

## Hyperparameters
- Model hyperparameters:
	- Number of layers
	- Number of neurons
	- Activation function
- Compile hyperparameters:
	- Optimizer
	- Loss function
	- Metric of training goodness
- Regularization hyperparmeters:
	- Dynamically adjust epochs
	- Metric to observe
- Tuning examples:
	- Number of neurons/layer
	- Different activations
- Training hyperparameters
	- num. epochs
	- batch size
	- validation data

- Measuring whether the model is overfitting
- Training vs. Validation Accuracy
- If the validation accuracy follows the training accuracy, the model is learning correctly.
- If the validation accuracy diverges, the model may be overfitting.
- Training vs. Validation Loss
- If validation loss is decreasing, the model generalizes well.
- If validation loss increases while training loss decreases, the model is overfitting.
- Final training results:
- Accuracy on Test Set: 0.8667
- Loss on Test Set: 0.3260
![](/machine-learning-foundations/attachments/cleanshot-2025-04-05-at-1151582x.png)

- Pytorch and Keras offer multiple optimization methods
- E.g., EarlyStopping implements a callback for the model.fit method.
- The callback fires at every epoch, reporting the value of a user-defined (hyperparameter) metric.
- Here, we use 'loss' and stop when it does not decrease for 5 consecutive epochs.
- We space
- Final training results with 15 epochs instead of 50 :
- Final Accuracy on Test Set: 0.8533 Vs. 0.8667
- Final Loss on Test Set: 0.3459 Vs. 0.3260