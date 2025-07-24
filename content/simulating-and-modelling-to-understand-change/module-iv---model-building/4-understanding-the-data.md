---
title: 4. Understanding the Data
---

Before creating a model, evaluating it and using it to try to make predictions, we
need to know what information we have. Normally, within the data collected, we
will have several variables that may or may not be good to include in our model.

The collected information will be stored in a dataset (database) tabularly ordered,
either an excel file, a .csv, a .txt, or other formats.

When we do data analysis, we will operate on datasets similar to the example in
the next slide, which, at the time of data collection, have been organized in a
tabular form so that:

- Each column of the dataset must be a variable and each row an observation. Each observation will be a different measurement and, therefore, a different value of the variable to be observed.
![](../attachments/screenshot-2024-03-17-at-122516.png)

Terms:
- A **variable** is a quantity, quality, or property that you can measure.
- A **value** is a state of a variable when you measure it. The value of a variable may change from measurement to measurement.
- An **observation** is a set of measurements made under similar conditions (you usually make all of the measurements in an observation at the same time and on the same object). An observation will contain several values, each associated with a different variable. I'll sometimes refer to an observation as a data point.
- **Tabular data** is a set of values, each associated with a variable and an observation. Tabular data is tidy if each value is placed in its own cell, each variable in its own column, and each observation in its own row.

![](../attachments/screenshot-2024-03-17-at-122755.png)

In real life, sometimes we are the ones who have to organize the data collected in a dataset.

In the same way, we may come across a dataset where there are **missing values**, values that have been recorded incorrectly or values in a format that is not correct.

In order to be able to use this data, we must know how they have been measured and how the data have been recorded, so that we can subsequently clean and correct the dataset.
Once we have the appropriate dataset, we will go on to **explore the data** we have so that we can analyze it and ask the most appropriate research questions. Through this analysis, we will also be able to make a selection of the variables to include in our model.

This process is known as Exploratory Data Analysis and is carried out after Data Cleansing.

We will not see in this course how to do a cleaning and a exploratory data analysis of the
variables of a dataset since you will see this content in many different courses during the
degree, but we will study how to find patterns in the data that will be very helpful in order to define our models.

To be able to build our models and choose the right variables, we must know what questions to ask ourselves to understand how our data are related.

There is no rule about which questions you should ask to guide your research.
However, two types of questions will always be useful for making discoveries
within your data. You can loosely word these questions as:
- What type of variation occurs within my variables?
- What type of covariation occurs between my variables?