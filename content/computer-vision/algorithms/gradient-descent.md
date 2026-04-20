---
title: Gradient Descent
---

## Overview

Gradient descent is an optimization algorithm that minimizes a function by iteratively moving in the direction of steepest descent (negative gradient).

## Basic Principle

To minimize a loss function $J(\theta)$, update parameters:

$$\theta_{t+1} = \theta_t - \alpha \nabla J(\theta_t)$$

Where:

- $\theta$ = model parameters (weights)
- $\alpha$ = learning rate (step size)
- $\nabla J(\theta)$ = gradient of loss with respect to parameters

---

## Standard Gradient Descent (Batch)

### Pseudocode

```
Algorithm BatchGradientDescent(model, X, y, loss_fn, alpha, epochs)
Input:
    - model: model with parameters θ
    - X: training data (N samples × D features)
    - y: ground truth labels (N samples)
    - loss_fn: loss function J(θ; X, y)
    - alpha: learning rate
    - epochs: number of iterations

Output:
    - trained model with optimized parameters

1. FOR epoch = 1 TO epochs DO:
2.
3.     // Forward pass: compute predictions
4.     y_pred ← model.FORWARD(X)
5.
6.     // Compute loss
7.     loss ← loss_fn(y_pred, y)
8.
9.     // Backward pass: compute gradients
10.    gradients ← COMPUTE_GRADIENT(loss, model.parameters)
11.
12.    // Update parameters
13.    FOR each parameter θ IN model.parameters DO:
14.        θ ← θ - alpha × gradients[θ]
15.    END FOR
16.
17.    // Optional: monitor progress
18.    IF epoch % 10 == 0 THEN:
19.        PRINT("Epoch:", epoch, "Loss:", loss)
20.    END IF
21.
22. END FOR

23. RETURN model
```

---

## Stochastic Gradient Descent (SGD)

Uses one sample at a time (or small batches):

```
Algorithm StochasticGradientDescent(model, X, y, loss_fn, alpha, epochs)
Input:
    - model: model with parameters θ
    - X, y: training data
    - loss_fn: loss function
    - alpha: learning rate
    - epochs: number of passes through data

Output:
    - trained model

1. N ← LENGTH(X)

2. FOR epoch = 1 TO epochs DO:
3.
4.     // Shuffle data
5.     indices ← RANDOM_PERMUTATION(N)
6.
7.     FOR i = 1 TO N DO:           // One sample at a time
8.
9.         idx ← indices[i]
10.        x_i ← X[idx]
11.        y_i ← y[idx]
12.
13.        // Forward pass (single sample)
14.        y_pred ← model.FORWARD(x_i)
15.
16.        // Compute loss for this sample
17.        loss ← loss_fn(y_pred, y_i)
18.
19.        // Backward pass
20.        gradients ← COMPUTE_GRADIENT(loss, model.parameters)
21.
22.        // Update parameters
23.        FOR each parameter θ IN model.parameters DO:
24.            θ ← θ - alpha × gradients[θ]
25.        END FOR
26.
27.    END FOR
28.
29. END FOR

30. RETURN model
```

---

## Mini-Batch Gradient Descent

Most commonly used - balances speed and stability:

```
Algorithm MiniBatchGradientDescent(model, X, y, loss_fn, alpha,
                                    epochs, batch_size)
Input:
    - model: model with parameters θ
    - X, y: training data (N samples)
    - loss_fn: loss function
    - alpha: learning rate
    - epochs: number of passes through data
    - batch_size: number of samples per batch

Output:
    - trained model

1. N ← LENGTH(X)
2. num_batches ← CEIL(N / batch_size)

3. FOR epoch = 1 TO epochs DO:
4.
5.     // Shuffle data
6.     indices ← RANDOM_PERMUTATION(N)
7.
8.     FOR batch = 0 TO num_batches-1 DO:
9.
10.        // Get batch indices
11.        start ← batch × batch_size
12.        end ← MIN(start + batch_size, N)
13.        batch_indices ← indices[start:end]
14.
15.        X_batch ← X[batch_indices]
16.        y_batch ← y[batch_indices]
17.
18.        // Forward pass (batch)
19.        y_pred ← model.FORWARD(X_batch)
20.
21.        // Compute average loss for batch
22.        loss ← MEAN(loss_fn(y_pred, y_batch))
23.
24.        // Zero gradients (important!)
25.        ZERO_GRADIENTS(model.parameters)
26.
27.        // Backward pass
28.        gradients ← COMPUTE_GRADIENT(loss, model.parameters)
29.
30.        // Update parameters
31.        FOR each parameter θ IN model.parameters DO:
32.            θ ← θ - alpha × gradients[θ]
33.        END FOR
34.
35.    END FOR
36.
37. END FOR

38. RETURN model
```

---

## Gradient Descent with Momentum

Adds "inertia" to help escape local minima and accelerate convergence:

