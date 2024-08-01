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

<img width="700" alt="image" src="https://github.com/user-attachments/assets/f84ae4c4-22e7-44ae-9d21-fa7976e163e4">

| **Option**                | **Description**                                                                                                                                                                                                 |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dataflow Gen2**         | The new generation of dataflows in Microsoft Fabric, offering improved features like **shorter authoring flows, auto-save, background publishing, and better integration with data pipelines**. Primarily focuses on the **transformation** of data.                      |
| **Data pipeline**         | A series of processes that move data from one system to another, involving data ingestion, transformation, and storage to ensure data is ready for analysis or other uses. Manages the **movement** of data, including ingestion, transformation, and loading.                                       |
| **Data Factory**          | A cloud-based data integration service that allows you to **create, schedule, and manage data pipelines**, supporting various data sources and providing tools for data transformation and movement.                  |
| **Data workflow (Preview)** | Uses **Apache Airflow to create and manage data workflows**, providing a cloud-based platform for developing, scheduling, and monitoring data workflows, making it easier to handle complex data processes.           |
| **Copy job (Preview)**    | Automates **data loading from Amazon S3 to Amazon Redshift**, detecting new files in specified paths and loading them automatically to simplify the data ingestion process.                                          |
| **API for GraphQL (Preview)** | Allows interaction with data using GraphQL, **a query language for APIs**, enabling **efficient querying of multiple data sources** and providing a flexible way to fetch data in a single request.                     |

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

#### **Data Integration Exercise**: 

> Set up a data pipeline using Data Factory in Fabric to integrate data from multiple sources, including Snowflake

1. **Access Data Factory within Fabric**:
    - Log in to the Microsoft Fabric portal.
    - Navigate to the Data Factory service within Fabric.
      
    <img width="200" alt="image" src="https://github.com/user-attachments/assets/3b57f63c-bb09-4f11-9012-06f59dfa4893">

2. **Create a New Data Pipeline**:
    - Click on the “Create pipeline” button.
    
    <img width="400" alt="image" src="https://github.com/user-attachments/assets/52cfe364-9022-47b0-a76d-33f78d85144e">

3. **Add Data Sources**:
    - Click on the “Activity” tab.
    - Add a Copy Data activity to the pipeline.
    - Select the type of data source (e.g., Snowflake, Oracle, MySQL).
    - Configure the connection settings for each data source (e.g., server name, database name, credentials).
    
    <img width="400" alt="image" src="https://github.com/user-attachments/assets/8032577f-b415-40a9-9610-9046dbae7870">

4. **Configure Data Integration**:
    - Add a sink to load the data into the desired destination (e.g., Azure Data Lake, OneLake).
    <img width="400" alt="image" src="https://github.com/user-attachments/assets/4fbaa9dc-8cb9-4d3f-99c1-88fe309362af">

5. **Run and Monitor the Pipeline**:
    - Save and publish the pipeline.
    - Trigger the pipeline to run.
    - Monitor the pipeline execution for any errors or issues.
    

#### **Report Creation with Copilot**: 

> Use Copilot in Power BI to generate reports and visualizations based on specific business questions.

1. **Access Power BI within Fabric:**
    - Open Power BI within the Microsoft Fabric portal.
    
    <img width="200" alt="image" src="https://github.com/user-attachments/assets/6145fce7-7e4d-4ada-882f-5d842d617ca8">

2. **Enable Copilot:**
   - Ensure that Copilot is enabled in your Power BI settings:
      1. **Sign in to Microsoft Fabric** using your admin account credentials.
      2. **Navigate to the Admin Portal**:
         - Select **Fabric settings** from the menu.
         - Choose **Admin portal**.
      
      3. **Enable Copilot**:
         - In the Admin portal, select **Tenant settings**.
         - Use the search feature to locate the **Copilot and Azure OpenAI Service (preview)** settings.
         - Toggle the switch to **Enable Copilot in Fabric**.
         - Click **Apply** to save your changes.
      
      4. **Verify Access**:
         - Ensure that your workspace is in either **Premium Power BI (P1 and above)** or **paid Fabric (F64 and above)** capacity.

3. **Create a New Report:**
    - Click on “Create” and select “Report”.
    
    <img width="300" alt="image" src="https://github.com/user-attachments/assets/572bfb26-9154-4ae9-99f7-24221fb9559e">

    - Choose the source 
    
    <img width="400" alt="image" src="https://github.com/user-attachments/assets/88fb050c-3919-4fb9-b27e-df590d546ab9">

4. **Use Copilot for Insights:**
    - In the report canvas, click on the Copilot icon.
    - Describe the insights or visualizations you need (e.g., “Show me sales trends over the last year”).
    - Copilot will generate the appropriate visuals and insights based on your description.

5. **Customize the Report:**
    - Adjust the visuals as needed (e.g., change chart types, add filters).
    - Add additional visuals or data points to enhance the report.
6. **Save and Share the Report:**
   - Save the report to your workspace.
   - Share the report with stakeholders or publish it to the Power BI Service.



3. **Mirroring Setup**: Demonstrate how to set up Mirroring for a Snowflake database and explore the replicated data in OneLake.

| **Activity** | **Steps** |
|--------------|------------|
| **Mirroring Setup** | 1. **Access Fabric**: <br> - Log in to the Azure portal. <br> - Navigate to the Fabric service. <br> 2. **Set Up Mirroring**: <br> - In Fabric, go to the Mirroring section. <br> - Click on "Create Mirroring". <br> 3. **Configure Snowflake Connection**: <br> - Select Snowflake as the source. <br> - Enter the connection details for your Snowflake database (e.g., account name, username, password). <br> 4. **Select Data to Mirror**: <br> - Choose the tables or schemas you want to replicate. <br> - Configure any transformation or filtering rules if needed. <br> 5. **Configure OneLake as Destination**: <br> - Select OneLake as the destination for the mirrored data. <br> - Configure the connection settings for OneLake. <br> 6. **Start Mirroring**: <br> - Save and start the mirroring process. <br> - Monitor the mirroring status to ensure data is being replicated correctly. <br> 7. **Explore Replicated Data**: <br> - Once mirroring is complete, access OneLake. <br> - Use tools like Power BI or Azure Synapse to explore and analyze the replicated data. |

## Recommended Trainings 
- [Use Data Factory pipelines in Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/use-data-factory-pipelines-fabric/): This module covers how to describe pipeline capabilities, use the Copy Data activity, create pipelines based on predefined templates, and run and monitor pipelines.
- [Extend data insights with Copilot in Power BI](https://learn.microsoft.com/en-us/training/modules/power-bi-copilot/): This module teaches you how to create reports and summaries using Copilot in Power BI, enhancing your data interaction and report creation experience.
- [Configure a Microsoft Fabric mirrored database from Snowflake](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/snowflake-tutorial): This tutorial guides you through configuring a mirrored database from Snowflake, including setting up a secure connection, starting the mirroring process, and exploring the mirrored data in OneLake.

