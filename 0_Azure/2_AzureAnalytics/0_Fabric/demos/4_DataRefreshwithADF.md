# Setting Up SQLDB Data Refresh and Publishing Pipelines with Azure Data Factory in Microsoft Fabric

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-27

----------

> Here is a small guide on how to set up a refresh with Azure Data Factory (ADF) in Microsoft Fabric, publish the data pipeline, and update the gateway.

## Wiki 

- [How to ingest data into Fabric using the Azure Data Factory Copy activity](https://learn.microsoft.com/en-us/fabric/data-factory/how-to-ingest-data-into-fabric-from-azure-data-factory)
- [On-premises data gateway FAQ](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem-faq)
- [Fabric Data Factory Pipeline: Incremental load](https://community.fabric.microsoft.com/t5/Data-Pipelines/Fabric-Data-Factory-Pipeline-Incremental-load/m-p/3262598)
- [Semantic model refresh activity in Data Factory for Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/semantic-model-refresh-activity)
- [What is an on-premises data gateway?](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem)
- [Example of script to update gateway PowerShell](https://github.com/Azure/Azure-DataFactory/blob/main/SamplesV2/SelfHostedIntegrationRuntime/AutomationScripts/script-update-gateway.ps1)
- [Public Preview: Azure SQL Database Mirroring in Microsoft Fabric](https://azure.microsoft.com/en-us/updates/public-preview-azure-sql-database-mirroring-in-microsoft-fabric/)
- [Mirroring Azure SQL Database (Preview)](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/azure-sql-database)
- [Announcing the Public Preview of Mirroring in Microsoft Fabric](https://blog.fabric.microsoft.com/en-us/blog/announcing-the-public-preview-of-database-mirroring-in-microsoft-fabric?ft=All)
- [Announcing Mirroring Azure SQL Database in Fabric for Public Preview](https://techcommunity.microsoft.com/t5/azure-sql-blog/announcing-mirroring-azure-sql-database-in-fabric-for-public/ba-p/4085988)

## How to set up

### General Steps

1. **Access Data Factory within Fabric**:
    - Log in to the Microsoft Fabric portal.
    - Navigate to the Data Factory service within Fabric.
      
      <img width="200" alt="image" src="https://github.com/user-attachments/assets/3b57f63c-bb09-4f11-9012-06f59dfa4893">

2. **Create a New Data Pipeline**:
    - Click on the “Create pipeline” button.
    
      <img width="400" alt="image" src="https://github.com/user-attachments/assets/52cfe364-9022-47b0-a76d-33f78d85144e">
    
    - Add activities to your pipeline, such as **Copy Data** or **Data Flow** activities, to define the data transformation and movement.

### Steps for Public Network

3. **Configure the Desired Connector**:
    - Use the desired connector to read from and write to your data sources.
    - Set up authentication using a service principal (SPN) or app registration.
4. **Schedule the Refresh**:
    - In your workspace, select the **Schedule Refresh** icon.
    - Turn on the scheduled refresh and configure the refresh times.
5. **Validate and Debug**:
    - Validate your pipeline to ensure there are no errors.
    - Use the **Debug** option to test the pipeline.
6. **Publish the Pipeline**:
    - Once validated, click on **Publish All** to publish your pipeline.
    - This will deploy the pipeline and make it available for execution.

### Steps for Private Network

3. **Set Up a Self-hosted Integration Runtime**:
    - Install the integration runtime on a machine within your network that has access to the SQL Server.
4. **Create Linked Services**:
    - In Azure Data Factory, create linked services for both your source (SQL Server) and destination (e.g., Azure Blob Storage, Azure SQL Database). Use the self-hosted integration runtime for the SQL Server connection.
5. **Define Datasets**:
    - Create datasets for the source and destination data.
6. **Create Pipelines**:
    - Build pipelines in Azure Data Factory to orchestrate the data movement and transformation.
7. **Schedule the Refresh**:
    - Configure the refresh schedule in your workspace.
8. **Validate and Debug**:
    - Validate your pipeline and use the debug option to test it.
9. **Publish the Pipeline**:
    - Publish your pipeline to make it available for execution.

## Mirroring SQL Database in Microsoft Fabric

> Mirroring for Azure SQL Database is now available in public preview. This feature allows you to replicate your data residing in Azure SQL databases in near real-time directly into Microsoft Fabric's OneLake. However, it currently does not support Azure SQL Database instances behind a private network. You must update your Azure SQL logical server firewall rules to allow public network access to use this feature.

### Alternatives for Near Real-Time Data

If you need near real-time data from SQLDB and your SQL Server is in a private network, consider the following alternatives:

1. **Change Data Capture (CDC)** is a feature that captures changes made to data in your SQL Server tables. It records insert, update, and delete activities and makes the change data available for downstream processing.
    - **How it works**: CDC captures changes from the transaction log and stores them in change tables. These changes can then be processed and replicated to other systems.
    - **Use case**: Ideal for scenarios where you need to track and replicate changes in near real-time without impacting the performance of your primary database.
2. **Azure Data Factory with Self-hosted Integration Runtime**: Allows you to securely connect to your on-premises SQL Server and replicate data to Azure services.
    - **How it works**: Install the self-hosted integration runtime on a machine within your network. Create pipelines in ADF to copy data from SQL Server to your destination (e.g., Azure Blob Storage, Azure SQL Database).
    - **Use case**: Suitable for environments where the SQL Server is behind a private network and you need to orchestrate complex data workflows.
3. **Azure Event Hubs**: Is a big data streaming platform and event ingestion service capable of receiving and processing millions of events per second.
    - **How it works**: Use CDC or other mechanisms to capture changes and send them to Event Hubs. From there, you can stream the data to Azure Synapse Analytics or Azure Data Lake Storage for processing.
    - **Use case**: Best for scenarios requiring high-throughput data ingestion and real-time analytics.
4. **Azure Synapse Analytics**: Integrates big data and data warehousing capabilities, allowing you to analyze large volumes of data in near real-time.
    - **How it works**: Use Synapse pipelines to orchestrate data movement and transformation. Stream data from Event Hubs or other sources into Synapse for real-time processing.
    - **Use case**: Ideal for complex analytics and reporting on large datasets.

### Architecture References
1. [Near Real-Time Lakehouse Data Processing](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/data/real-time-lakehouse-data-processing): This architecture uses Azure Event Hubs, Azure Synapse Analytics, and Azure Data Lake Storage to keep lakehouse data in sync in near real-time. It involves capturing changes using Debezium connectors, streaming data to Event Hubs, and processing it in Synapse Analytics.
2. [Mirroring Azure SQL Database in Microsoft Fabric](https://www.mssqltips.com/sqlservertip/8001/microsoft-fabric-mirroring-for-data-replication/): Mirroring in Microsoft Fabric allows for near real-time replication of Azure SQL Database into Fabric's OneLake. This feature leverages SQL's CDC stack to keep data in sync without complex ETL processes. For more [click here](https://techcommunity.microsoft.com/t5/azure-sql-blog/announcing-mirroring-azure-sql-database-in-fabric-for-public/ba-p/4085988).
3. [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-sql-database-well-architected-framework): This framework provides best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud. It includes guidance on using Active Geo-Replication and Auto Failover Groups for high availability and disaster recovery.

## Update the Gateway

1. **Check Gateway Version**:
   - Ensure your on-premises data gateway is up to date. Microsoft supports only the last six releases.
2. **Update the Gateway**:
   - Download the latest gateway version, click [here](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-install#download-and-install-a-standard-gateway) to understand more.
   - Install the update using the provided script or manually.

3. **Configure the Gateway**:
   - Ensure the gateway is properly configured to connect to your data sources.
   - Verify the gateway settings in the Azure Data Factory portal.

> **Monitor and Manage**: Regularly monitor the pipeline runs and gateway status to ensure everything is functioning smoothly.
