# Integration and Compatibility

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-07-30

----------

Azure Databricks can integrate with several other Azure services, enhancing its capabilities for data processing, analytics, and machine learning.

```mermaid
graph TD
    subgraph Azure Services
        A[Azure Data Lake Storage]
        B[Azure Synapse Analytics]
        C[Power BI]
        D[Azure Cosmos DB]
        E[Azure Data Factory]
        F[Azure Event Hubs]
        G[Azure Machine Learning]
        H[Azure SQL Database]
        I[SQL Server]
    end
    subgraph Open Source Tools
        J[Delta Lake]
        K[MLflow]
        L[Apache Spark]
    end
    M[Azure Databricks] --> A
    M --> B
    M --> C
    M --> D
    M --> E
    M --> F
    M --> G
    M --> H
    M --> I
    M --> J
    M --> K
    M --> L
```

| **Azure Service**              | **Integration Description**                                                                 |
|--------------------------------|--------------------------------------------------------------------------------------------|
| **Azure Data Lake Storage**    | Provides scalable storage for big data analytics. Azure Databricks can read and write data directly to Azure Data Lake Storage, enabling efficient data processing and storage. [Click here to understand more about how to connect](/0_Azure/1_AzureData/2_Databricks/0_Connections/0_ADLS)|
| **Azure Synapse Analytics**    | Integrates with Azure Synapse to enable advanced analytics and data warehousing solutions. This allows for seamless data movement and transformation between Databricks and Synapse. [Click here to understand more about how to connect](/0_Azure/1_AzureData/2_Databricks/0_Connections/1_Synapse)|
| **Power BI**                   | Connects with Power BI for real-time data visualization and business intelligence. Users can create interactive dashboards and reports based on data processed in Azure Databricks. |
| **Azure Cosmos DB**        | Allows for globally distributed, multi-model database integration. Azure Databricks can read from and write to Cosmos DB, enabling efficient data processing and analytics. [Click here to understand more about how to connect](#connecting-to-azure-cosmos-db)|
| **Azure Data Factory**         | Orchestrates data workflows and integrates with Azure Databricks for data movement and transformation. |
| **Azure Event Hubs**           | Ingests streaming data for real-time analytics and processing in Azure Databricks. |
| **Azure Machine Learning**     | Integrates with Azure Databricks for building, training, and deploying machine learning models. |
| **Azure SQL Database**    | Connects to Azure SQL Database for reading and writing data using JDBC or SQL connectors. [Click here to understand more about how to connect](#connecting-to-sql-databases)    |
| **SQL Server**               | Connects to SQL Server for data processing and analytics using JDBC or SQL connectors. [Click here to understand more about how to connect](#connecting-to-sql-databases)    |
