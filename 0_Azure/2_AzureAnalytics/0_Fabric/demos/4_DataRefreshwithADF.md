# Setting Up Data Refresh and Publishing Pipelines with Azure Data Factory in Microsoft Fabric

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-22

----------

> Here is a small guide on how to set up a refresh with Azure Data Factory (ADF) in Microsoft Fabric, publish the data pipeline, and update the gateway.

## Wiki 

- [How to ingest data into Fabric using the Azure Data Factory Copy activity](https://learn.microsoft.com/en-us/fabric/data-factory/how-to-ingest-data-into-fabric-from-azure-data-factory)
- [On-premises data gateway FAQ](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem-faq)
- [Fabric Data Factory Pipeline: Incremental load](https://community.fabric.microsoft.com/t5/Data-Pipelines/Fabric-Data-Factory-Pipeline-Incremental-load/m-p/3262598)
- [Semantic model refresh activity in Data Factory for Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/semantic-model-refresh-activity)
- [What is an on-premises data gateway?](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem)
- [Example of script to update gateway PowerShell](https://github.com/Azure/Azure-DataFactory/blob/main/SamplesV2/SelfHostedIntegrationRuntime/AutomationScripts/script-update-gateway.ps1)

## How to set up

1. **Access Data Factory within Fabric**:
    - Log in to the Microsoft Fabric portal.
    - Navigate to the Data Factory service within Fabric.
      
      <img width="200" alt="image" src="https://github.com/user-attachments/assets/3b57f63c-bb09-4f11-9012-06f59dfa4893">

2. **Create a New Data Pipeline**:
    - Click on the “Create pipeline” button.
    
      <img width="400" alt="image" src="https://github.com/user-attachments/assets/52cfe364-9022-47b0-a76d-33f78d85144e">
    
   - Add activities to your pipeline, such as **Copy Data** or **Data Flow** activities, to define the data transformation and movement.

3. **Configure the Fabric Lakehouse Connector**:
   - Use the Lakehouse connector to read from and write to Microsoft Fabric Lakehouse.
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
