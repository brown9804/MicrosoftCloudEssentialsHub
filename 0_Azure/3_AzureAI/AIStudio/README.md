# Azure AI Studio

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-09-11

----------

> You can create and manage Azure resources for Azure AI Studio via the Azure portal. 

## Content 

<!-- TOC -->
- [Wiki](#wiki)
- [Overview](#overview)

<!-- /TOC -->

## Wiki

- [Introducing Meta Llama 3 Models on Azure AI Model Catalog](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/introducing-meta-llama-3-models-on-azure-ai-model-catalog/ba-p/4117144)
- [Meta’s next generation model, Llama 3.1 405B is now available on Azure AI](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/meta-s-next-generation-model-llama-3-1-405b-is-now-available-on/ba-p/4198379)
- [Model benchmarks in Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/model-benchmarks)

## Overview 

- Provides a trusted and inclusive platform that empowers developers of all abilities and preferences to innovate with AI and shape the future.
- Seamlessly explore, build, test, and deploy using cutting-edge AI tools and ML models, grounded in responsible AI practices.
- Build together as one team.
- Improve customer experiences, reduce organizational risk, improve work quality, enhance productivity and efficiency.
- Built-in security and compliance investing USD20 billion in cybersecurity.
- 8,500 security and threat intelligence experts compliance certification portfolios.

  <img width="709" alt="image" src="https://github.com/brown9804/MSCloudEssentials_LPath/assets/24630902/ad165c2c-94ee-455d-8c90-55f56fb119b9"> 
  
  [image from](https://www.slideshare.net/slideshow/azure-ai-platform-automated-ml-workshop/133115961)

  | **Feature** | **Azure AI Studio** | **Azure OpenAI** |
  |-------------|----------------------|------------------|
  | **Scope** | Comprehensive platform for building, testing, and deploying generative AI applications | Specific service providing access to OpenAI's models |
  | **Model Catalog** | Includes models from OpenAI, Hugging Face, Meta, and more | Focuses on OpenAI models like GPT-4, Codex, and DALL-E |
  | **Collaboration** | Provides a collaborative environment with shared files and connections to pretrained models, data, and compute resources | Offers a playground for experimenting with OpenAI models |
  | **Tools** | Supports LLMOps for generative AI solutions, including evaluation, connection management, and flow logic | Allows users to manage deployments and models directly through the Azure OpenAI Studio |
  | **Use Cases** | Suitable for a wide range of AI applications, including text, image, and document processing | Primarily for text generation, summarization, translation, and question answering |


### Model Catalog 

> The Model Catalog in Azure AI Studio is a `central hub where you can discover, evaluate, and deploy a wide range of AI models`. It includes models from various providers such as Azure OpenAI Service, Mistral, Meta, Cohere, NVIDIA, and Hugging Face, as well as models trained by Microsoft.

<p float="left">
  <img src="https://github.com/user-attachments/assets/5d83afb8-9924-49f1-aebc-3ce90c58c58f" width="450" height="250" />
  <img src="https://github.com/user-attachments/assets/ab6f3f19-dafb-413f-8b9d-fe73dc4dd420" width="450" height="250" />
</p>

The model catalog offers two distinct `ways to deploy models` for your use:
- Managed Compute
- Serverless API.
  
  <img width="550" alt="image" src="https://github.com/user-attachments/assets/1f6d2b05-be72-46ed-bb2a-4141c4eadf6b">

| **Type of Model**            | **Description**                                                                 | **Examples**                          |
|------------------------------|---------------------------------------------------------------------------------|---------------------------------------|
| Curated by Azure AI          | Popular non-Microsoft models optimized for Azure AI platform.                   | Models from Hugging Face, NVIDIA      |
| Azure OpenAI Models          | Exclusive models available through Azure OpenAI Service, supported by Microsoft.| GPT-4, Codex, DALL-E                  |
| Open Models from Hugging Face| Hundreds of models from the Hugging Face hub, available for real-time inference. | Various NLP and vision models         |

### Model Benchmarks

> Model Benchmarks in Azure AI Studio is a feature that allows users to compare the performance of various AI models. This tool helps you make informed decisions about which model best suits your specific task by providing a comprehensive comparison of benchmarking metrics.

| Key Aspect                  | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Comparison of Models        | Compare LLMs and SLMs based on metrics like accuracy, coherence, fluency, and GPT (Generative Pre-trained Transformer) similarity this metric is particularly useful when comparing the performance of different language models. |
| Quality and Embeddings Benchmarks | Evaluate models based on quality and embeddings benchmarks.              |
| Efficiency                  | Reduce development time and infrastructure costs by identifying the most suitable model quickly. |
| User-Friendly               | Accessible within the same environment where you build, train, and deploy AI solutions. |

### Azure AI Services

> Azure AI Services is a comprehensive suite of AI tools and services provided by Microsoft to help developers and organizations build intelligent applications.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/823714d5-ccda-43c8-9fc8-3188c5fa5a7c">



## Componenets 

### Data 



### Deployments 

> Types of deployments available in Azure AI Studio:

| **Deployment Method**       | **Description**                                                                 | **Billing Model**                      |
|-----------------------------|---------------------------------------------------------------------------------|----------------------------------------|
| Serverless API              | Deploy models as serverless APIs, accessible via endpoints without managing infrastructure. | Pay-as-you-go (per token/request)      |
| Models as a Service (MaaS)  | Managed service where models are hosted and maintained by Azure.                | Pay-as-you-go (per token)              |
| Models as a Platform (MaaP) | Deploy models on dedicated virtual machines (VMs) for more control over resources. | Billed as VMs per-hour                 |
| Flows and Web Applications  | Deploy models as part of larger workflows or web applications.                  | Varies based on usage                  |
| Managed Compute             | Use Azure's managed compute resources to deploy and run models.                 | Combination of compute and storage costs|


### Indexes 

### Content Filter




