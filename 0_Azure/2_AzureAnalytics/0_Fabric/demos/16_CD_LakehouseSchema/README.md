# Fabric: Lakehouse Schema and Deployment Pipelines 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-19

------------------------------------------

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Table deletes, updates, and merges - DeltaTables](https://docs.delta.io/latest/delta-update.html#-merge-in-streaming)
- [DeltaLake - DeltaTables Releases](https://github.com/delta-io/delta/releases)
- [DeltaTable execute() example](https://github.com/delta-io/delta/blob/master/examples/python/quickstart.py#L50-L56)
- [Create deployment rules](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/create-rules?tabs=new)
- [Notebook source control and deployment](https://learn.microsoft.com/en-us/fabric/data-engineering/notebook-source-control-deployment)
- [Fabric: Understand the deployment process](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/understand-the-deployment-process)
- [Incremental refresh in Dataflow Gen2 - Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/dataflow-gen2-incremental-refresh)
- [Dataflow Gen2 refresh - Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/dataflow-gen2-refresh)
- [Announcing Public Preview: Incremental Refresh in Dataflow Gen2](https://blog.fabric.microsoft.com/en-us/blog/announcing-public-preview-incremental-refresh-in-dataflows-gen2/)
  
</details>

## Deployment Pipelines 

> [!Note]
> `Ownership and Deployment`: In Microsoft Fabric, only the owner of an artifact can deploy it. Non-owner admins do not have the permissions to deploy artifacts. You can create a service principal to act like an owner, allowing it to deploy artifacts on behalf of the actual owner. This ensures that deployment tasks can be automated and managed efficiently without compromising security. <br/> <br/>
> `Deployment Rules for Notebooks and Pipelines`: You can add `deployment rules` for notebooks and pipelines in Microsoft Fabric. Deployment rules `can be configured to manage different stages (development, test, production)` and to change content settings during deployment. For notebooks, you can set rules to specify the default lakehouse, which helps avoid manual changes to source and destination references post-deployment.

Process Overview:

1. **Pipeline Structure**: You define the deployment pipeline structure, which typically includes stages like development, test, and production. Each stage can have its own workspace.
2. **Adding Content**: Content can be added to a pipeline stage by assigning a workspace or deploying content from one stage to another. When you deploy content, Microsoft Fabric copies the metadata, reports, dashboards, and semantic models to the target stage.
3. **Content Cloning**: During deployment, the content from the source stage is cloned to the target stage. This includes the structure and semantic models but `not the actual data` within the tables. This means that while the structure and connections are maintained, the data itself needs to be refreshed or reloaded in the new stage.
4. **Autobinding**: Microsoft Fabric tries to maintain connections between items during deployment. For example, if a report is connected to a semantic model, this connection is preserved in the target stage.

> [!IMPORTANT]
> `Specifics for Lakehouse:` For lakehouses, the deployment process typically `includes the structure and metadata but not the actual data tables`. This is why you might see the structure and semantic models deployed, but the tables themselves need to be manually refreshed or reloaded in the target environment.<br/> <br/>
> `Deployment Rules:` You can set deployment rules to manage different stages and change content settings during deployment. For example, you can specify default lakehouses for notebooks to avoid manual changes post-deployment.

### Demo 

1. **Create a Workspace**:
   - Navigate to the Microsoft Fabric portal.
   - Click on `Create a new workspace`.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/58069226-12c5-43ca-9c0f-4f95d6d2a556" />

   - Name your workspace (e.g., `Analytics Dev`).
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/97bf47a4-00d8-4acc-af85-2fc52793a8f5" />
  
   - Ensure that your workspace is allocated to the appropriate Fabric Capacity:
   
      <img width="550" alt="image" src="https://github.com/user-attachments/assets/0cf11e09-dbc1-470a-9a77-6dbc279a5242" />

2. **Create a Lakehouse**:
   - Within your new workspace, select `New item` and choose `Lakehouse`.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/c391ccc3-408a-4a38-979c-acbe2fc65818" />

   - Name your lakehouse (e.g., `Sales_Data_Lakehouse`).

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/a69d3f63-4286-4368-8515-d0383b63b09c" />

   - Click on `Get data`, and `Upload files`:

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/e3dd716c-7391-4a03-9ff2-4f8722fd29bf" />

   - Load data into the tables:
  

     
2. **Define Schema for Dataset**:
   - In the lakehouse, create a new dataset.
   - Define the schema by adding tables and columns as needed.

3. **Auto-Generate Report with Copilot**:
   - Use Copilot to generate a report based on your dataset.
   - Ensure you have the necessary permissions and settings enabled for Copilot to access and use your data.
   - **Warning**: Make sure to configure Copilot settings correctly to avoid any data privacy or security issues.

4. **Create a Deployment Pipeline**:
   - Go back to the Microsoft Fabric portal and select "Deployment Pipelines".
   - Create a new pipeline and name it (e.g., "Dev to Prod Pipeline").
   - Add your "Development Workspace" as the source.
   - Create a new workspace for production (e.g., "Production Workspace").
   - Add the "Production Workspace" as the target.

5. **Deploy to Production**:
   - Use the deployment pipeline to move your lakehouse, dataset, and report from the "Development Workspace" to the "Production Workspace".
   - Verify that everything is working correctly in the production environment.



### How to refresh the data

> To ensure that data is refreshed and reloaded in the new stage of your deployment in Microsoft Fabric, you can use the following methods:

| **Type of Refresh**       | **Description**                                                                                                                                                                                                                     | **Details**                                                                                                                                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Scheduled Refresh**     | Automatically refreshes data at specified intervals to keep it up-to-date. This allows you to automatically refresh the data at specified intervals, ensuring that the data in the new stage is always up-to-date.                                                                                                                                                          | - Can be configured to run multiple times a day.<br>- Ensures data in the new stage is always current.                                                                                                                             |
| **On-Demand Refresh**     | Allows immediate data refresh, triggered manually or programmatically.                                                                                                                                                              | - Can be done through workspace list or lineage views.<br>- Can be triggered via a pipeline containing a dataflow activity.                                                                                                        |
| **Incremental Refresh**   | Refreshes only the data that has changed since the last refresh, improving efficiency. Click [here to understand more about incremental refresh](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/2_AzureAnalytics/0_Fabric/demos/11_PBi_IncreRefresh.md)                                                                                                                                       | - **Evaluate Changes**: Checks for changes in the data source based on a DateTime column.<br>- **Retrieve Data**: Only changed data is retrieved and loaded.<br>- **Replace Data**: Updated data is processed and replaced.       |


Steps to Set Up Incremental Refresh:
1. **Create or Open a Dataflow**: Start by creating a new Dataflow Gen2 or opening an existing one.
2. **Configure the Query**: Ensure your query includes a DateTime column that can be used to filter the data.
3. **Enable Incremental Refresh**: Right-click the query and select Incremental Refresh. Configure the settings, such as the DateTime column and the time range for data extraction.
4. **Publish the Dataflow**: Once configured, publish the dataflow. The dataflow will then automatically refresh the data incrementally based on the settings.

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
