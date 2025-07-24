---
title: Spark
---

Apache Spark is an open-source, distributed computing system designed for
large-scale data processing and analytics. It provides a fast and general-purpose
cluster computing framework for big data processing tasks. Spark was
developed to overcome the limitations of the traditional MapReduce model by
introducing in-memory processing and a more flexible and user-friendly
programming model.

# Components
## Driver
The driver is the central control node in a Spark application.
It is responsible for coordinating the execution of tasks across the worker nodes.
When you run a Spark application, the Driver program is the entry point to your application.

## Workers
Workers are the computing nodes in a Spark cluster.
They are responsible for executing tasks assigned to them by the Driver.
Each worker runs on a separate node in the cluster and performs computations on the data stored in its local memory.

## Context
When the Driver program starts, it creates SparkContext. The SparkContext is the entry point to any Spark functionality in your application.

The SparkContext is responsible for coordinating with the Cluster Manager to acquire resources (CPU, memory) from the cluster for the application.

## Cluster Manager
The Cluster Manager is responsible for managing and allocating resources across the worker nodes in the Spark cluster.

It is a separate component that handles the distribution of tasks and resources based on the application's requirements.

Examples: Apache Mesos, Hadoop Yarn, and Kubernetes.

# Operations (Transformations and Actions)
Spark applications consist of a series of operations that are categorized into transformations and actions.

## Transformations
Operations that create a new RDD (Resilient Distributed Dataset) from an existing one. E.g. map, filter, and reduceByKey.

## Actions
Operations that return a value to the Driver program or write data to an external storage system. Examples include count, collect, and SaveAsTextFile.

The Driver program defines these operations, and they are executed on the worker nodes.


Spark functionality: Graph, SQL, AI, Streaming

# How It Works
- Application Start
	- The Spark application begins with the execution of the Driver program.
	- The Driver creates a SparkContext, chich establishes communication with the Cluster Manager.
- Resource Allocation
	- The SparkContext communicates with the Cluster Manager to request resources for the application. This includes CPU cores and memory on the worker nodes.
- Task Distribution
	- The Driver breaks down the application into tasks and sends them to the Worker nodes.
	- Tasks are distributed to Workers based on the data locality, minimizing data transfer over the network.
- Task Execution
	- Workers execute the assigned tasks concurrently on their local data partitions.
	- The operations (transformations and actions) are performed on the distributed data in parallel.
- Result Aggregation
	- The results of the tasks are aggregated, and the final result is returned to the Driver program.
	- Actions trigger the actual computation, and the results may be collected to the Driver or stored in an external system.
- Resource Deallocation
	- Once the application completes, the SparkContext communicates with the Cluster Manager to release the allocated resources.

# Spark Core
The foundational component of Apache Spark.
Responsible for essential functionalities like task scheduling, memory management, and fault recovery.

## Resilient Distributed Datasets
Fundamental data structure in Spark.
Immutable, distributed collections of objects that can be processed in parallel.
Provide fault tolerance through lineage information, enabling the recovery of lost data.

## Distributed Task Execution
Spark allows the parallel execution of tasks across a cluster of machines.
Tasks are divided into stages, and stages are divided into tasks that can be executed in parallel.

## Key Components
### Memory Management
Utilizes in-memory processing for intermediate data storage, making it faster than traditional disk-based processing.

### Fault Recovery
RDDs facilitate fault recovery by allowing recomputation of last data from their creation lineage. If a node fails, Spark can recompute the lost partitions on other nodes.

### Cluster Manager Integration
Can integrate with various cluster managers like Apache Mesos, Hadoop YARN, and Kubernetes for resource allocation and management.


# Spark SQL
Enables the integration of structured data processing with Spark. Allows users to query structured data using SQL commands.

## Key Features
### DataFrame API
Represents a distributed collection of data organized into named columns.
Allows users to perform relational operations on both external data sources and Spark's built-in distributed collections.

### Structured Data Support
Spark SQL supports various data formats, including JSON, Parquet, Avro, and more.
Can read data from existing Hive installations.

### Unified Data Processing
Allows users to seamlessly mix SQL queries with Spark programs. Supports both batch and real-time processing.

# Spark Streaming
Enables real-time data processing and analytics. Useful for applications like fraud detection, monitoring, and live dashboards.

## Key Features
### Micro-Batch Processing
- Process data in small, user-defined batches.
- Enables near-real-time data processing with low-latency.
### Data Sources
- Supports a wide range of data sources, including HDFS, Kafka, Flume, and more.
- Can integrate with other Spark components for comprehensive data processing.
### Windowed Operations
- Supports windowed operations for processing data within specified time windows.
- Useful for tasks like fraud detection, monitoring, and analytics.

# MLib (Machine Learning Library)
A scalable machine learning library for Spark.
Provides algorithms for classification, regression, clustering, and collaborative filtering.

## Key Features
### Distributed Algorithms
- MLib algorithms are designed to work in a distributed environment.
- Enables processing large-scale datasets for machine learning tasks.
### High-Level APIs
- MLib provides high-level APIs in Java, Scala, Python, and R.
- Allows users to build and deploy machine learning models using familiar programming languages.
### Integration with Spark Ecosystem
- MLib seamlessly integrates with other Spark components for end-to-end machine learning workflows.

# Graph X
A graph processing framework built on top of Spark. Facilitates the analysis of graph-structured data.

## Key Features
## Graph Computation
- Allows users to express graph computation using a Pregel API.
- Supports iterative graph computation for algorithms like PageRank and connected components.
## Resilient Graphs
- GraphX graphs are fault-tolerant and can be recovered in the event of node failures.
## Graph Analytics
- Useful for analyzing relationships and patterns in data represented as graphs.

# Spark R
Allows R users to leverage Spark's capabilities. Enables distributed data analysis using R.
## Key Features
### R Language Integration
- Enables R users to interact with Spark data structures and algorithms.
- Provides a distributed dataframe implementation for parallel data processing.
### DataFrame Operations
- SparkR supports DataFrame operations similar to those in SparkSQL.
-  Allows users to perform data manipulations and analysis using R.

# Spark Most Common Functions
```python
df.select("col1", "col2")
df.filter(col("age") > 21)
df.groupBy("department").agg({"salary": "avg"})
df.orderBy("age")
df.withColumn("age_squared", col("age")**2)
df.select(col("age").alias("employee_age"))
df.select("department").distinct()
df1.join(df2, df1["key"] == df2["key"])
df.groupBy("department").pivot("month").agg({"sales": "sum"})
```