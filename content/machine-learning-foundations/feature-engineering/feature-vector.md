---
title: Feature Vector
weight: 1
---

A feature vector is a [[Vector]] in which each dimension $j = 1, \ldots, D$ contains a value that describes the example somehow. That value is called a **feature** and is denoted as $x^{(j)}$. 

For instance, if each example $\mathbf{x}$ in our collection represents a person, then the first feature, $x^{(1)}$, could contain height in cm, the second feature, $x^{(2)}$, could contain weight in kg, $x^{(3)}$ could contain gender, and so on. 

For all examples in the dataset, the feature at position $j$ in the feature vector always contains the same kind of information. It means that if $x_i^{(2)}$ contains weight in kg in some example $x_i$, then $x_k^{(2)}$ will also contain weight in kg in every example $x_k$, $k = 1, \ldots, N$. 

The label $y_i$ can be either an element belonging to a finite set of **classes** $\{1, 2, \ldots, C\}$, or a real number, or a more complex structure, like a [[vector]], a [[matrix]], a tree, or a graph. Unless otherwise stated, in this book $y_i$ is either one of a finite set of classes or a real number. You can see a class as a category to which an example belongs. For instance, if your examples are email messages and your problem is spam detection, then you have two classes $\{\text{spam}, \text{not\_spam}\}$.