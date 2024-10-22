# Fabric: How to Manage Accesss

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-07

------------------------------------------


## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Roles in workspaces in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/get-started/roles-workspaces#-workspace-roles)
- [Permission model](https://learn.microsoft.com/en-us/fabric/security/permission-model)
- [Row-level security (RLS) with Power BI](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security)
  
</details>


## Overview 

> Power BI offers a comprehensive suite of analytics tools for organizational insights. You can connect to hundreds of data sources, simplifies data preparation, and facilitates ad hoc analysis. Power BI allows you to produce beautiful reports, then publish them for your organization to consume on the web and across mobile devices.

Types of Access in Power BI:

| **Product**           | **Description**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| Power BI Desktop      | A Windows application for creating reports and data visualizations on your local computer. |
| Power BI Service      | An online SaaS (Software as a Service) where you can share and view dashboards and reports. |
| Power BI Mobile Apps  | Available on Windows, iOS, and Android devices for viewing reports and dashboards on the go. |


Roles and Permissions:

- **Admin**: Full control over the Power BI tenant, including user management and tenant settings.
- **Member**: Can edit and manage content within a workspace.
- **Contributor**: Can add and edit content, but cannot manage workspace settings.
- **Viewer**: Can only view content within a workspace.

Licensing:

| **License Type**     | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| Power BI Free        | Limited to individual use with no sharing capabilities.                         |
| Power BI Pro         | Allows sharing and collaboration, required for both creators and consumers of content. |
| Power BI Premium     | Provides dedicated capacity and advanced features, does not require Pro licenses for content consumers. |

Data Connectivity:

| **Category**         | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| Files                | Excel, CSV, XML, JSON                                                           |
| Databases            | SQL Server, Oracle, MySQL, PostgreSQL                                           |
| Online Services      | SharePoint, Dynamics 365, Google Analytics, Salesforce                          |
| Other Sources        | Web, OData, Active Directory                                                    |

Creating and Publishing Reports:

| **Step**             | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| Connect to Data      | Use Power BI Desktop to connect to your data source.                            |
| Transform Data       | Clean and transform your data using Power Query.                                |
| Create Visuals       | Build reports with interactive visuals.                                         |
| Publish              | Publish your reports to the Power BI service for sharing.                       |

Sharing and Security:
- **Row-Level Security (RLS)**: Restricts data access for given users, defined within roles.
- **Content Packs**: A way to share datasets, reports, and dashboards with other users.
- **Apps**: A collection of dashboards and reports bundled together and shared with users.

Consuming Reports:

| **Method**           | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| Power BI Service     | View and interact with reports in a web browser.                                |
| Power BI Mobile Apps | Access reports on mobile devices.                                               |
| Embedded             | Integrate reports into your own applications using Power BI Embedded.           |

## Demo 

> How to create a Power Bi Workspace App from the beginning and share it with external users. The same steps apply to security groups; simply replicate the process for a security group and add members to it.

1. Create your Fabric Capacity

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/8f259cac-1dcb-4129-9070-0b31899c4ab4">

2. Go to [Fabric](https://app.fabric.microsoft.com/), and assign the capacity created to the workspace desired.

   <img width="248" alt="image" src="https://github.com/user-attachments/assets/f9847839-9827-4ba4-8ca8-0f71a6229acc"> <br/>

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/a93b9b06-e887-45f2-a621-29ebab58f845"> <br/>

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/0b540105-e554-4056-b06c-cd3babc873e9">

3. Create a lakehouse to store your data:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/07aa957b-48f0-4114-926a-d6004d96f93c">

4. Get your data, in this case a CSV file will be used

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/d2949bee-f968-48d6-9c23-13984fde3311">

5. After uploading the information, create the tables or upload the information to your existing tables:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/664eeb04-7d09-4e7f-bd92-22e954ef689d">

6. Create a semantic model based on your tables:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/f892506e-46a5-42bd-ba2f-585601e5a7a1">

7. Now you are able to create a report based on the semantic model created, you can ask copilot to create a draft report with the `Auto-create report` option.

> [!NOTE]
> Make sure to activate the setting under `Admin Portal -> Tenant Settings -> Copilot/Data -> Enabled`.  [Click here for more details](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/2_AzureAnalytics/0_Fabric/demos/6_PBiCopilot.md#tenant-configuration)

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/aa306dcc-0bbd-4fdb-bb5f-04ef79e9dfc8">

  - You will see something like this:
    
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/c3101f92-d6cf-4df0-aabd-c0e0951994eb">

    <img width="955" alt="image" src="https://github.com/user-attachments/assets/99ec33b0-33c8-4fbc-93fb-8c8285ba5fae">

  - You can leverage copilot to modify your report:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/1d46a462-252a-44bc-9d6b-420816878546">

  - Once you are ready, save your report:
  
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/0d663e5a-2a8f-4e74-83d9-21e6bc4801ad">

  - At this point you will have your `lakehouse`, with your `SQL analytics endpoint`, the `semantic model` and `the report`.
    
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/180304fa-2bd5-4de4-9ef1-b4e290ce2929">

8. A paginated report, can also be created:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/ccccd176-dd0e-48cc-b6b8-1a7bab1e0a90">

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/26ec846b-3527-4328-9af0-6e17c60a256c">

9. Create an App, and assign the required audience:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/c575a4e3-d7bd-4eb6-b61f-ee8345ec5c68">

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/c68d60de-801a-4d9c-98aa-a66d0cfa9dc6">

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/e2f45540-1b89-46bb-82a2-997c36bb5351">

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/057aa31e-7818-40f5-ac60-5f12425380c1">

> [!IMPORTANT]
> If you encounter these errors, it's necessary to grant the appropriate `(semantic model, sql analytics endpoint, and the app` permissions for access.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/7361815f-7a53-4ae7-80f9-5bd6e3033b59">

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/05fac487-647a-48c2-b2b9-d9f1f0b172ea">

   - Let's say you want only `viewer` permissions:

     1. Need to give access to the lakehouse/sql analytics endpoint:
        
        <img width="436" alt="image" src="https://github.com/user-attachments/assets/814f831f-19b8-4939-a3e2-618385c4827b">

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/b87137f1-b464-43df-a04d-593a41b3131a">

      2. Make sure the person already have access to the semantic model:

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/f5344f85-53f3-48dc-b0b1-6b3c5995bbd6">

> Granting `Read, ReadData` access to the `semantic model, sql analytics endpoint`, grating `App audience` will enable the assigned individual to view it.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/353d88ad-a4a7-4aef-aff4-d584901c29d8">

