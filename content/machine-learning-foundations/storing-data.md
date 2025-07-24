---
title: Storing Data
---

- Store data in safe an secure locations.
- Limit data access by username, ip, etc
- Limit access on per row and per column basis.
- Limit access to read-only, add-only operations, limiting write and delete permissions.
- Consider encryption.
# Data Formats
- Dictionaries or gazetteers
- Table in a relational database
- Key-value
- Structured text file.

- CSV
- TSV
- XML
- JSON
# Data Storage
- Filesystem
- Object Storage
- Database
# Data Versioning
- Level 0: unversioned
- Level 1: versioned as a snapshot at training time
- Level 2: both data and code are versioned as one asset
- Level 3: using or building a specialized data versioning solution

Level 2 is recommended.

# Documentation & Metadata
- What the data means
- How it was collected, or methods used to create it (instructions to labelers and methods for quality control)
- Details of train-validation-test splits
- Details of all pre-processing steps
- Explanation of any data that was excluded
- What format is used to store the data
- Types of attributes or features (which values are allowed for each attribute or feature)
- number of examples
- possible values for labels or the allowable range for a numerical target.
# Data Lifecycle
Include a **data lifecycle document** for every sensitive data asset to describe the asset, circle of people who have permission, how long/whether it has to be destroyed.