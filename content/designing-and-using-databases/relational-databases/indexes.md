---
title: Indexes
---

Indexes are database structures that improve the speed of data retrieval operations, such as querying and sorting.

Without indexes, the database would have to scan every row in a table to find the requested data, which can be slow for large tables.

## How it works
Indexes are like a table of contents in a book, providing a quick reference to where data is located. They store a sorted list of values and pointers to the actual data rows.

## Advantages of Indexes
- Improved query performance: speeds up data retrieval operations.
- Efficient sorting: enhances sorting operations.
- Enforcement of Uniqueness: Enforces uniqueness constraints.
- Support for Joins: Facilitates efficient [Joins](/designing-and-using-databases/relational-databases/joins) operations.

