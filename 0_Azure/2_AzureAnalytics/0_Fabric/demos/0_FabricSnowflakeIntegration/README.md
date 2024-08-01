#  Microsoft Fabric for Power BI and Azure Data Factory (ADF) with a focus on Snowflake integration 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-01

------------------------------------------

Here are some key points and new features you can highlight:

## Microsoft Fabric for Power BI
1. **Copilot Integration**: Power BI now includes Copilot, which uses generative AI to help create reports and analyze data by simply describing the insights you need.
2. **Unified Platform**: Fabric brings together Power BI, Azure Synapse, and Azure Data Factory into one unified SaaS platform, making it easier for different roles to collaborate.
3. **Enhanced Data Integration**: With Data Factory in Fabric, you can unify hybrid and multicloud data estates, combining the ease of Power Query with the power of Data Factory.
4. **New Visualization Features**: Power BI has added new formatting capabilities, including dark mode support and improved visual calculations.

## Microsoft Fabric for Azure Data Factory (ADF)
1. **Data Integration**: Fabric Data Factory offers new connectors, including those for Oracle, MySQL, Google BigQuery, and Snowflake, enhancing data integration and transformation capabilities.
2. **Simplified Data Pipelines**: The new Data Factory in Fabric integrates better with the unified data platform, including Lakehouse and Data Warehouse, making data pipelines more efficient.
3. **Real-Time Data Replication**: Mirroring in Fabric allows for near real-time replication of data from various sources into OneLake, simplifying data management and analytics.

## Impact on Snowflake Usage
1. **Mirroring**: Fabric's Mirroring feature allows you to replicate data from Snowflake into OneLake in near real-time, reducing the need for complex ETL pipelines.
2. **Unified Analytics**: With data mirrored into OneLake, you can leverage Fabric's analytics tools, such as Spark, notebooks, and Power BI, to analyze and visualize data seamlessly.
3. **Cost and Latency**: Mirroring provides a low-cost and low-latency solution for data replication, making it easier to keep your data up-to-date and accessible for analytics.

## Demo

### Requirements

| **Category** | **Requirements** |
|--------------|------------------|
| **General Requirements** | - Active Microsoft Fabric subscription  <br> - Fabric capacity (measured in Capacity Units or CUs) |
| **Data Integration Exercise** | - Permissions to access and manage Data Factory within Microsoft Fabric  <br> - Credentials and connection details for data sources (e.g., Snowflake, Oracle, MySQL)  <br> - Configuration details for the destination (e.g., Azure Data Lake, OneLake) |
| **Report Creation with Copilot** | - Permissions to access and use Power BI within Microsoft Fabric  <br> - Copilot enabled in Power BI settings  <br> - A compatible workspace with write access assigned to a Copilot-enabled capacity (F64 or higher) or a Power BI Premium capacity (P1 or higher) [1](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-create-report-service) |
| **Mirroring Setup** | - Permissions to access and manage the Fabric service within the Azure portal  <br> - Connection details for Snowflake database (e.g., account name, username, password)  <br> - Configuration details for OneLake as the destination for mirrored data  <br> - Ability to choose specific tables for mirroring and control over the initiation and suspension of mirroring processes [2](https://eng.ms/docs/cloud-ai-platform/azure-data/azure-data-intelligence-platform/synapse-dw/fabric-dw-top-level-service/trident-dw/clientexperiences/mirroring/overview) |
| **Additional Considerations** | - User permissions for accessing and managing services and resources  <br> - Compliance with organizational security and compliance policies |

### Hands-On Activities

1. **Data Integration Exercise**: Set up a data pipeline using Data Factory in Fabric to integrate data from multiple sources, including Snowflake.
3. **Report Creation with Copilot**: Use Copilot in Power BI to generate reports and visualizations based on specific business questions.
4. **Mirroring Setup**: Demonstrate how to set up Mirroring for a Snowflake database and explore the replicated data in OneLake.

| **Activity** | **Steps** |
|--------------|------------|
| **Data Integration Exercise** | 1. Access Data Factory within Fabric: <br> - Log in to the Microsoft Fabric portal. <br> - Navigate to the Data Factory service within Fabric. <br> 2. Create a New Data Pipeline: <br> - In Data Factory, click on “Author & Monitor”. <br> - Click on the “Create pipeline” button. <br> 3. Add Data Sources: <br> - Click on the “Add Source” button. <br> - Select the type of data source (e.g., Snowflake, Oracle, MySQL). <br> - Configure the connection settings for each data source (e.g., server name, database name, credentials). <br> 4. Configure Data Integration: <br> - Add activities to the pipeline to extract data from the sources. <br> - Use Data Flow to transform the data as needed. <br> - Add a sink to load the data into the desired destination (e.g., Azure Data Lake, OneLake). <br> 5. Run and Monitor the Pipeline: <br> - Save and publish the pipeline. <br> - Trigger the pipeline to run. <br> - Monitor the pipeline execution for any errors or issues. |
| **Report Creation with Copilot** | 1. Access Power BI within Fabric: <br> - Open Power BI within the Microsoft Fabric portal. <br> 2. Enable Copilot: <br> - Ensure that Copilot is enabled in your Power BI settings. <br> 3. Create a New Report: <br> - Click on “Create” and select “Report”. <br> 4. Use Copilot for Insights: <br> - In the report canvas, click on the Copilot icon. <br> - Describe the insights or visualizations you need (e.g., “Show me sales trends over the last year”). <br> - Copilot will generate the appropriate visuals and insights based on your description. <br> 5. Customize the Report: <br> - Adjust the visuals as needed (e.g., change chart types, add filters). <br> - Add additional visuals or data points to enhance the report. <br> 6. Save and Share the Report: <br> - Save the report to your workspace. <br> - Share the report with stakeholders or publish it to the Power BI Service. |
| **Mirroring Setup** | 1. **Access Fabric**: <br> - Log in to the Azure portal. <br> - Navigate to the Fabric service. <br> 2. **Set Up Mirroring**: <br> - In Fabric, go to the Mirroring section. <br> - Click on "Create Mirroring". <br> 3. **Configure Snowflake Connection**: <br> - Select Snowflake as the source. <br> - Enter the connection details for your Snowflake database (e.g., account name, username, password). <br> 4. **Select Data to Mirror**: <br> - Choose the tables or schemas you want to replicate. <br> - Configure any transformation or filtering rules if needed. <br> 5. **Configure OneLake as Destination**: <br> - Select OneLake as the destination for the mirrored data. <br> - Configure the connection settings for OneLake. <br> 6. **Start Mirroring**: <br> - Save and start the mirroring process. <br> - Monitor the mirroring status to ensure data is being replicated correctly. <br> 7. **Explore Replicated Data**: <br> - Once mirroring is complete, access OneLake. <br> - Use tools like Power BI or Azure Synapse to explore and analyze the replicated data. |

## Recommended Trainings 
- [Use Data Factory pipelines in Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/use-data-factory-pipelines-fabric/): This module covers how to describe pipeline capabilities, use the Copy Data activity, create pipelines based on predefined templates, and run and monitor pipelines.
- [Extend data insights with Copilot in Power BI](https://learn.microsoft.com/en-us/training/modules/power-bi-copilot/): This module teaches you how to create reports and summaries using Copilot in Power BI, enhancing your data interaction and report creation experience.
- [Configure a Microsoft Fabric mirrored database from Snowflake](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/snowflake-tutorial): This tutorial guides you through configuring a mirrored database from Snowflake, including setting up a secure connection, starting the mirroring process, and exploring the mirrored data in OneLake.

