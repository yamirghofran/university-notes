---
title: 8. Cross Validation
---

A common danger in modeling is **overfitting**. Overfitting happens when we create a model that behaves perfectly with our data, predicting a large percentage of the dependent variable, but when generalizing it is not able to predict the data that come from reality. On the other hand, under-fitting occurs when we create a model that does not fit our data (our sample of the population), and therefore will not fit properly to the reality. In none of the cases we can say that our model is generalizable.

To explain it in a less technical language, let’s give an example. Imagine that you would like to move to Japan, and therefore you have decided to study the language from home.

- **Overfitting**: You decide that you are going to see all the episodes of Dragon Ball to get an idea of the language before going to Japan. You repeat all the sagas of this series several times during a year, and once you know perfectly the language of the series you think you are ready to start your trip to Japan. You pack your bag and take the first flight, and when you arrive at Tokyo airport you have your first conversation with a Japanese person. You quickly realize that you don’t understand practically anything he’s saying to you, and every time you talk he looks at you strangely, as if you weren’t speaking the right way. **You have trained your mind very well with specific data that is not able to be generalized to other contexts and situations, so it is not useful for your purpose**. This would be a case of Overfitting.
- **Under-fitting:** You decide that you are going to read some of the Japanese dictionary before you leave. You spend two days reading the dictionary and the third day you take a flight to Tokyo. Obviously, when you arrive at Tokyo airport and start talking to a Japanese person, you don’t understand anything he says to you and you can’t articulate a word. **You have trained your mind badly with very poor data, so although the words you have studied are used in more general contexts, you are not able to reach your goal**. This would be a case of Under-fitting.
![](../attachments/screenshot-2024-03-17-at-124715.png)

In the graphs we can identify, on the left, the under-fitted model, and on the right the overfitted model. But how could we solve this problem?
Following the example, let’s imagine that we find a bar in our city where we can talk to
Japanese people to practice our language. If we follow the first strategy, the first time we get there the same thing will happen, but we will realize about our mistakes in a controlled
environment and we have time to return home and train with other situations. This is called **Cross Validation**. We divide our data into training sets and test sets to check that our model not only works correctly with the data I use to train it, but also with new data that has nothing to do with the training set.

To avoid the over and underfitting problems we will use cross validation techniques. In
this section we will explain the four most important cross validation techniques. All of
them can be summarized in the following steps:
- Reserve a small sample of the data set
- Build (or train) the model using the remaining part of the dataset
- Test the effectiveness of the model on the reserved sample of the data set. If the model works well on the test dataset, then it's good.

## Train / test Split Cross Validation
Dividing a dataset into a training set and a testing set is a common and necessary
operation when making a predictive model. It is important that we learn how to do
this before we start creating any model. In general terms, an original dataset is
usually divided into two sets: training and testing. Sometimes it is divided into a
third subset called a validation set.

**Training dataset**: This is the set with which we build the model. With this set we
will calculate the parameters to obtain the equations that we will use later.

**Testing dataset**: It is the set with which we check the effectiveness of our model.
The equations and parameters of the original model are now used to calculate
which is the output (Dependent Variable) based on the inputs of the testing set
(Independent Variables). These outputs are used to compare the efficiency of the
model, and see if it is really useful to predict or not the result.
![](../attachments/screenshot-2024-03-17-at-124936.png)

Generally, the training set and the testing set are divided using a ratio of
75%(training)-25%(testing) or even 80%-20%.

There are many ways to divide data into two sections. The easiest way is to take
the first 75%-80% for training and the rest for testing. However, this method can
lead to problems because the first rows come from a different data source than
the middle and end rows, or because they are ordered by time and so the time
factor is important in the model. These situations can lead to the final result of the
model being deviated from what it should have been.

The most effective way is to use a method to select rows randomly.
![](../attachments/screenshot-2024-03-17-at-125011.png)

This cross validation method is the most classic, and although it is still the most
used, it is not the one that gives us the best results. Let’s look at two other
methods that are a little more complex: **Leave one out cross validation (LOOCV)**
**and K-fold cross validation**. Let’s see how each of them works and how to carry
them out using the caret library.

## Leave One Out Cross Validation (LOOCV)

This method works as follow:
1. Leave out one data point and build the model on the rest of the data set
2. Test the model against the data point that is left out at step 1 and record the test error associated with the prediction
3. Repeat the process for all data points
4. Compute the overall prediction error by taking the average of all these test error estimates recorded at step 2
![](../attachments/screenshot-2024-03-17-at-125119.png)

We’ll use the **LeaveOneOut** function from the library `sklearn` in order to use this cross validation technique when we build our models.

The advantage of the LOOCV method is that we make use all data points reducing potential bias.
However, the process is repeated as many times as there are data points, resulting to a higher execution time when n is extremely large. Additionally, we test the model performance against one data point at each iteration. This might result to higher variation in the prediction error, if some data points are outliers.

Of course, we cannot manage that number of datasets manually, so we will use LOOCV in predefined sklearn functions when estimating our models. We will see an applied example just to understand how are we going to apply LOOCV.

![](../attachments/screenshot-2024-03-17-at-125232.png)

## K-fold Cross Validation
The k-fold cross-validation method evaluates the model performance on different subsets of the training data and then calculate the average prediction error rate.
1. Randomly split the data set into k-subsets (or k-fold) (for example 5 subsets)
2. Reserve one subset and train the model on all other subsets
3. Test the model on the reserved subset and record the prediction error
4. Repeat this process until each of the k subsets has served as the test set.
5. Compute the average of the k recorded errors. This is called the cross-validation error serving as the performance metric for the model.

K-fold cross-validation (CV) is a robust method for estimating the accuracy of a model.

The most obvious advantage of k-fold CV compared to LOOCV is computational. A
less obvious but potentially more important advantage of k-fold CV is that it often
gives more accurate estimates of the test error rate than does LOOCV. Typical
question, is how to choose right value of k?
Lower value of K is more biased and hence undesirable. On the other hand, higher
value of K is less biased, but can suffer from large variability. It is not hard to see that
a smaller value of k (say k = 2) always takes us towards the train-test approach,
whereas a higher value of k (say k = number of data points) leads us to LOOCV
approach.

In practice, one typically performs k-fold cross-validation using k’s between 5 and
10, as these values have been shown empirically to yield test error rate estimates
that suffer neither from excessively high bias nor from very high variance.

We’ll use the **KFold** function from the library **sklearn** in order to use this cross
validation technique when we build our models.
![](../attachments/screenshot-2024-03-17-at-125333.png)

### Repeated K-fold Cross Validation
The process of splitting the data into k-folds can be repeated a number of times, this
is called repeated k-fold cross validation. The final model error is taken as the mean
error from the number of repeats. Is generally recommended to use the (repeated)
k-fold cross-validation to estimate the prediction error rate.

We’ll use the **RepeatedKFold** function from the library `sklearn` in order to use this
cross validation technique when we build our models.


Obviously, you can alter the number of repeats and subsets as you like. ![](../attachments/screenshot-2024-03-17-at-125425.png) 

