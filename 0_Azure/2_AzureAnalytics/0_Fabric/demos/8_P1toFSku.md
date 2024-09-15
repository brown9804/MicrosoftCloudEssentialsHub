# Transition from Power BI Premium (P-SKUs) to Fabric (F-SKUs)

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-09-15

----------

## Wiki 

- [Important update to Power BI Premium licensing](https://www.microsoft.com/en-us/licensing/news/power-bi-premium-sku-retirement)
- [Important update coming to Power BI Premium licensing - Blog](https://powerbi.microsoft.com/en-us/blog/important-update-coming-to-power-bi-premium-licensing/)
- [Microsoft Fabric concepts and licenses](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#per-user-licenses)
- [Moving Fabric (Power BI) Workspaces from Premium or Free Trial to new F SKUs](https://techcommunity.microsoft.com/t5/healthcare-and-life-sciences/moving-fabric-power-bi-workspaces-from-premium-or-free-trial-to/ba-p/4176482)

## Overview 

| Update                          | Details                                                                                                                                                                                                 |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Retirement of P-SKUs**        | - **New Customers**: As of July 1, 2024, new customers will no longer be able to purchase Power BI Premium per capacity (P-SKUs).<br> - **Existing Customers**: Those without an Enterprise Agreement (EA) can renew their P-SKUs until January 1, 2025. After this date, they will need to transition to Fabric SKUs at the end of their agreement. |
| **Transition to Fabric SKUs**   | - **Flexibility**: Fabric SKUs offer more flexibility in terms of size and billing options, including pay-as-you-go.<br> - **Azure Integration**: Fabric SKUs provide access to Azure-only features and are eligible for Microsoft Azure Consumption Commitment (MACC).<br> - **Unified Platform**: Microsoft Fabric combines Power BI, Azure Synapse Analytics, and Azure Data Factory into a single SaaS platform, offering all the capabilities of Power BI Premium plus additional workloads. |
| **Impact on Different Agreements** | - **Enterprise Agreement (EA) Customers**: Can continue to renew their P-SKUs annually until the end of their EA agreement. If the agreement ends after January 1, 2025, they will need to transition to Fabric SKUs.<br> - **Sovereign Cloud Customers**: Not impacted by this change as they do not currently have access to Microsoft Fabric. |

> `P1 SKU`: Best for organizations focused solely on `Power BI` with fixed capacity needs and AutoScale. <br/>
> `F SKU`: Ideal for those looking for a `more integrated, flexible, and scalable solution` that leverages Azure’s full capabilities.

| Feature/Aspect                     | Power BI Premium (P1 SKU)                  | Fabric (F SKU)                              |
|------------------------------------|--------------------------------------------|---------------------------------------------|
| **Flexibility and Scalability**    | Fixed capacity with predefined resource limits. Suitable for organizations with stable, predictable workloads. | Offers flexible options, including pay-as-you-go and various sizes to better match dynamic needs. Ideal for organizations with fluctuating workloads. |
| **Integration with Azure**         | Primarily focused on Power BI capabilities. Limited integration with other Azure services. | Integrates Power BI with Azure Synapse Analytics and Azure Data Factory, providing a unified platform for comprehensive data analytics and processing. |
| **AutoScale Feature**              | Includes AutoScale, which automatically adjusts capacity based on demand, ensuring optimal performance during peak times. | AutoScale is currently not available but is planned for future updates, aiming to provide similar dynamic scaling capabilities. |
| **Azure-Only Features**            | Limited to Power BI features, with no access to exclusive Azure functionalities. | Provides access to additional Azure-only features, enhancing data processing, analytics, and integration capabilities. |
| **Microsoft Azure Consumption Commitment (MACC)** | Not eligible for MACC, meaning Azure consumption commitments cannot be applied towards purchasing P1 SKUs. | Eligible for MACC, allowing organizations to use their Azure consumption commitments towards purchasing Fabric SKUs, optimizing overall cloud spending. |
| **Usage and Workloads**            | Designed for enterprises needing a complete BI solution with fixed capacity. Suitable for stable, predictable BI workloads. | Supports a broader range of workloads, including those from Power BI, Azure Synapse, and Azure Data Factory. Ideal for organizations needing a versatile, integrated data analytics platform. |
| **Performance and Scalability**    | Fixed performance based on the purchased capacity. May require manual adjustments to handle increased demand. | Enhanced performance and scalability options, with the ability to scale resources dynamically based on actual usage and demand. |
| **Cost Management**                | Fixed cost based on the purchased capacity, with potential additional costs for overages. | Flexible cost management with pay-as-you-go options, allowing for better alignment with actual usage and budget optimization. |
| **Support and Maintenance**        | Standard support and maintenance as part of the Power BI Premium offering. | Enhanced support and maintenance options, leveraging the broader Azure ecosystem for comprehensive service management. |
| **Future-Proofing**                | Limited to the current capabilities of Power BI Premium. May require additional investments for future upgrades. | Future-proof with ongoing updates and enhancements as part of the Microsoft Fabric platform, ensuring access to the latest features and innovations. |

## Impact on Existing Reports and Dashboards

| Impact Area            | Details                                                                                                                                                                                                 |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Seamless Transition**| - **No Immediate Changes**: Your existing reports and dashboards will continue to function as they do now during the transition period.<br> - **Migration Support**: Microsoft provides tools and support to help migrate your content from P-SKUs to F-SKUs, ensuring a smooth transition. |
| **Enhanced Capabilities** | - **New Features**: Once migrated, you’ll have access to additional features and capabilities available in Microsoft Fabric, which can enhance your reports and dashboards.<br> - **Improved Performance**: Fabric SKUs are designed to offer better performance and scalability, which can improve the responsiveness and efficiency of your reports. |
| **Integration with Azure** | **Azure-Only Features**: You’ll gain access to Azure-only features that can be integrated into your existing reports and dashboards, providing more advanced analytics and data processing options. |
| **No Data Loss**       | **Data Integrity**: The migration process ensures that there is no loss of data or functionality in your existing reports and dashboards. |

Here's a step-by-step guide to help you transition from Power BI Premium (P1 SKU) to Fabric (F SKU):

## How to transition 

1. **Review Current Capacity and Usage**:
   - **Assess Current Usage**: Evaluate your current Power BI Premium capacity usage to understand your needs.
   - **Identify Workspaces**: List all workspaces currently using P1 SKUs.
2. **Plan the Transition**:
   - **Set a Timeline**: Determine a timeline for the transition, considering your current agreement's renewal date.
   - **Communicate with Stakeholders**: Inform all relevant stakeholders about the upcoming changes and timeline.
3. **Purchase Fabric SKU**:
   - **Access Azure Portal**: Log in to the Azure portal.
   - **Navigate to Power BI**: Go to the Power BI section and select `Purchase Services`.
   - **Select Fabric SKU**: Choose the appropriate Fabric SKU based on your needs and complete the purchase.
4. **Migrate Workspaces**:
    1. Access Power BI Admin Portal
       - **Log In**: Open your web browser and go to the Power BI Admin portal. Log in using your administrator credentials.
       - **Navigate to Admin Portal**: Once logged in, click on the gear icon (⚙️) in the top right corner and select `Admin Portal` from the dropdown menu.

           <img width="550" alt="image" src="https://github.com/user-attachments/assets/ec0c32dc-17aa-46c5-9912-1f5920d7e0d3">

    2. Select Workspaces
       - **Go to Workspaces**: In the Admin Portal, navigate to the `Workspaces` section. This will display a list of all the workspaces in your organization.
       - **Identify Workspaces**: Identify the workspaces currently assigned to the P1 SKU that you want to migrate to the Fabric SKU.

           <img width="550" alt="image" src="https://github.com/user-attachments/assets/d9441ad8-1919-49c5-baf4-e0eaec050332">

    3. Reassign Capacity
       - **Select Workspace**: Click on the workspace you want to migrate. This will open the workspace settings.
       - **Change Capacity**: In the workspace settings, look for the `Capacity` section. You will see an option to change the capacity assignment.
       - **Select Fabric SKU**: From the dropdown menu, select the new Fabric SKU that you have purchased.
       - **Save Changes**: Click "Save" to apply the changes. The workspace will now be reassigned to the new Fabric SKU.

            <img width="550" alt="image" src="https://github.com/user-attachments/assets/3587658e-50b8-484a-b048-07de018a15fe">

5. **Verify Migration**:
   - **Check Functionality**: Ensure all reports and dashboards are functioning correctly after the migration.
   - **Monitor Performance**: Monitor the performance of your reports and dashboards to ensure they meet your expectations.
6. **Update Documentation and Training**:
   - **Update Internal Documentation**: Reflect the changes in your internal documentation.
   - **Train Users**: Provide training sessions for users to familiarize them with any new features and capabilities of the Fabric SKU.
