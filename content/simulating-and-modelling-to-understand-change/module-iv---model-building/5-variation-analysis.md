---
title: 5. Variation Analysis
---


## Variation
**Variation is the tendency of the values of a variable to change from measurement**
**to measurement.**

You can see variation easily in real life; if you measure any continuous variable
twice, you will get two different results. This is true even if you measure quantities
that are constant, like the speed of light. Each of your measurements will include a
small amount of error that varies from measurement to measurement.

**Categorical variables** can also vary if you measure across different subjects (e.g.
the eye colors of different people), or different times (e.g. the energy levels of an
electron at different moments). **Every variable has its own pattern of variation,**
**which can reveal interesting information**. The best way to understand that pattern
is to visualize the distribution of the variable’s values.

## Visualizing Distributions - Discrete Case
How you visualize the distribution of a variable will depend on whether the variable
is categorical or continuous. A variable is **categorical if it can only take one of a**
**small set of values**. In Python, categorical variables are usually saved as character
vectors. To examine the distribution of a categorical variable, use a bar chart:![](../attachments/screenshot-2024-03-17-at-123151.png)

![](../attachments/screenshot-2024-03-17-at-123208.png)

## Visualizing Distributions - Continuous Case
A **variable is continuous if it can take any of an infinite set of ordered values**.
Numbers and date-times are two examples of continuous variables. To examine
the distribution of a continuous variable, use a histogram:
![](../attachments/screenshot-2024-03-17-at-123305.png)

A histogram divides the x-axis into equally spaced bins and then uses the height of
a bar to display the number of observations that fall in each bin. In the graph
above, the tallest bar shows that almost 20,000 observations have a `carat` value
between 0 and 0.5, which are the left and right edges of the bar.

## Analyzing Plots
Now that you can visualize variation, what should you look for in your plots? And
what type of follow-up questions should you ask? The key to asking good
follow-up questions will be to rely on your curiosity (What do you want to learn
more about?) as well as your skepticism (How could this be misleading?).
In both bar charts and histograms, **tall bars show the common values of a**
**variable, and shorter bars show less-common values**. Places that do not have
bars reveal values that were not seen in your data.

To turn this information into useful questions, look for anything unexpected:
- Which values are the most common? Why
- Which values are rare? Does that match your expectations?
- Can you see any unusual patterns? What might explain them?

![](../attachments/screenshot-2024-03-17-at-123526.png)

As an example, the histogram suggests several interesting questions:
- Why are there more diamonds at whole carats and common fractions of carats?
- Why are there more diamonds slightly to the right of each peack than there are slightly to the left of each peak?
- Why are there no diamonds bigger than 3 carats?

Clusters of similar values suggest that subgroups exist in your data. To
understand the subgroups, ask:
- How are the observations within each cluster similar to each other?
- How are the observations in separate clusters different from each other?
- How can you explain or describe the clusters?

Many of the questions above will prompt you to explore a relationship between
variables, for example, to see if the values of one variable can explain the behavior
of another variable.