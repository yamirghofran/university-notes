---
title: Recommender Systems Handbook
---

- Item: what the system recommends to users
	- specific type of item.
- collaborative filtering
- user-generated-content (UGC)

## Data
- Items
- Users
- Ratings & evaluations for items (ch4)
- Ontological descriptions of users and books (ch3)
- Social relations of users (ch19)
- Activities of users (ch19)
	- Viewing a book
	- Favoriting a book
	- Liking a post about a book
	- Following an author
	- Following another user
- Transactions
	- Recorded interaction between a user and the RS. e.g. rating a recommendation
	- Tags e.g. "too long" for a movie RS.

## Content-based
System learns to recommend items that are similar to the ones that the user liked in the past. (ch3) similarity in item (e.g. genre)

## Collaborative Filtering
Recommends to the active user the items that other users with similar tastes liked in the past. similarity in rating history/activity. (ch4)
Most popular and widely implemented technique in RS.
- Neighborhood methods
- Matrix factorization (e.g. [SVD](/machine-learning-foundations/singular-value-decomposition-svd)) (ch5)

## Demographic
Recommends items based on the demographic profile of the user.

## Knowledge-based
Knowledge-based systems recommend items based on specific domain knowledge about how certain item features meet users needs and preferences and, ultimately, how the item is useful for the user. Notable knowledge based recommender systems are case-based.

## Community-based
This type of system recommends items based on the pref-
erences of the users friends. This technique follows the epigram “Tell me who your
friends are, and I will tell you who you are”. [8, 14]. Evidence suggests that people
tend to rely more on recommendations from their friends than on recommendations
from similar but anonymous individuals.

## Preference-based Systems (ch16)


## Presentation and Explanation techniques (ch17)


## Context (ch7)
- reduction-based (pre-filtering)
- contextual post filtering
- context modeling



## Practical Guideline
- ch10

## Evaluation
- offline and online
- ch8

## Challenges 
- proactive
- diversity
- long-term vs short term

## Data Mining
1. Similarity measure (mostly [Cosine Similarity](/matrices-and-linear-transformations/cosine-similarity))
2. [Sampling](/machine-learning-foundations/data-sampling). Common: standard random sampling without replacement 80-20
3. [Dimensionality Reduction](/machine-learning-foundations/dimensionality-reduction): [PCA](/machine-learning-foundations/principal-component-analysis-1) or [SVD](/machine-learning-foundations/singular-value-decomposition-svd)
4. Denoising (asking users to re-rate some item)
### Classification
- kNN
- Decision Tree
- Bayesian Networks / Naive Bayes classifier
- Support Vector Machines
- Ensembles of Classifiers, perform better than any classifier in isolation.
### Clustering Analysis
To improve efficiency by reducing number of operations. Has to be considered carefully to balance efficiency with possible loss in accuracy.
 - [Hierarchical Clustering](/machine-learning-foundations/hierarchical-clustering)
 - Partitional clustering


## Content-Based Systems
- Content Analyzer
	- Feature extraction from items like text as keyword vectors. 
	- Input to Profile Learner and Filtering Component
- Profile Learner
	- Collect data representative of the user preference and generalize using ML
	- Based on what the user has liked and not liked in the past.
- Filtering Component
	- Matches the user's profile representation against that of items to be recommended.
	- Results in a relevance judgment using a similarity metric (e.g. [Cosine Similarity](/matrices-and-linear-transformations/cosine-similarity))
![[CleanShot 2025-02-11 at 11.47.52@2x.png]]

1. Content Analyzer converts unstructured text into structured item representations, stores them in **Represented Items**.
2. User's reactions to items are collected and recorded in **Feedback** (called annotations or feedback). Later used with related item descriptions of learning model. Users can explicitly define areas of interest as an initial profile without providing any feedback.
	- Positive feedback: liked by user
	- Negative feedback: not liked by user.
	Recording user feedback can be explicit (directly asking user for rating on item), or implicit (inferring interest from user activity).

	Three approaches to collecting explicit feedback:
	- Like/Dislike
	- Rating: numerical scale
	- Text comments

	Implicit: assigning relevance score to user actions: 
	- Saving
	- Discarding
	- Recommending
	- Bookmarking
3. To build the profile of the active user $u_a$, the training set $TR_a$ for $u_a$ is defined as set of $\langle I_k, r_k \rangle$, where $r_k$ is the rating provided by $u_a$ on the item representation $I_k$. 
4. The Profile Learner applies supervised learning algorithms to generate a predictive model–the user profile–which is stored in a **profile** repository for later use by Filtering Component.
5. Given a new item representation, the Filtering Component predicts whether it is likely to be of interest for the active user, by comparing features in the item representation to those in the representation of user preferences (stored in the user profile). Filtering Components applies a ranking strategy and top-ranked items are included in a list of recommendations $L_a$, that is presented to $u_a$.
6. Up-to-date information should be maintained and provided to Profile Learner in order to automatically update the user profile.
7. Further feedback is gathered on generated recommendations by letting users state their satisfaction or dissatisfaction with items in $L_a$. 
8. Learning process is performed again using new training set and resulting profile is adapted to the updated user interests. (Creating the feedback-learning loop)
### Advantages
- User independence
	- Only need information for current users.
- Transparency
	- Explanations of recommendations can be provided by listing content features or descriptions that caused an item to be recommended.
- New items
	- They can recommend items that haven't been rated yet, based on features. Don't suffer from first-rater problem (in CF an item has to be rated by sufficient number of users)
### Limitations
- Limited content analysis
- Overspecialization
	- Limited degree of novelty in recommendations
- New User
	- Enough ratings have to be provided by a user to provide reliable recommendations.
Wordnet, Wikipedia Concepts, User-defined lexicons folksonomies, social tags as feedback on which recommendations are produced when few or no ratings for a specific user are available to the system.

### Item Representation
- VSM (Vector Space Model) with TF-IDF
- 