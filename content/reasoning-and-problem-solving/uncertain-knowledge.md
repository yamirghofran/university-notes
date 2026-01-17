---
title: Uncertain Knowledge
---

In the real world, we will need to handle uncertainty. Uncertainty can come from partial observability, non-determinism or adversaries.

Tracking belief states, as in problem-solving and logical agents, is limited
- Need to consider every possible explanation for sensor observations
- Plan for every eventuality
- No way to make decision if there's not guaranteed plan.

>[!Note] 
>Rational decisions depend on both the relative importance of various goals and the likelihood that, and degree to which, they will be achieved.

For this topic, the example that we will mostly use is the diagnosis of toothache.

Diagnosis is a general problem that always involves uncertainty.

>[!Error] Propositional Logic Doesn't Work
>- Toothache → Cavity: wrong as not all patients with toothache have cavities.
>- Toothache ⇒ Cavity∨GumProblem∨Abscess∨…, impossible to have the full list
>- Cavity → Toothache, not right either as not all cavities cause pain

Logic fails in diagnosis because of
- Laziness
	- too much work to find all the possible antecedents or consequents.
- Theoretical ignorance
	- there might not be a complete theory of the domain (e.g. in medicine)
- Practical ignorance
	- given that we might not be able to run a test or get a percept



