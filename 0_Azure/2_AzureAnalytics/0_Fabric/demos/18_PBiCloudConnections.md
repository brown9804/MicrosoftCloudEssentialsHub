# Power Bi: Cloud Connections & Gateways

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-15

------------------------------------------

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Create and share cloud data sources in the Power BI service](https://learn.microsoft.com/en-us/power-bi/connect-data/service-create-share-cloud-data-sources)
- [Connect to cloud data sources in the Power BI service](https://learn.microsoft.com/en-us/power-bi/connect-data/service-connect-cloud-data-sources)
- [Manage users around Cloud Connections](https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management#manage-users)
- [Migrate from Azure Analysis Services to Power BI Premium](https://learn.microsoft.com/en-us/power-bi/guidance/migrate-azure-analysis-services-to-powerbi-premium)
- [On-premises and virtual network (VNet) data gateways documentation](https://learn.microsoft.com/en-us/data-integration/gateway/)
- [What is an on-premises data gateway?](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem)
- [What is a virtual network (VNet) data gateway?](https://learn.microsoft.com/en-us/data-integration/vnet/overview)
- [Set privacy levels (Power Query) details](https://support.microsoft.com/en-us/office/set-privacy-levels-power-query-cc3ede4d-359e-4b28-bc72-9bee7900b540?ui=en-us&rs=en-us&ad=us)
- [What is the admin monitoring workspace? (Preview)](https://learn.microsoft.com/en-us/fabric/admin/monitoring-workspace)
- [Feature usage and adoption report (preview)](https://learn.microsoft.com/en-us/fabric/admin/feature-usage-adoption)

</details>

## How to Manage Cloud connections

Managing cloud connections in Power BI, below you can find differences between personal and shareable cloud connections:

> [!NOTE]
> `When you publish a .PBIX file` from Power BI Desktop that connects to a cloud data source, `Power BI automatically creates a personal cloud connection and binds it to your semantic model`. This means that the connection details and credentials you used in Power BI Desktop are carried over to the Power BI service, allowing the report to continue accessing the cloud data source without any additional configuration.

> Personal Cloud Connections

| **Aspect**                | **Details**                                                                                                                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Automatic Creation**    | When you publish a .PBIX file from Power BI Desktop that connects to a cloud data source, a personal cloud connection is automatically created and bound to your semantic model. This means the connection details and credentials used in Power BI Desktop are carried over to the Power BI service, allowing the report to continue accessing the cloud data source without additional configuration. |
| **Limitations**           | Personal cloud connections are tied to the individual user who created them and cannot be shared with others. This can be limiting if multiple users need to access the same data source.                                                                            |

> Shareable Cloud Connections

| **Aspect**                | **Details**                                                                                                                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Advantages**            | Shareable cloud connections allow multiple connections to the same data source with different settings and can be shared with other users. This makes data management more collaborative and flexible.                                                               |
| **Manual Creation**       | Unlike personal cloud connections, shareable cloud connections need to be created manually in the Power BI service. You can create a new shareable cloud connection directly from the Semantic model settings page under Gateway and cloud connections. Select the shareable cloud connection you want to use and apply it. |

### Creating Shareable Connections

> You can create a new shareable cloud connection directly from the Semantic model settings page under Gateway and cloud connections. Select the shareable cloud connection you want to use and apply it.

> [!IMPORTANT]
> Security: If a data source contains `highly sensitive or confidential data`, set the privacy level to `Private`.

| Privacy level | Details |
| --- | --- |
| Private | Contains sensitive or confidential information, and the visibility of the data source may be restricted to authorized users. It is completely isolated from other data sources. Examples include Facebook data, a text file containing stock awards, or a workbook containing an employee review. |
| Organizational    | Limits the visibility of a data source to a trusted group of people. It is isolated from all Public data sources, but is visible to other Organizational data sources. A common example is a Microsoft Word document on an intranet SharePoint site with permissions enabled for a trusted group. |
| Public | Gives everyone visibility to the data. Only files, internet data sources, or workbook data can be marked Public. Examples include data from a Wikipedia page, or a local file containing data copied from a public web page.| 

### Managing Connections

- `Switching to Shareable Connections`: If you want to switch from a personal cloud connection to a shareable one, you can do so in the Semantic model settings. This allows you to leverage the benefits of shareable connections, such as easier management and sharing capabilities.
- `Granular Access Control`: Power BI allows for granular access control at the tenant, workspace, and semantic model levels. This means you can enforce access policies to ensure that only authorized users can create or use specific connections.


## Admin Monitoring Workspace

> Can help to identify which Power BI Premium Users are making use of the Cloud connections

The admin monitoring workspace in Microsoft Fabric is designed for `administrators to monitor and manage workloads, usage, and governance within their tenant`. It provides insights into user activity, content sharing, and capacity performance. The workspace is `automatically installed the first time an admin accesses it`. It includes `few reports and semantic models for detailed analysis`, helping administrators keep track of how resources are being used and ensuring compliance with governance policies.

Steps to setup admin monitoring workspace:

- Go to [Power Bi](https://app.powerbi.com/)
- Click on ⚙️, and go to `Admin portal`
- Under `Usage metrics`, and go to `Open admin monitoring workspace`
  
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/fcf3adfa-ff37-488d-8bb0-165a6aa87a6d">

> The report can be accessed from the Admin monitoring workspace and is designed for admins to analyze various usage scenarios. 

| Report Name | Details |
| --- | --- | 
| Feature Usage and Adoption Report | This report provides an in-depth analysis of how different features are utilized and adopted across your Microsoft Fabric tenant. It includes pages for activity overview, analysis, and detailed activity scenarios, helping identify which users are making use of cloud connections. |
| Purview Hub | Offers insights into data governance and compliance. It helps administrators manage and monitor data policies, ensuring that data usage aligns with organizational standards and regulatory requirements. | 

<img width="550" alt="image" src="https://github.com/user-attachments/assets/7b40d8a6-bdf8-4a9c-b5dc-1772823c6c3e">

Some key limitations and considerations regarding reports in the admin monitoring workspace:

| **Category**               | **Details**                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Non-Modifiable Reports** | - ``Fixed Reports``: Reports in the admin monitoring workspace are often pre-configured and cannot be modified. This means you cannot change the visuals, add new data fields, or customize the layout to fit specific needs.<br/>- ``Limited Customization``: The inability to modify these reports can be restrictive if you need to tailor the data presentation to specific audiences or requirements. |
| **Access and Permissions** | - ``Restricted Access``: Only users with appropriate permissions can view these reports. This can limit the ability of other team members to access and utilize the data.<br/>- ``Data Sensitivity``: Since these reports often contain sensitive administrative data, access controls are crucial to ensure data security and compliance. |

Benefits of sharing the semantic model:

| **Category**               | **Details**                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Creating Custom Reports** | - ``Flexibility``: By sharing the semantic model, users can create their own reports using the same underlying data. This allows for greater flexibility in how data is visualized and analyzed.<br/>- ``Tailored Insights``: Users can customize reports to highlight specific metrics or insights that are most relevant to their needs. |
| **Collaboration**          | - ``Shared Understanding``: Sharing the semantic model promotes a shared understanding of the data across the organization. Different teams can collaborate more effectively by working with the same data definitions and structures.<br/>- ``Enhanced Data Utilization``: Multiple users can leverage the semantic model to create diverse reports, enhancing the overall utilization of the data. |
| **Consistency**            | - ``Standardized Data``: Using a shared semantic model ensures that all reports are based on the same data definitions and calculations, promoting consistency and accuracy in reporting.<br/>- ``Reduced Redundancy``: It reduces the need for multiple versions of the same data, minimizing redundancy and potential discrepancies. |

> [!IMPORTANT]
> Other ways to get insights: <br/>
> - `Monitoring Usage`: You can monitor and manage cloud connections through the Power BI service. By navigating to the Manage connections and gateways section, you can see which users have access to and are using specific cloud connections. <br/>
> <img width="550" alt="image" src="https://github.com/user-attachments/assets/d64e3acd-aef9-47ba-81c6-c0e92ae5518b">
> - `Premium Capacity Metrics`: For a more detailed analysis, you can use the Premium Capacity Metrics app, which provides insights into the usage and performance of your Power BI Premium capacities.

## Identify Access per report

- Go to your workspace
- Click on `...`, and select `Manage permissions`

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/7a0d0a96-6519-4d84-bd56-5aa7c2497cea">
  
- You will see something like this:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/11633c88-d19d-4e33-bf33-24c985afbb78">
