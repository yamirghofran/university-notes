---
title: Markov Chains
weight: 2
---
A Markov chain is an instance of a so-called [stochastic process](/prob-cs/stochastic-process), loosely speaking a random variable that evolves in time. [Markov Property](/prob-cs/markov-property)

Basis of Google PageRank algorithm, autocompletion.
## A First Example
![](../attachments/markov-0.png)

- Sunny and Rainy are called the **states** of the chain.
- The arrows are called **edges** and have a **transition probability** associated to them.
- The sum of the probabilities of edges leaving out from a state must add up to one.
- Often represented in a [Transition Matrix](/prob-cs/transition-matrix).
## Recurrent vs Transient
A state of a Markov chain is said to be **recurrent** if, starting from that state, there is a probability one of eventually returning to it.

A state is said to be **transient** if it is not recurrent.

![](../attachments/markov-1.png)
![](../attachments/markov-2.png)


## Reducible vs Irreducible
A Markov chain is said to be **irreducible** if it is possible to go from any state to any other state.

A Markov chain which is not irreducible is said to be **reducible**.

- If a Markov chain is irreducible then all its states are recurrent.
- The converse is not true!! A Markov chain whose all states are recurrent is not necessarily irreducible.


## Period of a State
The period of a state is the greatest common divisor of the length of the trips that would take to return to a state, given that you started at that state.
![](../attachments/markov-3.png)
## Periodic vs Aperiodic
A Markov chain is **aperiodic** if all its states have period one. A Markov chain which is not aperiodic is said to be **periodic** (it has at least one state with period bigger than one).
