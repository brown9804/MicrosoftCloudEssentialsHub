# Building a Scalable Cloud-Based Database for Automated PDF Invoice Processing and Analytics

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-18

----------

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>


> Using Azure Functions, Blob Storage, and Cosmos DB

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Azure Cosmos DB - Database for the AI Era](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
- [What is Azure SQL Database?](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql)
 
</details>

## Overview 

> Using Cosmos DB provides you with a flexible, scalable, and globally distributed database solution that can handle both structured and semi-structured data efficiently. <br/>
> - `Azure Blob Storage`: Store the PDF invoices. <br/>
> - `Azure Functions`: Trigger on new PDF uploads, extract data, and process it. <br/>
> - `Azure SQL Database or Cosmos DB`: Store the extracted data for querying and analytics. <br/> 

| Resource                  | Recommendation                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Azure Blob Storage**    | Use for storing the PDF files. This keeps your file storage separate from your data storage, which is a common best practice. |
| **Azure SQL Database**    | Use if your data is highly structured and you need complex queries and transactions.                                  |
| **Azure Cosmos DB**       | Use if you need a globally distributed database with low latency and the ability to handle semi-structured data.      |

### Step 1: Set Up Your Azure Environment

> An Azure `Resource Group` is a `container that holds related resources for an Azure solution`.
> It can include all the resources for the solution or only those you want to manage as a group.
> Typically, resources that share the same lifecycle are added to the same resource group, allowing for easier deployment, updating, and deletion as a unit.
> Resource groups also store metadata about the resources, and you can apply access control, locks, and tags to them for better management and organization.

1. **Create an Azure Account**: If you don't have one, sign up for an Azure account.
2. **Create a Resource Group**:
   - Go to the Azure portal.
   - Navigate to **Resource groups**.
   - Click **+ Create**.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/56d1e99f-0a22-4492-bd6f-d4e3a76aedd8">

   - Enter the Resource Group name (e.g., `RGContosoAI`) and select a region (e.g., `East US 2`). You can add tags if needed.
   - Click **Review + create** and then **Create**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/7ef5d701-5df7-4e18-a0d3-60a93d5076c9">

