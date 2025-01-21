# Microsoft Fabric: Power Bi View role - Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-19

-----------------------------------------

> **Microsoft Fabric** is an all-in-one data analytics solution that integrates various Azure data workloads with Power BI, enabling comprehensive data management, analysis, and visualization within a single environment. Fabric consolidates data movement, data science, real-time analytics, and business intelligence, making it easier to derive meaningful insights from your data.
> **Fabric F64** is a specific capacity SKU within Microsoft Fabric that provides enhanced features and capabilities for data analytics. `It allows users to view Power BI content without a per-user license, provided they are assigned the appropriate roles and added to the capacity`.


## Wiki 

<details>
<summary><b>Table of References </b> (Click to expand)</summary>

- [Microsoft Fabric features by SKU](https://learn.microsoft.com/en-us/fabric/enterprise/fabric-features)
- [Getting Started with Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric/getting-started)

</details>


1. **Create a Fabric Capacity**: Follow the prompts to configure and create the capacity.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/8f259cac-1dcb-4129-9070-0b31899c4ab4">

2. **Assign Viewer Role**:
   - Go to the workspace where your Power BI content is hosted.
   - Click on **Settings** and then `Permissions`.
   - Add the users and assign them the `Viewer` role. This allows them to access the content with a free license if the capacity is F64 or larger

3. **Add Users to Capacity**:
   - In the Power BI Admin portal, go to `Capacity settings`.
   - Select the F64 capacity you created.
   - Click on **Add users** and enter the email addresses of the users you want to add.
   - Ensure the users are added to the capacity to allocate the necessary resources for viewing the content

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
