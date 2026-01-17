---
title: Interaction Data
---

Interaction data is the data you can collect from user interactions with the system your model supports.

Good interaction data contains information on three aspects:
- **context** of interaction
- **action** of the user in that context
- **outcome** of interaction

## Example
A reranking model for a search engine reranks search results for each user individually.

It takes as input the list of links returned by the search engine, based on keywords provided by the user, and outputs another list with a different order.

The context is the search query and the hundred documents presented to the user.

The action is the click of the user on a particular result. Or "back". Or "Next page".

The outcome is how much time the user spent reading the document and whether they hit "back".