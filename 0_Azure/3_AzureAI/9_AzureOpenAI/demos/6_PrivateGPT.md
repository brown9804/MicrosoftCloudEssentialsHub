# Building a Private ChatGPT with Azure OpenAI

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-10

------------------------------------------

> This demo is about how to setup secure document searches within a designated network, ensuring that your data remains protected while leveraging the capabilities of Azure OpenAI.

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>
  
- [Create a private endpoint for a secure connection to Azure AI Search](https://learn.microsoft.com/en-us/azure/search/service-create-private-endpoint#use-the-azure-portal-to-access-a-private-search-service)
 
</details>

## How to 

> `same/different vent` -> `shared access` can be used <br/>
> `same vnet` -> `private endpoint` <br/>
> `different vnet` -> needs `vnet peering`

### Create an Azure OpenAI Resource:

- Sign in to the Azure portal.
- Navigate to `Create a resource` and search for `Azure OpenAI`.
- Configure the Resource: Follow the prompts to configure the resource
  - Subscription: Choose your subscription.
  - Resource Group: Create a new resource group or select an existing one.
  - Region: Choose the region closest to your users.
  - Name: Provide a unique name for your Azure OpenAI resource.
- Review and Create: Review your configuration and select `Create`.

 <img width="550" alt="image" src="https://github.com/user-attachments/assets/51f14c45-4167-48cb-9961-fa291ef78fea">

 <img width="550" alt="image" src="https://github.com/user-attachments/assets/d68922eb-b54d-4257-82aa-2d8e45128e32">

### Set Up Azure AI Search:

 - Create Azure AI Search Resource: In the Azure portal, create a new Azure AI Search resource.
 - Configure Search Service: Provide the necessary details
    - Name: Enter a name for your search service.
    - Resource Group: Use the same resource group as your Azure OpenAI resource.
    - Location: Use the same region for reduced latency.
    - Pricing Tier: Select a pricing tier based on your needs.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/09222c27-994f-44b6-bf04-fa9c3d0fb07e">

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/9420a863-f22c-4236-9687-9e3799af15c8">
    
- Establish the network connection by choosing to either set up the resource with a public configuration and adjust the network settings later, or integrate the network configuration during the resource creation process.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/b16c4621-9645-4c8f-9378-fb6674a7f7c6">

> [!NOTE]  
> About the exception checkmark `Allow Azure services on the trusted services list to access this search service`: <br/>
> This setting `allows trusted Azure services to bypass the network rules` and access your resource directly.
> These include services `like Azure Backup, Azure Site Recovery`, and others that are part of the trusted services list.
> Even with this setting enabled, `proper authentication is still required` to access the resource, such as Managed Identity or Service Principal.
> `Only resources within the specified IP address ranges or virtual networks will have access`.
> Resources from other tenants or subscriptions will not have access `unless they are explicitly granted access through the whitelist or fall under the allowed exceptions`.
> This setting is particularly useful for scenarios where you want to allow Azure Site Recovery to access your search service for disaster recovery purposes without needing to configure additional network rules.

### Integrate with Virtual Network (VNet)

>  Deploy your VMs, Azure AI Search, and Azure OpenAI within the VNet.

```mermaid
graph TD
    subgraph VNet["Virtual Network"]
        direction TB
        VM["VM"]
        SearchService["AI Search"]
        OpenAI["OpenAI"]
        NSG["NSG"]
        Subnet["Subnet"]
        NIC_VM["NIC VM"]
        NIC_SearchService["NIC AI Search"]
        NIC_OpenAI["NIC OpenAI"]
        PE_VM["Private Endpoint VM"]
        PE_SearchService["Private Endpoint AI Search"]
        PE_OpenAI["Private Endpoint OpenAI"]
        
        VM --> NIC_VM
        NIC_VM --> NSG
        NIC_VM --> Subnet
        NIC_VM --> PE_VM
        
        SearchService --> NIC_SearchService
        NIC_SearchService --> NSG
        NIC_SearchService --> Subnet
        NIC_SearchService --> PE_SearchService
        
        OpenAI --> NIC_OpenAI
        NIC_OpenAI --> NSG
        NIC_OpenAI --> Subnet
        NIC_OpenAI --> PE_OpenAI
        
        NSG --> Subnet
    end
```

1. **Navigate to VNet**: In the Azure portal, go to`Virtual networks` and select your VNet.
2. **Subnets**: Ensure that your subnets are correctly configured and have the necessary address space.
3. **Service Endpoints**: Add service endpoints for Azure OpenAI and Azure AI Search.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/3dcec8bc-8ee1-48ec-b262-d49c18e04436">
    
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/15332c2d-6df7-4663-88ea-414b64eacf47">
  
    <img width="951" alt="image" src="https://github.com/user-attachments/assets/1c5052b7-10ea-4d92-b54c-42d9777e9f5a">

### Configure Private Endpoints for Azure AI Search

1. **Navigate to Private Endpoint**: In the Azure portal, go to your Azure AI Search resource and select `Networking` > `Private endpoint connections`.
2. **Add Private Endpoint**: Click on `+ Private endpoint` to add a new private endpoint.
3. **Configure Private Endpoint**: Follow the prompts to configure the private endpoint
   - **Name**: Provide a name for the private endpoint.
   - **Virtual Network**: Select the same virtual network and subnet as used for Azure OpenAI.
   - **Integration**: Integrate with your DNS for name resolution.
4. **Approve Connection**: Once the private endpoint is created, approve the connection. 

  | **Network Configuration**            | **Use Case**                                                                                                                                   | **Considerations**                                                                                                                                                                                                 |
  |------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | **Shared Private Access** | - Simplifies the configuration by allowing you to create a private endpoint connection from Azure AI Search to Azure OpenAI without manually setting up private endpoints.<br>- Suitable when you want to establish a secure connection between resources in the same or different VNets.<br>- The connection must be approved by the owner of the target resource, adding an extra layer of security. | - VNet Peering or VPN Gateway is required if Azure AI Search and Azure OpenAI are in different VNets.<br>- Network Security Groups (NSGs) should be configured to allow traffic between the VNets if they are peered. |
  | **Private Endpoint Connection** | - Provides a network interface that connects you privately and securely to a service powered by Azure Private Link.<br>- Ideal for securing the connection between Azure AI Search and Azure OpenAI within the same Virtual Network.<br>- Offers a higher level of security by ensuring that the connection remains within the VNet.<br>- Can offer better performance as the traffic remains within the Azure backbone network. | - Requires manual setup of private endpoints for both Azure AI Search and Azure OpenAI.<br>- DNS settings must be correctly configured to resolve the private endpoints.                                                |
  | **VNet Peering**       | - Enables resources in different VNets to communicate with low latency and high bandwidth, as if they were within the same network.<br>- Useful when Azure AI Search and Azure OpenAI are in different VNets.<br>- Allows full connectivity between VNets, making it suitable for scenarios where multiple resources need to communicate across VNets. | - Peering links must be created in both VNets.<br>- NSGs should be configured to allow traffic from the peered VNet.<br>- Additional costs may be incurred for data transfer between VNets.                            |

  - Search for the resource ID of the Azure OpenAI service:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/d94492b6-f0cb-4a32-b5b9-9bf895fb464c">

 - Create the shared private link or the `private endpoint` as needed:

   > Shared private access:
   
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/0c1e7ca2-344d-4140-bf37-8dc1d2afa669">

    > Private Endpoint:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/1e59a0fc-9bc5-49fb-aa80-29fa47cd92f7">

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/3db7df26-b7ca-4519-b8bf-6f4abc9d5441">

    - While doing this you can also setup the Network Security Group (NSG) if it's not already set up.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/7f5a9363-e6da-4552-9375-8384e6a3bbc2">

### Configure Private Endpoints for Azure OpenAI

1. **Navigate to Private Endpoint**: In the Azure portal, go to your Azure OpenAI resource and select `Networking` > `Private endpoint connections`.
2. **Add Private Endpoint**: Click on `+ Private endpoint` to add a new private endpoint.
3. **Configure Private Endpoint**: Follow the prompts to configure the private endpoint:
   - **Name**: Provide a name for the private endpoint.
   - **Virtual Network**: Select the virtual network and subnet where the endpoint will be deployed.
   - **Integration**: Integrate with your DNS for name resolution.
4. **Approve Connection**: Once the private endpoint is created, approve the connection.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/10a3610c-a6a0-448a-ba54-389c1424f326">

  <img width="433" alt="image" src="https://github.com/user-attachments/assets/31aa0106-f734-42ef-9da4-b917bc191b67">

### Set Up Network Security Groups (NSGs)

1. **Create NSG**: In the Azure portal, create a new Network Security Group.
2. **Associate NSG with Subnet**: Associate the NSG with the subnet where your private endpoints are deployed.
3. **Configure Security Rules**: Add inbound and outbound security rules to allow traffic only from your specific network.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/669186f7-329e-4423-8359-27434b358ed2">
   

### Create index/Upload Documents 

> Since now we are in a private network, Azure AI Search only admits requests from clients in a virtual network instead of over a public internet. So we need to create a VM, and set that VM in a VNET. Click [here for a more detailed guide on how to Create a private endpoint for a secure connection to Azure AI Search](https://learn.microsoft.com/en-us/azure/search/service-create-private-endpoint#use-the-azure-portal-to-access-a-private-search-service)

> Connect the Azure AI Search service with the VNET:

- Create a virtual machine:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/e01ae8cd-b421-4d13-8b98-4812541e7d86">

  - Provide the necessary details:

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/34fce8f1-ddf5-4cfa-8306-6c03f59c1cf7">






- Create Index: Once the search service is created, set up an index to store your documents.

   <img width="310" alt="image" src="https://github.com/user-attachments/assets/7304b542-7bc9-4c59-a2a3-ae81d6be113a">

- Upload Documents: Use the data import wizard to upload your documents and configure the indexer to parse the content.
     
