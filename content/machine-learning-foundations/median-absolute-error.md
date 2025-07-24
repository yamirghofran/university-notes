---
title: Median Absolute Error
---

Mean Discrete Absolute Error (MdAE) is a metric used to evaluate the performance of models, particularly in scenarios where the predictions are discrete values. It is often used in fields such as image segmentation, where the goal is to predict discrete labels for each pixel or region. Here’s a detailed explanation of MdAE:

MdAE measures the average absolute error between the predicted discrete values and the actual discrete values. It provides a straightforward way to quantify the discrepancy between the model's predictions and the ground truth.

## Formula

The formula for MdAE is given by: $$\text{MdAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$$ where:

- $N$ is the total number of observations or predictions.
- $y_i$ is the actual discrete value.
- $\hat{y}_i$ is the predicted discrete value.
- $|y_i - \hat{y}_i|$ is the absolute difference between the actual and predicted values.

## Steps to Calculate MdAE

1. **Calculate the Differences**: For each observation, calculate the difference between the actual discrete value and the predicted discrete value.
2. **Take the Absolute Value**: Take the absolute value of each difference to ensure all values are positive.
3. **Average the Absolute Differences**: Calculate the mean of these absolute differences.

## Interpretation

- **MdAE Value**: A lower MdAE indicates better model performance, as it means the predictions are closer to the actual values. An MdAE of 0 would indicate perfect predictions, where all predicted values match the actual values.
- **Scale Independence**: Since MdAE is based on absolute differences, it is less sensitive to the scale of the data compared to metrics like RMSE. However, it is still important to interpret MdAE in the context of the specific application and the range of possible discrete values.

## Advantages

- **Simplicity**: MdAE is easy to understand and compute, making it a straightforward metric for evaluating model performance.
- **Robustness to Outliers**: Unlike RMSE, MdAE is not sensitive to the squaring of errors, making it less affected by outliers.

## Limitations

- **Lack of Sensitivity to Larger Errors**: Since MdAE uses absolute differences, it does not give more weight to larger errors, which might be important in some applications.
- **Discrete Nature**: MdAE is specifically designed for discrete values and may not be suitable for continuous data.

## Example

Suppose you have the following actual and predicted discrete values for a segmentation task:

| Actual (y) | Predicted (\(\hat{y}\)) |
|------------|----------------------|
| 1          | 1                     |
| 2          | 3                     |
| 3          | 2                     |
| 4          | 4                     |
| 5          | 5                     |

1. Calculate the absolute differences:
- $|1 - 1| = 0$
- $|2 - 3| = 1$
- $|3 - 2| = 1$
- $|4 - 4| = 0$
- $|5 - 5| = 0$
2. Average the absolute differences: $$\frac{0 + 1 + 1 + 0 + 0}{5} = \frac{2}{5} = 0.4$$ So, the MdAE for this set of predictions is 0.4. In summary, MdAE is a useful metric for evaluating the performance of models that predict discrete values. It provides a simple and straightforward measure of the average error between predicted and actual values, making it a valuable tool in applications such as image segmentation and other discrete prediction tasks.
