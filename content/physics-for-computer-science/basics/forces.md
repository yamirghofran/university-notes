---
title: Forces
---

What does an 'isolated object' mean? Strictly speaking, there is nothing in this universe that is completely isolated from everything else. If that object existed, it would mean there is no way to see it or communicate with it, thus it would only exist in our imagination. Fortunately, there are situations in which an object *weakly* interacts with its surroundings, so it behaves nearly as if it were isolated; thanks to these ideal simple movements we are able to conceptualize other more complex movements. For instance, if you don't hit the gas pedal in a car, it moves in straight line like an isolated particle, although the car eventually will stop moving due to friction with asphalt, air...

Nothing is isolated because anything is related to, at least, something else. Particles do not ignore each other, they 'communicate'. The physical manifestation of a relationship between objects is what we call **force**. The analytical form of a force is a description of how things are related to each other in terms of their movements.

We stated that an isolated body follows a uniform motion. Thus, we *define* a force as the cause of a changing velocity, this is, a force results in acceleration. This idea is essentially what the [Newton's second law](/physics-for-computer-science/mechanics---forces-and-energy/newtons-laws-of-motion) states:
$$\vec F\propto\vec a$$
The proportionality constant is what we call **mass**.

The second law simply expresses the fact that if a particle does not follow a linear motion, it must be because it is not isolated, and what is the absence of isolated? a relationship between motions, this, a force. Beautiful!

*Remark*: technically speaking, a body subjected to different forces and also follow a uniform motion as long as the compensate each other. **Forces are vectors, not scalars**.

Along the years, physicists have been able to identify **fundamental forces** that govern nature:
* the electromagnetic force,
* the gravitational force,
* the strong nuclear force,
* the weak nuclear force.

These forces dictate how particles relate to each other. Other common forces in our everyday life, like friction, come about as a byproduct of these fundamental interactions. The great dream is to have a theory that unifies all these forces. For instance, magnetic and electric forces were once thought to be independent forces, but their study showed that they are in fact expressions of a unique interaction: the electromagnetic force.

Generally speaking, interactions act both ways between a subsystem A and B. Nevertheless, it is useful to consider situations where interactions occur only in one way![[Pasted image 20240306130428.png]]
For instance, The Earth and a human body interact through gravity, but we only consider the former acting on the latter, because the force exerted by a human on the Earth is negligible.

The way we shall study the electromagnetic interaction actually follows this model. Charged particles interact with each other through electromagnetic forces. We shall decompose they dynamics of this interaction in two parts: a distribution of charges creates an electromagnetic field, and another distribution 'feels' the electromagnetic field created by the former. Of course, the second charge distribution also creates its own electromagnetic field, which in turn will affect the original electromagnetic field created by the first distribution. The idea is to assume that the effect of the second distribution on the first one is negligible.
![[Pasted image 20240306130626.png]]
