---
title: Bag of Words
---

A generalization of applying [One-Hot Encoding](/machine-learning-foundations/one-hot-encoding) to text data. You use it to represent an entire text document as a binary vector.

![](../attachments/cleanshot-2025-01-21-at-1051372x.png)

First, we have to [tokenize](/machine-learning-foundations/tokenization) the texts.
![](../attachments/cleanshot-2025-01-21-at-1054232x.png)

Next step is to build a vocabulary. It contains 16 tokens:
![](../attachments/cleanshot-2025-01-21-at-1054512x.png)

Then, we order the vocabulary in some way and assign a unique index to each one.
![](../attachments/cleanshot-2025-01-21-at-1055272x.png)

We transform our collection into a collection of binary feature vectors:
![](../attachments/cleanshot-2025-01-21-at-1056012x.png)

1 represents the presence of the token for each feature.

Now we can use the corresponding labeled feature vectors as the training data, which any classification learning algorithm can work with.

There are several bag of words flavors. Instead of the binary value for presence, you can use: 
- counts of tokens
- frequencies of tokens: num. tokens / length of document
- TF-IDF
	- increases proportionally to the frequency  of a word in the document and is offset by the number of documents in the corpus that contain that word. Adjusts for common words.

An extension of bag-of-words is **bag-of-n-grams**. Results in a more sparse feature vector but allows the model to learn more nuisance.