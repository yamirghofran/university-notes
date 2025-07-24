---
title: Testing Independence
---

Let's consider tests of the form: 
- $H_0$: $u_1,\ldots,u_N$ are independent.
- $H_a$: $u_1,\ldots,u_N$ are **not** independent.

In order to devise such a test, we need to come up with **a way to quantify how**
**dependent numbers in a sequence are on each other**.
## Correlation and Autocorrelation

**Correlation** tells you how two variables are linearly dependent on each other. 
**Autocorrelation** is when correlation is computed **between a sequence of numbers and itself**.

Suppose you have two sequences of numbers $u_1, \ldots, u_N \quad \text{and} \quad w_1, \ldots, w_N$. To compute the correlation you would look at the pairs $(u_1, w_1), (u_2, w_2), \ldots, (u_N, w_N)$ which considers two consecutive numbers and compute their correlation. Similarly, we could compute the correlation between $(u_1, u_{1+k}), (u_2, u_{2+k}), \ldots, (u_N, u_{N+k})$ between each number in the sequence and the one **k** positions ahead. 

This is what we call **autocorrelation of lag k**.

**If autocorrelations of several lags are close to zero, this gives an indication that the data is**
**independent.** If, on the other hand, the autocorrelation at some lags is big, then there is an
indication of dependence in the sequence of random numbers.

Autocorrelations are computed and plotted in Python using the `autocorrelation_plot`
function from `pandas`.
```python
df = pd.DataFrame(u1, columns=['values'])
pd.plotting.autocorrelation_plot(df['values'])
plt.show()
```
![](../attachments/screenshot-2024-02-27-at-113013.png)
The **blue line** in the previous plot is the **autocorrelation at several lags**, whilst the **dashed**
**grey lines are confidence bands**: if the line is **within the bands it means that we cannot reject**
**the hypothesis** that the autocorrelation of the associated lag is equal to zero, and, therefore,
we would not be able to reject the $H_0$ that the values are independent.

**Since the line is always within the confidence bands**, we have enough statistical evidence to say that all autocorrelations are not different from zero and consequently that **the data is independent** (it was indeed generating using the `np.random.uniform` function).

```python
u2 = np.array(list(np.repeat(np.arange(1, 11), repeats=4))*10)/10
u2 = u2 + np.random.normal(0, 0.02, size=400)
u2 = (u2 - np.min(u2)) / (np.max(u2) - np.min(u2))
df = pd.DataFrame(u2, columns=['values'])
pd.plotting.autocorrelation_plot(df['values'])
```

![](../attachments/screenshot-2024-02-27-at-113309.png)
Here, the sequence is uniform but not independent.

A test of hypothesis for independence can be created by checking if any of the
autocorrelations up to a specific lag are different from zero. This is could be done by using
the function `q_stat` from the `statsmodels.tsa.stattools` module in Python.

First we have to calculate the autocorrelation function using `acf`, so then we can apply the
Box test to the values of the autocorrelation function in different lags (10 in this case)

Let’s compute it for the two sequences u1 and u2 that we have defined before.

```python
acf, confint = stattools.acf(u1, nlags=10, alpha=0.05)
lbvalue, pvalue = stattools.q_stat(acf[1:], len(u1))
```
![](../attachments/screenshot-2024-02-27-at-113517.png)

```python
acf, confint = stattools.acf(u2, nlags=10, alpha=0.05)
lbvalue, pvalue = stattools.q_stat(acf[1:], len(u2))
```
![](../attachments/screenshot-2024-02-27-at-113542.png)

Here we chose a lag of 10 (it is usually not useful to consider larger lags), but you may want
to try a different value. The test confirms our observations of the autocorrelations.

- For the sequence u1 generated the test has a p-value greater than any reasonable value for ɑ for any lag and therefore we cannot reject the $H_0$ (independent).

- For the second sequence u2 which had very large autocorrelations has a p-value smaller than any reasonable value for ɑ for all lags and therefore we have enough statistical evidence reject the $H_0$ (not independent).