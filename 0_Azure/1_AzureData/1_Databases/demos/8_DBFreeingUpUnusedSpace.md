# Optimizing Database Performance by Freeing Up Unused Space 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-12-16

----------

> Microsoft offers a variety of database solutions, both relational and non-relational. Quick overview about strategies for managing and reducing their size, ensuring optimal performance and efficient use of storage resources. It's essential to `follow best practices and monitor the operation to avoid potential issues like long-running commands or blocking sessions`.

## Wiki 

<details>
<summary><b>Table of Wiki </b> (Click to expand)</summary>

- [Shrink a database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/shrink-a-database?view=sql-server-ver16)
- [Types of Databases](https://azure.microsoft.com/en-gb/products/category/databases/)
- [Shrink Database Task (Maintenance Plan)](https://learn.microsoft.com/en-us/sql/relational-databases/maintenance-plans/shrink-database-task-maintenance-plan?view=sql-server-ver16)

</details>

## Overview 

General Strategies for All Databases:

- **Archiving Old Data**: Move old or rarely accessed data to an archive database or storage solution. Reduces the size of the active database, improving performance and manageability. `Use SQL Server's built-in tools or third-party solutions to archive data based on specific criteria (e.g., date, usage).`
- **Data Compression**: Apply data compression techniques to reduce storage space.
- **Partitioning Tables**: Split large tables into smaller, more manageable pieces.
- **Index Optimization**: Regularly rebuild or reorganize indexes to reduce fragmentation.
- **Removing Unused Indexes**: Identify and remove indexes that are not being used.
- **Cleaning Up Unused Data**: Regularly delete or archive unused or obsolete data.
- **Monitoring and Maintenance**: Regularly monitor database size and performance, and perform maintenance tasks.
- **Using Filegroups**: Distribute database objects across multiple filegroups to improve performance and manageability.

## Relational Databases



| **Database Type** | **Strategies** | **Commands and Steps** |
|-------------------|----------------|------------------------|
| **Azure SQL Database** | - **Shrinking the Database**: Use `DBCC SHRINKDATABASE` <br/> - **Data Compression**: Apply `PAGE` or `ROW` compression <br/> - **Index Optimization**: Regularly rebuild or reorganize indexes <br/> - **Partitioning Tables**: Split large tables into partitions | - **Shrinking the Database**: <br/> ```DBCC SHRINKDATABASE (YourDatabaseName, 10);``` <br/> - **Data Compression**: <br/> ```ALTER TABLE YourTableName REBUILD WITH (DATA_COMPRESSION = PAGE);``` <br/> - **Index Optimization**: <br/> ```ALTER INDEX ALL ON YourTableName REBUILD;``` <br/> - **Partitioning Tables**: <br/> ```CREATE PARTITION FUNCTION MyPartitionFunction (datetime) AS RANGE LEFT FOR VALUES ('2023-01-01', '2024-01-01');``` |
| **Azure SQL Managed Instance** | - **Shrinking the Database**: Use `DBCC SHRINKDATABASE` <br/> - **Archiving Old Data**: Move old data to an archive database <br/> - **Removing Unused Indexes**: Identify and remove unused indexes <br/> - **Using Filegroups**: Distribute objects across multiple filegroups | - **Shrinking the Database**: <br/> ```DBCC SHRINKDATABASE (YourDatabaseName, 10);``` <br/> - **Archiving Old Data**: Use SQL Server's built-in tools or third-party solutions <br/> - **Removing Unused Indexes**: <br/> ```SELECT * FROM sys.dm_db_index_usage_stats WHERE user_seeks = 0 AND user_scans = 0 AND user_lookups = 0;``` <br/> - **Using Filegroups**: <br/> ```CREATE TABLE YourTableName (...) ON [PrimaryFileGroup];``` |
| **SQL Server on Azure Virtual Machines** | - **Cleaning Up Unused Data**: Regularly delete or archive obsolete data <br/> - **Monitoring and Maintenance**: Use built-in monitoring tools and maintenance plans <br/> - **Data Compression**: Apply compression techniques to tables and indexes | - **Cleaning Up Unused Data**: Implement regular maintenance tasks <br/> - **Monitoring and Maintenance**: Use SQL Server Management Studio (SSMS) or Azure Monitor <br/> - **Data Compression**: <br/> ```ALTER TABLE YourTableName REBUILD WITH (DATA_COMPRESSION = PAGE);``` |
| **Azure Database for PostgreSQL** | - **Partitioning Tables**: Use PostgreSQL's native partitioning features <br/> - **Index Optimization**: Regularly rebuild or reorganize indexes <br/> - **Archiving Old Data**: Move old data to an archive database | - **Partitioning Tables**: <br/> ```CREATE TABLE measurement_y2023m01 PARTITION OF measurement FOR VALUES FROM ('2023-01-01') TO ('2023-02-01');``` <br/> - **Index Optimization**: <br/> ```REINDEX TABLE YourTableName;``` <br/> - **Archiving Old Data**: Use PostgreSQL's built-in tools or third-party solutions |
| **Azure Database for MySQL** | - **Data Compression**: Use MySQL's compression features <br/> - **Index Optimization**: Regularly rebuild or reorganize indexes <br/> - **Cleaning Up Unused Data**: Regularly delete or archive obsolete data | - **Data Compression**: <br/> ```ALTER TABLE YourTableName ROW_FORMAT=COMPRESSED;``` <br/> - **Index Optimization**: <br/> ```OPTIMIZE TABLE YourTableName;``` <br/> - **Cleaning Up Unused Data**: Implement regular maintenance tasks |

## Non-Relational Databases

1. **Azure Cosmos DB**: A globally distributed, multi-model database service.

      > **Strategies**:

     - **Partitioning**: Use automatic partitioning to manage large datasets. Cosmos DB automatically partitions data based on the partition key you define. Ensure your partition key is chosen to evenly distribute data.
     - **Index Optimization**: Customize indexing policies to optimize performance. Customize indexing policies using the Azure Portal or SDK. Example:
       ```json
       {
         "indexingMode": "consistent",
         "automatic": true,
         "includedPaths": [
           { "path": "/*" }
         ],
         "excludedPaths": [
           { "path": "/\"_etag\"/?" }
         ]
       }
       ```
     - **Archiving Old Data**: Move old data to an archive database. Use Azure Data Factory to move old data to an archive storage solution.

2. **Azure Managed Instance for Apache Cassandra**: A managed instance of Apache Cassandra.

      > **Strategies**:
      
      - **Data Compression**: Use Cassandra's compression features. Enable compression on tables:
        ```sql
        CREATE TABLE my_table (id UUID PRIMARY KEY, data TEXT) WITH compression = {'class': 'LZ4Compressor'};
        ```
      - **Index Optimization**: Regularly rebuild or reorganize indexes. Rebuild indexes periodically:
        ```sql
        REBUILD INDEX my_index;
        ```
      - **Cleaning Up Unused Data**: Regularly delete or archive obsolete data. Use TTL (Time to Live) to automatically delete old data.
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

3. **Azure Cache for Redis**: An in-memory data store for caching and real-time analytics.

     > **Strategies**:

     - **Data Eviction Policies**: Use eviction policies to manage memory usage. Configure eviction policies in Redis configuration:
       ```
       maxmemory-policy allkeys-lru
       ```
     - **Monitoring and Maintenance**: Regularly monitor and maintain cache performance. Use Azure Monitor to set up alerts and monitor performance metrics. Example:
       ```
       az monitor metrics alert create --name "HighMemoryUsage" --resource-group "MyResourceGroup" --scopes "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Cache/Redis/{cache-name}" --condition "avg memory_usage_percentage > 80" --description "Alert when memory usage exceeds 80%"
       ```


