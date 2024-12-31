# Fabric capabilities based on SKU size 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-12-31

------------------------------------------

> Each license level provides different amounts of computational power and features, allowing organizations to choose the one that best fits their needs

## Wiki 

- [Microsoft Fabric trial capacity](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)
- [Buy a Microsoft Fabric subscription](https://learn.microsoft.com/en-us/fabric/enterprise/buy-subscription)
- [Microsoft Fabric pricing table: compute + storage](https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/)
- [Mirroring - Free storage limits](https://community.fabric.microsoft.com/t5/General-Discussion/Mirroring-Free-storage-limits/m-p/3807187)
- [Save costs with Microsoft Fabric Capacity reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/fabric-capacity)
- [Fabric Capacity Size](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#capacity)
- [Workspace license mode and user capabilities](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#workspace)
- [User license and capabilities](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#per-user-licenses)
- [Microsoft Fabric features by SKU](https://learn.microsoft.com/en-us/fabric/enterprise/fabric-features)
- [Understand how consumption is calculated](https://learn.microsoft.com/en-us/fabric/enterprise/plan-capacity#understand-how-consumption-is-calculated)
- [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?msockid=38ec3806873362243e122ce086486339)
- [Fabric Capacity and OneLake Consumption](https://learn.microsoft.com/en-us/fabric/onelake/onelake-capacity-consumption)

## Overview 

Explanation of Power BI SKUs:

- **Power BI SKUs** are applicable to certain licenses because they provide additional resources specifically for Power BI workloads. These SKUs (EM, A, and P series) are designed to support different levels of Power BI usage:
  - **EM SKUs** (Embedded) are for embedding Power BI content in applications.
  - **A SKUs** (Azure) are for Azure-based Power BI services.
  - **P SKUs** (Premium) are for high-end, enterprise-level Power BI capabilities.
- **Not applicable** for smaller licenses (F2, F4) because these licenses are intended for basic data integration and visualization without the need for extensive Power BI resources. These smaller licenses are more suited for individual users or small teams who do not require the advanced features and computational power provided by Power BI SKUs.

Detailed Features by License:

> [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?msockid=38ec3806873362243e122ce086486339) will calculate storage costs if you exceed the included limit for your selected SKU. If your usage stays within the included storage capacity, you shouldn’t see additional charges for storage. <br/> <br/> 
> The included storage in Microsoft Fabric primarily applies to **mirroring** across all F SKUs. This means that the free storage provided (e.g., 64 TB for F64) is specifically allocated for creating mirrored copies of your data to ensure redundancy and high availability. <br/> <br/>
> For other types of storage, such as general data storage or storage used by Data Factory and AI capabilities, you will be billed if you exceed the included storage or if compute capacity is paused.This applies to all F SKUs, from F2 to F2048.

> [!NOTE]
> - `Capacity Units (CU)`: Measure of compute power within a SKU. Higher CUs provide more computational capacity. <br/>
> - `Power BI SKU`: Different SKUs (A, EM, P, F) cater to various needs from individual users to large enterprises. <br/>
> - `Power BI v-cores`: Virtual cores dedicated to Power BI operations, ensuring consistent performance. <br/>
> - `Included Storage`: Amount of storage included with each license. Additional storage is billed separately. <br/>
> - `Max Concurrent Users`: The maximum number of users that can simultaneously access the service. <br/>
> - `Billing for Storage`: Storage is billed when usage exceeds included storage or if compute capacity is paused.
> - `Features`: Range from basic data integration to advanced AI and ML capabilities, including real-time analytics, deep learning models, and natural language processing. <br/>

| **License**   | **Capacity Units (CU)** | **Power BI SKU** | **Power BI v-cores** | **Included Storage** | **Max Concurrent Users** | **Features**                                                                                                                                                                                                 |
|---------------|-------------------------|------------------|----------------------|----------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Free Trial**| 64                      | Not applicable   | 8                    | 64 TB                | 100                      | Comprehensive data analytics, Data Factory, extensive AI capabilities, including deep learning models. Ideal for organizations with extensive data needs. **Copilot:** No **AI Skills:** Yes |
| **F2**        | 2                       | Not applicable   | 0.25                 | 2 TB                 | 10                       | Basic data integration, limited to small datasets. No advanced AI capabilities. Suitable for individual users or very small projects. **Copilot:** No **AI Skills:** No |
| **F4**        | 4                       | Not applicable   | 0.5                  | 4 TB                 | 20                       | Enhanced data integration, basic data transformation capabilities. No AI features. Ideal for small teams. **Copilot:** No **AI Skills:** No |
| **F8**        | 8                       | EM/A1            | 1                    | 8 TB                 | 50                       | Includes Data Factory for ETL processes, basic AI capabilities like automated ML. Suitable for medium-sized teams. **Copilot:** No **AI Skills:** Yes |
| **F16**       | 16                      | EM2/A2           | 2                    | 16 TB                | 100                      | Advanced data integration, Data Factory, and AI capabilities including custom ML models. Supports larger teams and more complex projects. **Copilot:** No **AI Skills:** Yes |
| **F32**       | 32                      | EM3/A3           | 4                    | 32 TB                | 200                      | High-performance data processing, Data Factory, advanced AI and ML capabilities, including real-time analytics. Suitable for large teams. **Copilot:** No **AI Skills:** Yes |
| **F64**       | 64                      | P1/A4            | 8                    | 64 TB                | 500                      | Comprehensive data analytics, Data Factory, extensive AI capabilities, including deep learning models. Ideal for organizations with extensive data needs. **Copilot:** Yes **AI Skills:** Yes |
| **F128**      | 128                     | P2/A5            | 16                   | 128 TB               | 1000                     | Substantial computational power, Data Factory, advanced AI and ML, including natural language processing (NLP). Suitable for large-scale projects. **Copilot:** Yes **AI Skills:** Yes |
| **F256**      | 256                     | P3/A6            | 32                   | 256 TB               | 2000                     | Extensive data processing, Data Factory, full suite of AI capabilities, including computer vision. Supports very large teams. **Copilot:** Yes **AI Skills:** Yes |
| **F512**      | 512                     | P4/A7            | 64                   | 512 TB               | 5000                     | High-end data processing, Data Factory, advanced AI and ML, including predictive analytics. Suitable for large enterprises. **Copilot:** Yes **AI Skills:** Yes |
| **F1024**     | 1024                    | P5/A8            | 128                  | 1024 TB              | 10000                    | Maximum computational power, Data Factory, comprehensive AI capabilities, including advanced analytics and big data processing. Ideal for large-scale enterprise applications. **Copilot:** Yes **AI Skills:** Yes |
| **F2048**     | 2048                    | Not applicable   | 256                  | 2048 TB              | 20000                    | Ultimate performance, Data Factory, full suite of AI and ML capabilities, including large-scale data processing and analytics. Suitable for the largest and most complex data environments. **Copilot:** Yes **AI Skills:** Yes |

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
