---
title: Data Warehouse
---

# What is a Data Warehouse?

**Definition:** A data warehouse is a centralized repository designed to store, integrate, and analyze large volumes of data from multiple sources.

**Purpose:** Facilitates decision-making by providing a unified view of historical and current data.

**Key Characteristics:**
- Subject-oriented
- Non-volatile
- Time-variant
- Integrated

# Why do we need data warehouses?

- **Challenges Without a Data Warehouse:**
  - Data silos and lack of integration
  - Inefficient reporting
  - Limited historical data analysis

- **Benefits:**
  - Improved decision-making
  - Centralized data for consistency
  - Efficient querying and reporting
  - Scalability for large datasets

# OLAP vs OLTP

# Online Analytical Processing (OLAP):
- **Focus:** Analytical queries and reporting  
- **Data:** Historical and aggregated  
- **Operations:** Read-heavy, complex queries
# Online Transaction Processing (OLTP):
- **Focus:** Day-to-day transactional processing
- **Data:** Current and detailed
- **Operations:** Write-heavy, simple queries
# Importance of Data Dimensionality
- Supports multi-dimensional analysis (e.g., sales by region and time).
- Enhances query performance.
- Simplifies data navigation.
## Benefits:
- Descriptive categories.
- Organize data into facts (measurable quantities) and dimensions.
- Enable intuitive and efficient data analysis.
- Dimensionality in data warehousing.
# Star Schema
- **Structure:**
  - Central fact table surrounded by multiple dimension tables.
- **Advantages:**
  - Simplified queries
  - Easy to understand and implement
- **Example:**
  - **Fact table:** Sales
  - **Dimensions:** Time, Product, Region

# Snowflake Schema
- **Structure:**
  - Dimension tables are further broken down into sub-dimensions.
- **Advantages:**
  - Reduces data redundancy
  - Saves storage space
- **Disadvantages:**
  - Increased query complexity
- **Example:**
  - Dimension "Product" split into "Category" and "Sub-category"

# ETL Processes
**Extract:** Gather data from multiple sources.  
**Transform:** Cleanse and format data.  
**Load:** Insert data into the data warehouse.  

**Importance:** Ensures data quality, consistency, and readiness for analysis.

**Data Sources:**
- Data Source A
- Data Source B
- Data Source C

**Process:**
- ETL (Extract, Transform, Load)

**Output:**
- Data Warehouse

# Tooling
- **Data Warehouse Platforms:**
  - Amazon Redshift
  - Google BigQuery
  - Snowflake
  - Microsoft Azure Synapse

- **ETL Tools:**
  - Apache NiFi
  - Talend
  - Informatica
  - Alteryx