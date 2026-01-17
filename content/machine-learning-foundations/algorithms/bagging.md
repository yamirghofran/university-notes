---
title: Bagging
---

Bagging (Bootstrap Aggregating) reduces variance without increasing bias.

1. **Bootstrap**: draw *n* samples with replacement from training data *n* times → *n* datasets of same size.  
2. **Train**: fit a high-variance model (e.g., decision tree) on each dataset → *n* predictors.  
3. **Aggregate**:  
   - Regression → average predictions  
   - Classification → majority vote  