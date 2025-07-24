---
title: Boruta
---

Iteratively train [random forest](/machine-learning-foundations/random-forest)s and run statistical tests to classify important/unimportant features.

Boruta is a heuristic. We run it multiple times, checking that the [feature selection](/machine-learning-foundations/feature-selection) is stable. We check that the number of [random forest](/machine-learning-foundations/random-forest) trees is large enough to generate stable outputs.