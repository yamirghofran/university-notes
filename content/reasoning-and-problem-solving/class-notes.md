---
title: Class Notes
---

> [!PDF|] [[Session23.pdf#page=7&selection=14,0,16,37|Session23, p.7]]
> > Decision theory = probability theory + utility theory
> 
> Expected utility = utility * probability of the utility happening

> [!PDF|] [[Session23.pdf#page=17&selection=2,14,2,25|Session23, p.17]]
> > independent
> 
> the more independent variables we have, the more scalable systems we can build. so, anytime reasonable, we will assume independence.

> [!PDF|] [[Session23.pdf#page=20&selection=53,0,61,68|Session23, p.20]]
> > However, the full joint distribution scales exponentially with the size of the variables (e.g. O(2n ) for n boolean variables), and is not practical in real situations.
> 
> The same problem as in truth tables in logic. Theoretically possible, but practically infeasible. That's why we make assumptions, etc.

> [!PDF|] [[Session23.pdf#page=35&selection=3,0,4,65|Session23, p.35]]
> > A variable is conditionally independent of all other nodes in the network, given its parents, children and children’s parents (aka its Markov blanket)
> 
> Let's us simplify a network to small independent groups that can be parallelized.

![Session23, p.35](../attachments/session23-p35-9868716d.png)

## Recap Presentations and Exam Tips
- explain a problem and ask for a good heuristic and why
- if you can't answer the question, talk about how you would think for a problem.

e.g. peg solitaire, is number of pegs
- doesn't differentiate between the equivalent nodes so doesn't give you more info so you can discard nodes or know which ones are better. So the `A*` would be the same as BFS.

- if there's a search tree, explain how it is reflected in the search tree
- if there is an example, use the example
- use the concepts from the course

Review the assingments.

### Konwledge based agents
- Sentences (axioms → we assume they're true)
- we use a syntax for representing
- semantics → represent truth of sentences within each world

- we can do inference (new knowledge from sentences)
	- ASK: QUERY
	- TELL: Add knowledge

Logical: propositional vs first order logic


FOL: objects, properties, relationships. PL: atomic facts only
FOL: predicates, variables, quantifiers, functions (more expessive). PL: no internal structure (less expressive)

epistemological commitmment: both true, false unknown


**Model**: complete assignment of truth values to all atomic propositions
**Satisfies**: a model satisfies a sentence a if a is true in that model.


Resolution rule: representing sentences as clauses (disjunction (OR) of literals)
Have p and not p in different clauses, cancel them out (resolution), and derive a new sentence.
can use proof by contradiction


FOL more convenient than PL (PL is a mess) but both can represent anything. Only FOL represents ni a high-level near-human way, propositional is much more lower level and inconvenient.


### Informed and Uninformed Search
Nodes represent state of the problem
Edges between nodes are the actions you can take in the action
e.g. don't use BFS if you have a super large state space.

### CSP
- variables
- domain (values you can assign variables)
- constraints

