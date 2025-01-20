# Azure Cosmos DB: Freeing Up Unused Space - Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-19

----------

A globally distributed, multi-model database service.

## Content 

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>

- [Content](#content)
- [Partitioning](#partitioning)
- [Index Optimization](#index-optimization)
- [Archiving Old Data](#archiving-old-data)

</details>

## Partitioning

> Use automatic partitioning to manage large datasets. Cosmos DB automatically partitions data based on the partition key you define. Ensure your partition key is chosen to evenly distribute data.

## Index Optimization

> Customize indexing policies to optimize performance. Customize indexing policies using the Azure Portal or SDK. Example:

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

## Archiving Old Data

> Move old data to an archive database. Use Azure Data Factory to move old data to an archive storage solution.


<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
