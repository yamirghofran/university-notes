---
title: Limitations of Game Search Algorithms
---

- Minimax (in the general case) needs to explore the whole tree: not of practical application
- Alpha-beta search: uses a heuristic function as an approximation of the expected utility
- Monte Carlo computers and approximate utility based on random playouts
	- Useful for games with good evaluation function or very high branching factor.

Alpha-beta search is limited by the heursitic function
- even randomly distributed in the evaluation function means that we might choose the wrong branch with high probability
- And if the errors are not independent, that might be worse (as we will systematically choose wrong branches)

Alpha-beta and Monte Carlo are designed to consider all legal moves:
- but sometimes there are moves that are obviously best (but hard to capture in the heuristic)
- Sometimes are moves that are symmetrical, and we will need to incorporate this (it is not by default)

Alpha-beta and Monte Carlo are designed to consider individual moves:
- Humans usually think in more abstract terms, trying to achieve goals
- Planning can be used, if we have a hierarchy of abstract to concrete representations (advanced topic, that we will not cover)

Lastly, all of this algorithms can be improved with machine learning:
- alphazero does, approximately, learn to calculate a better evaluation function for alpha-beta search based on self-play