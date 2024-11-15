# Azure SQL Database Services

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-15

----------

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>

## Wiki

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>
  
- [How to manage a Hyperscale database - Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/manage-hyperscale-database?view=azuresql)
- [Create a Hyperscale database - Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/hyperscale-database-create-quickstart?view=azuresql)
- [Single database vCore resource limits - Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/resource-limits-vcore-single-databases?view=azuresql)
- [Manage multiple databases with elastic pools - Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-pool-overview?view=azuresql)
- [Pricing - Azure SQL Database Elastic Pool | Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/elastic/)
- [What is the Hyperscale service tier? - Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tier-hyperscale?view=azuresql)
- [Pricing - Azure SQL Database Single Database | Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/single/)
- [Change automated backup settings for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-change-settings?view=azuresql)

</details>

## Overview

| Service | Meaning | Configuration | Charging |
|---------|---------|---------------|----------|
| **SQL Database Hyperscale - Storage** | This service is for storing data in a Hyperscale SQL database, which supports up to 100 TB of data and provides high throughput and performance. | Configure through Azure portal, Azure CLI, PowerShell, or REST API. Storage is automatically allocated between 10 GB and 100 TB, growing in 10 GB increments as needed. | Charged based on the actual storage allocation. Cost is calculated per GB of storage used. |
| **SQL DB Single/Elastic Pool Gen Pur-Compute G5** | Offers computing resources (vCores) for single databases or elastic pools in the General Purpose tier using Gen5 hardware. | Configure the compute resources through the Azure portal, specifying the number of vCores required. | Charges are based on the vCores used and the duration of usage. |
| **SQL DB Single Hyp-Storage** | This is for Hyperscale data storage but specifically for single databases. | Similar to the Hyperscale storage, configure via Azure portal, CLI, PowerShell, or REST API. | Charges are based on the storage used, dynamically allocated between 10 GB and 100 TB. |
| **SQL DB S0/S1/B Gen5 - Comp Gen5** | Provides computing resources (vCores) for SQL databases in the S0, S1, and Basic tiers using Gen5 hardware. | Scale compute resources by selecting the number of vCores needed through the Azure portal or other management tools. | Charges are based on the number of vCores and the duration they are used. |
| **SQL DB S0/S1/B Pool Hyp - Comp Gen5** | Provides computing resources (vCores) in a pool configuration for the same tiers and hardware as above. | Configure the pool and allocate vCores as needed through the Azure portal. | Charges are based on the total vCores allocated to the pool. |
| **SQL DB Single/Elastic Pool GP-SQL Licen** | Provides SQL licensing for single databases or elastic pools in the General Purpose tier. | Licensing is managed automatically when you configure your database or pool in the Azure portal. | Charges are included in the overall cost of the database or pool, based on the vCore model. |
| **SQL DB Single/Elastic Pool Purc-PurcStorage** | For storing data in the General Purpose tier for single databases or elastic pools. | Storage is configured automatically based on your database or pool settings. | Charges are based on the amount of data stored. |
| **SQL Database S0/S1/B Pool PITR Backup Storage** | For backup storage using RA-GRS (Read-Access Geo-Redundant Storage) for databases in the S0, S1, and Basic tiers. | Backup settings can be configured through the Azure portal, including retention policies and redundancy options. | Charges are based on the amount of backup storage used. |

### SQL Database Hyperscale - Storage
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Create a New SQL Database**:
   - Click on `Create a resource` > `Databases` > `SQL Database`.
   - Fill in the required details like `Subscription`, `Resource group`, `Database name`, and `Server`.
3. **Select Hyperscale Service Tier**:
   - Under `Compute + storage`, click `Configure database`.
   - Select `Hyperscale` from the `Service tier` dropdown.
   - Configure the `vCores` and `Storage size` as needed.
4. **Review and Create**: Click `Review + create` and then `Create`.

> Viewing and Managing:
- Navigate to your SQL Database in the Azure portal.
- Under `Settings`, select `Compute + storage` to view and manage your Hyperscale configuration.

### SQL DB Single Hyp-Storage
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Create a New SQL Database**:
   - Click on `Create a resource` > `Databases` > `SQL Database`.
   - Fill in the required details like `Subscription`, `Resource group`, `Database name`, and `Server`.
3. **Select Hyperscale Service Tier**:
   - Under `Compute + storage`, click `Configure database`.
   - Select `Hyperscale` from the `Service tier` dropdown.
   - Configure the `vCores` and `Storage size` as needed.
4. **Review and Create**: Click `Review + create` and then `Create`.

> Viewing and Managing:
- Navigate to your SQL Database in the Azure portal.
- Under `Settings`, select `Compute + storage` to view and manage your Hyperscale configuration.

