---
title: Knowledge Representation
---

How we use [First Order Logic](/reasoning-and-problem-solving/first-order-logic) to represent the world.
## Ontological Engineering
Representing abstract concepts in the domain.
- There are placeholder concepts, as we can't expect to represent everything in the world (e.g. "physical object" is a broad category)
- General framework is called **Upper Ontology**

e.g. the upper ontology of the world.
![](../attachments/cleanshot-2025-11-19-at-1501302x.png)

Capturing exceptions can be hard in First-Order Logic, as it works better for general rules.

In [Wumpus World](/reasoning-and-problem-solving/wumpus-world), we might only have wumpuses or we might want to have a general "Animal" category of which wumpuses are one individual, and even Animals could have a taxonomy (e.g. people eating or not)

It's not clear if there's a **general-purpose ontology** with the following characteristics:
- should be applicable to any special purpose domain
- different areas of knowledge should be unified, to allow reasoning across them (e.g. combine space and time aspects)

In practice, general ontologies aren't used, but in some domains there are broadly applicable ones (e.g. medicine, facts from wikipedia, etc.)

## Categories and Objects
Reasoning can take place at the level of categories. Categories help us make predictions about individual objects. Objects can be inferred from perceptual inputs and attached to a category.

Individuals inherit properties from the category.

Subcategories create a taxonomy of categories.

### Representation in First-Order Logic
- An object is a member of a category
	- BB ∈ Basketballs
- All members of a category have a property
	- (x ∈ Basketball) ⇒ Spherical(x)
- Members of a category can be recognized based on properties
	- Orange(x)∧Round(x)∧Diameter(x)=9.5”∧x∈Balls ⇒ x ∈ Basketball
- A category has some properties
	- Dogs∈DomesticatedSpecies

### Disjoint, Exhaustive decomposition and partition
- Disjoints have no members in common
	- Disjoint(s) ⇔ (∀c1 ,c2 c1∈s ∧ c2∈s ∧ c1 ≠ c2 ⇒ Intersection(c1 ,c2 ) = {})
	- Disjoint({Animals, Vegetables})
- Exhaustive decomposition repersent all possible subcategories
	- ExhaustiveDecomposition(s, c) ⇔ (∀i i∈c ⇔ ∃c2 c2∈s∧i∈c2 )
	- ExhaustiveDecomposition({Americans, Canadians, Mexicans}, NorthAmericans)
- Partition is an exhaustive decomposition of disjoint set
	- Partition(s, c) ⇔ Disjoint(s) ∧ ExhaustiveDecomposition(s, c)
	- Partition({Animals, Plants, Fungi, Protista, Monera}, LivingThings)
### Physical Composition
- PartOf relationship
	- Similar to subset, but for objects instead of categories
	- It is transitive: PartOf(x,y)∧PartOf(y,z)⇒PartOf(x,z)
	- And reflexive: PartOf(x,x)
- Composite objects, defined by the relationships between parts (PartOf, Attached, etc.)
	- we could define a PartPartition
- BunchOf to describe composite bundles of no particular structure
	- E.g. BunchOf({Apple1, Apple2, Apple3})
	- ∀x x∈s ⇒ PartOf(x, BunchOf(s))
	- ∀y \[∀x x∈s ⇒ PartOf(x,y)\] ⇒ PartOf(BunchOf(s),y) : Logical minimization
### Measurements
- We use unit functions, that take a number as an argument
	- Length(L1 ) = Inches(1.5) = Centimeters(3.81)
- We can express conversions across unites
	- Centimeters(2.54 x d) = Inches(d)
- Monetary units can also be used
	- $(x) represents a dollar value

## Event Calculus
Event calculus can express more complex actions, which might be ongoing, simultaneous, etc.

- Uses events, fluent, and time points.
- e.g. Shankar flying from SF to DC
	- E1∈Flyings∧Flyer(E1 ,Shankar)∧Origin(E1 ,SF)∧Destination(E1 ,DC)
	- Flyings is the category of all flying events
Event calculus uses a set of predicates:
- T(f, t1 , t2 ): Fluent f is true for all times between t1 and t2 
- Happens(e, t1 , t2 ): Event e starts at time t1 and ends at t2 
- Initiates(e, f, t): Event e causes fluent f to become true at time t 
- Terminates(e, f, t): Event e causes fluent f to cease to be true at time t 
- Initiated(f, t1 , t2 ): Fluent f becomes true at some point between t1 and t2 
- Terminated(f, t1 , t2 ): Fluent f ceases to be true at some point between t1 and t2 
- t1 < t2 : Time point t1 occurs before time t2

Axioms can be formed from this predicates, establishing order.

## Other Topics
- Things and stuff (i.e. contable vs uncountable)
- Mental object and Modal logic
- Reasoning Systems for Categories, allow us to organize and drive inferences based on categories and relationships
- Reasoning with Default Information, including circumscription to define exceptions and belief revision