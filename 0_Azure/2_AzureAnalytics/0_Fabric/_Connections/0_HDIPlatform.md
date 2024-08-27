# Connecting Microsoft Fabric to HDI Platform

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-01

----------

## Wiki 

- [Transform data by running an Azure HDInsight activity](https://learn.microsoft.com/en-us/fabric/data-factory/azure-hdinsight-activity)

> Prerequisites: 
>  1. **Install On-Premises Data Gateway**: Ensure you have an on-premises data gateway installed and configured. <br/>
>  2. **Install HDI Client**: Ensure the HDI client is installed on the machine running the on-premises data gateway. 

## How to

```mermaid
graph LR
    A[Install On-Premises Data Gateway] --> B[Install HDI Client]
    B --> C[Configure HDI Client]
    C --> D[Open Data Factory in Microsoft Fabric]
    D --> E[Connect Data Source]
    E --> F[Specify Connection Details]
    F --> G[Set Authentication]
    F --> H[Select Data Gateway]
```

### Set Up HDI Connection
1. **Install HDI Client**: Ensure the HDI client is installed on the machine running the on-premises data gateway.
2. **Configure HDI Client**: Follow the HDI platform's documentation to configure the client.

### Configure Connection in Data Pipeline
1. **Open Data Factory**: Go to the Data Factory pipeline in Microsoft Fabric.
2. **Connect Data Source**: Browse to the "Connect data source" section.
3. **Specify Connection Details**:
   - **Server**: Enter the HDI platform server details.
   - **Connection Name**: Provide a name for your connection.
   - **Data Gateway**: Select your on-premises data gateway.

### Set Authentication
1. **Authentication Kind**: Choose the appropriate authentication type.
2. **Credentials**: Enter your HDI platform credentials.

## Possible Connection Issues and Solutions

```mermaid
graph TD
    A[Client Configuration Issues]
    A1[Check HDI client setup]
    A --> A1

    B[Authentication Errors]
    B1[Verify credentials]
    B --> B1

    C[Data Gateway Issues]
    C1[Ensure data gateway is running]
    C --> C1
```


1. Client Configuration Issues
    - **Issue**: HDI client is not properly configured.
    - **Solution**: Follow the HDI platform's documentation to ensure correct configuration.
2. Authentication Errors
    - **Issue**: Incorrect authentication type or credentials.
    - **Solution**: Verify the authentication type and credentials.
3. Data Gateway Issues
    - **Issue**: On-premises data gateway is not running or not configured correctly.
    - **Solution**: Ensure the data gateway is installed, running, and properly configured.
