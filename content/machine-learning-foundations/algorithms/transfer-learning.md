---
title: Transfer Learning
---

- Using a pre-trained model to build a new model.
- Pretrained models are created using large amount of costly curated data.
- The parameters learned by the pretrained models can be useful for our tasks.
- A pre-trained model can be used in two ways:
- its learned parameters can be used to initialize your own model, or
- it can be used as a feature extractor for your model.
- Using a pretrained model as initializer:
- Current problem is similar to the one solved by the pretrained model
- The optimal parameters for our problem will be similar to the pretrained parameters
- Especially in the initial neural network layers (i.e., those closest to the input)
- Learning: faster because gradient descent searches for the optimal parameter values in a smaller region of potentially good values.
- If the model is pretrained on a dataset larger that ours, searching in a region of potentially good values might also lead to a better generalization.
- Increases chances to infer patterns that are not in our limited training set.

- Retraining pretrained models is potentially very expensive and resource intensive.
- Pretrained model are very deep: hundreds/thousands layers, millions/billions parameters
- present challenges of grading vanishing/explosion.
- Using Pretrained model as feature extractor:
- using some layers of the pre-trained model as feature extractors for your model
- Keep N initial layers of the pretrained model, closest to and including the input layer
- Keep their parameters "frozen," that is, unchanged and unchangeable (i.e., no retraining).
- Add new layers on top of the frozen layers, including the appropriate output layer
- Use a problem-specific dataset for the training of the added layers.
- Only the parameters of the new layers are updated by gradient descent during training
- Alternatively, several right-most old layers could be set as trainable.
- How many layers of the pretrained model to use or freeze in the new model?
- This is up to the analyst: it's part of the decisions we will make about the architecture that will work best for our problem.

![](/machine-learning-foundations/attachments/cleanshot-2025-04-20-at-2346352x.png)

