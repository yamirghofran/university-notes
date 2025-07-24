---
title: Matter, Space, and Time
---

Physics initially aimed for describing and predicting the movement of matter. What is the essential property of any material object? Its position in space. For a simple object, its position can be summarized with a point in space, determined by a position vector $\vec{r}$. A complete description would involve information about its orientation.

What determines whether our object is 'simple' enough or not: the context. A car is a big object, yet it is represented by a single point in a GPS.

Things change in time, so position is not enough to specify the state of an object. The change of position is what we call **velocity**. Mathematically, it is represented by its first derivative with respect to time.

$$\vec v=\frac{d\vec r}{dt}$$Similarly, we can investigate the change of velocity in time (the change of change), and this is what we call **acceleration**. Mathematically it's given by the second derivative with respect to time.

$$\vec a=\frac{d\vec v}{dt}=\frac{d^2\vec r}{dt^2}$$
One could continue defining rates of change *ad infinitum*. Nevertheless, it is not necessary to go beyond acceleration, why? because for a given isolated object, one can always find a framework in which velocity remains constant. This is the [first Newton's law](/physics-for-computer-science/mechanics---forces-and-energy/newtons-laws-of-motion). A constant velocity implies that the movement follows a straight-line or rectilinear motion (uniform motion).

## Symmetries and Conservation Laws
The fact that velocity doesn't change for an isolated object is an example of a conservation law (conservation of linear momentum in this case). Conservation laws are general principles that state that if a system fulfills certain conditions, there exists a certain quantity that remains constant in time. The most important conservation laws are the **conservation of linear momentum, the conservation of angular momentum and the conservation of energy**.

Why are conservation laws important? Simply because in physics we try to describe what changes in a system through what does not change. It could not be otherwise!

There is a close relationship between conservation laws and symmetries (which is the reason why physicists love symmetries): Conservation of linear momentum is obtained when a system looks the same when we displace it linearly in space; conservation of angular momentum is obtained when a system looks the same when we rotate it around a certain axis; finally, conservation of energy is derived when a system is indifferent to when we start counting time.