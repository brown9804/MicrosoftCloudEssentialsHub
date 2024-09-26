# Azure Open AI: Quota, Limits, Pricing 
Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)

Last updated: 2024-09-26

 ----------------------------

 ## Wiki 

 - [Azure OpenAI Service quotas and limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits)
 - [Azure OpenAI Service pricing table](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/)
 - [What is provisioned throughput?](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/provisioned-throughput)
 - [How to assign quota](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/quota?tabs=rest#assign-quota)
 - [Provisioned throughput units onboarding](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/provisioned-throughput-onboarding)
 - [Data, privacy, and security for Azure OpenAI Service](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=azure-portal)

 ## Deployments in Azure OpenAI Studio

> `Deployments` in Azure OpenAI Studio involve making AI models, workflows, and applications available for use in production environments. This includes hosting models on servers or in the cloud and creating APIs or other interfaces for users to interact with the models.

Types of deployments available in Azure OpenAI Studio:

| **Deployment Method**       | **Description**                                                                 | **Billing Model**                      | **Deployment Process**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------------|
| Serverless API              | Deploy models as serverless APIs, accessible via endpoints without managing infrastructure. | Pay-as-you-go (per token/request)      | 1. Create a project in Azure OpenAI Studio.<br/>2. Navigate to the project dashboard.<br/>3. Click on `Deployments`.<br/>4. Click `+ Deploy model`.<br/>5. Select a model from the catalog.<br/>6. Configure deployment settings.<br/>7. Click `Deploy`.<br/>8. Use the generated API endpoint to integrate the model. |
| Models as a Service (MaaS)  | Managed service where models are hosted and maintained by Azure.                | Pay-as-you-go (per token)              | 1. Create a project in Azure OpenAI Studio.<br/>2. Navigate to the project dashboard.<br/>3. Click on `Deployments`.<br/>4. Click `+ Deploy model`.<br/>5. Select a model from the catalog.<br/>6. Configure deployment settings.<br/>7. Click `Deploy`.<br/>8. Use the generated API endpoint to integrate the model. |
| Models as a Platform (MaaP) | Deploy models on dedicated virtual machines (VMs) for more control over resources. | Billed as VMs per-hour                 | 1. Create a project in Azure OpenAI Studio.<br/>2. Navigate to the project dashboard.<br/>3. Click on `Deployments`.<br/>4. Click `+ Deploy model`.<br/>5. Select a model from the catalog.<br/>6. Choose VM specifications.<br/>7. Configure deployment settings.<br/>8. Click `Deploy`.<br/>9. Use the generated API endpoint to integrate the model. |
| Flows and Web Applications  | Deploy models as part of larger workflows or web applications.                  | Varies based on usage                  | 1. Create a project in Azure OpenAI Studio.<br/>2. Navigate to the project dashboard.<br/>3. Click on `Deployments`.<br/>4. Click `+ Deploy model`.<br/>5. Select a model from the catalog.<br/>6. Configure deployment settings.<br/>7. Integrate the model into your workflow or web application.<br/>8. Click `Deploy`.<br/>9. Use the generated API endpoint to integrate the model. |
| Managed Compute             | Use Azure's managed compute resources to deploy and run models.                 | Combination of compute and storage costs| 1. Create a project in Azure OpenAI Studio.<br/>2. Navigate to the project dashboard.<br/>3. Click on `Deployments`.<br/>4. Click `+ Deploy model`.<br/>5. Select a model from the catalog.<br/>6. Choose managed compute resources.<br/>7. Configure deployment settings.<br/>8. Click `Deploy`.<br/>9. Use the generated API endpoint to integrate the model. |

1. **Create a Project**: Go to Azure OpenAI Studio, select `New Project`, enter a name, and choose a hub.
2. **Deploy a Model**: Navigate to the project, select `Deployments`, and click `+ Deploy model`.
3. **Select a Model**: Choose a model from the model catalog, such as an Azure OpenAI model.
4. **Configure Deployment**: Specify the deployment name and modify settings as needed.
5. **Deploy**: Click `Deploy` to make the model available as an API.
6. **Integrate and Use**: Use the generated API endpoint to integrate the deployed model with your applications.

## Key considerations to ensure optimal performance, security, and cost-efficiency

| Key Consideration     | Description                                                                |
|-----------------------------|---------------------------------------------------------------------------------|
| **Model Selection**         | - Choose a model that fits your use case. <br/> - Consider performance metrics such as accuracy, latency, and throughput. |
| **Scalability**             | - Configure auto-scaling to handle varying loads. <br/> - Allocate sufficient compute resources to meet expected demand. |
| **Security**                | - Implement data encryption both in transit and at rest to protect sensitive information. <br/> - Use role-based access control (RBAC) to restrict access to the deployed models. |
| **Cost Management**         | - Select the appropriate billing model (e.g., pay-as-you-go, per token/request) based on your usage patterns. <br/> - Regularly monitor usage and costs to avoid unexpected expenses. |
| **Integration**             | - Ensure the deployed model's API endpoints are easily accessible and well-documented for integration with other applications. <br/> - Consider how the model will fit into existing workflows and systems. |
| **Compliance**              | - Ensure your deployment complies with relevant regulations and industry standards. Maintain logs and audit trails for all interactions with the deployed models. |
| **Maintenance and Updates** | - Plan for regular updates and retraining of models to maintain accuracy and relevance. <br/> - Continuously monitor model performance and make adjustments as needed. |
| **User Experience**         | - Optimize for low latency to ensure a smooth user experience. <br/> - Implement mechanisms for users to provide feedback on model performance. |

## How to increase your quota in Azure OpenAI:

1. **Sign in to the Azure Portal**:
   - Open your web browser and go to portal.azure.com.
   - Enter your Azure account credentials to log in.
2. **Navigate to Quotas**:
   - In the search bar at the top of the Azure Portal, type "Quotas".
   - Select "My quotas" from the search results.
3. **Select the Resource**:
   - In the Quotas page, you will see a list of resources.
   - Find and click on the specific resource for which you want to increase the quota (e.g., Azure OpenAI).
4. **Request Quota Increase**:
   - Once you are on the resource page, look for an option that says "Request quota increase" or similar.
   - Click on this option to proceed.
5. **Enter New Limit**:
   - A form will appear where you can specify the new quota limit you need.
   - Enter the desired limit and provide any necessary details or justification for the increase.
6. **Submit the Request**: After filling out the form, click on the "Submit" button to send your request to Microsoft.
7. **Wait for Approval**:
   - Microsoft will review your request. This process may take some time.
   - You will receive a notification once your request has been approved or if additional information is needed.
8. **Check Status**: You can check the status of your quota increase request in the Azure Portal under the "Notifications" or "Support requests" section.


