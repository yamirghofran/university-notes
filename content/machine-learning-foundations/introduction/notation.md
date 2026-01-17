---
title: Notation
---

# Scalars, Vectors Sets

## Scalar
A scalar is a simple numerical value like 15 or -3.25. Variables or constants that take scalar values are denoted by an italic letter, like $x$ or $a$.
![[CleanShot 2024-12-19 at 20.44.12@2x.png]]

## Vector
A **vector** is an ordered list of scalar values, called attributes. We denote a vector as a bold character, for example, $\mathbf{x}$ or $\mathbf{w}$. Vectors can be visualized as arrows that point to some directions as well as points in a multi-dimensional space. Illustrations of three two-dimensional vectors, $\mathbf{a} = [2, 3]$, $\mathbf{b} = [-2, 5]$, and $\mathbf{c} = [1, 0]$ is given in fig. 1. We denote an attribute of a vector as an italic value with an index, like this: $w^{(j)}$ or $x^{(j)}$. The index $j$ denotes a specific **dimension** of the vector, the position of an attribute in the list. For instance, in the vector $\mathbf{a}$ shown in red in fig. 1, $a^{(1)} = 2$ and $a^{(2)} = 3$.

The notation $x^{(j)}$ should not be confused with the power operator, like this $x^2$ (squared) or $x^3$ (cubed). If we want to apply a power operator, say square, to an indexed attribute of a vector, we write like this: $(x^{(j)})^2$.

A variable can have two or more indices, like this: $x_i^{(j)}$ or like this $x_{i,j}^{(k)}$. For example, in neural networks, we denote as $x_{j,u}^{(l)}$ the input feature $j$ of unit $u$ in layer $l$

## Set
A **set** is an unordered collection of unique elements. We denote a set as a calligraphic capital character, for example, $\mathcal{S}$. A set of numbers can be finite (include a fixed amount of values). In this case, it is denoted using accolades, for example, $\{1, 3, 18, 23, 235\}$ or $\{x_1, x_2, x_3, x_4, \ldots, x_n\}$. A set can be infinite and include all values in some interval. If a set includes all values between $a$ and $b$, including $a$ and $b$, it is denoted using brackets as $[a, b]$. If the set doesn’t include the values $a$ and $b$, such a set is denoted using parentheses like this: $(a, b)$. For example, the set $[0, 1]$ includes such values as $0$, $0.0001$, $0.25$, $0.784$, $0.9995$, and $1.0$. A special set denoted $\mathbb{R}$ includes all numbers from minus infinity to plus infinity.

When an element $x$ belongs to a set $\mathcal{S}$, we write $x \in \mathcal{S}$. We can obtain a new set $\mathcal{S}_3$ as an **intersection** of two sets $\mathcal{S}_1$ and $\mathcal{S}_2$. In this case, we write $\mathcal{S}_3 \leftarrow \mathcal{S}_1 \cap \mathcal{S}_2$. For example $\{1, 3, 5, 8\} \cap \{1, 8, 4\}$ gives the new set $\{1, 8\}$.

We can obtain a new set $\mathcal{S}_3$ as a **union** of two sets $\mathcal{S}_1$ and $\mathcal{S}_2$. In this case, we write $\mathcal{S}_3 \leftarrow \mathcal{S}_1 \cup \mathcal{S}_2$. For example $\{1, 3, 5, 8\} \cup \{1, 8, 4\}$ gives the new set $\{1, 3, 4, 5, 8\}$.

# Capital Sigma Notation
The summation over a collection $X = \{x_1, x_2, \ldots, x_{n-1}, x_n\}$ or over the attributes of a vector $\mathbf{x} = [x^{(1)}, x^{(2)}, \ldots, x^{(m-1)}, x^{(m)}]$ is denoted like this:

$$
\sum_{i=1}^{n} x_i \overset{\text{def}}{=} x_1 + x_2 + \ldots + x_{n-1} + x_n, \quad $$
$$\text{or else:} $$
$$\quad \sum_{j=1}^{m} x^{(j)} \overset{\text{def}}{=} x^{(1)} + x^{(2)} + \ldots + x^{(m-1)} + x^{(m)}.
$$

The notation $\overset{\text{def}}{=}$ means "is defined as".

# Capital Pi Notation
A notation analogous to capital sigma is the **capital pi notation**. It denotes a product of elements in a collection or attributes of a vector:

$$
\prod_{i=1}^{n} x_i \overset{\text{def}}{=} x_1 \cdot x_2 \cdot \ldots \cdot x_{n-1} \cdot x_n,
$$

where $a \cdot b$ means $a$ multiplied by $b$. Where possible, we omit $\cdot$ to simplify the notation, so $ab$ also means $a$ multiplied by $b$.

# Operations on Sets
A derived set creation operator looks like this: $\mathcal{S}' \leftarrow \{x^2 \mid x \in \mathcal{S}, x > 3\}$. This notation means that we create a new set $\mathcal{S}'$ by putting into it $x$ squared such that $x$ is in $\mathcal{S}$, and $x$ is greater than 3.

