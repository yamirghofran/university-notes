---
title: System
---

A system is defined as a group of objects that are joined together in some regular interaction toward the accomplishment of some purpose.
e.g. considering a hospital as a system, doctors, nurses and patients would be the objects.

A system is often affected by changes occuring outside the system: **system environment**.
e.g. the arrival patients in a hospital

### Components of a System

- **Entity**: An object of interest in the system: machines, doctors or nurses in a hospital.
- **Attribute**: The property of an entity: speed, capacity, etc...
- **Activity**: A time period of specific length (can be endogenous or exogenous): surgical operation, room cleaning, etc...
- **State**: A collection of variables that describe the system in any time: status of machine (busy, inactive, down, etc...)
- **Event**: An instantaneous occurrence that might change the state of the system (can be endogenous or exogenous): e.g. breakdown.

So a **system** is a set of related entities, sometimes called **components** or **elements**.
These elements have certain characteristics or **attributes** that take on logical or numerical values.
e.g. in the hospital example, an attribute might be considered the number of beds in a room or the skill level of a professional.

Typically, the activities of individual components interact in time. These **activities** cause changes in the system's state.
e.g. the state of the hospital's waiting room might be described by the number of patients waiting for a doctor. When a patient arrives at the hospital or leaves it, the system jumps to a new state.

### Types of Systems
Depending on how we measure change in terms of system activities, we divide our system into two types:
- **[Discrete Events Systems](/simulating-and-modelling-to-understand-change/module-iii---discrete-events-simulation/discrete-events-simulation-python)** (DES): In those systems, the state variables change instantaneously through jumps at discrete points in time. e.g. a queue in a bank.
	![](../attachments/discrete-event-systems-example.png)
- **Continuous systems** (CS): Where state variables change continuously over time. e.g. water level in a dam.
	![](../attachments/continuous-system-example.png)
