# Fabric: Highlights into AI/LLMs

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-07

------------------------------------------

> Microsoft Fabric is a comprehensive data and analytics platform designed to unify various data operations and enhance AI capabilities. 

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Unleashing the Power of Microsoft Fabric and SynapseML](https://blog.fabric.microsoft.com/en-us/blog/unleashing-the-power-of-synapseml-and-microsoft-fabric-a-guide-to-qa-on-pdf-documents-2)
- [Building a RAG application with Microsoft Fabric](https://techcommunity.microsoft.com/t5/startups-at-microsoft/building-high-scale-rag-applications-with-microsoft-fabric/ba-p/4217816)
- [Building Custom AI Applications with Microsoft Fabric: Implementing Retrieval-Augmented Generation](https://support.fabric.microsoft.com/en-us/blog/building-custom-ai-applications-with-microsoft-fabric-implementing-retrieval-augmented-generation-for-enhanced-language-models?ft=Alicia%20Li%20%28ASA%29:author)
- [Avail the Power of Microsoft Fabric from within Azure Machine Learning](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/avail-the-power-of-microsoft-fabric-from-within-azure-machine/ba-p/3980702)
- [AI and Machine Learning on Databricks - Azure Databricks | Microsoft Learn]( https://learn.microsoft.com/en-us/azure/databricks/machine-learning)
- [Training and Inference of LLMs with PyTorch Fully Sharded Data Parallel](https://techcommunity.microsoft.com/t5/microsoft-developer-community/training-and-inference-of-llms-with-pytorch-fully-sharded-data/ba-p/3845995)
- [Harness the Power of LangChain in Microsoft Fabric for Advanced Document Summarization](https://blog.fabric.microsoft.com/en-us/blog/harness-the-power-of-langchain-in-microsoft-fabric-for-advanced-document-summarization)
- [Integrating Azure AI and Microsoft Fabric for Next-Gen AI Solutions](https://build.microsoft.com/en-US/sessions/91971ab3-93e4-429d-b2d7-5b60b2729b72)
- [Generative AI with Microsoft Fabric](https://techcommunity.microsoft.com/t5/microsoft-mechanics-blog/generative-ai-with-microsoft-fabric/ba-p/4219444)
- [Harness Microsoft Fabric AI Skill to Unlock Context-Rich Insights from Your Data](https://blog.fabric.microsoft.com/en-us/blog/harness-microsoft-fabric-ai-skill-to-unlock-context-rich-insights-from-your-data)

</details>

## Overview 

| Key Functionalities | Description |
|-----------------------------------------|-------------|
| **Unified Analytics Platform**          | Integrates multiple data services, including data engineering, data warehousing, data science, and real-time analytics, into a single platform. This unification simplifies data management and analytics workflows. |
| **Lake-Centric Architecture**           | Employs a lake-centric architecture, allowing data to be stored in a single, scalable data lake. This architecture supports open data formats and ensures seamless data access and management. |
| **Empowering Business Users**           | Designed to be user-friendly, enabling business users to create data pipelines, models, and reports without needing deep technical expertise. |
| **Built-in AI Capabilities**            | Includes built-in AI features that leverage Azure AI services. These capabilities enable advanced analytics, machine learning, and AI-driven insights directly within the platform. |

## Related to AI and LLMs

- **Integration with Azure OpenAI**: Microsoft Fabric integrates with Azure OpenAI services, allowing users to apply LLMs at scale. This integration supports a variety of natural language processing (NLP) tasks, including text generation, summarization, and question answering. By utilizing Azure OpenAI, Fabric can handle complex language tasks with high accuracy and efficiency. This integration also allows for the seamless application of LLMs in various scenarios, such as customer support automation, content creation, and data analysis. Additionally, Azure OpenAI's capabilities can be combined with other Azure services, like Azure Cognitive Search, to enhance the retrieval and processing of information from large datasets.
- **Azure Machine Learning Integration**: Microsoft Fabric integrates seamlessly with Azure Machine Learning, allowing users to build, train, and deploy ML models directly from the Fabric platform. This integration supports comprehensive MLOps practices, ensuring efficient model management and deployment. With AzureML, users can automate the entire machine learning lifecycle, from data preparation and feature engineering to model training, evaluation, and deployment. The integration also facilitates the use of advanced tools and frameworks, such as SynapseML, which enhances distributed computing capabilities and supports large-scale data processing. By leveraging AzureML, Fabric ensures that AI models are not only developed efficiently but also maintained and monitored effectively, reducing the complexity of ML operations and improving overall model performance.
- **SynapseML**: SynapseML is an integral component of Microsoft Fabric, designed to significantly enhance its AI and machine learning capabilities. This powerful library supports distributed computing with Apache Spark, enabling efficient handling of large datasets and the execution of complex machine learning tasks. SynapseML offers a comprehensive suite of tools for building, training, and deploying machine learning models. These tools facilitate various stages of the machine learning pipeline, from data preprocessing and feature engineering to model evaluation and deployment. By leveraging SynapseML, users can seamlessly integrate advanced machine learning workflows into their data processing and analytics operations, ensuring scalability and performance across diverse computing environments.
- **Document Processing and Q&A**: Microsoft Fabric leverages large language models (LLMs) to perform advanced document processing tasks. These tasks include extracting valuable information from unstructured documents, such as PDFs, and automating processes like document summarization and question answering. This capability is particularly beneficial for handling large volumes of text data efficiently. By utilizing LLMs, Fabric can streamline the extraction of insights from extensive and complex documents, making it easier to manage and analyze unstructured data. This automation not only saves time but also enhances the accuracy and consistency of information retrieval, supporting various applications in data processing and analytics.
- **OneLake Datastore**: Fabric's OneLake datastore provides a unified data storage solution that supports various data formats and sources. This feature simplifies data access and management, enabling efficient data preparation and model training. 
  > Relation with AI and LLMs: 
  
    | Feature | Description |
    |---------|-------------|
    | **Unified Data Storage** | OneLake acts as a centralized repository for all data types, including structured, semi-structured, and unstructured data. This centralization is crucial for AI and LLMs as it ensures that all necessary data is readily accessible for training and inference. |
    | **Seamless Integration with Azure Machine Learning** | OneLake integrates natively with Azure Machine Learning (AzureML), allowing users to build, train, and deploy machine learning models directly from the data stored in OneLake. This integration supports the entire ML lifecycle, from data ingestion to model deployment and monitoring. |
    | **Support for Large Language Models (LLMs)** | By providing a robust and scalable data storage solution, OneLake enables the efficient handling of large datasets required for training LLMs. This includes capabilities for data preprocessing, feature engineering, and model training, which are essential for developing sophisticated AI applications. |
    | **Enhanced Data Management** | OneLake simplifies data management by supporting various data formats and sources, including external data sources like Amazon S3 and Google Cloud Storage. This flexibility allows for more comprehensive data integration, which is vital for training accurate and reliable AI models. |
    | **Advanced Data Indexing and Retrieval** | With features like the OneLake files indexer, users can directly index and retrieve data from OneLake, enhancing the efficiency of data processing tasks. This is particularly useful for applications involving retrieval-augmented generation (RAG), where quick and accurate data retrieval is essential. |
  > Benefits with Delta Lake:
  
    | **Feature** | **Description** |
    |-------------|-----------------|
    | **Merger of Parquet with transaction logs** | Combining Parquet file format with transaction logs to ensure data consistency and reliability. |
    | **RDMS features on flat files** | Implementing Relational Database Management System (RDMS) functionalities on flat file structures. |
    | **Schema enforcement** | Ensuring that data adheres to a predefined schema, maintaining data integrity and quality. |
    | **ACID transactions (Atomicity, Consistency, Isolation, Durability)** | Guaranteeing that database transactions are processed reliably through Atomicity, Consistency, Isolation, and Durability properties. |
    | **Time Travel** | The ability to query historical versions of data for auditing or recovery purposes. |
    | **ANSI SQL (American National Standards Institute Structured Query Language)** | Using standardized SQL language for querying databases to ensure compatibility across different systems. |
    | **Less duplication of effort** | Reducing redundant work by streamlining processes and improving efficiency. |
    | **Decrease development speeds** | Accelerating the development process by using efficient tools and methodologies. |
    | **Unlimited Scale** | The capability to scale resources without limitations to handle large volumes of data or users. |
    | **Auto scale is in Databricks’ DNA** | Databricks inherently supports automatic scaling of resources based on demand. |
    | **Many levers to exactly fit your size** | Providing various options to customize resource allocation according to specific needs. |
    | **Acquire resources just when you need them** | Dynamically obtaining necessary resources at the moment they are required. |
    | **Release resources when you don’t** | Promptly releasing unused resources after they are no longer needed. |
    | **Spark is extremely powerful from a transformation perspective** | Spark provides robust capabilities for transforming large datasets efficiently. |
    | **Native ODBC/JDBC connectors available** | Native Open Database Connectivity (ODBC) and Java Database Connectivity (JDBC) connectors are available for seamless integration with various databases. |

- **LangChain Integration**: Microsoft Fabric integrates with LangChain, an open-source library designed for building sophisticated applications using large language models (LLMs). This integration enhances Fabric’s capabilities in advanced natural language processing, enabling tasks such as document summarization, organization, and information extraction. By leveraging LangChain, users can efficiently manage and process large volumes of text data, automating complex workflows and improving the accuracy and efficiency of document handling. This integration supports the development of robust applications that can seamlessly handle diverse and extensive text-based data, making it a valuable tool for data processing and analytics.
- **Enhanced MLOps/LLMOps**: Microsoft Fabric streamlines the entire machine learning operations (MLOps) and large language model operations (LLMOps) lifecycle, encompassing everything from data preparation to model deployment and monitoring. This comprehensive approach ensures that AI models are efficiently managed and maintained throughout their lifecycle. By reducing the complexity of ML operations, Fabric enhances the efficiency and reliability of AI model management, facilitating smoother transitions between different stages of the ML pipeline. This includes automating routine tasks, ensuring consistent performance, and providing robust monitoring and maintenance capabilities to keep models up-to-date and functioning optimally.
- **Embedding Generation and Storage**:  Microsoft Fabric can generate embeddings for text data using Azure OpenAI services. These embeddings are vector representations of text that capture semantic meaning, making them highly useful for various AI applications. By leveraging Azure OpenAI, Fabric can efficiently create embeddings that facilitate advanced tasks such as document retrieval, semantic search, and information extraction.
  > Relation with AI and LLMs:
    
    | Feature | Description |
    |---------|-------------|
    | **Efficient Document Retrieval** | Embeddings allow for the efficient retrieval of documents based on their semantic content rather than just keyword matching. This is particularly useful in applications like search engines and knowledge management systems, where finding relevant information quickly is crucial. |
    | **Semantic Search** | With embeddings, Fabric can perform semantic searches, which go beyond simple keyword searches to understand the context and meaning of the query. This enhances the accuracy and relevance of search results, making it easier to find the most pertinent information. |
    | **Integration with Azure Cognitive Search** | The embeddings generated by Azure OpenAI can be stored in Azure Cognitive Search, a powerful search service that supports vector search capabilities. This integration allows for the efficient indexing and retrieval of embeddings, enabling advanced search functionalities like similarity search and nearest neighbor search. |
    | **Support for Retrieval-Augmented Generation (RAG)** | Embeddings play a crucial role in RAG systems, where they are used to retrieve relevant documents or text chunks that can be used to augment the responses generated by LLMs. This improves the quality and relevance of the generated content by providing the LLMs with contextually relevant information. |
    | **Scalability and Performance** | By using distributed computing frameworks like Apache Spark, Fabric can generate and store embeddings at scale, handling large volumes of text data efficiently. This scalability ensures that even extensive datasets can be processed and searched quickly, supporting enterprise-level applications. |
