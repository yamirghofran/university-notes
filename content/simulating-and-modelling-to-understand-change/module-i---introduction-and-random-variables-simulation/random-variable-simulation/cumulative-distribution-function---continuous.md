---
title: Cumulative Distribution Function - Continuous
---

For a continuous random variable X the cumulative distribution function (cdf) is
equally defined as
$$F(x) = P(X \leq x),$$
where now 
$$P(X \leq x) = P(X < x) = \int_{-\infty}^{x} f(t) \, dt.$$
The cdf is basically the integral of the pdf.

In the donut shop example, the cdf is 
$$F(x) = \int_{-\infty}^{x} f(t) \, dt = \int_{-\infty}^{x} \frac{1}{4} e^{-\frac{t}{4}} \, dt.$$
This integral can be solved and F(x) can be calculated as
$$F(x) = 1 - e^{-\frac{x}{4}}$$
![](../attachments/screenshot-2024-02-27-at-115925.png)