# Fabric Tenant Migration - Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-12-28

----------

## Wiki 

<details>
<summary><b>Table of Wiki </b> (Click to expand)</summary>

- [Microsoft Fabric deployment patterns](https://learn.microsoft.com/en-us/azure/architecture/analytics/architecture/fabric-deployment-patterns)
- [Evaluate and optimize your Microsoft Fabric capacity](https://learn.microsoft.com/en-us/fabric/enterprise/optimize-capacity)
- [Configure Multi-Geo support for Fabric](https://learn.microsoft.com/en-us/fabric/admin/service-admin-premium-multi-geo?tabs=power-bi-premium)
- [Migrate workspaces to a different region with fabric items removed (MS community)](https://community.fabric.microsoft.com/t5/Service/Migrate-workspaces-to-a-different-region-with-fabric-items/m-p/3700743)
- [I'm looking to move my Premium capacity to another region, will my dataflows still work? (MS community)](https://community.fabric.microsoft.com/t5/Service/I-m-looking-to-move-my-Premium-capacity-to-another-region-will/m-p/991510)
- [Change Data Region (MS community)](https://community.fabric.microsoft.com/t5/Desktop/Change-Data-Region/td-p/2538791)

</details>

## Content

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>

</details>


## Overview 

> Below is a table with several scenarios that provide further details on when it is recommended to migrate your Fabric/Power BI tenant to a different region:

| **Action** | **Scenario** | **Example** | **Technical Details** |
|------------|--------------|-------------|-----------------------|
| **Migrate Tenant** | Data Sources in Different Region | Your data sources are in East US, and your current Fabric/Power BI tenant is in Central US. To optimize performance and ensure compliance, you migrate your tenant to East US, aligning it with your data sources to reduce latency and improve data processing speeds. | - Reduces latency by aligning tenant with data sources.<br>- Ensures compliance with data residency requirements.<br>- Simplifies management of data connections and credentials.<br>- Requires updating all data source connections and credentials to reflect the new tenant region.<br>- Potential downtime during migration, so plan for a maintenance window. |
| **Migrate Tenant** | Long-Term Regional Alignment | You plan to consolidate all resources in East US for better management and performance. Currently, your tenant is in Central US. You migrate your tenant to East US and then provision a new F256 capacity, aligning all resources in the same region. | - Aligns all resources in the same region for long-term management.<br>- Reduces complexity of multi-region setups.<br>- Ensures consistent performance and compliance.<br>- Requires thorough planning to ensure all services and data are migrated smoothly.<br>- May involve reconfiguring network settings and security policies. |
| **Migrate Tenant** | Compliance and Governance | Regulatory requirements mandate that your tenant and data sources be in the same region. Your data sources are in East US, but your tenant is in Central US. You migrate your tenant to East US to meet compliance requirements. | - Necessary for meeting specific compliance or governance requirements.<br>- Ensures data residency and regulatory compliance.<br>- Simplifies audit and management processes.<br>- Involves validating compliance requirements and ensuring all data is correctly migrated.<br>- May require coordination with legal and compliance teams. |
| **Reassign Workspaces** | Immediate Capacity Needs | Your current Power BI Premium P2 capacity in Central US is nearing its limit. You provision a new F256 capacity in East US and reassign your workspaces to this new capacity, addressing capacity issues immediately without migrating the tenant. | - Quick solution to manage capacity without full migration.<br>- Minimal disruption to ongoing operations.<br>- Ensure dataflows and datasets are configured for new capacity.<br>- Requires updating workspace settings to point to the new capacity.<br>- Monitor performance to ensure the new capacity meets your needs. |
| **Reassign Workspaces** | Temporary Solution | You need an immediate solution for capacity management and plan a future tenant migration. You provision a new F256 capacity in East US and reassign workspaces as a temporary measure, addressing current needs while planning for the tenant migration. | - Provides a temporary fix while planning for future migration.<br>- Avoids immediate complexities of tenant migration.<br>- Monitor performance and plan for eventual migration.<br>- Allows for phased migration, reducing risk of disruption.<br>- Requires careful tracking of which workspaces have been reassigned. |
| **Reassign Workspaces** | Performance Optimization | Your data sources are in East US, and you want to improve performance by reducing latency. You reassign workspaces to a new F256 capacity in East US, improving performance without migrating the tenant. | - Improves performance by moving workspaces closer to data sources.<br>- No need for full tenant migration.<br>- Ensure all datasets and dataflows are compatible with new capacity.<br>- Requires testing to ensure performance improvements are realized.<br>- May involve reconfiguring data refresh schedules to optimize performance. |



 <div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
