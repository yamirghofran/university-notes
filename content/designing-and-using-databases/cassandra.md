---
title: Cassandra
---

Apache Cassandra is a highly scalable, distributed NoSQL database management system designed for handling large amounts of data across many commodity servers without any single point of failure.

- **Scalability**: Linear scale-out architecture
- **Fault Tolerance**: No single point of failure
- **High Availability**: Replication across nodes
- **Flexible Schema**: No rigid schema like in traditional databases.


# Data Model
## Column-Family Data Model
- Cassandra uses a column-family data model, which is a NoSQL way of organizing and storing data.
- Data is organized into tables, similar to a relational database, but with a more flexible schema.

## Columns, Rows, and SuperColumns
- Rows are the basic unit of data storage.
- Columns are key-value pairs associated with rows.
- SuperColumns group related columns together.


# Cassandra Distributed Architecture
## Nodes and Rings
- **Nodes**: Individual servers in the Cassandra cluster.
- **Rings**: Logical representation of the data distribution. Each node in the cluster is a part of the ring.
## Tokens and Partitioning
- **Tokens**: Cassandra uses tokens to determine data distribution across the nodes.
- Data is partitioned based on these tokens.
## Replication
- Data is replicated across multiple nodes for fault tolerance.
- Replication strategy and factor can be configured.

# Cassandra Query Language
Cassandra Query Language is a SQL-like language for querying and interacting
with Cassandra.
It provides a familiar syntax for those accustomed to SQL.
SELECT, INSERT, UPDATE, DELETE operations.
CREATE KEYSPACE and CREATE TABLE for defining schema.

# Example
```sql
-- Creating a keyspace
CREATE KEYSPACE mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
-- Creating a table
CREATE TABLE mytable (id UUID PRIMARY KEY, name TEXT, age INT);
-- Inserting data
INSERT INTO mytable (id, name, age) VALUES (uuid(), 'John Doe', 25);
-- Querying data
SELECT * FROM mytable WHERE age > 21;
```

# Data Types and Collections
## Primitive Data Types
- Cassandra supports standard data types like INT, TEXT, UUID, etc.
## Collections
- Collections include LIST, SET, and MAP.
## Example
```sql
CREATE TABLE user_roles (username TEXT PRIMARY KEY, roles
SET<TEXT>);
```

# Secondary Indexes
Cassandra supports secondary indexes to enable querying on non-primary key
columns.
It allows for more flexible queries but should be used judiciously due to
performance implications.
`CREATE INDEX ON mytable (column_name);`

# Bloom Filters
- Bloom filters are probabilistic data structures used to test whether an element is a member of a set.
- In Cassandra, bloom filters are used to determine whether a particular [SSTables (Sorted String Tables)](/designing-and-using-databases/introduction/sstables-sorted-string-tables) has the data for a queried row.
## Benefits of Bloom Filters
- They reduce the number of disk seeks during read operations.
- They help Cassandra quickly eliminate [SSTables (Sorted String Tables)](/designing-and-using-databases/introduction/sstables-sorted-string-tables) that do no contain the necessary data.

# When to Use Cassandra
## Internet of Things (IoT) applications, sensor data, log data
Cassandra's ability to handle a high volume of writes and reads makes it suitable for scenarios where time-series data needs to be ingested and queried rapidly.

## Logging Systems and Event Tracking
Cassandra's distributed architecture allows it to horizontally scale,
providing **high write throughput** across multiple nodes. This makes it ideal for
scenarios where write operations are a primary concern.

## Global Applications with Users Distributed Across Regions
Cassandra's distributed architecture ensures that data is replicated
across nodes, providing fault tolerance and high availability. It is suitable for
applications that need to serve users globally without a single point of failure.