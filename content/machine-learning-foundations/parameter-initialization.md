---
title: Parameter Initialization
---

- Parameters = weights + biases
- Before training, the parameter values in all units (i.e., neurons) are unknown.
- Training algorithms for neural networks (e.g., gradient descent) are iterative
- Initialize the weights and biases before starting the first iteration,
- Weights initialization methods, sampling from:
- **Random normal**: normal distribution, typically mean 0 and SD 0.05 ;
- **Random uniform**: uniform distribution with range $[-0.05,0.05]$;
- **Xavier** normal: truncated normal distribution, centered on 0 , with $\mathrm{SD}=\sqrt{2 /(\text { in }+ \text { out })}$ rere "in" is the number of units in the preceding layer to which the current unit is connected (the one whose parameters you initialize); and "out" is the number of units on the subsequent layer to which the current unit is connected;
- **Xavier uniform**: uniform distribution within [-limit, limit], where "limit" is $\sqrt{6 /(\text { in }+ \text { out })}$, and "in" and "out" are defined as in Xavier normal, above.
- The bias term is usually initialized with 0 or 1 . Note: we cannot use 001 for weights

## He (Kaiming)
- There are other initialization strategies, notably **He** (also called **Kaiming**):
- Variants: **He normal** and **He uniform**, as with Xavier.
- Specifically designed to address training instabilities in deep neural networks, especially when using the **ReLU** activation function.
- Sets the initial weights using a variance scaling method designed to maintain the variance of activations across layers.
- Improves convergence, avoids vanishing/exploding gradients, and eliminates manual tuning of weight scales.
- Remember: activations and gradients can vanish or explode in deep networks.
- ReLU activation passes only positive values, dropping $1 / 2$ signal (negative side).
- He scales weights larger than Xavier; compensates for ReLU dropping 1/2 activations.
- He maintains stable forward signal variance and backpropagated gradient variance.