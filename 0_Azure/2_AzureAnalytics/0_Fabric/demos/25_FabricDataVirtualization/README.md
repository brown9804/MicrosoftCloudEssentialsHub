# Fabric: Data Virtualization Capabilities

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-12-30

----------

Data Virtualization can be leveraged either through a dedicated tool or an integrated approach:

> `Dedicated Tool`: Traditional data virtualization tools (e.g., Denodo, Informatica, etc) are specifically designed for data virtualization. <br/>
> `Integrated Approach`: Microsoft Fabric provides data virtualization capabilities by integrating a range of services, each specializing in areas such as data integration (Azure Data Factory), storage (Data Lake Storage), querying (Azure Synapse Analytics), and visualization (Power Bi).

## Wiki 

<details>
<summary><b>Table of Wiki </b> (Click to expand)</summary>

- [What is Microsoft Fabric?](https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview)
- [Introducing Microsoft Fabric: Data analytics for the era of AI](https://azure.microsoft.com/en-us/blog/introducing-microsoft-fabric-data-analytics-for-the-era-of-ai/)
- [Step-by-Step Tutorial: Building ETLs with Microsoft Fabric](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/step-by-step-tutorial-building-etls-with-microsoft-fabric/3885183)
- [What is Data Science in Microsoft Fabric?](https://learn.microsoft.com/en-us/fabric/data-science/data-science-overview)
- [Microsoft Fabric security white paper](https://learn.microsoft.com/en-us/fabric/security/white-paper-landing-page)
- [Microsoft Fabric security white paper - Git repo](https://github.com/MicrosoftDocs/fabric-docs/blob/main/docs/security/white-paper-landing-page.md)
- [Getting from Azure Data Factory to Data Factory in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/compare-fabric-data-factory-and-azure-data-factory)
- [Data virtualization with Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/data-virtualization-overview?view=azuresql&tabs=managed-identity)
- [Data virtualization now generally available in Azure SQL Managed Instance](https://techcommunity.microsoft.com/blog/azuresqlblog/data-virtualization-now-generally-available-in-azure-sql-managed-instance/3624292)
- [Announcing Data virtualization with Azure SQL Managed Instance – preview](https://techcommunity.microsoft.com/blog/azuresqlblog/announcing-data-virtualization-with-azure-sql-managed-instance-%E2%80%93-preview/3250347)


</details>

## Content

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>

</details>

## What is Data Virtualization?

> Data virtualization is a data management approach that `allows applications to retrieve and manipulate data without needing to know the technical details about the data, such as its format or physical location`.
> Is `commonly used in business intelligence, service-oriented architecture, cloud computing, and master data management`. It helps organizations `make data-driven decisions by providing a comprehensive and up-to-date view of their data`.

###  Key Features & Fabric Components

| Key Features | Fabric Component |
| --- | --- |
| **Unified Data Access**: Provides a single access layer for data from multiple sources, such as databases, data warehouses, and cloud services | - **OneLake**: Acts as a unified data lake, enabling seamless access to data from various sources. Centralizes data storage, making it easier to access and manage data from different sources. <br/> - **Azure Synapse Analytics**: Allows querying across different data sources without moving the data, providing a virtualized view. Offers a unified analytics platform that integrates big data and data warehousing, allowing for seamless data querying and analysis. |
| **Real-Time Data Integration**: Allows real-time access to data without moving it from its original location | - **Shortcuts and Mirroring (Data Factory)**: Facilitate real-time data integration and transformation, allowing you to work with data in its original location. <br/> - **Real-Time Intelligence**: Supports real-time analytics and insights, enhancing decision-making processes. <br/> - **Azure Stream Analytics**: Processes real-time data streams for immediate insights. Provides real-time data processing capabilities, enabling you to analyze data as it arrives. |
| **Flexibility and Efficiency**: Users can access and combine data quickly and cost-effectively, accelerating data delivery and decision-making | **Microsoft Fabric**: Provides a comprehensive data management and analytics solution. <br/> - **Power BI**: Connects to various data sources to create interactive reports and dashboards, enhancing data-driven decision-making. Enhances data visualization and reporting, allowing users to create interactive and insightful dashboards. <br/> - **Azure Data Factory**: Enables flexible data integration and transformation workflows. |

<p align="center">
  <img src="https://github.com/user-attachments/assets/44f2b7dc-ea99-4ea3-b4ec-90654cb434c1" alt="image" width="750">
</p>

###  Benefits:
- **Reduced Data Movement**: Minimizes the need to move data, reducing the risk of errors and ensuring the most current data is used.
- **Simplified Data Integration**: Makes it easier to integrate data from various sources, providing a unified view of the data.
- **Enhanced Data Governance**: Centralizes data security and governance, making it easier to manage and enforce policies.

### Example of how DV looks in Azure SQL MI

> Querying Azure Data Lake Storage files from Azure SQL Managed Instance via T-SQL queries:

<img width="450" alt="image" src="https://github.com/user-attachments/assets/af5a4c16-170c-4670-a6ca-b34df9312b76" />

## Demo 

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