The cardinality operator $|\mathcal{S}|$ returns the number of elements in set $\mathcal{S}$.

# Operations on Vectors
The sum of two vectors $\mathbf{x} + \mathbf{z}$ is defined as the vector $[x^{(1)} + z^{(1)}, x^{(2)} + z^{(2)}, \ldots, x^{(m)} + z^{(m)}]$.

The difference of two vectors $\mathbf{x} - \mathbf{z}$ is defined as the vector $[x^{(1)} - z^{(1)}, x^{(2)} - z^{(2)}, \ldots, x^{(m)} - z^{(m)}]$.

A vector multiplied by a scalar is a vector. For example, $c\mathbf{x} \overset{\text{def}}{=} [cx^{(1)}, cx^{(2)}, \ldots, cx^{(m)}]$.

A **dot-product** of two vectors is a scalar. For example, $\mathbf{w} \cdot \mathbf{x} \overset{\text{def}}{=} \sum_{i=1}^{m} w^{(i)} x^{(i)}$. In some books, the dot-product is denoted as $\mathbf{w} \cdot \mathbf{x}$. The two vectors must be of the same dimensionality. Otherwise, the dot-product is undefined.

The multiplication of a matrix $\mathbf{W}$ by a vector $\mathbf{x}$ gives another vector as a result. Let our matrix be,

$$
\mathbf{W} = \begin{bmatrix} w^{(1,1)} & w^{(1,2)} & w^{(1,3)} \\ w^{(2,1)} & w^{(2,2)} & w^{(2,3)} \end{bmatrix}.
$$

When vectors participate in operations on matrices, a vector is by default represented as a matrix with one column. When the vector is on the right of the matrix, it remains a column vector. We can only multiply a matrix by a vector if the vector has the same number of rows as the number of columns in the matrix. Let our vector be $\mathbf{x} \overset{\text{def}}{=} [x^{(1)}, x^{(2)}, x^{(3)}]$. Then $\mathbf{W}\mathbf{x}$ is a two-dimensional vector defined as,

$$
\mathbf{W}\mathbf{x} = \begin{bmatrix} w^{(1,1)} & w^{(1,2)} & w^{(1,3)} \\ w^{(2,1)} & w^{(2,2)} & w^{(2,3)} \end{bmatrix} \begin{bmatrix} x^{(1)} \\ x^{(2)} \\ x^{(3)} \end{bmatrix}
$$

$$
\overset{\text{def}}{=} \begin{bmatrix} w^{(1,1)}x^{(1)} + w^{(1,2)}x^{(2)} + w^{(1,3)}x^{(3)} \\ w^{(2,1)}x^{(1)} + w^{(2,2)}x^{(2)} + w^{(2,3)}x^{(3)} \end{bmatrix} = \begin{bmatrix} \mathbf{w}^{(1)} \mathbf{x} \\ \mathbf{w}^{(2)} \mathbf{x} \end{bmatrix}
$$

If our matrix had, say, five rows, the result of the above product would be a five-dimensional vector.

When the vector is on the left side of the matrix in the multiplication, then it has to be **transposed** before we multiply it by the matrix. The transpose of the vector $\mathbf{x}$ denoted as $\mathbf{x}^\top$ makes a row vector out of a column vector. Let’s say,

$$
\mathbf{x} = \begin{bmatrix} x^{(1)} \\ x^{(2)} \end{bmatrix},
$$

then,

$$
\mathbf{x}^\top \overset{\text{def}}{=} \begin{bmatrix} x^{(1)}, x^{(2)} \end{bmatrix}.
$$

The multiplication of the vector $\mathbf{x}$ by the matrix $\mathbf{W}$ is given by $\mathbf{x}^\top \mathbf{W}$,

$$
\mathbf{x}^\top \mathbf{W} = \begin{bmatrix} x^{(1)}, x^{(2)} \end{bmatrix} \begin{bmatrix} w^{(1,1)} & w^{(1,2)} & w^{(1,3)} \\ w^{(2,1)} & w^{(2,2)} & w^{(2,3)} \end{bmatrix}
$$

$$
\overset{\text{def}}{=} \begin{bmatrix} w^{(1,1)}x^{(1)} + w^{(2,1)}x^{(2)}, w^{(1,2)}x^{(1)} + w^{(2,2)}x^{(2)}, w^{(1,3)}x^{(1)} + w^{(2,3)}x^{(2)} \end{bmatrix}
$$

As you can see, we can only multiply a vector by a matrix if the vector has the same number of dimensions as the number of rows in the matrix.

# Functions
A **function** is a relation that associates each element $x$ of a set $\mathcal{X}$, the **domain** of the function, to a single element $y$ of another set $\mathcal{Y}$, the **codomain** of the function. A function usually has a name. If the function is called $f$, this relation is denoted $y = f(x)$ (read *f of x*), the element $x$ is the argument or input of the function, and $y$ is the value of the function or the output. The symbol that is used for representing the input is the variable of the function (we often say that $f$ is a function of the variable $x$).

