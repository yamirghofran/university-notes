---
title: Discrete Events Simulation Python
---

- [Discrete Events Simulation Modeling Approaches](/simulating-and-modelling-to-understand-change/module-iii---discrete-events-simulation/discrete-events-simulation-modeling-approaches)
- [Discrete Events Simulation Use Cases](/simulating-and-modelling-to-understand-change/module-iii---discrete-events-simulation/discrete-events-simulation-use-cases)
- [SimPy for Discrete Events Simulation](/simulating-and-modelling-to-understand-change/module-iii---discrete-events-simulation/simpy-for-discrete-events-simulation)

The complexity of many real-world systems involves unaffordable analytical models,
and consequently, such systems are commonly studied by means of simulation.
Different types of simulation apply depending on the nature of the system under
consideration. In the last chapter we focused on static simulation, also called Monte
Carlo simulation.

In this chapter we discuss discrete-event simulation (DES) which is a specific technique
for modelling stochastic, dynamic and discretely evolving systems.

Recall that different types of simulation apply depending on the nature of the system under
consideration. A common model taxonomy classifies simulation problems along three main
dimensions:
1. deterministic vs. stochastic
2. static vs. dynamic (depending on whether they require a time component)
3. continuous vs. discrete (depending on how the system changes).

For instance, Monte Carlo methods are well-known examples of static stochastic simulation
techniques. On the other hand, discrete-event simulation (DES) is a specific technique for
modelling stochastic, dynamic and discretely evolving systems.

Customers arriving at a bank, products being manipulated in a supply chain, or
packets traversing a network are common examples of such systems.

The discrete nature of a given system arises as soon as its behavior can be
described in terms of events, which is the most fundamental concept in DES.

**An event is an instantaneous occurrence that may change the state of the**
**system, while, between events, all the state variables remain constant.**

## DES Software
Specialized Software: [ARENA Software.](https://www.rockwellautomation.com/en-us/products/software/arena-simulation.html)
Python Libraries:
- [Simpy](https://simpy.readthedocs.io/en/latest/index.html): Low level python library that works for any discrete events simulation scenario.
- [ManPy](https://ieeexplore.ieee.org/document/7004969): High level python library designed for manufacturing processes (based on simpy).

