# Retrieval-Augmented Generation (RAG) pattern

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-14

------------------------------------------

## Wiki 

<details>
<summary><b>Table of Wiki </b> (Click to expand)</summary>
   
- [What's Azure AI Search?](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)
- [Indexer overview - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-indexer-overview)
- [Field mappings and transformations using Azure AI Search indexers](https://learn.microsoft.com/en-us/azure/search/search-indexer-field-mappings)
- [Azure AI Search Sample Data](https://github.com/Azure-Samples/azure-search-sample-data/tree/main)
- [RAG Microsoft Drawio/visio templates](https://github.com/Azure/GPT-RAG/blob/main/media/visio/Enterprise%20RAG.vsdx)
- [RAG Microsoft Enterprise RAG Solution Accelerator (GPT-RAG) - github repo](https://github.com/Azure/GPT-RAG)

</details>

## Overview 

| **Step**       | **Description**                                                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Retrieval**  | The system retrieves relevant documents or pieces of information from a knowledge base or external data source based on the input query. This step ensures that the model has access to up-to-date and specific information that can enhance the response. |
| **Augmentation** | The retrieved information is then used to augment the input query. This augmented input provides additional context and details that the generative model can use to produce a more informed response.                                                   |
| **Generation** | A generative model (such as GPT-4) processes the augmented input to generate a coherent and contextually relevant response. The output is a combination of the model's language generation capabilities and the retrieved factual information.               |

> Applications of RAG Pattern:
- **Question Answering**: Providing accurate answers by retrieving relevant documents and generating responses based on them.
- **Document Summarization**: Summarizing documents by retrieving key sections and generating concise summaries.
- **Conversational AI**: Enhancing chatbot responses with up-to-date information from external sources.

> Implementing RAG Pattern with Azure AI:

```mermaid
graph LR
    A[Set Up a Knowledge Base] --> B[Configure a Retrieval System] --> C[Integrate with a Generative Model]
```

1. **Set Up a Knowledge Base**: Store your documents in Azure Storage Blob Containers or another accessible data source.
2. **Configure a Retrieval System**: Use Azure AI Search to index and retrieve relevant documents based on user queries.
3. **Integrate with a Generative Model**: Use a generative model like GPT-4 to process the retrieved documents and generate responses.

> Traditional methods and the `Retrieval-Augmented Generation (RAG)` pattern:

| **Aspect**                | **Traditional Methods**                                                                 | **RAG Pattern**                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Model Type**            | Static, pre-trained models that rely on historical data. These models do not update dynamically and can become outdated. | Dynamic integration of retrieval and generative models, allowing for real-time data updates, keeping responses current and relevant. |
| **Data Freshness**        | Relies on pre-trained data, which may not reflect the latest information.                | Retrieves the most recent data from external sources, ensuring up-to-date information.            |
| **Context Understanding** | Often lacks the ability to fully understand the context of a query, leading to less accurate results. | Enhances context understanding by incorporating real-time information retrieval, providing richer context for responses. |
| **Retrieval Techniques**  | Uses keyword matching techniques like BM25 and TF-IDF, which may not capture the semantic meaning of queries. | Employs advanced semantic search techniques that better understand the intent behind queries, leading to more relevant results. |
| **Accuracy**              | May struggle with understanding context and semantic meaning, resulting in less accurate responses. | Improves accuracy by grounding responses in verified external knowledge, reducing the likelihood of errors. |
| **Risk of Hallucinations**| Higher risk of generating incorrect information as responses are based solely on training data. | Reduces this risk by grounding responses in real-time, verified information from external sources. |
| **Flexibility**           | Limited to specific data types and formats, which can restrict their applicability.      | Capable of handling various data types, including text, images, and videos, making it more versatile. |
| **Adaptability**          | Requires extensive retraining to incorporate new information, which can be time-consuming and costly. | More adaptable as it integrates real-time data without the need for frequent retraining.           |
| **Cost Efficiency**       | Can be resource-intensive due to the need for frequent retraining and large labeled datasets. | More cost-effective as it minimizes the need for extensive retraining and leverages existing data sources. |
| **Applications**          | Suitable for basic search and static content generation.                                | Ideal for complex applications such as healthcare, customer support, and content creation, where up-to-date and contextually relevant information is crucial. |

## Demo 

> Components:
- Search Service: The core component for querying and indexing.
- Indexer: Automates data ingestion from Azure Storage Blob Containers.
- Skillsets: Enhance indexing with AI capabilities like OCR for scanned documents and image analysis1.
- Vision: For processing images within documents
- Zero Trust Architecture: Security model that assumes no part of the network is inherently secure 

### Search Service 

> Azure AI Search (formerly known as Azure Cognitive Search) is a powerful, enterprise-ready search and retrieval system designed for high-performance applications. It integrates advanced search technologies to support both traditional and generative AI scenarios

![image](https://github.com/brown9804/SDLC-Cloud_Lpath/assets/24630902/bdaebc61-162f-4c0f-855f-6dc74de38397)

| **Category**        | **Details**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Key Features**    | - `Full-Text Search`: Rich query syntax, fuzzy search, autocomplete, geo-search <br/> - `Vector Search`: Similarity searches using vector embeddings <br/> - `Hybrid Search`: Combines full-text and vector search |
| **Core Components** | - `Indexing`: Data ingestion, text tokenization, vectorization, AI skills <br/> - `Querying`: Executes traditional and vector queries, semantic ranking |

> Steps:
- Create a AI Search Resource, click on `Create a resource`
- Search for `ai search`, you can check `Azure Services only` for a faster search.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/7e9e34b9-73d5-4c94-944a-7cd020b471e7">

- Configure Search Service: Provide the necessary details
    - Name: Enter a name for your search service.
    - Resource Group: Use the same resource group as your Azure OpenAI resource.
    - Location: Use the same region for reduced latency.
    - Pricing Tier: Select a pricing tier based on your needs.
      
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/9420a863-f22c-4236-9687-9e3799af15c8">

### Indexer 

Indexers can be scheduled to run at regular intervals or triggered on-demand, making them flexible for various data ingestion needs

> Key Functions of Indexers: 
1. **Data Extraction**: Indexers pull data from supported data sources like Azure Blob Storage, Azure SQL Database, and Azure Cosmos DB. This process is often referred to as a "pull model" because the search service pulls data into the index without requiring custom code.
2. **Field Mapping**: They map fields from the source data to the search index. This includes both implicit mappings (where field names and types match) and explicit mappings (where you define how fields should be mapped).
3. **Skillset Execution**: Indexers can apply AI skills to enrich the data during indexing. This includes tasks like optical character recognition (OCR), text translation, and key phrase extraction.

> Stages of Indexing:
1. **Document Cracking**: Extracts text and metadata from documents.
2. **Field Mappings**: Maps source fields to index fields.
3. **Skillset Execution**: Applies AI skills for data enrichment.
4. **Output Field Mappings**: Maps enriched data to the final index fields.

> Usage Scenarios:
- **Single Data Source**: Indexing content from one data source.
- **Multiple Data Sources**: Combining content from various sources into a single index.
- **Content Transformation**: Using AI skills to transform and enrich data during indexing.

> Steps:

- Add `Overview`, click on `Import Data`:
  
     <img width="550" alt="image" src="https://github.com/user-attachments/assets/0b5b9fb8-65ea-435a-b836-368bb9480537">

- 

### Zero Trust Architecture

 >  For Azure AI Search and OpenAI in a Retrieval-Augmented Generation (RAG) setup, find below an example of how these components are interconnected within a secure Azure environment.

Components:

1. **Azure Services Subscription**: The overarching subscription under which all services are organized.
2. **Resource Group (RG) for RAG**: A logical container that holds related resources, ensuring they are managed and secured together.
3. **Storage Account**: Used to store data securely.
4. **AI + Machine Learning Services**: This includes:
   - **Azure AI Search**: For indexing and searching documents.
   - **Azure OpenAI**: For generating responses based on retrieved documents.
   - **Azure Key Vault**: For securely storing secrets like API keys and connection strings.
5. **Virtual Network (VNet)**: Provides network isolation and security. It contains subnets such as:
   - **AI-services-subnet**: Hosts AI-related services.
   - **app-service-subnet**: Hosts application services.
6. **VM for Data Science**: A virtual machine used for data science tasks within the AI-services-subnet.
7. **App Service Plan and Web App**: Part of the app-service-subnet, used to host web applications.

> Workflow in Zero Trust Architecture:

1. **User Interaction**: The user initiates a request from their device.
2. **Azure Front Door and WAF**: The request is routed through Azure Front Door and Web Application Firewall (WAF) for initial security checks.
3. **App Service (Frontend)**: The request reaches the frontend application hosted on Azure App Service via a private endpoint.
4. **Orchestrator (Azure Function)**: The frontend communicates with an orchestrator function within the VNet, which manages the flow of data.
5. **Database Access**: The orchestrator accesses Azure Cosmos DB to retrieve conversation history.
6. **Vector Embedding**: The orchestrator requests Azure OpenAI to generate vector embeddings from the user’s query.
7. **Key Vault Access**: The orchestrator retrieves the AI Search API key from Azure Key Vault.
8. **Document Retrieval**: The orchestrator queries Azure AI Search to retrieve relevant documents.
9. **Response Generation**: The orchestrator uses Azure OpenAI to generate a response based on the retrieved documents.
10. **Response Delivery**: The response is sent back to the user through the same secure path.

> Network Interface & Network Security Groups

![nic-nsg-detailed](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/3_AzureAI/0_AISearch/demos/0_RAG/docs/0_nic-nsg-detailed.png)

> Zero trust phase0

![zero-trust-phase0](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/3_AzureAI/0_AISearch/demos/0_RAG/docs/1_zero-trust-phase0.png)

> Microsoft Enterprise RAG Solution Accelerator 

![Microsoft-RAG_Azure-Template](https://github.com/brown9804/MicrosoftCloudEssentialsHub/blob/main/0_Azure/3_AzureAI/0_AISearch/demos/0_RAG/docs/2_Microsoft-RAG_Azure-Template.png)
