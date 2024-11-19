# MySQL and Fabric connection

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-19

------------------------------------------

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>
  
 - [Set up your MySQL database connection](https://learn.microsoft.com/en-us/fabric/data-factory/connector-mysql-database)
 - [MySQL Connection in Power Query](https://community.fabric.microsoft.com/t5/Desktop/Mysql-Connection/td-p/2650110)
  
</details>

## Overview 

| **Deployment Type**            | **Suggested Connection Method**                                                                 | **Security Considerations**                                                                 |
|--------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| On-Premises Deployment         | MySQL Database Connector in Dataflow Gen2 with On-Premises Data Gateway, [click to see more about Connecting Microsoft Fabric to On-Premises MySQL](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/2_AzureAnalytics/0_Fabric/_Connections/4_OnPremMYSQL.md#connecting-microsoft-fabric-to-on-premises-mysql)                     | Secure connection using on-premises data gateway, supports Basic and Windows authentication. |
| Infrastructure as a Service (IaaS) | MySQL Database Connector in Dataflow Gen2 or Power Query                                  | Secure connection using cloud provider's security features, supports various authentication types. |
| Platform as a Service (PaaS)   | Power Query                                                                                 | Managed service with built-in security features, supports organizational account authentication. |
| Database as a Service (DBaaS)  | Power Query                                                                                 | Fully managed service with automated security updates, supports various authentication types. |
| Dedicated Server               | MySQL Database Connector in Dataflow Gen2 with On-Premises Data Gateway                     | Secure connection using on-premises data gateway, supports Basic and Windows authentication. |
| Shared Server                  | MySQL Database Connector in Dataflow Gen2 or Power Query                                   | Secure connection using appropriate authentication methods, supports various authentication types. |
| Multicloud Environments        | Power Query                                                                                 | Secure connection using cloud provider's security features, supports various authentication types. |
| Private Cloud                  | MySQL Database Connector in Dataflow Gen2 with On-Premises Data Gateway                     | Secure connection using on-premises data gateway, supports Basic and Windows authentication. |

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>