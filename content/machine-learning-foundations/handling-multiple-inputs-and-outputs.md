---
title: Handling Multiple Inputs and Outputs
---

Machine learning engineers often work with multimodal data. E.g., input: image and a text; output: whether the text describes the given image.

[Shallow Learning](/machine-learning-foundations/shallow-learning) algorithms are:
- Difficult to work with multimodal data.
- Vectorize each input with the corresponding feature engineering method.
- Concatenate two feature vectors to form one wider feature vector.
- E.g., image features $=\left[i^{(1)}, i^{(2)}, i^{(3)}\right]$; text features $=\left[t^{(1)}, t^{(2)}, t^{(3)}, t^{(4)}\right]$; concatenated feature vector $=\left[i^{(1)}, i^{(2)}, i^{(3)}, t^{(1)}, t^{(2)}, t^{(3)}, t^{(4)}\right]$.

For [Neural Network](/machine-learning-foundations/neural-networks)s:
- We can build two subnetworks, one for each input type.
- [CNN](/machine-learning-foundations/convolutional-neural-networks) subnetwork reads the image, while an [RNN](/machine-learning-foundations/recurrent-neural-networks) subnetwork reads the text.
- The last subnetwork layer is an image (CNN) and a text (RNN) embedding.
- Concatenate the two embeddings and add a classification layer (softmax or logistic sigmoid) on top of the concatenated embeddings.
- Neural network libraries provide simple-to-use tools that allow concatenating or averaging layers from several subnetworks.

- We want to predict multiple outputs for one input.
- Use a multi-label/multi-class classification problem:
- Multi-label: labels are monomodal and independent, e.g., [cat, dog, rabbit] or the tags in social media posts [AI, Deep Learning, ML].
- Multi-class: labels are monomodal and interdependent, e.g., [red, green, circle, line]. We enumerate and label all the combinations of the labels, e.g., [green circle, red line, etc.].
- Warning: multi-class works grow exponentially with \# of labels.
- Use a subnetwork that works as an encoder:
- Outputs are multimodal and their combinations cannot be effectively enumerated
- E.g., detecting an object on an image, returning its coordinates + description tag.
- We read the input image using N convolution layers.
- The encoder's last layer is the image embedding.
- We add two subnetworks on top of the embedding layer, each taking the embedding vector as input and predicting the coordinates of the object, and the tag
![](../attachments/image0-1.jpg)
![](../attachments/image1-1.jpg)
Multimodal Neural Network architecture.

First subnetwork (coordinates):
- Takes the embedding vector as input.
- Has a ReLU last layer to predict coordinates as positive real numbers.
- Use the mean squared error cost C1.
- Alternatively the coordinates can be in the range [0,1], last layer has four logistic sigmoid outputs + average four binary cross-entropy cost functions for
Second subnetwork (tags):
- Takes the same embedding vector as input.
- Predicts the probabilities for each tag.
- Has a Softmax last layer for multiclass classification.
- Uses the averaged negative log-likelihood cost C2 (also called cross-entropy cost).,
- Might solve a multi-label classification problem (in which case it would also have several sigmoid outputs and average several binary cross entropy costs, one per tag).


- We want accurate predictions of both the coordinates and the tags.
- It is impossible to optimize two cost functions at once. By trying to improve one, we risk hurting the other one, and vice-versa.
- Add another hyperparameter $\gamma$, in the range $(0,1)$, and define the combined cost function as $\gamma \times \mathrm{C} 1+(1-\gamma) \times \mathrm{C} 2$.
- Tune the value for $\gamma$ on the validation data, just like any other hyperparameter.