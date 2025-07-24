---
title: Replication and Partitioning
---

Partitioning and replication are essential database concepts that help manage large data volumes, optimize performance, and ensure availibility.

## Cap Theorem
In the presence of a network partition, a distributed system can only guarantee two of the following three properties.
![](../attachments/cleanshot-2024-10-31-at-1228142x.png)
**Consistency**: Every read from the database returns the most recent write. i.e. all nodes in the system see the same data at the same time.

**Availability**: Ensures that every request (read or write) receives a response, without guaranteeing that it contains the most recent write. Prioritizes uptime and responsiveness over data accuracy.

**Partition Tolerance**: The system continues to operate despite arbitrary message loss or failure of part of the system. Crucial for distributed database systems because network failures are inevitable. (May compromise on consistency or availability)
# Partitioning
The process of dividing a database into distinct, independent parts. Each partition holds a subset of data.

## Advantages of Partitioning
- Improved query performance
	- Queries can focus on specific partitions, reducing the volume of data scanned.
- Better Resource Management
	- Load is distributed across different servers or disks, enhancing system performance.
- Increased Scalability
	- Allows horizontal scaling, letting you add storage and compute power as data grows.

## Challenges with Partitioning
- Skewed Data
	- If data isn't distributed evenly, some partitions can become "hotspots" with more load than others.
- Complexity
	- Queries and joins become more complex since data resides in separate partitions.
- Data Consistency
	- Synchronizing updates across partitions can add complexity.

# Types of Partitioning

## Range Partitioning
- Partitions data based on ranges of a key field (e.g. date, numeric range).
- Use Case: Sales data split by year or month for easy retrieval and deletion of old data.
## Hash Partitioning
- Uses a hash function on a key field to distribute data evenly across partitions.
- Use Case: Balances data evenly, especially useful when data access patterns are unpredictable.

## List Partitioning
- Divides data based on specific values of a key field.
- Use Case: Partitioning customer data by region, where each partition corresponds to a geographical area.

## Composite Partitioning
- Combines multiple partitioning strategies, such as range-hash or range-list.
- Use Case: Combines benefits of two strategies, e.g. range partitioning for dates and hash for distributing workload evenly within each date range.

# Replication
The process of copying data across multiple database instances to enhance data availability and reliability.
## Advantages of Replication
- High Availability
	- Ensures continuous data availability, especially during server failures.
- Improved Read Performance
	- Allows read operations to be distributed across multiple replicas, reducing load on the primary server.
- Data Recovery
	- Replication can act as a disaster recovery solution by maintaining up-to-date copies of data in multiple locations.

## Challenges with Replication
- Consistency
	- Keeping replicas synchronized with each other is challenging, especially with high write loads.
- Conflict Resolutions
	- Master-master setups require conflict resolution mechanisms when data changes conflict.
- Latency
	- Synchronous replication can introduce latency in applications sensitive to real-time responses.

# Types of Replication

## Master-Slave Replication
- A primary(master) database serves write request, and one or more replicas (slaves) serve read requests.
- Use Case: High-read, low-write workloads where data consistency requirements are moderate.
## Master-Master Replication
- Two or more databases can serve both read and write requests.
 - Use Case: Systems requiring high availability and where nodes are in close proximity to reduce conflict resolution issues.
## Synchronous vs. Asynchronous Replication
- Synchronous: Data changes are immediately replicated. Ensures strong consistency but has higher latency.
- Asynchronous: Data changes are eventually replicated. Has lower latency but may cause temporary inconsistencies.
- Use Case: Synchronous is used for critical applications needing immediate consistency, while asynchronous fits applications prioritizing performance over immediate consistency.
## Multi-Region Replication
- Replicates data across geographically distributed data centers.
- Use Case: Improves data access speed for globally distributed users, as they access data from the nearest data.

MYSQL Tutorial: https://www.youtube.com/watch?v=aMHQCS-WiLQ
