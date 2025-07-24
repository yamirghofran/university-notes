---
title: Generating a Dummy Dataset
---

Another possible application of simulation is the generation of dummy datasets.
This dummy datasets allow us to check that our methods and tools work correctly before
going into reality and spending money and resources on gathering information.
The basic concept behind a dummy dataset: a dummy dataset is a collection of random
variables generated through simulation techniques. We can use all the tools we have
acquired in the last sessions to generate all kinds of variables.
The most essential aspect in the generation of a dummy dataset is the previous information.

Let’s build a simple dummy dataset.
- Create a dummy dataset with 100 cases. It will be composed by a variable A
that is distributed in a normal way with mean 0 and standard deviation 1, a
normal variable B with mean 1.5 and standard deviation 2.5 and a uniform
variable C with minimum 5 and maximum 32.

```python
import numpy as np
import pandas as pd
# Generating random numbers
A = np.random.normal(0, 1, 100)
B = np.random.normal(1.5, 2.5, 100)
C = np.random.uniform(5, 32, 100)
# Creating a DataFrame
data = pd.DataFrame({'A': A, 'B': B,
'C': C})
# Displaying the first few rows
print(data.head())
```
![](../attachments/screenshot-2024-02-27-at-124753.png)
We can also generate dummy datasets with categorical variables using the
function, `choice()`
- We will create a new column in our dummy data frame that indicates the
gender for each row, but in this case we want there to be 20% men and 80%
women.

```python
# Generating the Gender data
Gender = np.random.choice(['Male', 'Female'], 100, replace=True, p=[0.20, 0.80])
# Adding Gender to the DataFrame
data['Gender'] = Gender
# Displaying the first few rows
print(data.head())
```
![](../attachments/screenshot-2024-02-27-at-124833.png)