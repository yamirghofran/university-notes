---
title: Estimating Complexity
---

- No standard complexity estimation model.
## Major unknowns:
- Can the required quality be attained in practice?
- How much data will we need to reach the required quality?
- What/how many features for the model to learn and generalize sufficiently?
- How large should the model be?
- How long/much computation will it take to train one model?
- How many model trainings to reach the desired level of performance (e.g. model accuracy)?

## Rules of Thumb
Required accuracy of 99% will always have insufficient quantity of labeled data.
In some problems, even 95% accuracy is considered very hard to reach.
If the baseline is human performance, it will typically be a hard problem.

## Divide and Conquer / Simplifying the Problem
Make an educated guess:
- Simplify the problem
- Solve a simpler problem first.
The quantity of data needed to learn to distinguish between more classes usually grows superlinearly with the number of classes.