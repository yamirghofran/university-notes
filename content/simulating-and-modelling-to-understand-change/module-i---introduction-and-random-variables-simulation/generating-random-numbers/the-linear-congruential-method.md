---
title: The Linear Congruential Method
---

The linear congruential method produces a sequence of integers between 0 and $m-1$ using this formula:

$$X_i = (aX_{i-1} + c) \mod m $$
$\text{for } i = 1, 2, \ldots$
Where there are 3 parameters to be chosen: a, c, and m:

- m > 0
- 0 < a < m
- $0 \leq c \lt m$
- $0 \leq X_0 \lt m$

Random number (u): $u_i = x_i / m$

Implementing in python:
```python
def LCM(n, seed, a, c, m):
	x = []
	x.append(seed)
	for i in range(1, n+1):
		x.append((a*x[i-1]+c)%m)
	u = np.array(x)/m
	return (list(u))
LCM(n=8, seed=4, a = 13, c = 0, m = 64)
#returns
[0.0625, 0.8125, 0.5625, 0.3125, 0.0625,
0.8125, 0.5625, 0.3125, 0.0625]
```
Standard properties are: a = 1102515245, c = 12345, m = 2^32