```
Algorithm SGDWithMomentum(model, X, y, loss_fn, alpha, epochs,
                          batch_size, beta)
Input:
    - beta: momentum coefficient (typically 0.9)

Output:
    - trained model

1. N ← LENGTH(X)
2.
3. // Initialize velocity for each parameter
4. velocity ← {}
5. FOR each parameter θ IN model.parameters DO:
6.     velocity[θ] ← ZEROS(SHAPE(θ))
7. END FOR

8. FOR epoch = 1 TO epochs DO:
9.
10.    // Shuffle and create batches
11.    indices ← RANDOM_PERMUTATION(N)
12.
13.    FOR each batch IN CREATE_BATCHES(indices, batch_size) DO:
14.
15.        X_batch ← X[batch]
16.        y_batch ← y[batch]
17.
18.        // Forward and backward pass
19.        y_pred ← model.FORWARD(X_batch)
20.        loss ← MEAN(loss_fn(y_pred, y_batch))
21.        gradients ← COMPUTE_GRADIENT(loss, model.parameters)
22.
23.        // Update with momentum
24.        FOR each parameter θ IN model.parameters DO:
25.            // Update velocity
26.            velocity[θ] ← beta × velocity[θ] + gradients[θ]
27.
28.            // Update parameter
29.            θ ← θ - alpha × velocity[θ]
30.        END FOR
31.
32.    END FOR
33.
34. END FOR

35. RETURN model
```

---

## Adam Optimizer (Adaptive Moment Estimation)

Combines momentum with adaptive learning rates:

```
Algorithm AdamOptimizer(model, X, y, loss_fn, alpha, epochs,
                       batch_size, beta1, beta2, epsilon)
Input:
    - alpha: learning rate (typically 0.001)
    - beta1: first moment decay (typically 0.9)
    - beta2: second moment decay (typically 0.999)
    - epsilon: small constant for numerical stability (typically 1e-8)

Output:
    - trained model

1. N ← LENGTH(X)
2. t ← 0    // Time step

3. // Initialize first and second moment estimates
4. m ← {}   // First moment (mean of gradients)
5. v ← {}   // Second moment (uncentered variance)
6. FOR each parameter θ IN model.parameters DO:
7.     m[θ] ← ZEROS(SHAPE(θ))
8.     v[θ] ← ZEROS(SHAPE(θ))
9. END FOR

10. FOR epoch = 1 TO epochs DO:
11.
12.    indices ← RANDOM_PERMUTATION(N)
13.
14.    FOR each batch IN CREATE_BATCHES(indices, batch_size) DO:
15.
16.        t ← t + 1
17.
18.        X_batch ← X[batch]
19.        y_batch ← y[batch]
20.
21.        // Forward and backward pass
22.        y_pred ← model.FORWARD(X_batch)
23.        loss ← MEAN(loss_fn(y_pred, y_batch))
24.        gradients ← COMPUTE_GRADIENT(loss, model.parameters)
25.
26.        // Update each parameter
27.        FOR each parameter θ IN model.parameters DO:
28.            g ← gradients[θ]
29.
30.            // Update biased first moment estimate
31.            m[θ] ← beta1 × m[θ] + (1 - beta1) × g
32.
33.            // Update biased second raw moment estimate
34.            v[θ] ← beta2 × v[θ] + (1 - beta2) × g²
35.
36.            // Compute bias-corrected estimates
37.            m_hat ← m[θ] / (1 - beta1^t)
38.            v_hat ← v[θ] / (1 - beta2^t)
39.
40.            // Update parameter
41.            θ ← θ - alpha × m_hat / (SQRT(v_hat) + epsilon)
42.        END FOR
43.
44.    END FOR
45.
46. END FOR

47. RETURN model
```

---

## Learning Rate Scheduling

```
Algorithm StepDecay(initial_lr, epoch, drop_factor, epochs_drop)
    lr ← initial_lr × drop_factor^FLOOR(epoch / epochs_drop)
    RETURN lr

Algorithm ExponentialDecay(initial_lr, epoch, decay_rate)
    lr ← initial_lr × EXP(-decay_rate × epoch)
    RETURN lr

Algorithm CosineAnnealing(initial_lr, epoch, max_epochs)
    lr ← initial_lr × (1 + COS(π × epoch / max_epochs)) / 2
    RETURN lr
```

---

## Comparison of Optimizers

| Optimizer      | Update Rule                                             | Pros                     | Cons                       |
| -------------- | ------------------------------------------------------- | ------------------------ | -------------------------- |
| SGD            | $\theta -= \alpha \nabla J$                             | Simple, generalizes well | Slow, gets stuck           |
| SGD + Momentum | $v = \beta v + \nabla J$<br>$\theta -= \alpha v$        | Faster convergence       | Extra hyperparameter       |
| RMSprop        | $\theta -= \alpha \frac{\nabla J}{\sqrt{v} + \epsilon}$ | Good for non-stationary  | Can diverge                |
| Adam           | Adaptive + momentum                                     | Fast, works well         | May not generalize as well |

---

## Python Implementation (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define model, loss, and optimizer
model = MyModel()
criterion = nn.CrossEntropyLoss()

# Choose optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# or
optimizer = optim.Adam(model.parameters(), lr=0.001, betas=(0.9, 0.999))

# Training loop
for epoch in range(num_epochs):
    for batch_x, batch_y in dataloader:
        # Forward pass
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)

        # Backward pass
        optimizer.zero_grad()    # Clear gradients
        loss.backward()          # Compute gradients
        optimizer.step()         # Update parameters
```
