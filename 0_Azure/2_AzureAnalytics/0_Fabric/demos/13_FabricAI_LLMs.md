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

> Microsoft Fabric is a comprehensive data analytics platform that brings together various data services to provide an end-to-end solution for data engineering, data science, data warehousing, real-time analytics, and business intelligence. It's designed to simplify the process of working with data and to enable organizations to gain insights more efficiently. <br/>
> Capabilities Enabled by LLMs: <br/>
> - `Document Summarization`: LLMs can process and summarize large documents, making it easier to extract key information. <br/>
> - `Question Answering:` Users can perform Q&A tasks on PDF documents, allowing for interactive data exploration. <br/>
> - `Embedding Generation`: LLMs can generate embeddings for document chunks, which can be stored in a vector store for efficient search and retrieval.

| Key Functionalities | Description |
|-----------------------------------------|-------------|
| **Unified Analytics Platform**          | Integrates multiple data services, including data engineering, data warehousing, data science, and real-time analytics, into a single platform. This unification simplifies data management and analytics workflows. |
| **Lake-Centric Architecture**           | Employs a lake-centric architecture, allowing data to be stored in a single, scalable data lake. This architecture supports open data formats and ensures seamless data access and management. |
| **Empowering Business Users**           | Designed to be user-friendly, enabling business users to create data pipelines, models, and reports without needing deep technical expertise. |
| **Built-in AI Capabilities**            | Includes built-in AI features that leverage Azure AI services. These capabilities enable advanced analytics, machine learning, and AI-driven insights directly within the platform. |

## Related to AI and LLMs

- **Integration with Azure OpenAI**: Microsoft Fabric works with Azure OpenAI services, letting users use large language models (LLMs) on a big scale. This integration supports a differents natural language processing (NLP) tasks, including text generation, summarization, and question answering. With Azure OpenAI, Fabric can do these tasks accurately and efficiently. This connection also makes it easy to use LLMs in several situations, like automating customer support, creating content, and analyzing data. Azure OpenAI can work with other Azure services, like Azure AI Search, to better find and use information from large amounts of data.
    
    | **Tool**     | **Description**|
    |--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **LangChain**| LangChain is a framework for developing applications powered by language models. It can be used with Azure OpenAI to build applications that require natural language understanding and generation. <br>**Use Case**: Creating complex applications that involve multiple steps or stages of processing, such as preprocessing text data, applying a language model, and postprocessing the results. |
    | **SynapseML**| SynapseML is an open-source library that simplifies the creation of massively scalable machine learning pipelines. It integrates with Azure OpenAI to provide distributed computing capabilities, allowing you to apply large language models at scale. <br>**Use Case**: Applying powerful language models to massive amounts of data, enabling scenarios like batch processing of text data or large-scale text analytics. |

- **Azure Machine Learning Integration**: Microsoft Fabric streamlines the entire machine learning operations (MLOps) and large language model operations (LLMOps) lifecycle, from data preparation to model deployment and monitoring. By integrating seamlessly with Azure Machine Learning, Fabric allows users to build, train, and deploy ML models directly from its platform. This integration supports comprehensive MLOps practices, ensuring efficient model management and deployment. With AzureML, users can automate the entire machine learning lifecycle, including data preparation, feature engineering, model training, evaluation, and deployment. The integration also facilitates the use of advanced tools and frameworks, such as SynapseML, which enhances distributed computing capabilities and supports large-scale data processing. By leveraging AzureML, Fabric ensures that AI models are not only developed efficiently but also maintained and monitored effectively, reducing the complexity of ML operations and improving overall model performance. This comprehensive approach enhances the efficiency and reliability of AI model management, automating routine tasks, ensuring consistent performance, and providing robust monitoring and maintenance capabilities to keep models up-to-date and functioning optimally.
  
    | **Tool**     | **Description**|
    |--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **LangChain**| LangChain can be used in the broader context of machine learning to chain together various components of an ML pipeline, such as preprocessing data, applying a language model, and postprocessing the results. <br>**Use Case**: Chaining together various components of an ML pipeline, such as preprocessing data, applying a language model, and postprocessing the results. |
    | **SynapseML**| SynapseML supports a wide range of machine learning tasks, including those that involve language models. It can be used to build and train custom ML models, including those that incorporate LLMs for tasks like text classification and sentiment analysis. <br>**Use Case**: Building and training custom ML models, including those that incorporate LLMs for tasks like text classification and sentiment analysis. |

- **SynapseML**: SynapseML is an integral component of Microsoft Fabric, designed to significantly enhance its AI and machine learning capabilities. This powerful library supports distributed computing with Apache Spark, enabling efficient handling of large datasets and the execution of complex machine learning tasks. SynapseML offers a comprehensive suite of tools for building, training, and deploying machine learning models. These tools facilitate various stages of the machine learning pipeline, from data preprocessing and feature engineering to model evaluation and deployment. By leveraging SynapseML, users can seamlessly integrate advanced machine learning workflows into their data processing and analytics operations, ensuring scalability and performance across diverse computing environments.

