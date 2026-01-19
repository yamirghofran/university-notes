---
title: Deep Learning
---

Most model parameters are learned not directly from the features of the training examples, but from the outputs of the preceding layers.
When compared to Shallow Learning
- Models complex patterns and representations in data.
- Excels with **large-scale**, unstructured data like images, audio, text.
- Breakthroughs in computer vision, NLP, and robotics
Type of machine learning that consists of multiple layers designed to automatically learn complex data patterns.
[Neural Network](/machine-learning-foundations/deep-learning/neural-networks)s dominate deep learning, but they are not the only deep machine learning models/algorithms.
Deep learning requires:
- **Multiple processing layers**: hierarchical feature learning.
- **Non-linearity**: model complex relationships.
- **Large parameter space**: up to millions of parameters
- **Optimization**: [Backpropagation](/machine-learning-foundations/deep-learning/backpropagation) gradient-based methods, or other learning rules.
Multiple models/algorithms satisfy these requirements.
- Decision tree-based
	- Uses layered decision trees instead of neurons.
	- [Gradient Boosting Machines](/machine-learning-foundations/algorithms/gradient-boosting-machines) (e.g. XGBoost, LightGBM, CatBoost): handle structured/tabular data better than deep neural networks.
	- [Random Forest](/machine-learning-foundations/algorithms/random-forest)s: works well for small datasets.
- Kernel-based
	- "Mimic" deep neural networks with hierarchical kernel functions.
	- [Support Vector Machines](/machine-learning-foundations/algorithms/support-vector-machines) (SVMs) with deep kernel: small-scale tasks with high-dimensional data but computationally expensive for large datasets.
- Evolutionary & reinforcement learning
	- **Genetic Algorithms** (e.g. NEAT): Uses genetic evolution to evolve neural network architectures for game playing, robot control.
	- **Reinforcement Learning + Neural Networks** (e.g. DQN, PPO, A3C); learning policies without backpropagation for robotics, autonomous driving, gaming (e.g. AlghaGo)
- Deep Probabilistic Models
	- **Deep Gaussian Processes**: stacked layers of Gaussian processes best used for probabilistic modeling with uncertainty estimation.
	- **Bayesian Learning + Neural Networks**: uses Bayesian principles with neural networks. Important for uncertainty estimation in medical ML and self-driving cars.
## Why Neural Networks Dominate Deep Learning?
- **Scalability**: Can train on huge datasets efficiently.
- **Transfer Learning**: Pre-trained models generalize well.
- **State-of-the-art Performance**: Outperforms other models in vision, NLP, etc.
- **Flexibility**: Many different neural network architectures.
# Deep Model Training Strategy
## Starting with shortlisting a [Neural Network](/machine-learning-foundations/deep-learning/neural-networks) architecture.
- Images → [CNN](/machine-learning-foundations/deep-learning/convolutional-neural-networks) with at least one convolutional layer, followed by a max-pooling layer, and one fully connected layer.
- Language → [Transformers](/machine-learning-foundations/deep-learning/transformers) or [LSTM](/machine-learning-foundations/deep-learning/long-short-term-memory), based on the dataset size.
- Structured Data → [Feedforward Neural Networks](/machine-learning-foundations/deep-learning/feedforward-neural-networks) or [Transformers](/machine-learning-foundations/deep-learning/transformers), depending on the dataset size.
## Starting with a pre-trained model instead of training from scratch
- Ready to use or fine-tuned for our specific task.
- Limited Data
- pretrained models already contain rich knowledge learned from large datasets, so they're ideal for scenarios with small labeled datasets.
- Fast Training
- fine-tuning pretrained models is quicker than training a model from scratch.
- Common tasks
- classification, sentiment analysis, image recognition, text generation, translation, etc have many pretrained models available.
- State-of-the-art results
- pretrained models are often well-optimized and provide strong baseline performance.
**Why using pretrained model**
- Pretrained models often improve the quality of the model, compared to training a model from scratch.
- Pretrained on large datasets (e.g., ImageNet, Wikipedia) often unavailable to typical ML engineer.
- Can be used in different ways, depending on:
- The amount of labeled data available (if any)
- The similarity of our dataset with the one of the pretrained model
- Whether we want to develop our own model
- Three main strategies:
- Using the pretrained model directly (no retraining)
- Finetune a pretrained model on our dataset (same task/model type)
- Transfer pretrained weights into your own model (transfer learning), e.g., Using BERT pretrained on text for sentiment analysis.
- Identify a pretrained model suited to our task:
	- Text/NLP: GPT-4, BERT, T5, RoBERTa for sentiment, classification, generation
	- Vision: Vision Transformer, EfficientNet, CLIP for image classification,
	object detection
	- Speech: Whisper, Wav2Vec 2.0 for speech recognition, speech-to-text
	- Multimodal: CLIP, ALIGN, GPT-4V for vision-language tasks, image captioning
	- Time-Series: PatchTST, Informer, TimesNet for forecasting, anomaly detection
- Obtain and explore the model:
	- We use libraries like HuggingFace Transformers (NLP) or Torchvision (images).
- Fine-tune on our data (optional but common):
	- We replace the final layers or fine-tune all layers, depending on the task and data size.
- Evaluate performance and adjust:
	- If accuracy is insufficient, we consider adjusting training parameters or model selection.

## Using Pretrained Model Directly and with Finetuning
### Directly
![](/machine-learning-foundations/attachments/cleanshot-2025-03-26-at-2024092x.png)
- We don't modify layers or weights
- We don't train anything.
- We just use the model for inference (i.e. predictions)
### Finetuning
![](/machine-learning-foundations/attachments/cleanshot-2025-03-26-at-2024172x.png)
- The model starts with pretrained weights.
- We train the model further on our own dataset (i.e. adjusting weights)
- This improves accuracy on our specific data.

![](/machine-learning-foundations/attachments/cleanshot-2025-03-26-at-2027132x.png)
- Pretrained with finetuning
- Adapt the pretrained model to our specific task by training on our own dataset.
- Keep most pretrained weights, adjusting only the final layers to specialize the model.
- Example of finetuning BERT for text classification.

### Using Pretrained Weights or Embeddings
![](/machine-learning-foundations/attachments/cleanshot-2025-03-26-at-2028332x.png)
- We only reuse the learned parameters, i.e. weights and biases.
- Our model may have new layers or different structure.
- We might use just part of the pretrained model (e.g. BERT encoder only)
- We must manage weight loading carefully, e.g. shapes must match or be adapted.