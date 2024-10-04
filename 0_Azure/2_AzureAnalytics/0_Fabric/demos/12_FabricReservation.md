# Fabric Capacity Reservations

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-04

------------------------------------------

> Each license level provides different amounts of computational power and features, allowing organizations to choose the one that best fits their needs

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>
  
- [Microsoft Fabric trial capacity](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)
- [Buy a Microsoft Fabric subscription](https://learn.microsoft.com/en-us/fabric/enterprise/buy-subscription)
- [Microsoft Fabric pricing table: compute + storage](https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/)
- [Save costs with Microsoft Fabric Capacity reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/fabric-capacity)
- [General availability: Reservations for Microsoft Fabric](https://azure.microsoft.com/en-us/updates/general-availability-fabric-capacity-reservations/)
- [Fabric Capacity Size](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#capacity)
- [Workspace license mode and user capabilities](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#workspace)
- [User license and capabilities](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#per-user-licenses)
- [Microsoft Fabric features by SKU](https://learn.microsoft.com/en-us/fabric/enterprise/fabric-features)
- [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?msockid=38ec3806873362243e122ce086486339)

</details>

## Overview 

| **Benefit**               | **Description**                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------|
| **Cost Savings**          | - **Discounts**: By committing to a one-year reservation, you can save up to 41% compared to pay-as-you-go prices. <br> - **Predictable Costs**: Reservations provide predictable billing, which helps in budgeting and forecasting. |
| **Operational Efficiency**| - **Consistent Workloads**: Ideal for predictable and steady workloads, ensuring you get the most out of your reserved resources. <br> - **Flexibility**: You can exchange or refund reservations if your needs change, providing operational agility. |
| **Payment Flexibility**   | **Upfront or Monthly Payments**: You can choose to pay for reservations upfront or with monthly payments, without any additional fees. |
| **Enhanced Resource Management** | - **Scope Options**: Apply reservations to specific resource groups, subscriptions, or management groups to optimize resource allocation. <br> - **Automatic Application**: The reservation discount automatically applies to matching resources, simplifying management. |
| **Compliance and Governance** | **Policy Enforcement**: Use Azure Policy to ensure resources comply with organizational standards and regulatory requirements. |

## How to make a reservation

1. Sign in to the Azure Portal: Go to the Azure portal and sign in with your Microsoft account credentials.
2. Navigate to Reservations: In the left-hand menu, select **All services** and then **Reservations** or use the search bar.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/cd710088-7b71-4323-873d-b849700063ff">

3. Click on `+ Add`, and select **Microsoft Fabric** from the list of available reservations.

   <img width="298" alt="image" src="https://github.com/user-attachments/assets/3455239f-e704-48ea-bc62-1a4a5a6553fb">

4. Choose a Subscription: Select the subscription you want to use for the reservation.
5. Select a Scope: Define the scope of the reservation
    
    | **Scope Option**         | **Description**                                                                                       |
    |--------------------------|-------------------------------------------------------------------------------------------------------|
    | **Single resource group**| Applies the reservation discount to the matching resources in the selected resource group only.       |
    | **Single subscription**  | Applies the reservation discount to the matching resources in the selected subscription.              |
    | **Shared**               | Applies the reservation discount to matching resources in eligible subscriptions within the billing context. |
    | **Management group**     | Applies the reservation discount to the matching resources in the list of subscriptions that are part of both the management group and billing scope. |

6. Choose a Region: Select the Azure region where the reservation will apply. This is important for ensuring that your resources are located in the desired geographical area.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/7f10db21-d922-4437-acbf-e0a6f383091f">

7. Add to Cart: Add the desired quantity of Capacity Units (CUs) to your cart. For example, if you need 64 CUs, add 64 CUs to your cart.
8. Review and Purchase: Review your selections and proceed to purchase. You can choose to pay upfront or with monthly payments.
9. Manage Your Reservation: After purchasing, you can manage your reservation settings, including enabling automatic renewal if desired.

> Additional Considerations
> - **Service Availability**: Ensure that the services you need are available in the selected region.
> - **Pricing**: Check the pricing for your desired region to ensure it fits within your budget.
> - **Latency**: Consider the proximity of the region to your users to reduce latency and improve performance.
> - **Data Residency and Compliance**: Ensure the region complies with any legal or regulatory requirements for your data.
> - **Availability Zones**: Some regions offer availability zones for enhanced resilience and availability.
> - **Paired Regions**: Consider using paired regions for geo-redundant storage and other services that depend on replication.