We say that $f(x)$ has a **local minimum** at $x = c$ if $f(x) \ge f(c)$ for every $x$ in some open interval around $x = c$. An **interval** is a set of real numbers with the property that any number that lies between two numbers in the set is also included in the set. An **open interval** does not include its endpoints and is denoted using parentheses. For example, $(0, 1)$ means greater than 0 and less than 1. The minimal value among all the local minima is called the **global minimum**. See illustration in fig. 2.

A **vector function**, denoted as $\mathbf{y} = f(\mathbf{x})$, is a function that returns a vector $\mathbf{y}$. It can have a vector or a scalar argument.

![[CleanShot 2024-12-19 at 20.55.36@2x.png]]

# Max and Arg Max
Given a set of values $\mathcal{A} = \{a_1, a_2, \ldots, a_n\}$, the operator,

$$
\max_{a \in \mathcal{A}} f(a)
$$

returns the highest value $f(a)$ for all elements in the set $\mathcal{A}$. On the other hand, the operator,

$$
\operatorname{arg\,max}_{a \in \mathcal{A}} f(a)
$$

returns the element of the set $\mathcal{A}$ that maximizes $f(a)$. Sometimes, when the set is implicit or infinite, we can write $\max_a f(a)$ or $\operatorname{arg\,max}_a f(a)$.

Operators $\min$ and $\operatorname{arg\,min}$ operate in a similar manner.

# Assignment Operator
The expression $a \leftarrow f(x)$ means that the variable $a$ gets the new value: the result of $f(x)$. We say that the variable $a$ gets assigned a new value. Similarly, $\mathbf{a} \leftarrow [a_1, a_2]$ means that the two-dimensional vector $\mathbf{a}$ gets the value $[a_1, a_2]$.

# Derivative and Gradient
A **derivative** $f'$ of a function $f$ is a function or a value that describes how fast $f$ grows (or decreases). If the derivative is a constant value, like 5 or $-3$, then the function grows (or decreases) constantly at any point $x$ of its domain. If the derivative $f'$ is a function, then the function $f$ can grow at a different pace in different regions of its domain. If the derivative $f'$ is positive at some point $x$, then the function $f$ grows at this point. If the derivative of $f$ is negative at some $x$, then the function decreases at this point. The derivative of zero at $x$ means that the function’s slope at $x$ is horizontal.

The process of finding a derivative is called **differentiation**.

Derivatives for basic functions are known. For example if $f(x) = x^2$, then $f'(x) = 2x$; if $f(x) = 2x$ then $f'(x) = 2$; if $f(x) = 2$ then $f'(x) = 0$ (the derivative of any function $f(x) = c$, where $c$ is a constant value, is zero).

If the function we want to differentiate is not basic, we can find its derivative using the **chain rule**. For example if $F(x) = f(g(x))$, where $f$ and $g$ are some functions, then $F'(x) = f'(g(x))g'(x)$. For example if $F(x) = (5x + 1)^2$ then $g(x) = 5x + 1$ and $f(g(x)) = (g(x))^2$. By applying the chain rule, we find $F'(x) = 2(5x + 1)g'(x) = 2(5x + 1)5 = 50x + 10$.

**Gradient** is the generalization of derivative for functions that take several inputs (or one input in the form of a vector or some other complex structure). A gradient of a function is a vector of **partial derivatives**. You can look at finding a partial derivative of a function as the process of finding the derivative by focusing on one of the function’s inputs and by considering all other inputs as constant values.

For example, if our function is defined as $f([x^{(1)}, x^{(2)}]) = ax^{(1)} + bx^{(2)} + c$, then the partial derivative of function $f$ with respect to $x^{(1)}$, denoted as $\frac{\partial f}{\partial x^{(1)}}$, is given by,

$$
\frac{\partial f}{\partial x^{(1)}} = a + 0 + 0 = a,
$$

where $a$ is the derivative of the function $ax^{(1)}$; the two zeroes are respectively derivatives of $bx^{(2)}$ and $c$, because $x^{(2)}$ is considered constant when we compute the derivative with respect to $x^{(1)}$, and the derivative of any constant is zero.

Similarly, the partial derivative of function $f$ with respect to $x^{(2)}$, $\frac{\partial f}{\partial x^{(2)}}$, is given by,

$$
\frac{\partial f}{\partial x^{(2)}} = 0 + b + 0 = b.
$$

The gradient of function $f$, denoted as $\nabla f$ is given by the vector $\left[ \frac{\partial f}{\partial x^{(1)}}, \frac{\partial f}{\partial x^{(2)}} \right]$.

The chain rule works with partial derivatives too, as I illustrate in Chapter 4.

![[CleanShot 2024-12-19 at 20.58.53@2x.png]]