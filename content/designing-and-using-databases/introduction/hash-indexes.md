---
title: Hash Indexes
---

 A Hash Index is a data structure used in databases to facilitate fast data retrieval. It's based on the concept of hash functions.

## How it works
- Hash Indexes use a hash function to map keys (eg column values) to specific locations in memory.
- Each unique key generates a hash value, which is used as an index to access the associated data.
https://visualgo.net/en/hashtable


## Pros and Cons of Hash Indexes
### Benefits
- Fast Retrieval
	- Hash indexes offer constant-time (O(1)) retrieval, making them exceptionally fast for exact-mach queries.
- No Sorting
	- Data is stored in an unordered fashion, eliminating the need for sorting.
	- Ideal for scenarios where sorting is not a requirement.

### Challenges
- Collisions
	- Hash collisions occur when two different keys produce the same hash value.
	- Collision resolution techniques (eg chaining, open addressing) are used to handle this issue.

## Use Cases and Limitations
### Use Cases
- Hash indexes are highly effective for primary key and exact-match lookups.
- Commonly used in in-memory databases and scenarios where retrieval speed is paramount.
### Limitations
- Inflexible for range queries or partial matches.
- Not suitable for scenarios requiring ordered data retrieval.