---
title: Storing and Documenting Features
---

-   Schema file that describes the features’ expected properties.
-   **Machine-readable** (e.g., JSON, CSV, or YAML), versioned, and updated when we update our features.
-   Note: we can automate the creation and ingestion of the schema file.
-   Creation: Loop over the features (e.g., the column in a DataFrame) and extract the feature name, data type, missing values (% or count), unique values, range, min/max, mean, variance, allowed values (categorical), transformation steps (feature engineering), popularity, etc.
-   Deep dive. E.g., popularity:
   -  Depends on the definition of feature popularity: which metric?
   -  Missing values: the fewer the missing values in a feature, the more popular that feature is.
   -  Importance score in a model: score the impact of a feature in a model (e.g., [Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html))
   -  Unique value distribution: the more unique values a feature has, the less useful it can be (e.g., ID).


![](../attachments/cleanshot-2025-01-23-at-2048092x.png)