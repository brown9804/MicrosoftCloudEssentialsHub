# Azure Managed Instance for Apache Cassandra: Freeing Up Unused Space - Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-19

----------

A managed instance of Apache Cassandra.

## Content 

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>

- [Content](#content)
- [Data Compression](#data-compression)
- [Index Optimization](#index-optimization)
- [Cleaning Up Unused Data](#cleaning-up-unused-data)

</details>


## Data Compression

> Use Cassandra's compression features. Enable compression on tables:

```sql
CREATE TABLE my_table (id UUID PRIMARY KEY, data TEXT) WITH compression = {'class': 'LZ4Compressor'};
```

## Index Optimization

> Regularly rebuild or reorganize indexes. Rebuild indexes periodically

```sql
REBUILD INDEX my_index;
```

## Cleaning Up Unused Data

> Regularly delete or archive obsolete data. Use TTL (Time to Live) to automatically delete old data.

```sql
CREATE TABLE my_table (id UUID PRIMARY KEY, data TEXT) WITH default_time_to_live = 86400;
```

The value 86400 in the context of the default_time_to_live setting for Apache Cassandra represents the Time to Live (TTL) for data in seconds. Specifically, 86400 seconds is equivalent to 24 hours (1 day). This means that any data inserted into the table will automatically be deleted after 24 hours.

```
86400 seconds = 24 hours = 1 day
```

> So, when you set default_time_to_live = 86400, it ensures that data in the table will expire and be removed after one day. If you want to set a different TTL, you can adjust this value accordingly. For example:

```
3600 seconds = 1 hour
604800 seconds = 7 days (1 week)
```

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
