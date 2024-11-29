# Strategies to Prevent Capacity Spikes - Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-28

----------

> [!NOTE]
> In Microsoft Fabric, `smoothing is automatically applied to help manage and optimize capacity usage by spreading the compute demand over time`. This helps prevent sudden spikes and ensures more consistent performance. <br/>
> However, there is no automatic autoscale feature available. Instead, you need to manually adjust your capacity based on your usage patterns and needs. 


## Wiki 

<details>
<summary><b>Table of Wiki</b> (Click to expand)</summary>

</details>


## Monitor Usage 

Below, you will find a quick overview of ways to monitor your usage with tools:

- [Microsoft Fabric Capacity Metrics App](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/2_AzureAnalytics/0_Fabric/demos/20_FabricCapacityMetrics.md#microsoft-fabric-capacity-metrics-app): Powerful tool for administrators to `monitor and manage their capacity usage`. It provides detailed insights into `capacity utilization, throttling, and system events, helping to optimize performance and resource allocation`. By tracking these metrics, admins can make informed decisions to ensure efficient use of resources.
- [Admin Monitoring workspace](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/2_AzureAnalytics/0_Fabric/demos/20_FabricCapacityMetrics.md#admin-monitoring): Centralized hub for `tracking and analyzing usage metrics across the organizatio`n. It includes `pre-built reports and semantic models that provide insights into feature adoption, performance, and compliance`. This workspace helps administrators maintain the health and efficiency of their Fabric environment by offering a comprehensive `view of usage patterns and system events`.
- [Monitor Hub](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/2_AzureAnalytics/0_Fabric/demos/20_FabricCapacityMetrics.md#monitor-hub): Allows users to `view and track the status of activities across all workspaces they have permissions for`. It provides a detailed overview of operations, `including dataset refreshes, Spark job runs, and other activities`. With features like historical views, customizable displays, and filtering options, the Monitor Hub helps ensure smooth operations and timely interventions when needed.
