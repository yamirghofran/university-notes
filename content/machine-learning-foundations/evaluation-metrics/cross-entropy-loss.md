---
title: Cross-Entropy Loss
---

## Cross-Entropy
A measure of the difference between two probability distributions, commonly used in classification tasks.
$$
\text{Cross-Entropy Loss} = -\frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{m} y_{ij} \log(\hat{y}_{ij})
$$
- ${y_{ij}}$: true label for class ${j}$ in sample ${i}$
- ${\hat{y}_{ij}}$: predicted aprobability for class ${j}$ in sample ${i}$
- ${n}$: number of samples
- ${m}$: number of classes
### Purpose
Measures the performance of a classification model; lower values indicate better performance.
### Properties
- Non-negative: Cross-Entropy Loss is always zero or positive.
- Suitable for multi-class classification problems.
## Categorical Cross Entropy
The categorical cross-entropy loss for classification of example i as defined as
$$
\text{CCE}_i^{\text{def}} = -\sum_{j=1}^{C} \left[ y_{i,j} \times \log_2(\hat{y}_{i,j}) \right]
$$
- $C$: Number of classes.
- $y_{i,j} \in \{0, 1\}$: One-hot encoded true label for example $i$, class $j$.
- $\hat{y}_{i,j} \in [0, 1]$: Predicted probability for example $i$, class $j$, typically from Softmax.
**Why we use CCE for multi-class and not multi-label classification:**
- In multi-class classification each input belongs to one and only one class.
- One-hot encoding ensures $\sum_{j=1}^{C} y_{i,j} = 1$ for every $i$.
- The Softmax activation function ensures that $\sum_{j=1}^{C} \hat{y}_{i,j} = 1$, i.e., the model outputs a probability distribution across classes.
- CCE compares the predicted distribution $\hat{y}_i$ to the true distribution $y_i$, penalizing incorrect probabilities.
## Binary Cross Entropy
- **In multi-label classification:**
	- Each input can belong to zero, one, or multiple classes simultaneously.
	- Label vector $y_i \in \{0, 1\}^C$ can have multiple 1s, e.g., $y_i = [1, 0, 1, 0]$, i.e., class 1 and 3 are both relevant (this can be referred to as multi-hot instead of one-hot encoding).
	- Thus, Softmax no longer works as it forces mutual exclusivity, i.e., $\sum_{j=1}^{C} \hat{y}_{i,j} = 1$ is invalid for multi-label.
	- We need independent predictions per class.
- **For multi-label, we use the sigmoid activation function instead of Softmax:**
	- Each $\hat{y}_{i,j} \in [0, 1]$ is independent and represents the probability that class $j$ is present.
	- No requirement that $\sum_{j=1}^{C} \hat{y}_{i,j} = 1$
- **Now we need a loss function for each class, i.e., the BCE:**
  $$
  \text{BCE}_i = -\sum_{j=1}^{C} \left[ y_{i,j} \cdot \log(\hat{y}_{i,j}) + (1 - y_{i,j}) \cdot \log(1 - \hat{y}_{i,j}) \right]
  $$
- The loss is computed independently per class and summed across classes.
- Each class is treated as a binary classification task.
## Illustrative End-to-End Example
### Multiclass Classification
- We classify animal images as either cats (class 0), dogs (class 1) or rabbits (class 2)
- Each image shows one and only one animal.
- Input: Image 1 shows a dog
- Encoding (one-hot): $y=[0,1,0]$
- FFW prediction (Softmax output): $\hat{y}=[0.2,0.7,0.1]$
- CCE calculation, only the term for class 1 is non-zero:
$$\mathrm{CCE}_{i} \stackrel{\text { def }}{=}-\sum_{j=1}^{C}\left[y_{i, j} \times \log _{2}\left(\hat{y}_{i, j}\right)\right]$$
$$\mathrm{CCE}=-\left[0 \cdot \log _{2}(0.2)+1 \cdot \log _{2}(0.7)+0 \cdot \log _{2}(0.1)\right]=-\log _{2}(0.7) \approx 0.514$$
- CCE is appropriate because only one class is correct, and the model's Softmax ensures predictions sum to 1
- CCE is the penalty assigned to the model's confidence in the correct class $\left(\log _{2}\right)$.
- 0.0: perfect prediction ( $\hat{y}=1$ ); 0.152: high confidence ( $\hat{y}=0.9$ ); 0.514: moderate ( $\hat{y}=0.7$ );

- 1.0: low ( $\hat{y}=0.5$ ); 1.585: very low ( $\hat{y}=0.3 / 3$ classes random); 3.322: Wrong ( $\hat{y}=0.1$ ).

### Multi-label Classification
- We classify animal images as either cats (class 0), dogs (class 1) or rabbits (class 2)
- Each image may show any combination of animals.
- Input: Image 2 shows a cat and a rabbit
- Encoding (multi-hot): $y=[1,0,1]$
- FFW prediction (Sigmoid output): $\hat{y}=[0.8,0.4,0.6]$
- BCE calculation, independently for each class and then the total sum of classes:

- Class 0:

$$
y_{0}=1, \hat{y}_{0}=0.8
$$
$$
\begin{gathered}
\mathrm{BCE}_{0}=-\left[1 \cdot \log _{2}(0.8)+(1-1) \cdot \log _{2}(1-0.8)\right] \\
\mathrm{BCE}_{0}=-\left[\log _{2}(0.8)+0 \cdot \log _{2}(0.2)\right]=-(-0.322)=0.322
\end{gathered}
$$

- Class 1:
$$
\begin{gathered}
y_{1}=0, \hat{y}_{1}=0.4 \\
\mathrm{BCE}_{1}=-\left[0 \cdot \log _{2}(0.4)+1 \cdot \log _{2}(1-0.4)\right] \\
\mathrm{BCE}_{1}=-\left[0+\log _{2}(0.6)\right]=-(-0.737)=0.737
\end{gathered}
$$

- Class 2:

$$
y_{2}=1, \hat{y}_{2}=0.6
$$

$$
\begin{gathered}
\mathrm{BCE}_{2}=-\left[1 \cdot \log _{2}(0.6)+0 \cdot \log _{2}(1-0.6)\right] \\
\mathrm{BCE}_{2}=-(-0.737+0)=0.737
\end{gathered}
$$

- Total BCE loss: $\mathrm{BCE}=\mathrm{BCE}_{0}+\mathrm{BCE}_{1}+\mathrm{BCE}_{2}=0.322+0.737+0.737=1.796$
- BCE is correct here because multiple classes can be 1, and each sigmoid prediction is treated independently.
- BCE is a diagnostic signal: how far our model is from predicting true labels correctly?
- 1.796 tells us that the model is moderately off. This is consistent with $\hat{y}=[0.8,0.4,0.6]$ where 0.8 is very good, 0.4 is moderately bad (should be lower) and 0.6 is also moderately bad (should be higher).
- $0.0-0.5=$ very good match between prediction and true labels; $0.5-1.0$ : good; $1.0-$ 2.0: moderately wrong; $>2.0$ : wrong.