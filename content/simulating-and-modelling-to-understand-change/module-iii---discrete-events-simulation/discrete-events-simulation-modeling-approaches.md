---
title: Discrete Events Simulation Modeling Approaches
---

### Activity-oriented Approach
A model consists of sequences of activities, or operations, waiting to be executed
depending on some conditions. The simulation clock advances in fixed time
increments. At each step, the whole list of activities is scanned, and their
conditions, verified.

Activity-oriented simulations concentrate on the duration and time management
of activities. There's less emphasis on the specific events that start or end these
activities.

It's useful in situations where the time occupation or resource utilization is critical
and well-defined, such as in modelling manufacturing systems or in simulating
industrial processes.

### Event-oriented Approach
It completely bypasses the issue of time increment sensitivity by maintaining a list
of scheduled events ordered by time of occurrence. Then, the simulation just
consists in jumping from event to event, sequentially executing the associated
routines.

This approach is primarily concerned with the sequence of events and their impact
on the system. The simulation advances from event to event, updating the
system's state with each change.

It's particularly suited for systems where state changes are clearly defined and
critical to the system's dynamics, such as in telecommunications network
simulations or queueing systems.

### Process-oriented Approach
It refines the latter with the addition of interacting processes, whose activation is
triggered by events. In this case, the modeller defines a set of processes, which
correspond to entities or objects of the real system, and their life cycle.

The process-oriented approach models the simulation as a series of processes. A process is a sequence of events and activities that describe the behavior of a system component over time.

Process-based models allow for a more intuitive and detailed description of the
system's logic. They facilitate the modeling of complex interactions and
dependencies between different system components.

This approach is highly versatile and can be used in a wide range of applications,
including healthcare systems simulation, logistics, and any other system where
interactions and processes are complex and intertwined.
