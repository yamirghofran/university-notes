---
title: Deep Learning Optimization Algorithms
---

- Gradient and stochastic gradient descent are the most frequently used optimization algorithms.

## Gradient Descent
- Iterative optimization algorithm used to find a local minimum of any differentiable function.
- We start at some random point in the domain of the function, then we move proportionally to the negative of the gradient of the function at the current point.
- **Epochs**: using the training set entirely to update each weight/bias.
- **Backpropagation** algorithm: computes the partial derivatives of each weight/bias using the chain rule.
- **Learning rate**: controls how much the weights/biases are updated at each epoch.
- **Convergence**: the values of weights/biases don't change much after each epoch.
- Gradient descent is sensitive to the value of the learning rate hyperparameter:
- Too high: might not reach convergence at all.
- Too small: can slow down the learning to the point of no progress.
### Gradient Descent Improvements
Gradient descent is slow for large datasets because it uses the entire dataset to compute the gradient of each parameter at each epoch.
- Minibatch stochastic gradient descent (minibatch SGD):
	- Approximates the gradient using small subsets of the training data called minibatches.
	- The size of the minibatch is a hyperparameter that requires tuning.
	- Powers of two, between 32 and a few hundred, are recommended: 32, 64, 128, 256.
	- Note: learning rate still needs to be carefully chosen. Learning can still stagnate at later epochs, oscillating around the minimum due to too (relatively) large updates.
- Learning rate decay:
	- Allow progressively reducing the learning rate as the epochs progress.
	- Faster gradient descent convergence (faster learning) and higher model quality.
	- Several techniques known as 'schedules'.
- Time-based learning rate decay schedules:
	- Alter the learning rate depending on the learning rate of the previous epoch.
	
	$$
	\alpha_{n} \leftarrow \frac{\alpha_{n-1}}{1+d \times n}
	$$
	
	- Where: $a_{n}$ : new value of the learning rate; $a_{n-1}$ : value of the learning at the previous epoch $n-1 ; d$ : decay rate, a hyperparameter.
- Step-based learning rate decay schedules:
	- Change the learning rate according to some pre-defined drop steps.
	$$
	\alpha_{n} \leftarrow \alpha_{0} e^{-d \times n}
	$$
	
	- Where: $d$ is the decay rate and $e$ is Euler's number.
- Momentum, Root Mean, Squared Propagation (RMSProp), and Adam:
	- Update the learning rate automatically based on the performance of the learning process.
	- Eliminate the need of learning rate, decay schedule, rate and related hyperparameters.
	- Adam is the most recent and versatile. Start training with Adam and if the model quality is poor, try a different cost function optimization algorithm.