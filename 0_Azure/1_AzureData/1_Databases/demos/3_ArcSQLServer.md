# Arc SQL Server - Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-15

----------

> Once Azure Arc is connected, you can manage your SQL Server instances from the Azure portal, allowing you to view detailed inventory, run cross-SQL Server queries, and optimize configurations based on best practices

## Wiki 

- [Overview - SQL Server enabled by Azure Arc](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/overview?view=sql-server-ver16)
- [Benefit from Azure Arc-enabled SQL Managed Instance](https://techcommunity.microsoft.com/t5/azure-arc-blog/benefit-from-azure-arc-enabled-sql-managed-instance-even-without/ba-p/3259167)
- [Enabling hybrid solutions on any cloud, on any infrastructure](https://techcommunity.microsoft.com/t5/azure-arc-blog/enabling-hybrid-solutions-on-any-cloud-on-any-infrastructure/ba-p/2476120)
- [Public preview: Bring enhanced manageability to your SQL Server](https://azure.microsoft.com/en-us/updates/public-preview-bring-enhanced-manageability-to-your-sql-server-anywhere-with-azure-arc/)
- [Azure Arc: Extending Azure management to any infrastructure](https://azure.microsoft.com/en-us/blog/azure-arc-extending-azure-management-to-any-infrastructure/)
- [Best practices assessment for Azure Arc Enabled SQL Server](https://techcommunity.microsoft.com/t5/azure-arc-blog/evaluate-sql-server-configuration-using-best-practices/ba-p/3773382)
- [Prerequisites - SQL Server enabled by Azure Arc](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/prerequisites?view=sql-server-ver16&tabs=azure)
- [Understanding Azure Arc Enabled SQL Server](https://learn.microsoft.com/en-us/shows/data-exposed/understanding-azure-arc-enabled-sql-server)
- [Connect on-premises machines - Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-machines)
- [Plan and deploy Azure Arc-enabled servers - Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/servers/plan-at-scale-deployment)
- [3 steps to secure your multicloud and hybrid infrastructure with Azure Arc](https://www.microsoft.com/en-us/security/blog/2022/03/29/3-steps-to-secure-your-multicloud-and-hybrid-infrastructure-with-azure-arc/)
- [Azure Arc-enabled server configurations](https://learn.microsoft.com/en-us/azure/architecture/hybrid/azure-arc-hybrid-config)
- [Configure Microsoft Defender for Cloud for Azure Arc-enabled servers](https://learn.microsoft.com/en-us/training/modules/configure-defender-cloud-azure-arc-enabled-servers/)
- [SQL Managed Instance enabled by Azure Arc Overview](https://learn.microsoft.com/en-us/azure/azure-arc/data/managed-instance-overview)
- [Analyze metrics with Azure Monitor metrics explorer](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/analyze-metrics#pin-charts-to-dashboards)
- [Administer SQL Server with Azure Arc - Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/hybrid/azure-arc-sql-server)

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/df22531f-c57c-43dd-9fdf-d38549ff6926">


| **Benefit**                     | **Description**                                                                                                                                       |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unified Management**          | Manage all SQL Server instances from a single point of control in the Azure portal, including on-premises, multi-cloud, and edge environments.         |
| **Enhanced Security**           | Use Microsoft Entra ID for authentication, providing enhanced security features like multifactor authentication (MFA) and single sign-on (SSO).        |
| **Consistent Updates and Patching** | Receive frequent updates, including servicing patches and new features, ensuring SQL Server instances are always up-to-date with the latest enhancements. |
| **Scalability and Flexibility** | Deploy, manage, and monitor Azure SQL Managed Instance in various environments, including on-premises, edge locations, and public clouds using Kubernetes. |
| **Cloud Benefits in Any Environment** | Extend cloud benefits such as automated backups, high availability, and self-service provisioning to SQL Server instances, regardless of hosting location. |
| **Improved Operational Insights** | Gain comprehensive operational insights across all databases using tools like Azure Monitor, aiding in proactive management and troubleshooting.         |
| **Best Practices Assessment**   | Optimize the configuration of SQL Server instances for performance and security with best practices assessments offering specific recommendations.       |
| **Connectivity Modes**          | Supports both directly connected and indirectly connected modes, benefiting from most services even with intermittent or no internet connectivity.       |


## Where can it be enabled in SQL context

| Environment             | Description                                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **On-Premises**         | You can connect your on-premises SQL Server instances to Azure Arc. This allows you to manage and monitor them through the Azure portal, providing a unified management experience. |
| **Azure**               | Azure Arc can also be used with SQL Server instances running on Azure Virtual Machines (VMs). This extends the capabilities of Azure Arc to your cloud-based SQL Servers, enabling centralized management and governance. |
| **Other Clouds**        | Azure Arc supports SQL Server instances running in other cloud environments, such as AWS or Google Cloud. This ensures you can manage your SQL Servers across different cloud providers from a single pane of glass. |
| **AKS**                 | Running SQL Server in Azure Kubernetes Service (AKS) allows for containerized deployment, scalability, resilience, and integration with other Azure services. This provides a robust, scalable, and flexible solution for managing SQL Server workloads. |
| **Edge Locations**      | SQL Server instances running in edge locations, such as retail stores or remote offices, can be connected to Azure Arc. This allows for centralized management and monitoring of these distributed instances. |
| **Azure VMware Solution** | SQL Server instances running on Azure VMware Solution can also be managed through Azure Arc. This provides a consistent management experience for SQL Servers running in a VMware environment. |
| **Azure Stack HCI**     | SQL Server instances running on Azure Stack HCI (Hyper-Converged Infrastructure) can be connected to Azure Arc. This enables hybrid cloud scenarios where you can manage on-premises resources alongside Azure resources. |

## How to setup Azure Arc on your on-premises SQL Server

> Prerequisites
> 1. **Azure Account**: Ensure you have an active Azure subscription.
> 2. **SQL Server**: Make sure your SQL Server instance is running and you have administrative access, also supported versions include SQL Server 2012 and later.
> 3. **Network**: Open necessary firewall ports to allow communication with Azure services. Ensure outbound connectivity to the Azure Arc Data Processing Service on port 443.
> 4. **Proxy**: If using a proxy server, set the `NO_PROXY` environment variable to exclude proxy traffic for `localhost` and `127.0.0.1`.
> 5. **Resource Providers**: Register the `Microsoft.AzureArcData` and `Microsoft.HybridCompute` resource providers in your Azure subscription.
>     - Go to **Subscriptions**.
>     - Select your subscription.
>     - Under **Settings**, select **Resource providers**.
>     - Search for `Microsoft.AzureArcData` and `Microsoft.HybridCompute`, click **Register**.

  <img width="700" alt="image" src="https://github.com/user-attachments/assets/bfda2892-c917-49f4-a8c0-12feedea116c">

  <img width="700" alt="image" src="https://github.com/user-attachments/assets/250c6f3f-50c0-47e1-8a12-4218c66c0bb6">

### Installation Guide

- Step 1: Install the Azure Arc Agent
   1. **Download the Agent**: Go to the [Azure Arc page](https://learn.microsoft.com/en-us/azure/azure-arc/servers/agent-overview) and download the Azure Arc agent installer.
   2. **Install the Agent**:
      - The user or service principal must have read permission on the subscription and local administrator permission on the operating system to install and configure the Arc agent.
      - For SQL Server, the service account must be a member of the `sysadmin` fixed server role on each SQL Server instance.
      - Run the installer on your SQL Server machine. Follow the prompts to complete the installation.
      - Verify that the Arc connected machine agent is installed and running in `full` mode.
- Step 2: Connect SQL Server to Azure Arc
   1. **Generate Onboarding Script**:
      - In the Azure portal, navigate to **Azure Arc** > **SQL Server** > **+ Add**.
        
        <img width="700" alt="image" src="https://github.com/user-attachments/assets/62f4be21-c24b-490a-bb1e-b41a88711b72">
        
      - Follow the wizard to generate an onboarding script. This script will connect your SQL Server instance to Azure Arc.
   2. **Run the Script**: Execute the script on your SQL Server machine. This will install the necessary extensions and connect your SQL Server instance to Azure Arc.
- Step 3: Validate the Connection
   1. **Check in Azure Portal**:
        - Go to the Azure portal and navigate to **Azure Arc** > **SQL Server**.
        - Ensure your SQL Server instance appears in the list of connected servers.
- Step 4: Configure and Manage
    1. **Configure Settings**: Use the Azure portal to configure settings, apply policies, and manage your SQL Server instance.
        - **Azure Monitor**: Use Azure Monitor to track performance and events for systems running in Azure, on-premises, or in other clouds.
        - **Azure Policy**: Implement Azure Policy guest configuration to audit operating systems and machine configurations.
        - **Azure Log Analytics**: Utilize Azure Log Analytics for data analysis and visualization.
    2. **Monitor and Optimize**: Utilize Azure tools to monitor performance, apply updates, and optimize configurations.
        - **Activate Defender for Cloud**: Once your machines are connected, activate Microsoft Defender for Cloud to monitor and secure your on-premises workloads.
        - **Microsoft Sentinel**: Use Microsoft Sentinel for intelligent security analytics and threat intelligence.

## How to setup Azure Arc on Azure SQL Managed Instance

| Prerequisite                     | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| **Azure Subscription**           | Ensure you have an active Azure subscription.                               |
| **Azure Data Studio**            | Install Azure Data Studio with the Azure Arc extension.                     |
| **Azure CLI**                    | Install the Azure CLI with the `arcdata` extension.                         |
| **Kubernetes Cluster**           | Ensure you have a Kubernetes cluster where the SQL Managed Instance will be deployed. |
| **Azure Arc Data Controller**    | Set up an Azure Arc Data Controller in your Kubernetes cluster.             |

- Step 1: Configure the providers required within the subscription:
> - **Resource Providers**: Register the `Microsoft.AzureArcData`,  `Microsoft.ExtendedLocation`, `Microsoft.KubernetesConfiguration` and `Microsoft.Kubernetes` resource providers in your Azure subscription.
>     - Go to **Subscriptions**.
>     - Select your subscription.
>     - Under **Settings**, select **Resource providers**.
>     - Search for `Microsoft.AzureArcData`, `Microsoft.ExtendedLocation`, `Microsoft.KubernetesConfiguration` and `Microsoft.Kubernetes`, click **Register**.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/bfda2892-c917-49f4-a8c0-12feedea116c">

<img width="550" alt="image" src="https://github.com/user-attachments/assets/7dca4eb1-90af-49a6-be7b-a8d864e8ae87">

<img width="550" alt="image" src="https://github.com/user-attachments/assets/66237fec-c7a4-45f5-bb1f-de794b5fc31e">

- Step 2: AKS cluster needs to meet certain requirements

    | **Category**               | **Details**                                                                                                                                                                                                 |
    |----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Kubernetes Version**     | Ensure your AKS cluster is running a supported version of Kubernetes. Azure Arc-enabled data services typically support the last three stable versions of Kubernetes.                                        |
    | **Node Configuration**     | - **Node Size**: Use nodes with sufficient CPU and memory resources. For production workloads, it's recommended to use at least Standard_D4s_v3 or equivalent. <br/> - **Node Count**: Have a minimum of three nodes to ensure high availability and redundancy. |
    | **Storage**                | - **Persistent Storage**: Configure persistent storage for your AKS cluster. Azure Disk or Azure Files are commonly used for this purpose. <br> - **Storage Class**: Ensure you have a default storage class set up in your cluster. |
    | **Networking**             | - **Network Policies**: Implement network policies to control traffic between pods and services. <br/> - **Load Balancer**: Ensure your cluster has a load balancer configured for external access. |
    | **RBAC**                   | Enable RBAC in your AKS cluster to manage permissions and access control.                                                                                                                                   |
    | **Azure Arc Extensions**   | Install the necessary Azure Arc extensions on your AKS cluster: <br/> `az extension add --name connectedk8s` <br/> `az extension add --name k8s-extension`                                       |
    | **Security**               | Implement security best practices, such as using Azure Policy for Kubernetes, enabling Azure Defender for Kubernetes, and regularly updating your cluster and nodes.                                        |

- Step 3: Install the necessary Azure Arc extensions on your AKS cluster:
    1. Go to your AKS and run the instructions via Azure CLI:

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/8623dd30-6bce-4c2b-9179-9755696363bd">
  
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/5021f8b8-6145-48a1-b2f5-41c37ff12233">

        - Connect your AKS cluster to Azure Arc:  `az connectedk8s connect --name <clusterName> --resource-group <resourceGroupName> --location <location> --tags <key1=value1> <key2=value2> --correlation-id <correlationId>`

            <img width="550" alt="image" src="https://github.com/user-attachments/assets/0c9aee09-3ac0-41a1-b623-c87c8583c21d">

        - Validate is connected:

            <img width="550" alt="image" src="https://github.com/user-attachments/assets/5469daa0-8e97-42b4-a658-8f8cd701be24">

       - Run the following command in the k8s: `az k8s-extension create --name azuremonitor-containers --extension-type Microsoft.AzureMonitor.Containers --scope cluster --cluster-name <clusterName> --resource-group <resourceGroupName> --cluster-type connectedClusters`
       
           <img width="550" alt="image" src="https://github.com/user-attachments/assets/c14d0add-47b8-4ae1-a1d0-39b8494586c8">

        - Validate that the extention was added:
          
            <img width="550" alt="image" src="https://github.com/user-attachments/assets/92c4db6b-c0dc-483b-a6db-a272c7cdd9ec">

       - Run the following command in the k8s: `az aks enable-addons --addons monitoring --name <cluster-name> --resource-group <resource-group-name>`

            <img width="550" alt="image" src="https://github.com/user-attachments/assets/7ef454aa-3d5b-4739-b6a2-8381b8726226">

- Step 4: **Create Custom Location**:
  - Install the required Azure CLI extensions: `az extension add --name customlocation` 
  - Enable the custom locations feature: `az connectedk8s enable-features -n <clusterName> -g <resourceGroupName> --features cluster-connect custom-locations`

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/4069fbaf-0da2-4c46-adb7-d9bb6c58fe60">

  - Create a custom location: `az customlocation create --name <customLocationName> --resource-group <resourceGroupName> --namespace <namespace> --host-resource-id <hostResourceId> --cluster-extension-ids <extensionId> --location <location>`

    | Parameter           | Description                                      |
    |-----------------------|--------------------------------------------------|
    | `<customLocationName>`| The name of your custom location.                |
    | `<resourceGroupName>` | The name of your resource group.                 |
    | `<namespace>`         | The namespace for the custom location.           |
    | `<extensionId>`       | The ID of the cluster extension.                 |
    | `<hostResourceId>`    | The host resource ID of your connected cluster.  |

      - Get the Cluster Extension IDs: `az k8s-extension list --cluster-name <clusterName> --resource-group <resourceGroupName> --cluster-type connectedClusters`
      - Get the Host Resource ID: `az connectedk8s show --name <clusterName> --resource-group <resourceGroupName>`
      - If want to explore the a GUI method, you can go to the Azure portal, navigate to **Custom locations** under **Azure Arc**.
          - Click on **+ Add** and follow the prompts to create a custom location linked to your Kubernetes cluster.
        
            <img width="550" alt="image" src="https://github.com/user-attachments/assets/78a79f8d-aab2-403b-b732-f2d57f505491">
    
            <img width="550" alt="image" src="https://github.com/user-attachments/assets/2b041545-c425-4167-b4aa-592a132c0b28">
    
            <img width="550" alt="image" src="https://github.com/user-attachments/assets/0fb0e335-7c2f-40d6-98a7-ec63dbb2babf">
    
          - Validate that the custom location is created, you should see something like this:
    
            <img width="550" alt="image" src="https://github.com/user-attachments/assets/0ac58efb-8a8e-4097-a049-30ef8dfe8bea">

- Step 5: Set Up Azure Arc Data Controller

  > The Azure Arc data controller is a key component of Azure Arc-enabled data services. It allows you to run Azure data services on-premises, at the edge, and in multi-cloud environments using Kubernetes.
  
    | **Feature**                | **Description**                                                                 |
    |----------------------------|---------------------------------------------------------------------------------|
    | **Provisioning and Management** | Consistent way to provision, manage, and monitor data services across environments. |
    | **Elastic Scaling**        | Scale data services up or down based on demand.                                 |
    | **Automated Updates**      | Ensures data services are always up-to-date with automated updates.             |
    | **High Availability and Backup** | Built-in high availability and backup capabilities for data resilience.         |
    | **Azure Integration**      | Integrates with Azure for additional functionalities like monitoring and security. |

    > Understanding Azure Arc data controller types of connection
    
    | Feature/Aspect                | Directly Connected Mode                                                                 | Indirectly Connected Mode                                                                 |
    |-------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
    | **Real-time Integration**     | Yes, real-time integration with Azure services like Azure Monitor, Security Center, etc. | No, periodic synchronization with Azure                                                   |
    | **Azure Portal Access**       | Full access, manage and monitor directly from the Azure Portal                           | Read-only access, view inventory and details but cannot manage directly                   |
    | **Updates**                   | Automatic updates and patches                                                            | Manual updates and patches                                                                |
    | **Use Cases**                 | Ideal for environments with reliable internet connectivity and real-time monitoring needs | Suitable for highly secure environments or those with limited internet connectivity       |
    | **Kubernetes Requirement**    | Yes, requires a Kubernetes cluster connected to Azure                                    | No, the Azure Arc data controller can be deployed without the Kubernetes cluster being connected to Azure |
    | **Network Requirements**      | Stable and continuous internet connection                                                | Periodic internet connectivity                                                            |
    | **Security**                  | Integrated security features                                                             | More isolation, manual security management                                                |
    | **Management Overhead**       | Lower, due to automation and real-time management                                        | Higher, due to manual updates and limited Azure Portal access                             |

    1. Enable both features:

         `az connectedk8s enable-features -n <cluster-name> -g <resource-group> --features cluster-connect custom-locations`

    2. Create the Data Controller:

       `az arcdata dc create --name <data-controller-name> --resource-group <resource-group> --custom-location <custom-location> --connectivity-mode <direct|indirect> --location <location> --k8s-namespace <namespace>`
       
        - You can also use the Azure Portal:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/d5b8aa74-81f9-4a0f-90f2-315d1d035710">

       - Choose the connection mode:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/da314a80-9c39-4528-9515-8fa95dadb4de">

        - Complete all the required information:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/181a0516-4c8d-4e48-9f32-d5d9ab3dfbb9">

    3. Connect SQL Managed Instance to Azure Arc
       - **Navigate to Azure Arc Data Services**: Go to the Azure portal. In the left-hand menu, select **Azure Arc** > **Data services**.
        
           <img width="550" alt="image" src="https://github.com/user-attachments/assets/8710b913-5f1e-4a6e-af92-cd2cf9f99dca">

       - **Add SQL Managed Instance**:
          - Click on **+ Add**.
          - Select **SQL Managed Instance**.
          - Choose your **Subscription**, **Resource group**, and **Custom location**.
          - Specify the **Name**, **vCores**, **Storage**, and other settings for your SQL Managed Instance.
          - Click **Review + create** and then **Create**.

            <img width="550" alt="image" src="https://github.com/user-attachments/assets/819b7d6e-c4eb-4137-bc66-9659db40a920">

          - Validate the Connection:  Go back to the Azure portal, navigate to **Azure Arc** > **Data services**, and ensure your SQL Managed Instance appears in the list of Arc-enabled data services.

            <img width="550" alt="image" src="https://github.com/user-attachments/assets/e7be6923-ea8a-4545-82e1-49e34e0afe9b">

- Step 6: Manage and Monitor
    - Utilize the Azure portal to manage and monitor your SQL Managed Instance.
    - You can apply policies, monitor performance, and manage security settings.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/4339c27f-ef5c-4ca7-9b4f-58f3a2545462">

## Troubleshooting

- [Resolve errors when enabling or disabling Azure Arc on your AKS workload clusters in AKS enabled by Arc](https://learn.microsoft.com/en-us/azure/aks/hybrid/known-issues-arc)

## Recommended Trainings

- [Implement Azure Arc-enabled SQL Managed Instance in your hybrid environment](https://learn.microsoft.com/en-us/training/paths/get-started-azure-arc-sql-managed-instance/)

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>