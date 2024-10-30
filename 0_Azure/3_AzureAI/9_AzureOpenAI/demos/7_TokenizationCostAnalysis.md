# Azure OpenAI: Tokenization & Cost Analysis 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-30

----------

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>
  
- [Azure OpenAI Service - Pricing](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/openai-service/)
- [Plan to manage costs for Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/manage-costs)
- [Chapter 9 - Cost Management and Optimization](https://azure.github.io/AI-in-Production-Guide/chapters/chapter_09_managing_expedition_cost_management_optimization)
- [Pricing Update: Token Based Billing for Fine Tuning Training](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/pricing-update-token-based-billing-for-fine-tuning-training/ba-p/4164465)
- [Tokenizer - tool from OpenAI](https://platform.openai.com/tokenizer)
- [Customize views in cost analysis](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/customize-cost-analysis-views)
- [Group and filter options in Cost analysis and budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/group-filter)
- [Manage costs with automation](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/manage-automation)
- [Group and allocate costs using tag inheritance](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance)
- [Tags - List](https://learn.microsoft.com/en-us/rest/api/resources/tags/list?view=rest-resources-2021-04-01)
  
</details>

## Cost Analysis 

> Azure OpenAI Service provides several ways to track and analyze costs, including model usage and cost distribution.

| **Key Point** | **Details** |
|---------------|-------------|
| **Cost Management and Analysis** | Use **Cost Management + Billing** in the Azure portal to: <ul><li>**Track costs** associated with Azure OpenAI Service.</li><li>**Analyze cost patterns** and identify spending trends.</li><li>**Set budgets** and create alerts for overspending.</li></ul> |
| **Cost Analysis for Azure OpenAI Service** | In the **Cost analysis** section of the Azure portal, you can: <ul><li>**Group costs** by various attributes, such as resource group, location, or meter.</li><li>**Filter costs** to focus on specific resources or services.</li><li>**Visualize costs** over time to understand spending patterns.</li></ul> |
| **Pricing Models** | Azure OpenAI Service supports different pricing models, including: <ul><li>**Standard (On-Demand)**: Pay only for the tokens processed.</li><li>**Provisioned Throughput Units (PTUs)**: Ensure consistent throughput and minimal latency variance for scalable solutions.</li></ul> |
| **Detailed Pricing Information** | The pricing details for Azure OpenAI Service are available on the  [Azure OpenAI Service pricing page](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/). This includes costs per **1,000,000 tokens** for various models and the rates for PTUs. |
| **Monitoring Usage** | You can monitor the usage of different models and their associated costs. Azure provides metrics and logs that can help you understand the usage patterns of your deployed models. |
| **Exporting Cost Data** | For more advanced analysis, you can export your cost data to a storage account. This allows you to use tools like Excel or Power BI for custom reporting and analysis. |
| **Budgeting and Alerts** | You can create budgets in Azure Cost Management and set alerts to notify you when spending exceeds predefined thresholds. |

## Deployments type

| Deployment Type   | Best Suited For                                                                 | How It Works                                                                 | Cost                                                                 | Tokenization                                                                 |
|-------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| Global-Batch      | Offline scoring, non-latency sensitive workloads                                 | Asynchronous groups of requests with separate quota, 24-hour target turnaround | Least expensive                                                      | Tokens calculated based on input file and generated output                  |
| Global-Standard   | Recommended starting place for customers                                        | Traffic may be routed anywhere in the world                                  | Access to all new models with larger quota allocations, Global pricing | Tokens calculated per request, including both input and output tokens       |
| Global-Provisioned| Real-time scoring for large consistent volume                                   | Traffic may be routed anywhere in the world                                  | Cost savings for consistent usage, Regional pricing                   | Tokens calculated per request, including both input and output tokens       |
| Standard          | Optimized for low to medium volume, real-time scoring for large consistent volume| Traffic may be routed anywhere in the world                                  | Pay-per-call flexibility                                              | Tokens calculated per request, including both input and output tokens       |
| Provisioned       | Use cases with data residency requirements                                      | Regional access with very high & predictable throughput                      | Hourly billing with optional purchase of monthly or yearly reservations | Tokens calculated per request, including both input and output tokens       |

## Billing models

| Billing Model                | Description                                                                                     | Cost Calculation                                                                                       | Use Cases                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Pay-As-You-Go                | - Charged based on the number of tokens processed<br/>- Suitable for variable or unpredictable usage patterns | - Cost per unit of tokens, different rates for different model series<br/>- Includes both input and output tokens | - Applications with variable or unpredictable usage patterns<br/>- Flexibility in usage       |
| Provisioned Throughput Units | - Reserved processing capacity for deployments<br/>- Ensures predictable performance and cost<br/>- **Reserved Capacity:** PTU provides reserved processing capacity for your deployments, ensuring predictable performance and cost.<br/>- **Capacity Planning:** It's important to estimate the required PTUs for your workload to optimize performance and cost. The token totals are calculated using the following equation:<br/><br/>$$\text{Total Tokens} = \text{Peak calls per minute} \times (\text{Tokens in prompt call} + \text{Tokens in model response})$$ <br/> Click [here for more explanation on how to calculate it](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/3_AzureAI/9_AzureOpenAI/demos/4_PTUs_TPM.md#ptus-and-tpm-relationship)| - Hourly rate based on the number of PTUs deployed<br/>- Regardless of the number of tokens processed   | - Well-defined, predictable throughput requirements<br/>- Consistent traffic<br/>- Real-time or latency-sensitive applications<br/>- **Cost Predictability:** PTU offers more predictable costs compared to the pay-as-you-go model, which can vary based on usage.<br/>- **Performance Guarantees:** PTU provides guaranteed throughput and latency constraints, which can be beneficial for real-time or latency-sensitive applications. |

## Tokenization 

> Tokenization is the process of breaking down text into smaller units called tokens. In Azure OpenAI Service, tokenization is used to calculate the number of tokens processed, which directly impacts the cost. `Tokens are pieces of words`. When processing text, Azure OpenAI Service breaks down the input into tokens, which `can be as short as one character or as long as one word`.
> These tokens are used by the model to understand and generate text.

Process: 
1. **Text Splitting:** The input text is split into tokens, which can be as short as one character or as long as one word. This splitting is done using a method called **Byte-Pair Encoding (BPE)**.
2. **Byte-Pair Encoding (BPE):** BPE is a tokenization method that merges the most frequently occurring pairs of characters into a single token. This approach is particularly effective in handling rare words and subwords, as it allows the model to break down complex or unseen words into more manageable pieces.
3. **Token Limits:** Each model in Azure OpenAI has a maximum token limit per request. It's important to be aware of these limits when designing your prompts and handling responses.
4. **Tokenization Example:** To illustrate, the word "hamburger" might be tokenized into ["ham", "bur", "ger"], while a common word like "pear" would remain as a single token ["pear"]. Many tokens also start with a whitespace, for example, " hello" and " bye".

| **Process**               | **Description**                                                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Input Tokenization**    | The input text is tokenized into individual tokens. For example, the sentence "Hello, world!" would be tokenized into `["Hello", ",", " world", "!"]`. |
| **Output Tokenization**   | The model’s response is also tokenized. For example, if the model generates the text "Hi there!", it might be tokenized into `["Hi", " there", "!"]`. |
| **Total Tokens Processed**| The total number of tokens processed is the sum of the input tokens and the output tokens.                                                        |
| **Cost Calculation**      | The cost is calculated based on the total number of tokens processed, using the pricing information provided by Azure.                            |


The cost for using Azure OpenAI can be calculated using the following general formula:

$$\text{Cost} = \left( \frac{\text{Number of Tokens}}{N} \right) \times \text{Price per N Tokens}$$

Where:
- **Number of Tokens** is the total number of tokens processed (input tokens + output tokens).
- **N** is the number of tokens for which the price is specified (e.g., 100,000 tokens).
- **Price per N Tokens** is the cost rate for processing N tokens, which varies based on the model and region.

## Optimization: Best Practices Overview

| Optimization Aspect | Technical Details                                                                                     | Best Practices                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Input Optimization  | - **Token Efficiency:** Reducing the number of tokens in the input can significantly lower costs.<br/>- **Prompt Engineering:** Crafting prompts that achieve the desired result with fewer tokens.<br/>- **Context Management:** Including only the necessary context in the input to minimize token usage. | - **Concise Prompts:** Use the shortest possible prompts that still convey the necessary information.<br/>- **Avoid Redundancy:** Remove any repetitive or unnecessary words from the prompts.<br/>- **Template Design:** Design prompt templates that are efficient in terms of token usage. |
| Output Optimization | - **Response Length Control:** Limiting the length of the model's response can help manage and predict costs.<br/>- **Stop Sequences:** Using stop sequences to control where the model should stop generating further tokens.<br/>- **Max Tokens Parameter:** Setting an appropriate limit on the number of tokens in the response. | - **Set Max Tokens:** Use the `max_tokens` parameter to limit the length of the model's response.<br/>- **Use Stop Sequences:** Define stop sequences to control the verbosity of the output.<br/>- **Quality Check:** Regularly review the model's responses to ensure they are within the expected length and quality. |

## Cost Tracking with API calls
> Postman: Is a popular API platform that simplifies the process of building, testing, and managing APIs (Application Programming Interfaces). It provides a user-friendly interface for making HTTP requests, viewing responses, and debugging issues. <br/>
> Azure API Management Developer Portal (API Playground) to track costs with the Azure Cost Management API. 

### Register an Application in Azure AD
1. Go to the **Azure portal**.
2. Navigate to **Azure Entra ID** > **App registrations** > **New registration**.
3. Fill in the required details and register the application.
4. Note down the `clientId`, `clientSecret`, and `tenantId`.
  
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/24f37a9b-2bf1-4d99-9cf0-98e32c0f233a">
  
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/1d27f632-9cf9-4f55-a542-a871ecd55ee3">
  
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/c098a93e-8c1f-47c6-91bf-a3c05daaecfa">

### Grant API Permissions
1. In the Azure portal, go to **Azure Entra ID** > **App registrations** > **Your App** > **API permissions**.
2. Add the necessary permissions, such as `Consumption Billing`.
3. Click on **Grant admin consent** if required.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/2ff80cb7-fef7-4c40-bac8-1442c3c43183">

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/5aa9d4ac-d017-4794-a2a7-5237e0d7f88c">

### Get an Access Token

> Search for the tenant id in `Entra ID`, if you don't have it yet:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/4000b88a-c16f-49c2-9aa5-b0b5c456cbba">

<img width="550" alt="image" src="https://github.com/user-attachments/assets/4db051ce-0f71-4417-aa90-4a05b31a481b">

> Get your `client secret` or create one if needed:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/790de4ac-5d6e-4a86-ae5d-c74f1cdfbf77">

1. Use the OAuth 2.0 client credentials flow to get an access token. 

    ```http
    POST https://login.microsoftonline.com/{tenantId}/oauth2/token
    Content-Type: application/x-www-form-urlencoded
    
    grant_type=client_credentials
    &client_id={clientId}
    &client_secret={clientSecret}
    &resource=https://management.azure.com/
    ```

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/a78a37f9-cd7f-41aa-bc9d-73986c7f46cc">

2. **Use the Access Token** in your API calls:

     ```http
     Authorization: Bearer {accessToken}
     ```

3. **Make API Call**:

> Grant permission before using the access token, you need to assign the app created, you can find it by name:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/61dd61e5-4bba-4c66-bb9d-fa0801b376be">

<img width="550" alt="image" src="https://github.com/user-attachments/assets/28f841fa-3f33-44a3-9e51-3c3931522bcb">

> Retrieve the data and consider applying filters, check the following section for more information:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/00f48833-a34e-48df-848e-d8b104ff272d">

 ```http
 GET https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Consumption/usageDetails?api-version=2019-10-01
 Authorization: Bearer {accessToken}
 ```

### Adding Filters

> [!NOTE]
> General API Call Structure: 
> Azure Cost Management APIs typically follow a RESTful structure. Here's a basic example of an API call to retrieve cost data:

```http
GET https://management.azure.com/{scope}/providers/Microsoft.Consumption/usageDetails?api-version=2019-10-01
```

Key Components:  
1. **Base URL**: `https://management.azure.com/` 
2. **Scope**: This defines the level at which you want to retrieve cost data. It can be a subscription, resource group, or a specific resource. For example: 
    - Subscription: `/subscriptions/{subscriptionId}` 
    - Resource Group: `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}` 
    - Resource: `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}` 
3. **Resource Path**: `/providers/Microsoft.Consumption/usageDetails` 
4. **API Version**: `api-version=2019-10-01` 

> Example API Call: <br/>
> To get usage details for a specific subscription, your API call might look like this:

```http
GET https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Consumption/usageDetails?api-version=2019-10-01
```

You can add various filters to narrow down the data. Here’s a table of common filters:

| **Filter**         | **Description**                                      | **Example**                                                                 |
|--------------------|------------------------------------------------------|-----------------------------------------------------------------------------|
| Date Range         | Filter by a specific date range                      | `$filter=properties/usageStart ge '2023-01-01' and properties/usageEnd le '2023-01-31'` |
| Resource Group     | Filter by resource group name                        | `$filter=properties/resourceGroup eq 'yourResourceGroupName'`               |
| Resource Type      | Filter by resource type                              | `$filter=properties/resourceType eq 'Microsoft.Compute/virtualMachines'`    |
| Meter Category     | Filter by meter category                             | `$filter=properties/meterCategory eq 'Virtual Machines'`                    |
| Tag                | Filter by tag name and value                         | `$filter=tags/yourTagName eq 'yourTagValue'`                                 |
| Location           | Filter by resource location                          | `$filter=properties/location eq 'eastus'`                                   |
| Charge Type        | Filter by type of charge (e.g., usage, purchase)     | `$filter=properties/chargeType eq 'Usage'`                                   |
| Invoice ID         | Filter by specific invoice ID                        | `$filter=properties/invoiceId eq 'yourInvoiceId'`                            |

> Examples API Call with Filters

```http
GET https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Consumption/usageDetails?$filter=properties/usageStart ge '2023-01-01' and properties/usageEnd le '2023-01-31'&api-version=2019-10-01
```

```http
GET https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Consumption/usageDetails?$filter=properties/usageStart ge '2023-01-01' and properties/usageEnd le '2023-01-31' and properties/resourceGroup eq 'yourResourceGroupName' and tags/yourTagName eq 'yourTagValue'&api-version=2019-10-01
Authorization: Bearer {accessToken}
```

## Tagging Resources Demo

### Tagging the Azure OpenAI Resource

1. **Log in to the Azure Portal**: Go to [portal.azure.com](https://portal.azure.com/) and log in with your Azure account.
2. **Navigate to the Azure OpenAI Resource**:
   - In the left-hand menu, select **Resource groups**.
   - Select the resource group that contains your Azure OpenAI resource.
   - Click on the Azure OpenAI resource.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/ba1029b5-3e38-4155-bdcd-83b4ac8d50cf">

3. **Add Tags to the Resource**:
   - In the left-hand menu of the resource, select **Tags**.
   - Add tags to the resource. For example, you can add tags like `Department-Marketing`, `Department-Sales`, etc.
   - Click **Apply**.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/a2040de0-245b-4b77-bf44-a59684d95a01">

### Using Tags in API Calls

> Give the required roles to be able to call the model `(Cognitivie Services User, Cognitive Services OpenAI User)`:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/66b5d293-9d60-47e5-ab90-0dc5602f234d">

<img width="550" alt="image" src="https://github.com/user-attachments/assets/03874b34-c995-4966-8b64-1145cd28863f">

To ensure that API calls from different departments are tagged correctly, you can include the tags in the API requests. Here’s an example of how to do this:

- **Set Up the API Call**:
   - Use the Azure OpenAI API to make requests.
   - Include the tags in the request headers or body as needed.

> **Example API Call with Tags**:
   ```http
   POST https://api.openai.azure.com/v1/engines/davinci-codex/completions
   Content-Type: application/json
   Authorization: Bearer {accessToken}

   {
     "prompt": "Translate the following English text to French: '{text}'",
     "max_tokens": 60,
     "tags": {
       "Department": "Marketing"
     }
   }
   ```

#### 3. Generating Billing Reports Based on Tags

1. **Navigate to Cost Management + Billing**:
   - In the Azure portal, go to **Cost Management + Billing**.

2. **Cost Analysis**:
   - Select **Cost Analysis**.
   - Use the **Add filter** option to filter costs by tags.
   - For example, filter by `Department:Marketing` to see the costs associated with the Marketing department.

3. **Group by Tags**:
   - Use the **Group by** option to group costs by tags.
   - This will allow you to see a breakdown of costs by department.

#### 4. Automating Tagging with Azure Policy

To ensure that all resources are tagged consistently, you can use Azure Policy to enforce tagging.

1. **Create a Tagging Policy**:
   - Go to **Azure Policy** in the Azure portal.
   - Click on **Definitions** and then **+ Policy definition**.
   - Create a policy definition that requires tags on resources.

2. **Assign the Policy**:
   - Assign the policy to the subscription or resource group.
   - This will ensure that all new resources are tagged according to the policy.


