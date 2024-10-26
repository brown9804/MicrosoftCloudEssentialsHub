# Azure OpenAI: Tokenization & Cost Analysis 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-25

----------

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>
  
- [Azure OpenAI Service - Pricing](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/openai-service/)
- [Plan to manage costs for Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/manage-costs)
- [Chapter 9 - Cost Management and Optimization](https://azure.github.io/AI-in-Production-Guide/chapters/chapter_09_managing_expedition_cost_management_optimization)
- [Pricing Update: Token Based Billing for Fine Tuning Training](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/pricing-update-token-based-billing-for-fine-tuning-training/ba-p/4164465)
- [Tokenizer - tool from OpenAI](https://platform.openai.com/tokenizer)
  
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



