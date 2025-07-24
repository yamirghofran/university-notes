---
title: SQLite
---

- Lightweight, serverless SQL database engine.
- Self-contained and zero configuration.
- A single .sqlite or .db file contains the entire database.
- No dedicated server process required.

# Why use SQLite?

- **Use Cases**
  - Mobile apps (e.g., Android, iOS).
  - IoT devices.
  - Embedded systems.
  - Testing and prototyping.
  - Websites with low concurrent usage.

- **Advantages**
  - Simple setup and portability.
  - Fast and efficient for read-heavy applications.
  - ACID-compliant.

# Limitations

- Not suitable for:
  - High-concurrency applications.
  - Complex queries with heavy workloads.
- Limited to single write operations at a time.
- No built-in user management or advanced security.

# Scale Database Structure

- Cross-platform compatibility.
- Application metadata.
- Tables, indices, triggers, views.
- File includes.
- Enrite database in one file.

# Accessing files

- Open SQLite databases using:
  - SQLite CLI.
  - GUI tools like DB Browser for SQLite.
  - Programmatic access (e.g., Python, Java).

- Filesystem-level details:
  - .sqlite files are binary files.
  - Portable across systems.

# Storage classes

- **NULL**: Represents missing values.
- **INTEGER**: Signed integers (1, 2, 4, 8 bytes).
- **REAL**: Floating-point values (8 bytes).
- **TEXT**: Strings, encoded in UTF-8, UTF-16BE, or UTF-16LE.
- **BLOB**: Binary Large Objects, stored as-is.

# Type Affinity

Columns have type affinities, not strict types.  
**Affinity Categories:**  
- **TEXT:** Converts to text.  
- **NUMERIC:** Converts to number.  
- **INTEGER:** Prefers integers.  
- **REAL:** Prefers floating-point.  
- **NONE:** No affinity.

# SQLite Architecture Overview

- **Frontend:**  
  - Receives SQL queries.
- **Parser and Code Generator:**  
  - Converts SQL into bytecode.

- **Virtual Database Engine (VDBE):**  
  - Executes bytecode.

- **B-Tree:**  
  - Organizes data.

- **Pager:**  
  - Manages reading and writing to the database file.

# Concurrency in SQLite

- **Modes:**
  - SHARED: Multiple readers.
  - EXCLUSIVE: Single writer.

- **Write-Ahead Logging (WAL):**
  - Improves concurrent reads.
  - Enables multiple readers and one writer.

- **Best Practice:** Minimize write locks to enhance performance.