### SQL DB S0/S1/B Gen5 - Comp Gen5
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Create a New SQL Database**:
   - Click on `Create a resource` > `Databases` > `SQL Database`.
   - Fill in the required details like `Subscription`, `Resource group`, `Database name`, and `Server`.
3. **Select Service Tier**:
   - Under `Compute + storage`, click `Configure database`.
   - Select `General Purpose` from the `Service tier` dropdown.
   - Choose `Gen5` hardware and configure the `vCores` as needed.
4. **Review and Create**: Click `Review + create` and then `Create`.

> Viewing and Managing:
- Navigate to your SQL Database in the Azure portal.
- Under `Settings`, select `Compute + storage` to view and manage your configuration.

### SQL DB S0/S1/B Pool Hyp - Comp Gen5
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Create a New Elastic Pool**:
   - Click on `Create a resource` > `Databases` > `SQL Elastic Pool`.
   - Fill in the required details like `Subscription`, `Resource group`, `Elastic pool name`, and `Server`.
3. **Select Service Tier**:
   - Under `Compute + storage`, click `Configure pool`.
   - Select `General Purpose` from the `Service tier` dropdown.
   - Choose `Gen5` hardware and configure the `vCores` as needed.
4. **Add Databases**: Add your databases to the pool.
5. **Review and Create**: Click `Review + create` and then `Create`.

> Viewing and Managing:
- Navigate to your Elastic Pool in the Azure portal.
- Under `Settings`, select `Compute + storage` to view and manage your configuration.

### SQL DB Single/Elastic Pool Gen Pur-Compute G5
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Create a New SQL Database or Elastic Pool**:
   - Click on `Create a resource` > `Databases` > `SQL Database` or `SQL Elastic Pool`.
   - Fill in the required details like `Subscription`, `Resource group`, `Database/Elastic pool name`, and `Server`.
3. **Select Service Tier**:
   - Under `Compute + storage`, click `Configure database/pool`.
   - Select `General Purpose` from the `Service tier` dropdown.
   - Choose `Gen5` hardware and configure the `vCores` as needed.
4. **Review and Create**: Click `Review + create` and then `Create`.

> Viewing and Managing:
- Navigate to your SQL Database or Elastic Pool in the Azure portal.
- Under `Settings`, select `Compute + storage` to view and manage your configuration.

### SQL DB Single/Elastic Pool GP-SQL Licen
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Create a New SQL Database or Elastic Pool**:
   - Click on `Create a resource` > `Databases` > `SQL Database` or `SQL Elastic Pool`.
   - Fill in the required details like `Subscription`, `Resource group`, `Database/Elastic pool name`, and `Server`.
3. **Select Service Tier**:
   - Under `Compute + storage`, click `Configure database/pool`.
   - Select `General Purpose` from the `Service tier` dropdown.
   - Choose `Gen5` hardware and configure the `vCores` as needed.
4. **Review and Create**: Click `Review + create` and then `Create`.

> Viewing and Managing:
- Navigate to your SQL Database or Elastic Pool in the Azure portal.
- Under `Settings`, select `Compute + storage` to view and manage your configuration.

### SQL DB Single/Elastic Pool Purc-PurcStorage
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Create a New SQL Database or Elastic Pool**:
   - Click on `Create a resource` > `Databases` > `SQL Database` or `SQL Elastic Pool`.
   - Fill in the required details like `Subscription`, `Resource group`, `Database/Elastic pool name`, and `Server`.
3. **Select Service Tier**:
   - Under `Compute + storage`, click `Configure database/pool`.
   - Select `General Purpose` from the `Service tier` dropdown.
   - Choose `Gen5` hardware and configure the `vCores` as needed.
4. **Review and Create**: Click `Review + create` and then `Create`.

> Viewing and Managing:
- Navigate to your SQL Database or Elastic Pool in the Azure portal.
- Under `Settings`, select `Compute + storage` to view and manage your configuration.

### SQL Database S0/S1/B Pool PITR Backup Storage
> Configuration Steps:
1. **Navigate to Azure Portal**: Go to Azure Portal.
2. **Select Your SQL Database**:
   - Navigate to your SQL Database.
   - Under `Settings`, select `Backups`.
3. **Configure Backup Settings**:
   - Select `Retention policies`.
   - Configure the `Point-in-time restore (PITR)` retention period and `Backup storage redundancy`.
4. **Save Changes**: Click `Save` to apply the changes.

> Viewing and Managing:
- Navigate to your SQL Database in the Azure portal.
- Under `Settings`, select `Backups` to view and manage your backup configuration.
