---
title: 2. Higher Order or Polynomial Models
---

# Higher Order Terms
Many times, the relationship between two variables is not well described with a straight line. Imagine you are doing an EDA and you get the next scatterplot, what model do you apply to analyze this relationship?

![](../attachments/screenshot-2024-05-11-at-223347.png)

In these last topics we have been working with first order models, i.e. with straight line models. We can continue using them but, sometimes, we can improve the fit by using more flexible models like polynomial or gam models.

![](../attachments/screenshot-2024-05-11-at-223416.png)

All of the models discussed in the previous sections proposed straight line relationships between E(y) and each of the independent variables in the model. In this section, we consider models that allow for curvature in the relationships. A quadratic model is a second order model because it includes a $x^2$ term (polynomial family).

## A Quadratic (Second-Order) Model in a Single Quantitative Indpendent Variable

For example, consider a model that includes only **one quantitative independent variable x**. The form of this **quadratic model** is:

**E(y) = 𝜷0 + 𝜷1x + 𝜷2x2**

The term involving **$x^2$, called quadratic term (or second order term)**, enables us to hypothesize curvature in the graph of the response model relating y to x.

Interpretation 𝜷0 : **Only meaningful if 0 is within the values range of all the independent variables**. Is the average value of y when the value of all the independent variables is zero.

Interpretation 𝜷1 : Since the quadratic term is present in the model, this is no longer the slope of the line. It is simply a location parameter. **It has no meaning for us**.

Interpretation 𝜷2 : The sign of the coefficient of the quadratic term, is the indicator of whether the curve **is convex (mound shaped) or concave (bowl shaped). Rather than interpreting the numerical value of 𝜷 itself, we utilize a graphical interpretation to describe**
**the model.**

## Second Order Model Relationship
![](../attachments/screenshot-2024-05-11-at-223643.png)

To run this type of model in Python you only have to add the **quadratic term** in the ols function using the function I() to build the model. Check help().

`quadratic_model = smf.ols(formula = 'Y ~ X + I(X**2)', data = data).fit()`

## Higher Order Models in Polynomial Regression

As you can imagine, **when the line that describes the relationship between an independent variable and the dependent variable is not a straight line, but neither is it a simple curve, there are other functions or models that could describe this relationship**. Higher order models.

In polynomial regression, when the variable is squared, it is a second order term (quadratic);
**when it is cubed, it is a third order term (cubic); when it is raised to the power of four, it is a fourth order term (quartic); and so on.**

Which order of polynomial you include in your model is a matter of empirical adequacy.

### Quadratic Family
![](../attachments/screenshot-2024-05-11-at-223832.png)

- 2 oscillations
- Positive 𝜷: mound shaped 
- Negative 𝜷: bowl shaped 
- E(y) = 𝜷0 + 𝜷1x + 𝜷2x^2 
- Model formula: ‘y ~ x + I(x**2)’


### Cubic Family
- 3 oscillations
- Positive $\beta$: curve will initially bend downwards, then upwards.
- Negative 𝜷: curve will initially bend upwards, then downwards.
- E(y) = 𝜷0 + 𝜷1x + 𝜷2x^2 + 𝜷3x^3
- Model formula: ‘y ~ x + I(x**2) + I(x**3)’


### Quadratic Family
- 4 oscillations
- Positive 𝜷: curve will initially bend downwards, then upwards, then downwards
- Negative 𝜷: curve will initially bend upwards, then downwards, then upwards
- E(y) = 𝜷0 + 𝜷1x + 𝜷2x^2 + 𝜷3x^3 + 𝜷4x^4 
- Model formula: ‘y ~ x + I(x**2) + I(x**3) + I(x**4)’


## Higher Order Models in Polynomial Regression

Notice that the interpretation of the parameters of a polynomial regression then becomes more difficult compared to the straight linear case.

Therefore you should include more flexible models only if there is a clear increase in model fit and if the assumption of linearity is not met.

One more important rule: if you include a power of order n in your model, than all other powers of a smaller order should be included in the model even if not significant.

You will want to model your data as close as possible, but you want to avoid having too high a degree of polynomiality. Things to consider:

- You start with second-order polynomials. Then you plot the relationship, and you explore if a higher-order polynomial is necessary.
- Polynomials of orders higher than three or four are usually a bad idea.
- Polynomial terms are a bit restrictive so we normally use other flexible models as gam but when a polynomial function describes well the relationship between variables, a polynomial regression is usually more useful than a gam (generalized additive model) because is simpler.


## More Complex Modes
All the new terms that we used in interaction and higher order models can be combined to create more complex and powerful models.

One example of a more complex model is a complete second order model. When two or more quantitative independent variables are included in a second order model, we can incorporate squared terms for each x in the model, as well as the interaction between the two independent variables.

![](../attachments/screenshot-2024-05-11-at-224427.png)

![](../attachments/screenshot-2024-05-11-at-224439.png)

![](../attachments/screenshot-2024-05-11-at-224452.png)

Now that you know how to interpret each of the metrics, you can try to fit more complex models by combining first order or higher order terms, interaction terms and dummy variables.
In case you want to do so and need help with the syntax, let me know.