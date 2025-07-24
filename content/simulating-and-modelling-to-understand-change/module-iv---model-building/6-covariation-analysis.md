---
title: 6. Covariation Analysis
---

## Covariation
If variation describes the behavior **within** a variable, **covariation** describes the
behavior **between** variables. Covariation is the tendency for the values of two or
more variables to vary together in a related way. The best way to spot covariation
is to visualise the relationship between two or more variables. How you do that
should again depend on the type of variables involved.

## A Categorical and a Continuous Variable
It’s common to **explore the distribution of a continuous variable broken down by a**
**categorical variable**.
For example, let’s explore how the price of a diamond varies with its quality:
![](../attachments/screenshot-2024-03-17-at-123848.png)

Another alternative to display the distribution of a continuous variable broken down by a
categorical variable is the boxplot. A boxplot is a type of visual shorthand for a distribution of
values that is popular among statisticians. Each boxplot consists of:
- Visual points that display observations that fall more than 1.5 times the IQR from either edge of the box. These outlying points are unusual so are plotted individually.
- A line (or whisker) that extends from each end of the box and goes to the farthest non-outlier point in the distribution.
- A box that stretches from the 25th percentile of the distribution to the 75th percentile, a distance known as the interquartile range (IQR). In the middle of the box is a line that displays the median, ie 50th percentile, of the distribution. These three lines give you a sense of the spread of the distribution and whether or not the distribution is symmetric about the median or skewed to one side.

![](../attachments/screenshot-2024-03-17-at-124118.png)

We see much less information about the distribution, but the boxplots are much
more compact so we can more easily compare them (and fit more on one plot).
It supports the counterintuitive finding that better quality diamonds are cheaper on
average.

## Two Categorical Variables
To visualise the covariation between categorical variables, you’ll need to count the
number of observations for each combination. We can do this using a cross table
as follows:
![](../attachments/screenshot-2024-03-17-at-124151.png)
![](../attachments/screenshot-2024-03-17-at-124201.png)

To visualize the covariation between two continuous variables, draw a scatter plot.
You can use the `plot()` function.
Scatterplots become less useful as the size of your dataset grows, because points
begin to overplot, and pile up into areas of uniform black (as below), but you can
find alternatives and ways to solve this changing the parameters of the plot as you
have learned in data viz.

![](../attachments/screenshot-2024-03-17-at-124231.png)