---
title: Convolutional Neural Networks
---

- Specialized NN designed for image processing and spatial data.
- **Use**: image classification, object detection, facial recognition, medical imaging.
- **Data flow**: hierarchical feature extraction, moving from low-level features (edges) to high-level features (objects).
- **Structure**: convolutional layers → Pooling layers → Fully connected layers → Output
- **Activation function**: ReLU in hidden layers, Sigmoid for binary classification, Softmax for multi-class classification.
- **Loss function**: MSE for regression, cross-entropy loss for classification.
- **Learning**: uses gradient descent, backpropagation, and filters (called kernels) to extract spatial patterns.
- **Pros**: great for images, less parameters than FNNs, translationally invariant.
- **Cons**: large labeled datasets, computationally expensive, no temporal awareness.
![](/machine-learning-foundations/attachments/cleanshot-2025-03-02-at-2242172x.png)
 - LeNet-5: one of the earliest CNNs that promoted deep learning.
- Uses convolutional and pooling layers to extract features.
- Ends with fully connected layers for classification.
- Inspired modern CNNs like AlexNet, VGG, and ResNet.
