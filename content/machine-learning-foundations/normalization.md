---
title: Normalization
---

-  Converting an actual range of values, which a numerical feature can take, into a predefined and artificial range of values, typically in the interval [0, 1] or [−1, 1].
-  Normalization formula [0, 1]:

  $$
  \bar{x}^{(j)} \leftarrow \frac{x^{(j)} - \min^{(j)}}{\max^{(j)} - \min^{(j)}}
  $$

  where $x^{(j)}$ is the value of feature $j$; $\min^{(j)}$ and $\max^{(j)}$ are, respectively, the minimum and the maximum value of the feature $j$ in the training data.
-  Note: max and min are usually outliers. Thus, normalization compresses the feature values into a small range.
-  **Winsorization**: setting all outliers to a specified percentile of the data.
-  Python:

  ```python
  from scipy.stats.mstats import winsorize
  winsorize(list_of_numbers, limits=[0.05, 0.05])
```


