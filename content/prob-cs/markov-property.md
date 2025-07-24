---
title: Markov Property
weight: 3
---
The future depends only on the present and not on the past.

Let $X_0, X_1, \ldots, X_t$ be a [Markov Chain](/prob-cs/markov-chains) and write $P(X_t = x_t | X_{t-1} = x_{t-1})$ as $P(x_t | x_{t-1})$ for instance. Then
$$
P(x_t | x_{t-1}, x_{t-2}, \ldots, x_0) = P(x_t | x_{t-1})
$$
The next step of the Markov chain only depends on the current state and not on how we got to that state.