- **LangChain Integration**: Microsoft Fabric integrates with LangChain, an open-source library designed for building sophisticated applications using large language models (LLMs). This integration enhances Fabric’s capabilities in advanced natural language processing, enabling tasks such as document summarization, organization, and information extraction. By leveraging LangChain, users can efficiently manage and process large volumes of text data, automating complex workflows and improving the accuracy and efficiency of document handling. This integration supports the development of robust applications that can seamlessly handle diverse and extensive text-based data, making it a valuable tool for data processing and analytics.

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

  
- **Embedding Generation and Storage**:  Microsoft Fabric can generate embeddings for text data using Azure OpenAI services. These embeddings are vector representations of text that capture semantic meaning, making them highly useful for various AI applications. By leveraging Azure OpenAI, Fabric can efficiently create embeddings that facilitate advanced tasks such as document retrieval, semantic search, and information extraction.

  > Relation with AI and LLMs:
    
    | Feature | Description |
    |---------|-------------|
    | **Efficient Document Retrieval** | Embeddings allow for the efficient retrieval of documents based on their semantic content rather than just keyword matching. This is particularly useful in applications like search engines and knowledge management systems, where finding relevant information quickly is crucial. |
    | **Semantic Search** | With embeddings, Fabric can perform semantic searches, which go beyond simple keyword searches to understand the context and meaning of the query. This enhances the accuracy and relevance of search results, making it easier to find the most pertinent information. |
    | **Integration with Azure AI Search** | The embeddings generated by Azure OpenAI can be stored in Azure AI Search (formely known as Cognitive Search), a powerful search service that supports vector search capabilities. This integration allows for the efficient indexing and retrieval of embeddings, enabling advanced search functionalities like similarity search and nearest neighbor search. |
    | **Support for Retrieval-Augmented Generation (RAG)** | Embeddings play a crucial role in RAG systems, where they are used to retrieve relevant documents or text chunks that can be used to augment the responses generated by LLMs. This improves the quality and relevance of the generated content by providing the LLMs with contextually relevant information. |
    | **Scalability and Performance** | By using distributed computing frameworks like Apache Spark, Fabric can generate and store embeddings at scale, handling large volumes of text data efficiently. This scalability ensures that even extensive datasets can be processed and searched quickly, supporting enterprise-level applications. |

## Demo 

- Step 1: Set Up Your Environment
    1. **Register the Resource Provider**: Ensure that the `microsoft.fabric` resource provider is registered in your subscription.
       
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/de708b6b-90e9-42b0-957a-7c045d15f699">

    2. **Create a Microsoft Fabric Resource**:
       - Navigate to the Azure Portal.
       - Create a new resource of type **Microsoft Fabric**.
       - Choose the appropriate subscription, resource group, capacity name, region, size, and administrator.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/a860911c-0ab8-469e-82d9-d0495268bd3b">

3. **Enable Fabric Capacity in Power BI**:
   - Go to the Power BI workspace.
   - Select the Fabric capacity license and the Fabric resource created in Azure.

4. **Pause Fabric Compute When Not in Use**:
   - To save costs, remember to pause the Fabric compute in Azure when you're not using it.

### Step 2: Install Required Libraries
1. **Install SynapseML on Your Cluster**:
   - Configure your cluster to include the SynapseML package.
   - Use the following configuration:
     ```json
     {
       "name": "synapseml",
       "conf": {
         "spark.jars.packages": "com.microsoft.azure:synapseml_2.12:0.11.1-10-5e9c0c19-SNAPSHOT,org.apache.spark:spark-avro_2.12:3.3.1",
         "spark.jars.repositories": "https://mmlspark.azureedge.net/maven",
         "spark.jars.excludes": "org.scala-lang:scala-reflect,org.apache.spark:spark-tags_2.12,org.scalactic:scalactic_2.12,org.scalatest:scalatest_2.12,com.fasterxml.jackson.core:jackson-databind",
         "spark.yarn.user.classpath.first": "true",
         "spark.sql.parquet.enableVectorizedReader": "false",
         "spark.sql.legacy.replaceDatabricksSparkAvro.enabled": "true"
       }
     }
     ```

2. **Install LangChain and Other Dependencies**:
   - Use `%pip install` to install the necessary packages:
     ```python
     %pip install openai langchain pdf2image pdfminer.six pytesseract unstructured
     ```

### Step 3: Configure Azure OpenAI Service
1. **Set Up API Keys**:
   - Provide the keys for Azure OpenAI to authenticate the applications:
     ```python
     import os
     from synapse.ml.core.platform import find_secret

     openai_api_key = find_secret("openai-api-key")
     openai_api_base = "https://synapseml-openai.openai.azure.com/"
     openai_api_version = "2022-12-01"
     openai_api_type = "azure"
     deployment_name = "text-davinci-003"
     bing_search_url = "https://api.bing.microsoft.com/v7.0/search"
     bing_subscription_key = find_secret("bing-search-key")

     os.environ["BING_SUBSCRIPTION_KEY"] = bing_subscription_key
     os.environ["BING_SEARCH_URL"] = bing_search_url
     os.environ["OPENAI_API_TYPE"] = openai_api_type
     os.environ["OPENAI_API_VERSION"] = openai_api_version
     os.environ["OPENAI_API_BASE"] = openai_api_base
     os.environ["OPENAI_API_KEY"] = openai_api_key
     ```

