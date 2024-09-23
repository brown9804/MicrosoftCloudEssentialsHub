# Fabric capabilities based on SKU size 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-09-23

------------------------------------------

> Each license level provides different amounts of computational power and features, allowing organizations to choose the one that best fits their needs

## Wiki 

- [Fabric Capacity Size](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#capacity)
- [Workspace license mode and user capabilities](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#workspace)
- [User license and capabilities](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#per-user-licenses)
- [Microsoft Fabric features by SKU](https://learn.microsoft.com/en-us/fabric/enterprise/fabric-features)

## Overview 

Explanation of Power BI SKUs:

- **Power BI SKUs** are applicable to certain licenses because they provide additional resources specifically for Power BI workloads. These SKUs (EM, A, and P series) are designed to support different levels of Power BI usage:
  - **EM SKUs** (Embedded) are for embedding Power BI content in applications.
  - **A SKUs** (Azure) are for Azure-based Power BI services.
  - **P SKUs** (Premium) are for high-end, enterprise-level Power BI capabilities.
- **Not applicable** for smaller licenses (F2, F4) because these licenses are intended for basic data integration and visualization without the need for extensive Power BI resources. These smaller licenses are more suited for individual users or small teams who do not require the advanced features and computational power provided by Power BI SKUs.

Detailed Features by License:

| **License** | **Capacity Units (CU)** | **Power BI SKU** | **Power BI v-cores** | **Features** |
|-------------|-------------------------|------------------|----------------------|--------------|
| **F2**      | 2                       | Not applicable   | 0.25                 | Basic data integration, limited to small datasets. <br/> No advanced AI capabilities. <br/> Suitable for individual users or very small projects. <br/> **Copilot:** No <br/> **AI Skills:** No <br/> **Mirroring:** No |
| **F4**      | 4                       | Not applicable   | 0.5                  | Enhanced data integration, basic data transformation capabilities. <br/> No AI features. <br/> Ideal for small teams. <br/> **Copilot:** No <br/> **AI Skills:** No <br/> **Mirroring:** No |
| **F8**      | 8                       | EM/A1            | 1                    | Includes Data Factory for ETL processes, basic AI capabilities like automated ML. <br/> Suitable for medium-sized teams. <br/> **Copilot:** No <br/> **AI Skills:** Yes <br/> **Mirroring:** No |
| **F16**     | 16                      | EM2/A2           | 2                    | Advanced data integration, Data Factory, and AI capabilities including custom ML models. <br/> Supports larger teams and more complex projects. <br/> **Copilot:** No <br/> **AI Skills:** Yes <br/> **Mirroring:** No |
| **F32**     | 32                      | EM3/A3           | 4                    | High-performance data processing, Data Factory, advanced AI and ML capabilities, including real-time analytics. <br/> Suitable for large teams. <br/> **Copilot:** No <br/> **AI Skills:** Yes <br/> **Mirroring:** No |
| **F64**     | 64                      | P1/A4            | 8                    | Comprehensive data analytics, Data Factory, extensive AI capabilities, including deep learning models. <br/> Ideal for organizations with extensive data needs. <br/> **Copilot:** Yes <br/> **AI Skills:** Yes <br/> **Mirroring:** Yes |
| **F128**    | 128                     | P2/A5            | 16                   | Substantial computational power, Data Factory, advanced AI and ML, including natural language processing (NLP). <br/> Suitable for large-scale projects. <br/> **Copilot:** Yes <br/> **AI Skills:** Yes <br/> **Mirroring:** Yes |
| **F256**    | 256                     | P3/A6            | 32                   | Extensive data processing, Data Factory, full suite of AI capabilities, including computer vision. <br/> Supports very large teams. <br/> **Copilot:** Yes <br/> **AI Skills:** Yes <br/> **Mirroring:** Yes |
| **F512**    | 512                     | P4/A7            | 64                   | High-end data processing, Data Factory, advanced AI and ML, including predictive analytics. <br/> Suitable for large enterprises. <br/> **Copilot:** Yes <br/> **AI Skills:** Yes <br/> **Mirroring:** Yes |
| **F1024**   | 1024                    | P5/A8            | 128                  | Maximum computational power, Data Factory, comprehensive AI capabilities, including advanced analytics and big data processing. <br/> Ideal for large-scale enterprise applications. <br/> **Copilot:** Yes <br/> **AI Skills:** Yes <br/> **Mirroring:** Yes |
| **F2048**   | 2048                    | Not applicable   | 256                  | Ultimate performance, Data Factory, full suite of AI and ML capabilities, including large-scale data processing and analytics. <br/> Suitable for the largest and most complex data environments. <br/> **Copilot:** Yes <br/> **AI Skills:** Yes <br/> **Mirroring:** Yes |

