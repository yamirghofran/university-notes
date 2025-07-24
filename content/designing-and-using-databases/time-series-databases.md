---
title: Time-Series Databases
---

Time-series data is a sequence of data points collected or recorded at specific time intervals. Each data point is associated with a timestamp, allowing you to analyze how values change over time:
- Stock prices.
- Weather measurements
- Sensor data
- Application logs

**High Throughput**
Time-series data often involves a high volume of incoming data points. Time-series databases are optimized for efficient write operations, enabling real-time data ingestion.

**Optimized Storage**
To handle large volumes of time-series data, these databases employ storage techniques like data **compression** and **downsampling** to minimize storage requirements while retaining the essential data points.

**Fast Query Performance**
Time-series databases are designed for quick retrieval and analysis of data over specific time ranges, making them well-suited for trend analysis and anomaly detection.

**Data Retention Policies**
They allow you to define how long data is retained, enabling automatic purging of old data that is no longer needed.

**Downsampling**
Time-series databases can automatically reduce the granularity of data as it gets older, saving storage space while preserving overall trends.

**Continuous Queries**
They support continuous or sliding window queries, enabling real-time analytics and monitoring of data streams.




1. InfluxDB
InfluxDB is an open-source time-series database designed for high write and query performance.
It is popular in IoT, monitoring, and DevOps use cases. Link
2. TimescaleDB
TimescaleDB is an extension of PostgreSQL, designed to handle both relational and time-series
data, making it a versatile choice for applications that require both types of data storage.
3. Prometheus
Prometheus is an open-source monitoring and alerting toolkit that uses a time-series database
to store and analyze metrics data.