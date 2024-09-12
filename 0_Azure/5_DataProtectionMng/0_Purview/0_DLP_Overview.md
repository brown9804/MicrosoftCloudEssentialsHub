# Data Loss Prevention (DLP) in Azure Purview

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-09-12

----------

> `Microsoft Priva` is tailored for managing privacy risks and ensuring compliance with `privacy regulations`. It helps organizations automate privacy operations and manage consent and data subject requests. <br/>
> `Microsoft Purview` offers a broader range of `data governance and protection capabilities`, focusing on securing and managing data across the entire organization, including compliance and risk management.

## Wiki 

- [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
- [Get started with collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started?tabs=purview-portal%2Cpurview)
- [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Announcing machine learning features in Microsoft Purview Data Loss Prevention](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/announcing-machine-learning-features-in-microsoft-purview-data/ba-p/3583916)
- [Common questions on Microsoft Purview Data Loss Prevention for endpoints](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/common-questions-on-microsoft-purview-data-loss-prevention-for/ba-p/3732610)
- [Configure endpoint data loss prevention settings](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings)
- [Use data loss prevention policies for non-Microsoft cloud apps](https://learn.microsoft.com/en-us/purview/dlp-use-policies-non-microsoft-cloud-apps?tabs=purview)
- [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference)
- [Govern your data wherever it resides with Azure Purview](https://azure.microsoft.com/en-us/blog/govern-your-data-wherever-it-resides-with-azure-purview/)
- [Frequently asked questions (FAQ) about Microsoft Purview data governance solutions](https://learn.microsoft.com/en-us/purview/frequently-asked-questions)
- [Data loss prevention Exchange conditions and actions reference](https://learn.microsoft.com/en-us/purview/dlp-exchange-conditions-and-actions)
- [Introducing HTTP and Custom Connector Support for Data Loss Prevention Policies - Power Platform](https://www.microsoft.com/en-us/power-platform/blog/power-automate/introducing-http-and-custom-connector-support-for-data-loss-prevention-policies/)
- [Connector classification - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/dlp-connector-classification)
- [DLP for custom connectors](https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)

## Overview 

> Microsoft Purview is a comprehensive set of solutions designed to help organizations govern, protect, and manage their data across their entire data estate.

| **Feature**                     | **Microsoft Priva**                                                                 | **Microsoft Purview**                                                                 |
|---------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Primary Focus**               | Privacy management and compliance                                                   | Data governance, protection, and compliance                                          |
| **Key Capabilities**            | - Privacy Risk Management<br>- Subject Rights Requests<br>- Consent Management      | - Data Loss Prevention<br>- Information Protection<br>- Insider Risk Management      |
| **Data Handling**               | Focuses on personal data privacy and regulatory compliance                          | Manages and protects data across the entire data estate                              |
| **Integration**                 | Integrates with Microsoft Purview for data classification and labeling               | Integrates with Microsoft 365 and Azure for comprehensive data governance            |
| **Use Cases**                   | - Automating privacy assessments<br>- Managing consent<br>- Handling data subject requests | - Mapping data estate<br>- Classifying and protecting sensitive data<br>- Managing insider risks |
| **Compliance Tools**            | Privacy-specific compliance tools and assessments                                   | Broad compliance tools including audit, eDiscovery, and communication compliance     |
| **Target Users**                | Privacy officers, compliance teams                                                  | Data governance teams, security officers, compliance teams                           |


### Key Features of Microsoft Purview

| **Category**           | **Feature**                        | **Description**                                                                 |
|------------------------|------------------------------------|---------------------------------------------------------------------------------|
| **Data Security**      | Data Loss Prevention               | Protects sensitive information from risky and unauthorized access.              |
|                        | Information Protection             | Identifies, classifies, and protects sensitive data.                            |
|                        | Insider Risk Management            | Detects and acts on critical risks like data theft and leaks.                   |
|                        | Privileged Access Management       | Manages and secures privileged access to sensitive data.                        |
| **Data Governance**    | Data Map                           | Registers and scans data sources to map the data estate and identify sensitive data. |
|                        | Data Catalog                       | Curates data sources, manages data integrity, and secures sensitive data.       |
|                        | Unified Data Governance            | Manages data services across on-premises, multicloud, and SaaS environments.    |
| **Risk and Compliance**| Audit                              | Supports forensic investigations and meets regulatory requirements.             |
|                        | Communication Compliance           | Detects sensitive or inappropriate content in communication channels.           |
|                        | Compliance Manager                 | Translates regulatory requirements into specific improvement actions.           |
|                        | eDiscovery                         | Manages data for internal or legal investigations.                              |


### Benefits of Microsoft Purview

| **Benefit**                       | **Description**                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------|
| Visibility                        | Gain insights into data across your organization.                               |
| Security                          | Safeguard data throughout its lifecycle.                                        |
| Governance                        | Seamlessly govern data in new, comprehensive ways.                              |
| Compliance                        | Minimize compliance risks and meet regulatory requirements.                     |
| Sensitive Data Detection          | Identifies sensitive information using deep content analysis.                   |
| Policy Creation and Enforcement   | Allows creation and enforcement of DLP policies across various services.        |
| Machine Learning Integration      | Enhances detection accuracy with machine learning algorithms.                   |
| Comprehensive Monitoring          | Monitors actions on sensitive items and prevents unintentional sharing.         |
| Integration with Sensitivity Labels| Unifies data security and compliance with sensitivity labels from Microsoft Information Protection. |

## Boundaries of DLP without Microsoft Purview

> Data Loss Prevention (DLP) without Microsoft Purview can still be effective, but it has some limitations compared to the comprehensive features offered by Purview.

| Limitation                | Description                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| Limited Integration       | DLP solutions might not integrate as seamlessly with other Microsoft 365 services and third-party applications. |
| Reduced Coverage          | Limited support for non-Windows devices compared to Purview's extensive coverage across Windows, macOS, iOS, and Android. |
| Policy Management         | More challenging to manage and enforce DLP policies without the centralized management capabilities provided by Purview. |
| Advanced Features         | Less robust features like Endpoint DLP and integration with non-Microsoft cloud apps.            |
| Compliance and Reporting  | Fewer advanced compliance and reporting tools to help meet regulatory requirements and monitor data usage effectively. |

## Limitation & Workarounds 

| **Limitation**                   | **Description**                                                                 | **Workaround**                                                                 |
|----------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Policy and Rule Limits           | Constraints on the number of policies and rules you can create. For instance, the maximum number of DLP rules in a tenant is 600, and the maximum size of an individual DLP rule is 100 KB. | - **Prioritize Critical Policies**: Focus on creating policies that address the most critical data protection needs first. <br/> - **Combine Rules**: Where possible, combine multiple conditions into a single rule to stay within the limits. |
| File Type Restrictions           | DLP policies are primarily effective for specific file types, mainly Office files. This can limit the scope of protection for other file formats. | - **Custom Connectors**: Use custom connectors to extend DLP capabilities to other file types and applications. <br/> - **Third-Party Tools**: Integrate third-party DLP solutions that support a broader range of file types. |
| Text Extraction Limits           | The maximum size of text that can be extracted from a file for scanning is 2 MB. | - **Pre-Processing**: Pre-process files to reduce their size before they are scanned by DLP policies. <br/> - **Selective Scanning**: Focus on scanning the most critical parts of documents, such as headers, footers, and specific sections. |
| Policy Size and Complexity       | The maximum size of a DLP policy is 100 KB, which can limit the complexity and number of rules within a single policy. | - **Modular Policies**: Break down complex policies into smaller, modular policies that can be managed more easily. <br/> - **Regular Reviews**: Regularly review and optimize policies to ensure they remain within size limits. |
| Integration Limitations          | The data map in Microsoft Purview does not currently support DLP capabilities for Microsoft 365 apps and services. | - **Manual Processes**: Implement manual processes to complement DLP policies where integration is not supported. <br/> - **Custom Scripts**: Use custom scripts to automate data protection tasks that are not covered by DLP policies. |
| License Restrictions             | Some advanced DLP features are only available with higher-tier licenses, such as Office 365 E5. | - **Evaluate Needs**: Assess your organization's specific needs to determine if higher-tier licenses are necessary. <br/> - **Leverage Available Features**: Make the most of the features available in your current license tier while planning for future upgrades if needed. |

## Azure Cloud Services related with Microsoft Purview 

> These services work together with Microsoft Purview to `provide comprehensive data governance, protection, and management across your entire data estate`.

| **Service**                  | **Description**                                                                 |
|------------------------------|---------------------------------------------------------------------------------|
| **Azure Synapse Analytics**  | Integrates with Purview for data lineage and unified analytics.                  |
| **Azure SQL Database**       | Works with Purview for data classification and governance.                      |
| **Azure Data Factory**       | Connects with Purview for data integration and orchestration.                   |
| **Azure Blob Storage**       | Supports data storage and integrates with Purview for data governance.          |
| **Azure Data Lake Storage**  | Provides scalable storage and integrates with Purview for data management.      |
| **Power BI**                 | Integrates with Purview for data visualization and governance.                  |
| **Azure Cosmos DB**          | Works with Purview for managing and governing globally distributed data.        |
| **Azure SQL Managed Instance** | Supports data governance and classification with Purview.                      |
| **Azure HDInsight**          | Integrates with Purview for big data analytics and governance.                  |
| **Azure Databricks**         | Connects with Purview for advanced analytics and data governance.               |

## Custom Connectors

Find below some examples of custom connectors for Data Loss Prevention (DLP) in Azure Purview. These custom connectors `can be created and managed using the Power Platform admin center`, where you can classify them into different categories such as `Business, Non-Business, or Blocked`. `This classification helps in applying appropriate DLP policies` to ensure data protection across various environments.

1. **Custom API Connectors**:
   - **Example**: A custom connector to a proprietary HR system API to monitor and protect sensitive employee data.
   - **Usage**: This connector can be used to enforce DLP policies on data being transferred between the HR system and other applications.

2. **Third-Party Cloud Services**:
   - **Example**: A custom connector for a third-party cloud storage service like Box or Dropbox.
   - **Usage**: This allows DLP policies to monitor and control the flow of sensitive information to and from these services.

3. **Legacy Systems**:
   - **Example**: A custom connector to a legacy on-premises database.
   - **Usage**: Enables DLP policies to be applied to data being accessed or transferred from older systems that do not natively support modern DLP features.

4. **Custom File Processing Services**:
   - **Example**: A custom connector for a file processing service that converts documents to different formats.
   - **Usage**: Ensures that sensitive information is not inadvertently exposed during the conversion process.

5. **Custom Email Gateways**:
   - **Example**: A custom connector for an email gateway that handles outbound emails.
   - **Usage**: Applies DLP policies to monitor and prevent the leakage of sensitive information through email communications.

## Setting Up Foundational Elements in Azure Purview

### **Data Cataloging**

| **Component**       | **Description**                                                                 | **Best Practices**                                                                 |
|---------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Data Map**        | - Automated Metadata Scanning: Automate the scanning of metadata from various data sources. <br> - Data Lineage: Track the lineage of data to understand its flow from source to destination. | - Use built-in and custom classifiers for accurate data discovery and classification. <br> - Ensure comprehensive lineage tracking for compliance and auditing. |
| **Data Catalog**    | - Governance Domains: Create governance domains to distribute ownership and maintenance tasks. <br> - Glossary Terms: Define glossary terms to standardize data definitions across the organization. | - Distribute governance responsibilities to make data easily discoverable. <br> - Standardize data definitions to enhance understanding and usage. |

### **Handling Data Subject Requests**

| **Component**               | **Description**                                                                 | **Best Practices**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Self-Service Access Requests** | - Access Workflow: Enable users to request access to data assets directly through the Purview catalog. <br> - Data Access Policies: Implement data access policies to ensure only authorized users can access sensitive data. | - Streamline access requests by automating workflows. <br> - Protect privacy and comply with regulations through strict access policies. |

### **Additional Best Practices**

| **Practice**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Federated Governance**    | Adopt a federated governance approach to distribute data governance responsibilities across the organization. |
| **Data Quality and Trust**  | Enhance data quality and trustworthiness by implementing governance-focused actions and creating source-of-truth data products. |
| **Business Value Creation** | Align data governance with business practices to unlock business value and make data more accessible and useful for decision-making. |

