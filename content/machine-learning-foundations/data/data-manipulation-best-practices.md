---
title: Data Manipulation Best Practices
---

# Reproducibility
- Avoid transforming the data manually, or using shell commands with regular expressions, "quick and dirty" awk or sed commands, and piped expressions.
- Each step in data collection and transformation has to be implemented as a software script, e.g. python or R scripts with their inputs and outputs.
- Run the entire process as a pipeline (or workflow)

# Data first, algorithm second
Spend most of our effort and time on getting more data of wide variety and high quality, instead of trying to squeeze the maximum out of a learning algorithm.