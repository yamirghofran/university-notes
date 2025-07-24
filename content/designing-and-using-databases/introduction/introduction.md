---
title: Introduction
---

# Databases

A Database is a structured collection of data that in organized and stored for efficient retrieval and manipulation.

It serves as a digital repository for information, making data accessible, manageable, and secure.

# Anatomy of a Database
- **Tables**: Data is organized into tables, each representing a specific entity(e.g. customers, products, etc.)
- **Records**: Rows within tables, containing individual data entries.
- **Fields**: Columns within records, holding specific types of data (e.g. name, age, address)
- **Keys**: Unique identifiers used to link records between tables for efficient data retrieval.

The structure and relationships between these components define the database's schema.

# Types of Databases
- Relational
- NoSQL
- Object-Oriented
## Classic Approach (Relational)
Relational databases are structured databases that organize data into tables with predefined schemas.

**SQL (Structured Query Language)**: SQL is the standard language used for managing and querying relational databases.

**ACID Properties**: Relational databases prioritize data consistensy and support ACID properties (Atomicity, Consistency, Isolation, Durability) to ensure data integrity.

**Schema**: Enforces a fixed schema where tables have predefined structures with specific data types.

**Data Relationships**: Embedded documents and references are used to represent relationships within documents.

**Querying and Performance**: SQL provides powerful querying capabilities, but complex joins can impact performance.

## Embracing Flexibility (NoSQL)
NoSQL databases are non-relational databases designed for flexibility in handling diverse data types.

**Diverse Types**: NoSQL includes subtypes like document stores, key-value stores, and graph databases, eacd tailored for specific data models and use cases.

**Scalability**: NoSQL databases are known for their ability to scale horizontally, making them well-suited for handling large, dynamic datasets.

**Use Cases**: NoSQL databases are often used for unstructured or semi-structured data, such as social media posts, internet of things data, and user profiles.

## Object-Oriented Databases
Object-Oriented databases store data as objects, mirroring the constructs of object-oriented programming languages.

**Complex Data Structures**: They are ideal for managing complex, interconnected data structures, such as those found in CAD (Computer-aided design) systems or multimedia databases.

**Persistence**: Object-oriented databases provide object persistence, simplifying the storage and retrieval of objects without the need for complex mappings.

**Use Cases**: These databases are commonly used in applications where rich object-oriented data models are crucial, such as scientific simulations, geographical information systems (GIS), and multimedia content management.