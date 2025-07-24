---
title: Doing Science
---

1. **Empirical observation**. This refers to collecting data concerning the system we want to study. In a simple physical system this could the position and velocity of a particle, or the temperature and concentration of a chemical element. In a biological system this might be data regarding blood pressure or the number of a certain species in an ecosystem. In an economic system this might be the GDP or the Gini coefficient of a country.
	- The process of gathering data usually requires measurement instruments and sensors.
	- In simple systems we are quite confident about all the variables involved, but in complex systems (like financial systems or social systems), the number of variables to collect data from become exceedingly large. Thus we are forced to select those we believe are more relevant.
2. Our observations give us hints concerning unobserved values of the system variables, the relationship between variables of the system, or how they system would behave when stimulated in a certain fashion. We formulate reasonable **hypothesis** or guess about the system: **from particular cases we infer a pattern**. Yet, our hypothesis must fulfill certain criteria to be regarded as an admissible scientific hypothesis:
	- It must be specific. In other words, it must be expressed in mathematical terms (or it can unambiguously translated into it). [why?]
	- Can you prove it wrong? If the answer is no, then it is not scientific. A **falsifiable** statement means that could be shown to be false, by direct observation or by experiment (Karl Popper's solution to demarcation problem).
	- It should be consistent with previously validated scientific hypothesis, but not necessarily!
3. From our hypothesis, we deduce consequences by means of logic reasoning and maths. This consequences may be straightforward of more convoluted. This a **deduction** process: **from a general statement we infer particular observations**. In a few words, we claim something like 'If I look there, then I should encounter this or that'.
	- A theory can be impossible to test completely, but we can test weather it fails in its predictions. Modus tollens: if $A\implies B$, then from $\neg B$ we infer $\neg A$.
4. **Experimentation**. With an experiment we can test whether our hypothesis holds when their *consequences* are compared with reality. Experiments allow us to test cause-effect relationships, unlike empirical observation alone! 
	
	In an experiment there are two groups of variables: dependent variables and independent variables (or controlled variables). What really characterizes an experiment is our control of independent variables and to observe the effect of dependent variables. There must be at least one variable that is manipulated and one variable that is measured.

	- Why is experimentation important? With empirical observations, the data points collected do not control for the variables that could potentially affect the variables involved in your hypothesis, you just collected data points! This means that you don't really know the validity of your statements under general conditions.

	- There are phenomena that is not spontaneously produced in nature, only in lab conditions!

	- An admissible experiment must be reproducible by other independent experimentalists.

	- In many disciplines it is very difficult, if not impossible, to perform a controlled experiment. So instead the look for confirmation in past. They try to confirm an hypothesis in looking at the past: this is called *backtesting* in contrast to experimentation, not the same! Others try to mathematically take into account dependent variables with multivariate regression analysis, but this is not the same either! and they often lead to false conclusions.

	- Unlike philosophical inquiry. Measurement instruments and experimentation is an active process that costs money. Science cannot progress without investment.
5. **Statistical tests and inference**. The data collected in the experiment is mathematically analyzed by means of statistical procedures. From this analysis we can validate (at least temporarily) our hypothesis, or refute it (or modify it accordingly).

	- As we use statistical inference, in many cases our conclusions are confirmed within a *level of confidence*, this is, a probability of being correct in your statement (examples, A is greater than B, or there is a linear relationship between A and B).

	- As a product of our experiments, we calculate properties that would probably be impossible to measure directly. Once we accept a scientific theory, many experiments are indeed perform to measure this qualities.

	- In machine learning validation is often used without an experiment: we simply split our data set into training and test. This way, one could identify patterns existing in our dataset, but not the real world!

	- As part of the validation process, it is important to include the whole scientific community: that's why scientific publications a peer reviewed journals are also part of the process. Read this article concerning the validation and the reproducibility crisis [https://towardsdatascience.com/the-machine-learning-crisis-in-scientific-research-91e61691ae76](https://towardsdatascience.com/the-machine-learning-crisis-in-scientific-research-91e61691ae76)



A collection of precise definitions and validated hypothesis about a system or phenomenon in such a way that we form a consistent and complete picture is what makes a scientific theory.

Science is not able to tell if a statement is absolutely true, but it can demonstrate its falsehood. Any scientific statement is therefore always open to question.
  


## How NOT to do science
Some ways of screwing up
1. You have an hypothesis based on data from the past, which explains very well what happened in the past, but you do NOT perform any experiment that controls for variables involved in the system (backtesting is not experimentation!)
2. You have an hypothesis before you examine the data. Then you look for data that confirms your hypothesis and neglect data refuting your hypothesis (Confirmation bias)
3. You perform experiments in such a way that they cannot be replicated.

## Challenges and limits of science
* What happens when we cannot measure what we want to study? (black holes)
* What happens when we cannot put a system into a lab? (societies, economies...)
* What happens when we confront ethical issues? (experimentation with people, animals...)