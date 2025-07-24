---
title: Equations of Motion
---

The final aim of physics is to be able to describe and predict the movement of any dynamical system, and to do so we quantify the exact manner in which forces modify position and velocity of particles. Mathematically speaking, this effort is translated into finding the **equations of motion** for a given dynamical system.

Newton's second law is the most basic way to derive the equations of motion, knowing the force as a function of position $\vec r$ and velocity $\vec v$, this is, $\vec F=\vec F(\vec r,\vec v)$. By doing so, we arrive to a **second order differential equation** for position (and in the general case, a system of coupled second order differential equations).

For example, using Newton's law we can describe the motion of planets in their orbits, or the trajectory of a rocket to land on the Moon, by solving
  

$$\frac{d^{2} \mathbf{r}_{i}}{d t^{2}}=G \sum_{i \neq j} \frac{m_{i} m_{j}}{\left|\mathbf{r}_{j}-\mathbf{r}_{i}\right|^{3}}\left(\mathbf{r}_{j}-\mathbf{r}_{i}\right)$$
Solving equations of motion allows us to calculate how the system is going to evolve through time, assuming the initial conditions (initial position and velocity) are known. However, the fact that we can write down the equations of motion of a given system does not imply we can solve them analytically...

For example, the problem of two bodies subjected to their gravitational interaction (like the Earth-Moon system) is completely solvable analytically. But the three body problem is not.

What can we do? we may use computers. We cannot solve many equations analytically, but we can almost always resort to numerical solutions by means of numerical methods.

Example of numerical method. What is the solution to $x^2-e^x+1=0$? Analytical solution is not obvious. Let's use Newton-Raphson method to compute a solution, following the update rule

$$x_{n+1}=x_{n}-\frac{f\left(x_{n}\right)}{f^{\prime}\left(x_{n}\right)}$$
```python
import numpy as np

def fun(x):
	return x**2+np.exp(x)-2

def numerical_derivative(x):
	ϵ=0.01
	return (fun(x)-fun(x+ϵ))/ϵ

def analytical_derivative(x):
	return 2*x+np.exp(x)
```

```python
tolerance=0.01 #criteria to stop the loop. It breakes the loop when precision achives a given tolerance.

x=2 #initial guess

x2=2

error=1 #just a value greater than tolerance

while error>=tolerance:

	#Newton-Raphson with numerical derivative
	
	x_sol=x-fun(x)/analytical_derivative(x)
	
	#Newton-Raphson with analytical derivative
	
	x_sol2=x-fun(x2)/analytical_derivative(x2)
	
	# we calculate error
	
	x=x_sol
	
	x2=x_sol2
	
	error=np.abs(fun(x_sol))

print('solution (numerical derivative): ', x_sol)

print('solution (analytical derivative): ',x_sol2)

print('check zero: ',fun(x_sol))

#solution (numerical derivative): 0.5374491629314389 
#solution (analytical derivative): 0.5374491629314389 
#check zero: 0.0004867890934292518
```

It might seem that with computers we could predict absolutely everything at hand... but unfortunately that's not the case. Certain equations of motion present chaotic behavior, this is, small perturbations in the initial conditions totally change the value of the solution for long enough periods of time (usually referred as extreme sensitivity to initial conditions).

![Alt Text](https://upload.wikimedia.org/wikipedia/commons/4/45/Double-compound-pendulum.gif)



