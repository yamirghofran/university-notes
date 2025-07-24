---
title: Types of Simulation Models
---

The simulation model you choose will depend upon the [System](/simulating-and-modelling-to-understand-change/module-i---introduction-and-random-variables-simulation/system) you are trying to understand.

## Deterministic vs Stochastic

A **deterministic model** is a model whose behavior is **entirely predictable**. Given a set of inputs, the model will always result in a unique set of outputs.

A **stochastic or probabilistic model** is a model that has **random variables** as inputs, and consequently its outputs are random.

For example: In a donut shop simulation, with a deterministic model, we would assume that a new customer arrives every 5 minutes and an employee takes 2 minutes to serve a customer. 
In a stochastic/probabilistic model we would assume that the arrival times and the serving time follows some random variables like the normal distribution.

## Static vs Dynamic

Simulation models that represent the system **only at a particular point in time** are called **static**. This type of simulations are often called [[Monte Carlo Simulation in Python | Monte Carlo simulations]].

**Dynamic** simulation models represent systems that **evolve over time**. The simulation of the donut shop during its working hours is an example of a dynamic model.

## Discrete vs Continuous
Dynamic simulations can be further categorized into discrete or continuous.

In **Discrete** simulation models, the variables of interest **change only at a discrete set of points** in time. The number of people queuing in the donut shop is an example of a discrete simulation. The number of customer changes only when a new customer arrives or when a customer has been served.
![](../attachments/screenshot-2024-02-25-at-202137.png)
For specific periods of times, the system doesn't change state. Therefore, time is handled using the **next-event technique.** The model is only examined and updated **when the system is due to change**. These changes are usually called **events**.

In **Continuous** simulation models, the variables of interest change continuously over time. 

e.g. a simulation model for a car journey where the interest is on the **speed of the car throughout the journey**.
![](../attachments/screenshot-2024-02-25-at-202702.png)