---
title: Brief History
weight: 1
---

## Inception (1943-1956)
First work generally recognized as AI (McCulloch, Pitts, 1943)
- Model of artificial neurons (on/oﬀ, with a switch based on stimulus)
- Based on some extensive work by others (Rashevsky, Russell, Whitehead, Turing)
- Showed that it could express any computable function![](../attachments/cleanshot-2025-09-05-at-1231182x.png)
- First learning (Hebbian learning) added later (Hebb, 1949)
	- Updating the rule to modify connection strength between neurons
- SNARC, first neural network computer (Minsky, Edmonds, 1950)
	- 3000 vacuum tubes, network of 40 neurons
- Checkers-playing programs (Strachery 1952, Samuel 1952)
![](../attachments/cleanshot-2025-09-05-at-1234392x.png)

 - Computing Machinery and Intelligence, Turing 1950
	 - Based on lectures since 1947
	 - Introduces Turing test, machine learning, genetic algorithms and reinforcement learning
	 - Focused on learning over programming by hand
	 - Optimist, though aware of some of the potential perils of AI
- Dartmouth workshop was the peek of this cycle
- Greatest experts in the field got together for 2 months, but not much came from it
- Logic Theorist (LT), Newell, Simon, 1956
- Proved basic mathematical theorems
- Used of the search tree concepts we are go to explore more
- Lots of enthusiasm, "mind-body" problem solved?

## Early Enthusiasm (1952-1969)
- Many problems were solved during this time (games, puzzles, etc)
- Geometry Theorem Prover, Gelernter 1959
- Reinforcement learning on checkers (Samuel, 1956)
	- Shown on television
	- Played better than its creator, demonstrating learning
- General Problem Solver (GPS), Newell and Simon
	- Approached problems in similar ways to humans
	- Used predicate logic and search as well to find solutions, with improvements
- Physical symbol system hypothesis: "a physical symbol system has the necessary and suﬃcient means for general intelligent action"
	- Challenged on many grounds
### McCarthy
- Lisp, high-level language used broadly for AI (1958)
	- Still in some use, Clojure is based on it
	```lisp
	(defun fibonacci (N)
"Compute the N'th Fibonacci number."
(if (or (zerop N) (= N 1))
1
(+ (fibonacci (- N 1)) (fibonacci (- N 2)))))(defun fibonacci (N)
"Compute the N'th Fibonacci number."
(if (or (zerop N) (= N 1))
1
(+ (fibonacci (- N 1)) (fibonacci (- N 2)))))
	```

- "Programs with Common Sense"
	- Conceptual proposal for AI system based on knowledge and reasoning
	- Describes an "Advice Taker" system
	- Can be updated with new axioms, without being re-programmed
- Work on general-purpose methods for logical reasoning
### Minsky
Focused on working programs over logic, microworlds
- Students worked on many problems
	- Solved closed-form calculus integration problems, IQ test problems, etc.
	- Vision and constraint propagation (Waltz)
	- Learning theory (Winston)
	- Natural language understanding (Winograd)
- Perceptron convergence theorem (Block et all, 1962)
	- Learning algorithm can adjust the connection strengths of a perceptron to match any input data, provided such a match exists
## Missed Expectations (1966-1973)
- Progress grew slower, and high expectations were not met
- E.g. Simon's 1957 expectations took 40 instead of 10 years (e.g. world chess champion)
- Early systems failed on more diﬃcult problems
>It is not my aim to surprise or shock you—but the simplest way I can summarize is
to say that there are now in the world machines that think, that learn and that
create. Moreover, their ability to do these things is going to increase rapidly
until—in a visible future—the range of problems they can handle will be
coextensive with the range to which the human mind has been applied – Herbert Simon and Allen Newell

- Failures due to:
	- Informed introspection (about how humans think) rather than careful analysis of the problem
	- Lack of appreciation of the complexity of some problems (e.g. brute force solvers don't work on hard problems)
		- Theory of computational complexity was not yet developed
		- Genetic programming also was not just a resource availability problem
- AI research was even dropped on some universities
- Basic structures (e.g. perceptrons) were limited
	- Complex problems could not even be represented
	- Much of the work was on two-input perceptrons
	- Neural network research basically disappeared
- From weak methods (non-scalable general solutions) to solutions with domain-specific knowledge
- DENDRAL (Buchanan et al, 1969)
	- Infer molecule structure from mass spectrometer
	- Instead of searching over all possible values, codify domain-expert knowledge as rules
- MYCIN
	- 450 rules to diagnose blood infections
	- Rules reflected uncertainty with "certainty factors"
- Expert systems became very popular across all major corporations
- Started being applied to NLU
- New representation and reasoning tools
	- Prolog
	- PLANNER
	- Frames (structured approach to taxonomies and knowledge about objects)
- Lead to the re-establishment of AI as a field of interest![](../attachments/cleanshot-2025-09-05-at-1243472x.png)

## Today
- Neural networks, v2 (since 1986)
	- Thanks, in no small part, to growth in compute power
- Probabilistic reasoning and ML (since 1987)
	- Thanks to hidden Markov models and Bayesian networks
- Big data (since 2001 aprox)
	- Facilitated by the web and other massive data sources (e.g. new and cheaper sensors)
	- Created new interest for corporations
- Deep learning (since 2011)
	- Took oﬀ with speech recognition and image understanding
	- Specialized hardware helped achieve the necessary parallelism and compute
- Transformers/LLMs (since 2017)
- The private investment in AI in 2021 totaled around $93.5 billion—more than double the total private investment in 2020
- Large language models are setting new records on technical benchmarks, but new data shows that larger models are also more capable of reflecting biases from their training data
- Since 2018, the cost to train an image classification system has decreased by 63.6%, while training times have improved by 94.4%.
### Machine Translation
- Very high quality translations in languages with lots of training data
- But progress is also being made on languages that are underinvested (Google, Facebook)
- Lots of evolution in modeling and learning techniques
### Speech Recognition
- Similarly to translation, quality today usually suprasses human level on high investment languages
- Finally progress is being made on others (e.g. Indian and African languages), or with low representation accents/dialects
- Measured in WER (Word Error Rates), improvements have been constant for the last 10+ years
### Self-driving
- First demonstration 1980
- DARPA Grand challenge 2005
- Waymo test vehicles 2018 passed 10 million miles (16 million km)
- Tesla passed 35 million miles in 22 in Full Self-Driving
### Games
- 1996–1997 Kasparov v. Deep Blue (Chess)
- 2011 IBM Watson Wins Jeopardy!
- 2013 DeepMind Beats Atari
- 2016 AlphaGo v. Lee Sedol (Go)
- 2017 AlphaZero Masters Chess, Go, and Shogi
- 2019 AlphaStar (top 0.2% globally)
### Medicine
- Identification of cancerous cells
- Protein folding
- Designing and validating new drugs
### Image Understanding
- Google Photos (2015) introduced search across faces, subjects, landmarks…
	- But that came with challenges
- Segmentation is so commonplace it's taken for granted
	- Background change or blur, portrait mode, etc
- Key element of self-driving (especially Tesla's approach)