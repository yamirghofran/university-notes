---
title: Mean Average Precision
---

Mean Average Precision (MAP) is a widely used metric for evaluating the performance of **information retrieval systems**. It provides a single-figure measure of quality across recall levels, giving a comprehensive view of how well a system retrieves relevant documents. Here’s a detailed explanation of MAP:

## Definition

MAP is the mean of the Average Precision (AP) scores for a set of queries. Average Precision is the average of precision values at each rank where a relevant document is retrieved. MAP is particularly useful in scenarios where the order of retrieved documents is important, such as in search engines and recommendation systems.

## Components

1. **Precision (P)**: The proportion of retrieved documents that are relevant to the query. $$P = \frac{\text{Number of relevant documents retrieved}}{\text{Total number of documents retrieved}}$$
2. **Recall (R)**: The proportion of relevant documents that are successfully retrieved. $$R = \frac{\text{Number of relevant documents retrieved}}{\text{Total number of relevant documents}}$$
3. **Average Precision (AP)**: The average precision at each rank where a relevant document is retrieved.

## Formula

The formula for Average Precision (AP) for a single query is: $$\text{AP} = \frac{1}{R} \sum_{k=1}^{n} P(k) \times \text{rel}(k)$$ where:

- $R$ is the total number of relevant documents for the query.
- $n$ is the total number of retrieved documents.
- $P(k)$ is the precision at rank $k$.
- $\text{rel}(k)$ is an indicator function that is 1 if the document at rank $k$ is relevant and 0 otherwise. The formula for Mean Average Precision (MAP) is: $$\text{MAP} = \frac{1}{Q} \sum_{q=1}^{Q} \text{AP}_q$$ where:
- $Q$ is the total number of queries.
- $\text{AP}_q$ is the Average Precision for query $q$.

## Steps to Calculate MAP

4. **Retrieve Documents**: For each query, retrieve a ranked list of documents.
5. **Calculate Precision at Each Rank**: For each rank where a relevant document is retrieved, calculate the precision.
6. **Compute Average Precision**: For each query, compute the Average Precision by averaging the precision values at each rank where a relevant document is retrieved.
7. **Average Across Queries**: Compute the mean of the Average Precision scores across all queries to get the MAP.

## Interpretation

- **MAP Value**: A higher MAP value indicates better performance of the retrieval system. A MAP of 1.0 would indicate perfect retrieval, where all relevant documents are retrieved at the top ranks.
- **Comprehensive Evaluation**: MAP provides a comprehensive evaluation of the retrieval system's performance by considering the order of retrieved documents and the precision at each relevant rank.

## Advantages

- **Order Sensitivity**: MAP considers the order of retrieved documents, making it suitable for evaluating systems where the order of results matters.
- **Comprehensive Metric**: It provides a single-figure measure that summarizes the performance across multiple queries and recall levels.

## Limitations

- **Complexity**: Calculating MAP can be more complex and computationally intensive compared to simpler metrics like precision or recall.
- **Interpretation**: Interpreting MAP results may require a deeper understanding of the retrieval system and the specific queries being evaluated.

## Example

Suppose you have the following retrieval results for three queries:

| Query | Retrieved Documents | Relevant Documents | Precision at Relevant Ranks |
|-------|---------------------|-------------------|--------------------------------|
| Q1    | D1, D2, D3, D4      | D2, D4            | P(2) = 0.5, P(4) = 0.5         |
| Q2    | D1, D2, D3          | D1, D3            | P(1) = 1.0, P(3) = 0.67       |
| Q3    | D1, D2, D3, D4, D5  | D2, D4, D5        | P(2) = 0.5, P(4) = 0.6, P(5) = 0.6|

1. **Calculate AP for each query**:
- For Q1: $\text{AP}_1 = \frac{0.5 + 0.5}{2} = 0.5$
- For Q2: $\text{AP}_2 = \frac{1.0 + 0.67}{2} = 0.835$
- For Q3: $\text{AP}_3 = \frac{0.5 + 0.6 + 0.6}{3} = 0.567$
2. **Calculate MAP**: $$\text{MAP} = \frac{0.5 + 0.835 + 0.567}{3} = 0.634$$
	So, the MAP for this set of queries is approximately 0.634. In summary, MAP is a valuable metric for evaluating the performance of information retrieval systems, providing a comprehensive and order-sensitive measure of precision across multiple queries and recall levels.
