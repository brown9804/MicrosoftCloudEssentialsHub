# Baseline Considerations for Deployments on Azure Machine Learning Service

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


| **Category**          | **Considerations**                                                                                   | **Details**                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Architectural**     | Deployment Methods                                                                                   | Choose between real-time (online) inference for low-latency needs and batch (offline) inference for processing large datasets. |
|                       | Consistency                                                                                          | Use containerization (e.g., Docker) or virtualization to ensure consistent environments across development, staging, and production. |
| **Security**          | Network Security                                                                                     | Implement network segmentation, use Network Security Groups (NSGs) to control traffic, and deploy services into a private Virtual Network (VNet). |
|                       | Identity Management                                                                                  | Use Azure Active Directory (AAD) for managing identities and access controls.                     |
|                       | Data Protection                                                                                      | Ensure data at rest and in transit is encrypted. Use managed identities for secure access to resources. |
| **Monitoring & Performance** | Performance Metrics                                                                          | Track metrics such as accuracy, latency, and throughput. Set up alerts to notify you when performance falls below acceptable levels. |
|                       | Application Insights                                                                                 | Utilize built-in monitoring capabilities to view metrics and create alerts for your deployed models. |
| **Compliance**        | Regulatory Compliance                                                                               | Ensure your deployment adheres to relevant regulatory requirements. Use Azure Policy definitions to measure compliance with security benchmarks. |
