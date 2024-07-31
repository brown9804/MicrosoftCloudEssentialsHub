# Data Protection and Management

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-07-30

----------

Understanding the distinctions between data governance, management, and security is essential for effective data handling and protection. The table below highlights these differences, including relevant Microsoft products and usage examples. 

| **Category**       | **Definition**                                                                 | **Focus**                                      | **Activities**                                                                 | **Microsoft Products**                          | **Examples of Use**                                                                 |
|--------------------|--------------------------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------|
| **Data Governance**| Establishes policies, procedures, and standards for data usage and protection. | Ensures data is managed as a critical asset.   | Setting data policies, data quality standards, compliance measures, data stewardship. | Microsoft Purview                              | Defining data policies for compliance with GDPR, managing data lineage.             |
| **Data Management**| Encompasses the entire lifecycle of data, from creation to disposal.           | Implements policies and procedures for data.   | Data preparation, data pipelines, ETL processes, data cataloging, data warehousing.  | Azure Data Factory, Azure Synapse Analytics    | Building data pipelines for ETL, managing a data warehouse for business analytics.  |
| **Data Security**  | Protects data from unauthorized access, breaches, and other threats.           | Ensures confidentiality, integrity, availability of data. | Implementing encryption, access controls, monitoring for threats.                   | Azure Security Center, Azure Sentinel          | Encrypting sensitive data, monitoring for security breaches, setting access controls.|

## How to connect Azure Blob Storage with Snowflake


| Connection Method                                | Description                                                                 | Security Level       | Cost Estimate (Monthly) |
|--------------------------------------------------|-----------------------------------------------------------------------------|----------------------|-------------------------|
| **Azure Private Link**                           | Provides private connectivity, keeping traffic within the Azure network.    | Very High            | High                    |
| **Storage Integration with Azure Service Principal** | Uses Snowflake storage integration for secure authentication.               | High                 | Medium                  |
| **Azure Data Factory (ADF)**                     | Securely transfers data using managed identities.                           | High                 | Medium                  |
| **Snowpipe with Azure Event Grid**               | Automates data ingestion with secure configurations.                        | Medium to High       | Medium                  |
| **Shared Access Signature (SAS) Token**          | Provides limited access to storage resources.                               | Medium               | Low                     |
| **Direct Credentials**                           | Uses storage account keys or access keys.                                   | Low                  | Low                     |
| **Firewall Settings and Whitelisting IP Ranges** | Additional security measures to restrict access and enhance security.       | Medium to High       | Low to Medium           |

> Applying firewall settings and whitelisting IP ranges enhances security by restricting access, though they aren't direct connection methods.

