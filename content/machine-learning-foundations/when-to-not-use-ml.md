---
title: When to (not) Use ML
---

# Use ML When
- Problem is **too complex** for coding
	- Spam detection: too many rules, exceptions. Unmaintainable over time.
- Problem is **constantly changing**
	- Web scraping: pages constantly change leading to constant failures and thus constant unsustainable maintenance.
- **Perceptive problem**
	- speech, image, and video recognition
- **Unstudied phenomenon**
	- Make predictions of a not well-studied phenomenon but examples of it are observable. e.g. hidden data patterns for personalized medicine, computer/network logs, human behavior.
- Simple objective
	- yes/no decisions or a single number e.g. 42
- Cost-effective
	- Collecting, preparing, and cleaning the data; training and running the model cost less than other suitable alternatives.

# Don't Use ML When
- Every action of the system or a decision made by it must be **explainable**
- The **cost of an error** made by the system is too high
- We want to get to the market **as fast as possible**
- Getting the [right data](/machine-learning-foundations/good-data) is too hard or impossible
- We can solve the problem using traditional software development at a lower cost
- A simple heuristic would work reasonably well
- We build a system that will not have to be improved over time.