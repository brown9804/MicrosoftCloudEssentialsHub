# Fabric: Lakehouse Schema and Deployment Pipelines 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-26

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