2. **Initialize Azure OpenAI Class**:
   - Create an instance of the Azure OpenAI class:
     ```python
     from langchain.llms import AzureOpenAI

     llm = AzureOpenAI(
         deployment_name=deployment_name,
         model_name=deployment_name,
         temperature=0.1,
         verbose=True,
     )
     ```

### Step 4: Basic Usage of LangChain Transformer
1. **Create a Prompt Template**:
   - Define a prompt template for generating definitions:
     ```python
     from langchain.prompts import PromptTemplate

     copy_prompt = PromptTemplate(
         input_variables=["technology"],
         template="Define the following word: {technology}",
     )
     ```

2. **Set Up an LLMChain**:
   - Create an LLMChain with the defined prompt template:
     ```python
     from langchain.chains import LLMChain

     chain = LLMChain(llm=llm, prompt=copy_prompt)
     ```

3. **Configure LangChain Transformer**:
   - Set up the LangChain transformer to execute the processing chain:
     ```python
     from synapse.ml.cognitive.langchain import LangchainTransformer

     transformer = (
         LangchainTransformer()
         .setInputCol("technology")
         .setOutputCol("definition")
         .setChain(chain)
         .setSubscriptionKey(openai_api_key)
         .setUrl(openai_api_base)
     )
     ```

4. **Create a Test DataFrame**:
   - Construct a DataFrame with technology names:
     ```python
     df = spark.createDataFrame(
         [(0, "docker"), (1, "spark"), (2, "python")],
         ["label", "technology"]
     )
     display(transformer.transform(df))
     ```

### Step 5: Using LangChain for Large Scale Literature Review
1. **Define Functions for Content Extraction and Prompt Generation**:
   - Extract content from PDFs linked in arXiv papers and generate prompts for extracting specific information:
     ```python
     from langchain.document_loaders import OnlinePDFLoader

     def paper_content_extraction(inputs: dict) -> dict:
         arxiv_link = inputs["arxiv_link"]
         loader = OnlinePDFLoader(arxiv_link)
         pages = loader.load_and_split()
         return {"paper_content": pages[0].page_content + pages[1].page_content}

     def prompt_generation(inputs: dict) -> dict:
         output = inputs["Output"]
         prompt = (
             "find the paper title, author, summary in the paper description below, output them. "
             "After that, Use websearch to find out 3 recent papers of the first author in the author section below "
             "(first author is the first name separated by comma) and list the paper titles in bullet points: "
             "<Paper Description Start>\n" + output + "<Paper Description End>."
         )
         return {"prompt": prompt}
     ```

2. **Create a Sequential Chain for Information Extraction**:
   - Set up a chain to extract structured information from an arXiv link:
     ```python
     from langchain.chains import TransformChain, SimpleSequentialChain

     paper_content_extraction_chain = TransformChain(
         input_variables=["arxiv_link"],
         output_variables=["paper_content"],
         transform=paper_content_extraction,
         verbose=False,
     )

     paper_summarizer_template = """
     You are a paper summarizer, given the paper content, it is your job to summarize the paper into a short summary, 
     and extract authors and paper title from the paper content.
     """
     ```

### Step 6: Machine Learning Integration with Microsoft Fabric
1. **Train and Register Machine Learning Models**:
   - Use Microsoft Fabric's native integration with the MLflow framework to log the trained machine learning models, the used hyperparameters, and evaluation metrics:
     ```python
     import mlflow
     from mlflow.models import infer_signature
     from sklearn.datasets import make_regression
     from sklearn.ensemble import RandomForestRegressor

     # Generate synthetic regression data
     X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)

     # Model parameters
     params = {"n_estimators": 3, "random_state": 42}

     # Model tags for MLflow
     model_tags = {
         "project_name": "grocery-forecasting",
         "store_dept": "produce",
         "team": "stores-ml",
         "project_quarter": "Q3-2023"
     }

     # Log MLflow entities
     with mlflow.start_run() as run:
         # Train the model
         model = RandomForestRegressor(**params).fit(X, y)

         # Infer the model signature
         signature = infer_signature(X, model.predict(X))

         # Log parameters and the model
         mlflow.log_params(params)
         mlflow.sklearn.log_model(model, artifact_path="sklearn-model", signature=signature)

         # Register the model with tags
         model_uri = f"runs:/{run.info.run_id}/sklearn-model"
         model_version = mlflow.register_model(model_uri, "RandomForestRegressionModel", tags=model_tags)

         # Output model registration details
         print(f"Model Name: {model_version.name}")
         print(f"Model Version: {model_version.version}")
     ```

2. **Compare and Filter Machine Learning Models**:
   - Use MLflow to search among multiple models saved within the workspace:
     ```python
     from pprint import pprint
     from mlflow.tracking import MlflowClient

     client = MlflowClient()
     for rm in client.list_registered_models():
         pprint(dict(rm), indent=4)
     ```

