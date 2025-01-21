# Azure Database for MySQL: Freeing Up Unused Space - Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-19

----------

To optimize Azure Database for MySQL, you can:

## Content 

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>

- [Content](#content)
- [Data Compression](#data-compression)
- [Index Optimization](#index-optimization)
- [Cleaning Up Unused Data](#cleaning-up-unused-data)

</details>

## Data Compression

> Use MySQL's compression features to save space:

 ```sql
 ALTER TABLE YourTableName ROW_FORMAT=COMPRESSED;
 ```

## Index Optimization

> Regularly rebuild or reorganize indexes to keep the database performing well:

```sql
OPTIMIZE TABLE YourTableName;
```

## Cleaning Up Unused Data

> Regularly delete or archive obsolete data to maintain database efficiency.

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
