# Azure SQL Database - Overview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-02

----------


> Azure SQL Database is a relational database-as-a-service (DBaaS) that supports both standalone databases and elastic pools. It uses the latest stable version of the SQL Server Database Engine and offers features like T-SQL commands for creating tables, bulk loading data, and querying data

## Wiki 

## Overview

| Topic                        | Description                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fault Tolerance**          | Azure SQL Database ensures fault tolerance through various redundancy options at physical, server, and database levels. SQL Database Hyperscale separates compute and storage layers for increased redundancy. Azure's infrastructure can handle hardware failures by moving virtual machines to other physical nodes. |
| **High Availability**        | Achieved through local and zone redundancy, allowing quick recovery from failures and minimal downtime. Supports active geo-replication and failover groups to enhance availability.                                                              |
| **Disaster Recovery**        | Provides automated backups, geo-redundant storage, and active geo-replication to ensure data protection and quick restoration in the event of a regional outage.                                                                                   |
| **Authentication and Authorization** | Supports both SQL authentication and Microsoft Entra ID (formerly Azure Active Directory) authentication for secure and centralized management of user identities and permissions. Entra ID enables multifactor authentication and conditional access controls. |

## Deploying MS SQL Server in Azure Tenant

1. **Sign in to Azure Portal**: Use your Azure account to sign in.
2. **Create a SQL Server/DB**:
   - Search for Azure SQL.
   - Click on `Create` to create a new SQL Service.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/ec41ae87-b441-4791-8b2a-b48cf9de8723">

   - Choose the deployment option:
     
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/631f176f-2724-4f71-9ab7-e7edebe03587">

      | Deployment Option       | Description                                                                 | Features                                      | Use Case                                                                                   | Resource Type          |
      |-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------|------------------------|
      | **SQL Databases**       | Best for modern cloud applications.                                         | Hyperscale and serverless options available.  | Ideal for scalable, managed databases with minimal administrative overhead.                | Single database        |
      | **SQL Managed Instances** | Best for most migrations to the cloud.                                      | Lift-and-shift ready.                         | Suitable for migrating existing SQL Server workloads to Azure with minimal changes.        | Single instance        |
      | **SQL Virtual Machines** | Best for migrations and applications requiring OS-level access.             | Full control over OS and SQL Server settings. | Ideal for custom OS or SQL Server configurations, or applications requiring OS-level access. | Development/Testing, Production |

       - If you don't have a SQL server in place, please create one.
       - Fill in the required details like server name, admin login, and password.
    
          <img width="550" alt="image" src="https://github.com/user-attachments/assets/ecf6b6aa-e1d9-4e38-82ae-8664d4002b69">
          
          | Topic                        | Description                                                                                                                                                                                                 |
          |------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
          | **Availability of Services** | Not all Azure services and features are available in every region. It's important to check the [Azure Products by Region page](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/) to see which services are available in your desired region.                     |
          | **Redundancy Options**       | Azure SQL Database supports local and zonal redundancy options. Local redundancy provides resiliency within a datacenter, while zonal redundancy improves resiliency by protecting against outages of an availability zone within a region. |
          | **Compliance and Data Residency** | Different regions have specific compliance and data residency requirements. Azure regions are designed to meet these requirements, ensuring that your data stays within the specified geographic boundaries. |
          | **Virtual Network Rules**    | For SQL Database, virtual network rules must reference subnets hosted in the same geographic region as the database. Each server can have up to 128 ACL entries for any virtual network.                     |
          | **Authentication Methods**   | - **SQL Authentication**: Users connect using a username and password. <br/> - **Microsoft Entra Authentication**: Users authenticate using their Microsoft Entra ID credentials, which supports enhanced security features like multifactor authentication and conditional access policies. |
          | **Microsoft Entra Admin**    | The Microsoft Entra admin center is a unified portal for managing Microsoft Entra products, including identity and access management solutions. It provides tools for user and group management, device management, application management, security and compliance, and identity governance. This centralized interface helps streamline administrative tasks and enhances security. |

   - Choose the pricing tier and performance level that suits your needs.
       
      <img width="370" alt="image" src="https://github.com/user-attachments/assets/26488350-7622-494e-8980-262f78b663e3">

2. **Configure Networking**:
   - Set up firewall rules to allow access to your SQL Server.
   - Choose the appropriate network settings based on your security requirements.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/aa53de28-eba1-4214-bb81-e6e1420a458d">

3. **Configure Security**:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/1e0d9519-fd0c-43cb-a825-ceaaf27731be">
   
4. **Configure Additional Settings**:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/6539e0ba-053d-4b9e-8b24-9a3e0d9c6e10">

7. **Deploy and Manage**:
   - Use tools like SQL Server Management Studio (SSMS) or Azure Data Studio to manage your databases.
   - Implement backup and disaster recovery strategies.
   - Monitor performance and set up alerts for any issues.
