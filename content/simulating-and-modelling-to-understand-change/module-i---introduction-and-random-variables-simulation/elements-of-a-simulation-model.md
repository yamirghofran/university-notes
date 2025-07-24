---
title: Elements of a Simulation Model
---

A simulation model is often made of:
### Objects of the model
- **Entities**: Individual elements of the system that are being simulated and whose behavior is being explicitly tracked. Each entity can be individually identified.
- **Resources**: Individual elements of the system but they are not modelled individually. They are treated as countable items whose behavior is not tracked.

The decision of treating an element as an entity or as a resource is up to the modeller's discretion and depends on the purpose of the simulation.

e.g. in the donut shop simulation example, **clients** would be resources since we're not interested in what each of them do. **Employees** may either be considered as **entities or resources**: in the former case, we want to track the amount of time each of them are working; in the latter, the model would only be able to output an overview of how busy overall the employees are.

### Organization of objects
We can classify and organize objects according to their **attributes, state, or order**.
- **Attributes**: Properties of objects (entities). They are often used **to control the behavior of the object**. In our donut shop, an attribute may be whether an employee is busy or available, or the type of donut a customer will but (for instance, chocolate, vanilla, or jam).
- **State**: Collection of variables necessary to describe the system at any time point. In the donut shop example, they would be the number of customers queuing and number of busy employees.
- **List**: Collection of entities or resources ordered in some logical fashion. e.g. customers waiting in the shop may be ordered in "first come, first served" scheme.

### Operations of the objects
During a simulation study, entities and resources will cooperate and therefore change state. The following terminology describes this as well as the flow of time.

- **Event:** Instant of time where the state of the system changes. In the donut shop example, an event is when a customer has finished being served: the number of busy employees decreases by one and there is one less customer queuing.
- **Activity**: A time period of specified length which is known when it begins (although its length may be random). The time an employee takes to serve a customer is an example of an activity: this may be specified in terms of a random distribution.
- **Delay**: Duration of time of unspecified length, which is not known until it ends. This is not specified by the modeller ahead of time but is determined by the conditions of the system. Very often, this is one of the desired outputs of the simulation. e.g. a delay is the waiting time of a customer in the queue of our donut shop.
- **Clock**: Variable representing simulated time.