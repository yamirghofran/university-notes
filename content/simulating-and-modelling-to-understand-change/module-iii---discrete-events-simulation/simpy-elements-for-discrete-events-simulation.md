---
title: SimPy Elements for Discrete Events Simulation
---


- **Entities** are the things flowing through the sequential processes in the model (e.g. patients, telephone calls, blood test results).
- **Generators** are the way in which entities enter the model and come into being (e.g. brought in by paramedics, self-presenting). Sometimes you will only have one generator, but some other times you will need multiple generators.
- **Inter-arrival** Times specify the time between entities being generated (arriving in the model). You may have different inter-arrival times for different generators. 
- **Activities/Servers** represent the activities that happen to entities (e.g. triage, treatment, ward admission).
- **Activity/Server** Time represents the amount of time it takes for an activity to happen to an entity. 
- **Resources** are required for activities to take place and may be shared between activities (e.g. nurse, doctor, receptionist, bed).
- **Queues** are where entities are held until an activity has capacity and the required resources to begin. 
- **Sinks** are how entities leave the model. Like generators, you can have more than one (e.g. Out, Died).