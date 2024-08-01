# Microsoft Fabric 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-01

----------

Microsoft Fabric is an end-to-end analytics and data platform designed for enterprises that require a unified solution. It's built on a foundation of `Software as a Service (SaaS)` and `combines both new and existing components from Power BI, Azure Synapse Analytics, Azure Data Factory, and more services into a unified environment`.

> Microsoft Fabric covers Azure Data and Azure Analytics: <br/>
> `Azure Data`: Fabric integrates data engineering and data management tools. <br/>
> `Azure Analytics`: It includes business intelligence and analytics tools, especially with its integration with Power BI.

## Wiki 

<details>
  <summary>Click here to display </summary>
  <ul>
    <li><a href="https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview">What is Microsoft Fabric</a></li>
    <li><a href="https://www.microsoft.com/en-us/microsoft-fabric">Data Analytics</a></li>
    <li><a href="https://www.bing.com/videos/riverview/relatedvideo?q=microsoft+fabric+what+is&mid=17839F76B326A15F559417839F76B326A15F5594&FORM=VIRE">MS Fabric Public Preview - Video</a></li>
    <li><a href="https://atlan.com/microsoft-fabric/">What is Microsoft Fabric?: Features, Architecture & FAQs</a></li>
    <li><a href="https://github.com/MicrosoftDocs/fabric-docs/blob/main/docs/get-started/microsoft-fabric-overview.md">Microsoft Open Source Code of Conduct</a></li>
    <li><a href="https://learn.microsoft.com/en-us/fabric/get-started/end-to-end-tutorials">End-to-end tutorials in Microsoft Fabric</a></li>
    <li><a href="https://learn.microsoft.com/en-us/fabric/onelake/onelake-shortcuts">OneLake shortcuts</a></li>
    <li><a href="https://learn.microsoft.com/en-us/fabric/onelake/create-on-premises-shortcut">Create shortcuts to on-premises data</a></li>
    <li><a href="https://support.fabric.microsoft.com/en-US/blog/public-preview-of-onelake-shortcuts-to-s3-compatible-data-sources/">Public Preview of OneLake shortcuts to S3-compatible data sources</a></li>
    <li><a href="https://learn.microsoft.com/en-us/fabric/onelake/create-s3-compatible-shortcut">Create an Amazon S3 compatible shortcut</a></li>
    <li><a href="https://learn.microsoft.com/en-us/fabric/database/mirrored-database/overview">What is Mirroring in Fabric?</a></li>
    <li><a href="https://support.fabric.microsoft.com/en-us/blog/announcing-the-public-preview-of-database-mirroring-in-microsoft-fabric?ft=Roadmap:category">Announcing the Public Preview of Mirroring in Microsoft Fabric</a></li>
    <li><a href="https://support.fabric.microsoft.com/en/blog/introducing-mirroring-in-microsoft-fabric?ft=All">Introducing Mirroring in Microsoft Fabric</a></li>
    <li><a href="https://learn.microsoft.com/en-us/fabric/database/mirrored-database/azure-sql-database">Mirroring Azure SQL Database (Preview)</a></li>
  </ul>
</details>


- [What is the difference between Real-Time Intelligence and comparable Azure solutions?](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/real-time-intelligence-compare)
<img width="700" alt="image" src="https://github.com/user-attachments/assets/a26c562f-373a-4df5-a334-447c42acbdaf">

- [Process Azure Event Hubs data using Azure Data Factory Mapping Data Flows](https://medium.com/microsoftazure/process-azure-event-hubs-data-using-azure-data-factory-mapping-data-flows-c62ee157582b)

<img width="700" alt="image" src="https://github.com/user-attachments/assets/fcd6e652-2de5-4f62-849f-a6e734508710">



## Key Components

- **Data Engineering, Data Factory, Data Science, Real-Time Analytics, Data Warehouse, and Databases**: These are the key services offered by Microsoft Fabric.
- **OneLake**: This is the unification of lakehouses.
- **Real-Time hub**: This is the unification of data streams.

<img width="709" alt="image" src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/c2c78b3f-7d92-4cef-91b4-54c281c40fd9">

> Before Fabric

<p float="left">
  <img src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/c47ad7c0-375e-4257-b56e-7b3b89619e2f" width="450" height="200" />
  <img src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/64812721-7c24-4771-90f4-27f7a21fa9e0" width="350" height="200" />
</p>

## Features

- **Unification with SaaS foundation**: Fabric integrates workloads such as Data Engineering, Data Factory, Data Science, Data Warehouse, Real-Time Intelligence, Industry solutions, and Power BI into a shared SaaS foundation.
- **AI Integration**: The entire Fabric stack has AI integration and it accelerates the data journey.
- **Unified Management and Governance**: Fabric seamlessly integrates data and services, enabling unified management, governance, and discovery.
- **Security**: It ensures security for items, data, and row-level access.

<img width="709" alt="image" src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/f75bfae7-91af-4f4d-9ca7-8e9c625c4b93">

> OneLake allows storage of delta parquet files, which can be read and worked with throughout all workloads. It's a single, unified, logical data lake for the whole organization. Like OneDrive, OneLake comes automatically with every Microsoft Fabric tenant and is designed to be the single place for all your analytics data.

<p float="left">
  <img src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/8566f641-277b-4746-826a-efc0bcd73d5a" width="450" height="300" />
  <img src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/54455481-fc87-40c2-b6ce-88895429257c" width="350" height="300" />
</p>


<img width="709" alt="image" src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/4d9d5e6d-ff9c-4f21-954e-61f644c750bd">

## Shortcuts & Mirroring

| **Feature** | **Shortcuts** | **Mirroring** |
|-------------|---------------|---------------|
| **Definition** | Objects that point to other storage locations, either internal or external to OneLake. | A data replication solution that continuously replicates data from various sources into OneLake. |
| **Purpose** | To unify data across different domains, clouds, and accounts by creating a single virtual data lake. | To bring data from different systems together into a single analytics platform, ensuring data is up-to-date and readily available for analysis. |
| **Data Movement** | No data is copied or moved. Shortcuts link directly to the source data. | Data is copied and stored in OneLake, providing a low-latency and centralized data management solution. |
| **Usage** | Shortcuts appear as folders in OneLake and can be used by any service or workload that has access to OneLake. | Mirrored data can be accessed and analyzed using various tools within Microsoft Fabric, such as Power BI and Azure Synapse. |
| **Benefits** | - Reduces data duplication. <br> - Enhances accessibility by providing a unified view of data. <br> - Simplifies data management by abstracting the data retrieval process. | - Provides real-time data replication. <br> - Ensures data consistency and availability. <br> - Simplifies the process of keeping data synchronized across different systems. |
| **Key Differences** | - No data movement. <br> - Live access to external data sources. <br> - Ideal for accessing data across multiple locations without duplication. | - Data is physically replicated. <br> - Access to a centralized, up-to-date copy of data. <br> - Suitable for centralized analysis and ensuring data consistency. |
| **Compatible Products** | - Azure Data Lake Storage (ADLS) Gen2 <br> - Amazon S3 <br> - Google Cloud Storage <br> - Dataverse <br> - On-premises data sources via Fabric on-premises data gateway | - Azure SQL Database <br> - Azure Cosmos DB <br> - Snowflake |





## Recommended Trainings 

- [Get started with Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/)

