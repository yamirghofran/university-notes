---
title: Boruta
---

Iteratively train [Random Forest](/machine-learning-foundations/algorithms/random-forest)s and run statistical tests to classify important/unimportant features.

Boruta is a heuristic. We run it multiple times, checking that the [Feature Selection](/machine-learning-foundations/feature-engineering/feature-selection) is stable. We check that the number of [Random Forest](/machine-learning-foundations/algorithms/random-forest) trees is large enough to generate stable outputs.