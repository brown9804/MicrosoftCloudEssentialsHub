# Automated PDF Invoice Processing <br/> using Function App + OpenFramework 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-28

----------

> Using Azure Functions, Blob Storage, and Cosmos DB. <br/>

> [!NOTE]
> Limitations of this approach: <br/>
> - Requires significant manual effort to structure and format extracted data. <br/>
> - Limited in handling complex layouts and non-text elements like images and charts. <br/>

<img width="550" alt="image" src="https://github.com/user-attachments/assets/cda874fc-6cca-4857-ac5d-2f8d7887e36d">

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Azure Cosmos DB - Database for the AI Era](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
- [What is Azure SQL Database?](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql)
- [App settings reference for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings)
- [Storage considerations for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations?tabs=azure-cli)

</details>

## Content

- [Wiki](#wiki)
- [Content](#content)
- [Overview](#overview)
    - [Function App Hosting Options](#function-app-hosting-options)
- [Step 1: Set Up Your Azure Environment](#step-1-set-up-your-azure-environment)
- [Step 2: Set Up Azure Blob Storage for PDF Ingestion](#step-2-set-up-azure-blob-storage-for-pdf-ingestion)
- [Step 3: Set Up Azure Cosmos DB](#step-3-set-up-azure-cosmos-db)
- [Step 4: Set Up Azure Functions for Document Ingestion and Processing](#step-4-set-up-azure-functions-for-document-ingestion-and-processing)
    - [Create a Function App](#create-a-function-app)
    - [Configure/Validate the Environment variables](#configurevalidate-the-environment-variables)
    - [Develop the Function](#develop-the-function)
- [Step 5: Test the solution](#step-5-test-the-solution)

## Overview 

> Using Cosmos DB provides you with a flexible, scalable, and globally distributed database solution that can handle both structured and semi-structured data efficiently. <br/>
> - `Azure Blob Storage`: Store the PDF invoices. <br/>
> - `Azure Functions`: Trigger on new PDF uploads, extract data, and process it. <br/>
> - `Azure SQL Database or Cosmos DB`: Store the extracted data for querying and analytics. <br/> 

| Resource                  | Recommendation                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Azure Blob Storage**    | Use for storing the PDF files. This keeps your file storage separate from your data storage, which is a common best practice. |
| **Azure SQL Database**    | Use if your data is highly structured and you need complex queries and transactions.                                  |
| **Azure Cosmos DB**       | Use if you need a globally distributed database with low latency and the ability to handle semi-structured data.      |

### Function App Hosting Options 

> In the context of Azure Function Apps, a `hosting option refers to the plan you choose to run your function app`. This choice affects how your function app is scaled, the resources available to each function app instance, and the support for advanced functionalities like virtual network connectivity and container support.

| **Plan**                | **Scale to Zero** | **Scale Behavior**                     | **Virtual Networking** | **Dedicated Compute & Reserved Cold Start** | **Max Scale Out (Instances)** | **Example AI Use Cases**                                                                 |
|-------------------------|-------------------|----------------------------------------|------------------------|---------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------|
| **Flex Consumption**    | `Yes`             | `Fast event-driven`                    | `Optional`             | `Optional (Always Ready)`                   | `1000`                         | `Real-time data processing` for AI models, `high-traffic AI-powered APIs`, `event-driven AI microservices`. Use for applications needing to process large volumes of data in real-time, such as AI models for fraud detection or real-time recommendation systems. Ideal for deploying APIs that serve AI models, such as natural language processing (NLP) or computer vision services, which require rapid scaling based on demand. |
| **Consumption**         | `Yes`             | `Event-driven`                         | `Optional`             | `No`                                        | `200`                          | `Lightweight AI APIs`, `scheduled AI tasks`, `low-traffic AI event processing`. Suitable for deploying lightweight AI services, such as sentiment analysis or simple image recognition, which do not require extensive resources. Perfect for running periodic AI tasks, like batch processing of data for machine learning model training or scheduled data analysis. |
| **Functions Premium**   | `No`              | `Event-driven with premium options`    | `Yes`                  | `Yes`                                       | `100`                          | `Enterprise AI applications`, AI services requiring `VNet integration`, `low-latency AI APIs`. Use for mission-critical AI applications that require high availability, low latency, and integration with virtual networks, such as AI-driven customer support systems or advanced analytics platforms. Ideal for AI services that need to securely connect to on-premises resources or other Azure services within a virtual network. |
| **App Service**         | `No`              | `Dedicated VMs`                        | `Yes`                  | `Yes`                                       | `Varies`                       | `AI-powered web applications` with integrated functions, AI applications needing `dedicated resources`. Great for web applications that incorporate AI functionalities, such as personalized content delivery, chatbots, or interactive AI features. Suitable for AI applications that require dedicated compute resources for consistent performance, such as intensive data processing or complex AI model inference. |
| **Container Apps Env.** | `No`              | `Containerized microservices environment` | `Yes`                  | `Yes`                                       | `Varies`                       | `AI microservices architecture`, containerized AI workloads, `complex AI event-driven workflows`. Perfect for building a microservices architecture where each service can be independently scaled and managed, such as a suite of AI services for different tasks (e.g., image processing, text analysis). Ideal for deploying containerized AI workloads that need to run in a managed environment, such as machine learning model training and deployment pipelines. Suitable for orchestrating complex workflows involving multiple AI services and event-driven processes, such as automated data pipelines and real-time analytics. |

## Step 1: Set Up Your Azure Environment

> An Azure `Resource Group` is a `container that holds related resources for an Azure solution`.
> It can include all the resources for the solution or only those you want to manage as a group.
> Typically, resources that share the same lifecycle are added to the same resource group, allowing for easier deployment, updating, and deletion as a unit.
> Resource groups also store metadata about the resources, and you can apply access control, locks, and tags to them for better management and organization.

1. **Create an Azure Account**: If you don't have one, sign up for an Azure account.
2. **Create a Resource Group**:
   - Go to the Azure portal.
   - Navigate to **Resource groups**.
   - Click **+ Create**.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/56d1e99f-0a22-4492-bd6f-d4e3a76aedd8">

   - Enter the Resource Group name (e.g., `RGContosoAI`) and select a region (e.g., `East US 2`). You can add tags if needed.
   - Click **Review + create** and then **Create**.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/324c1157-9566-4b30-bb36-bd0efb0a1bf3">

## Step 2: Set Up Azure Blob Storage for PDF Ingestion

> An `Azure Storage Account` provides a `unique namespace in Azure for your data, allowing you to store and manage various types of data such as blobs, files, queues, and tables`. It serves as the foundation for all Azure Storage services, ensuring high availability, scalability, and security for your data. <br/> <br/>
> A `Blob Container` is a `logical grouping of blobs within an Azure Storage Account, similar to a directory in a file system`. Containers help organize and manage blobs, which can be any type of unstructured data like text or binary data. Each container can store an unlimited number of blobs, and you must create a container before uploading any blobs.

1. **Create a Storage Account**:
   - In the Azure portal, navigate to your **Resource Group**.
   - Click **+ Create**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/dd4579b3-2f95-4a24-b9ef-178ee14c9e98">

   - Search for `Storage Account`.
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/09616373-c3b2-459c-89b8-59c6db6beaea">

   - Select the Resource Group you created.
   - Enter a Storage Account name (e.g., `contosostorageaidemo`).
   - Choose the region and performance options, and click `Next` to continue.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/4db31956-2d36-4581-98cf-ec0e68d55037">

   - If you need to modify anything related to `Security, Access protocols, Blob Storage Tier`, you can do that in the `Advanced` tab.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/5d3da139-6e7a-4bb6-a695-deb1c314ccd3">

   - Regarding `Networking`, this example will cover `Public access` configuration. However, please ensure you review your privacy requirements and adjust network and access settings as necessary for your specific case.
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/0273e197-6e5b-4a1c-93cc-7597730c384b">

   - Click **Review + create** and then **Create**. Once is done, you'll be able to see it in your Resource Group.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/8b61b79c-9f3f-47f0-b59f-6720edebe41e">

2. **Create a Blob Container**:
   - Go to your Storage Account.
   - Under **Data storage**, select **Containers**.
   - Click **+ Container**.
   - Enter a name for the container (e.g., `pdfinvoices`) and set the public access level to **Private**.
   - Click **Create**.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/9b4900e3-7ce8-42aa-b5d9-c2fbb2417721">

## Step 3: Set Up Azure Cosmos DB

> `Azure Cosmos DB` is a globally distributed,` multi-model database service provided by Microsoft Azure`. It is designed to offer high availability, scalability, and low-latency access to data for modern applications. Unlike traditional relational databases, Cosmos DB is a `NoSQL database, meaning it can handle unstructured, semi-structured, and structured data types`. `It supports multiple data models, including document, key-value, graph, and column-family, making it versatile for various use cases.` <br/> <br/>
> An `Azure Cosmos DB container` is a `logical unit` within a Cosmos DB database where data is stored. `Containers are schema-agnostic, meaning they can store items with different structures. Each container is automatically partitioned to scale out across multiple servers, providing virtually unlimited throughput and storage`. Containers are the primary scalability unit in Cosmos DB, and they use a partition key to distribute data efficiently across partitions.

1. **Create a Cosmos DB Account**:
   - In the Azure portal, navigate to your **Resource Group**.
   - Click **+ Create**.
   - Search for `Cosmos DB`, click on `Create`:
     
      <img width="550" alt="image" src="https://github.com/user-attachments/assets/ecdb9a17-5623-4dc0-a607-92448950b7a0">

   - Choose your desired API type, for this will be using `Azure Cosmos DB for NoSQL`. This option supports a SQL-like query language, which is familiar and powerful for querying and analyzing your invoice data. It also integrates well with various client libraries, making development easier and more flexible.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/db942359-8a81-4289-9ea7-91234b4c3802">

   - Please enter an account name (e.g., `contosocosmosdbaidemo`). As with the previously configured resources, we will use the `Public network` for this example. Ensure that you adjust the architecture to include your networking requirements.
   - Select the region and other settings.
   - Click **Review + create** and then **Create**.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/42b415d3-0d38-4b69-9e18-7bc4015b4a6d">

2. **Create a Database and Container**:
   - Go to your Cosmos DB account.
   - Under **Data Explorer**, click **New Database**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/5f816576-8160-444c-8abc-086b450d98b1">

   - Enter a database name (e.g., `ContosoDBAIDemo`) and click **OK**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/5dcb8d28-b042-4038-ac37-2663b8013a3a">

   - Click **New Container**.
   - Enter a container name (e.g., `Invoices`) and set the partition key (e.g., `/transactionId`).
   - Click **OK**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/0232de53-ee75-4f20-a45d-49cf54e3f794">

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/50fc8358-c33d-436d-9661-4127465fc21b">

## Step 4: Set Up Azure Functions for Document Ingestion and Processing

> An `Azure Function App` is a `container for hosting individual Azure Functions`. It provides the execution context for your functions, allowing you to manage, deploy, and scale them together. `Each function app can host multiple functions, which are small pieces of code that run in response to various triggers or events, such as HTTP requests, timers, or messages from other Azure services`. <br/> <br/>
> Azure Functions are designed to be lightweight and event-driven, enabling you to build scalable and serverless applications. `You only pay for the resources your functions consume while they are running, making it a cost-effective solution for many scenarios`.

### Create a Function App

- In the Azure portal, go to your **Resource Group**.
- Click **+ Create**.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/efac220b-72db-447b-98a7-58196b3d39dd">

- Search for `Function App`, click on `Create`:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/571c2880-cff7-4ed5-9840-2f1b5f58ce46">

- Choose a `hosting option`; for this example, we will use `Consumption`. Click [here for a quick overview of hosting options](https://github.com/brown9804/MicrosoftCloudEssentialsHub/tree/main/0_Azure/3_AzureAI/14_AIUseCases/0_PDFProcessingFAOF#function-app-hosting-options):
       
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/a8bd30c5-7b21-4aac-adf2-6e1dc5ec509a">

- Enter a name for the Function App (e.g., `ContosoFunctionAppAI`).
- Choose your runtime stack (e.g., `.NET` or `Python`).
- Select the region and other settings.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/e32fb474-c954-475b-971e-599f9909d35a">

- Select **Review + create** and then **Create**. Verify the resources created in your `Resource Group`.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/352c95c7-bf6a-4e1d-937b-98dc018b69a4">

 > [!IMPORTANT]
 > This example is using system-assigned managed identity to assign RBACs (Role-based Access Control).
 > <img width="550" alt="image" src="https://github.com/user-attachments/assets/dd5ce062-9720-40d3-b860-778048c38e6c">

- Please assign the `Storage Blob Data Contributor` and `Storage File Data SMB Share Contributor` roles to the `Function App` within the `Storage Account` related to the runtime (the one created with the function app).

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/a08f77bf-71d4-4922-8001-cf402e9e81f2">

- Assign `Storage Blob Data Reader` to the `Function App` within the `Storage Account` that will contains the invoices, click `Next`. Then, click on `select members` and search for your `Function App` identity. Finally click on `Review + assign`:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/dcfdd7f0-f7a6-4829-876a-87383887e0e2">

- Also add `Cosmos DB Operator`, `DocumentDB Account Contributor`, `Azure AI Administrator`, `Cosmos DB Account Reader Role`, `Contributor`:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/7570747e-a5f1-4090-98ce-b44928ef1f57">

- To assign the `Microsoft.DocumentDB/databaseAccounts/readMetadata` permission, you need to create a custom role in Azure Cosmos DB. This permission is required for accessing metadata in Cosmos DB. Click [here to understand more about it](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/security/how-to-grant-data-plane-role-based-access?tabs=built-in-definition%2Ccsharp&pivots=azure-interface-cli#prepare-role-definition).

    | **Aspect**         | **Data Plane Access**                                                                 | **Control Plane Access**                                                                 |
    |--------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
    | **Scope**          | Focuses on `data operations` within databases and containers. This includes actions such as reading, writing, and querying data in your databases and containers. | Focuses on `management operations` at the account level. This includes actions such as creating, deleting, and configuring databases and containers. |
    | **Roles**          | - `Cosmos DB Built-in Data Reader`: Provides read-only access to data within the databases and containers. <br> - `Cosmos DB Built-in Data Contributor`: Allows read and write access to data within the databases and containers. <br> - `Cosmos DB Built-in Data Owner`: Grants full access to manage data within the databases and containers. | - `Contributor`: Grants full access to manage all Azure resources, including Cosmos DB. <br> - `Owner`: Grants full access to manage all resources, including the ability to assign roles in Azure RBAC. <br> - `Cosmos DB Account Contributor`: Allows management of Cosmos DB accounts, including creating and deleting databases and containers. <br> - `Cosmos DB Account Reader`: Provides read-only access to Cosmos DB account metadata. |
    | **Permissions**    | - `Reading documents` <br> - `Writing documents` <br> - Managing data within containers. | - `Creating or deleting databases and containers` <br> - Configuring settings <br> - Managing account-level configurations. |
    | **Authentication** | Uses `Azure Active Directory (AAD) tokens` or `resource tokens` for authentication.                      | Uses `Azure Active Directory (AAD)` for authentication.                                 |

> Steps to assing it:

1. **Open Azure CLI**: Go to the [Azure portal](portal.azure.com) and click on the icon for the Azure CLI.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/b2643d9a-7364-454a-bb24-f16270e99d92">

2. **List Role Definitions**: Run the following command to list all of the role definitions associated with your Azure Cosmos DB for NoSQL account. Review the output and locate the role definition named `Cosmos DB Built-in Data Contributor`.

     ```powershell
     az cosmosdb sql role definition list \
         --resource-group "<your-resource-group>" \
         --account-name "<your-account-name>"
     ```
    
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/4c19d70e-d525-4c15-bb0e-518f50f61b37">
    

3. **Get Cosmos DB Account ID**: Run this command to get the ID of your Cosmos DB account. Record the value of the `id` property as it is required for the next step.

     ```powershell
     az cosmosdb show --resource-group "<your-resource-group>" --name "<your-account-name>" --query "{id:id}"
     ```

     Example output:
    
     ```json
    {                                                               
      "id": "/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.DocumentDB/databaseAccounts/{cosmos-account-name}"
    }     
     ```
    
     <img width="750" alt="image" src="https://github.com/user-attachments/assets/f3426130-2de5-46a0-96f0-4c6e15e57975">

4. **Assign the Role**: Assign the new role using `az cosmosdb sql role assignment create`. Use the previously recorded role definition ID for the `--role-definition-id` argument, the unique identifier for your identity for the `--principal-id` argument, and your account's ID for the `--scope` argument.
  
     > You can extract the `principal-id`, from `Identity` of the `Function App`:
    
      <img width="550" alt="image" src="https://github.com/user-attachments/assets/89c524ce-a392-4507-90ad-19becddff923">
    
     ```powershell
     az cosmosdb sql role assignment create \
         --resource-group "<your-resource-group>" \
         --account-name "<your-account-name>" \
         --role-definition-id "<role-definition-id>" \
         --principal-id "<principal-id>" \
         --scope "/subscriptions/{subscriptions-id}/resourceGroups/{resource-group-name}/providers/Microsoft.DocumentDB/databaseAccounts/{cosmos-account-name}"
     ```

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/72e1e4f9-9228-4ec0-aade-20ad4aaa1f4f">
    
    > After a few minutes, you will see something like this:
    
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/5caea3b9-3e4d-4791-8376-fda4547547bd">

5. **Verify Role Assignment**: Use `az cosmosdb sql role assignment list` to list all role assignments for your Azure Cosmos DB for NoSQL account. Review the output to ensure your role assignment was created.
    
     ```powershell
     az cosmosdb sql role assignment list \
         --resource-group "<your-resource-group>" \
         --account-name "<your-account-name>"
     ```

    <img width="750" alt="image" src="https://github.com/user-attachments/assets/8c7675cf-8183-433c-a21b-f9b7029642d9">
    
### Configure/Validate the Environment variables

- Under `Settings`, go to `Environment variables`. And `+ Add` the following variables:

 -  `COSMOS_DB_ENDPOINT`: Your Cosmos DB account endpoint.
 -  `COSMOS_DB_KEY`: Your Cosmos DB account key.
 -  `contosostorageaidemo_STORAGE`: Your Storage Account key.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/ab7cdaad-8939-4a82-99e3-5e7cfd24e908">

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/905aa59c-9083-4cad-8eb8-b73e5712d2df">

 - Click on `Apply` to save your configuration.

### Develop the Function
- You need to install [VSCode](https://code.visualstudio.com/download)
- Install python from Microsoft store:
   
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/30f00c27-da0d-400f-9b98-817fd3e03b1c">

- Open VSCode, and install some extensions: `python`, and `Azure Tools`.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/715449d3-1a36-4764-9b07-99421fb1c834">

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/854aa665-dc2f-4cbf-bae2-2dc0a8ef6e46">

- Click on the `Azure` icon, and `sign in` into your account. Allow the extension `Azure Resources` to sign in using Microsoft, it will open a browser window. After doing so, you will be able to see your subscription and resources.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/4824ca1c-4959-4242-95af-ad7273c5530d">

- Under Workspace, click on `Create Function Project`, and choose a path in your local computer to develop your function.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/8db80e51-725e-45fe-91b5-7158fd94be8e">

- Choose the language, in this case is `python`:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/2fb19a1e-bb2d-47e5-a56e-8dc8a708647a">

- Select the model version, for this example let's use `v2`:
 
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/fd46ee93-d788-463d-8b28-dbf2487e9a7f">

- For the python interpreter, let's use the one installed via `Microsoft Store`:

    <img width="741" alt="image" src="https://github.com/user-attachments/assets/3605c959-fc59-461f-9e8d-01a6a92004a8">

- Choose a template (e.g., **Blob trigger**) and configure it to trigger on new PDF uploads in your Blob container.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/0a4ed541-a693-485c-b6ca-7d5fb55a61d2">

- Provide a function name, like `BlobTriggerContosoPDFInvoicesRaw`:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/9cbc7605-8cb3-41f8-b3f7-3dfc9b8e67b5">

- Next, it will prompt you for the path of the blob container where you expect the function to be triggered after a file is uploaded. In this case is `pdfinvoices` as was previously created.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/7005dc44-ffe2-442b-8373-554b229b3042">

- Click on `Create new local app settings`, and then choose your subscription.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/07c211d6-eda0-442b-b428-cdaed2bf12ac">

- Choose `Azure Storage Account for remote storage`, and select one. I'll be using the `contosostorageaidemo`. 

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/1ca2a494-2716-4b5a-8e7d-caca1eaf88ab">

- Then click on `Open in the current window`. You will see something like this:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/59fa0a79-2a23-4864-968f-9f933826dbca">

- Now we need to update the function code to extract data from PDFs and store it in Cosmos DB, use this an example:

 > 1. **Blob Trigger**: The function is triggered when a new PDF file is uploaded to the `pdfinvoices` container. <br/>
 > 2. **PDF Processing**: The read_pdf_content function uses pdfminer.six to read and extract text from the PDF. <br/>
 > 3. **Data Extraction**: The extracted text is processed to extract invoice data. The `generate_id` function generates a unique ID for each invoice. <br/>
 > 4. **Data Storage**: The processed invoice data is saved to Azure Cosmos DB in the `ContosoAIDemo` database and `Invoices` container. 

 > `pdfminer.six` is an open-source framework. It is a community-maintained fork of the original PDFMiner,` designed for extracting and analyzing text data from PDF documents`. The framework is built in a modular way, allowing each component to be easily replaced or extended for various purpose

 - Update the `function_app.py`:

  | Template Blob Trigger | Function Code updated |
  | --- | --- |
  |      <img width="550" alt="image" src="https://github.com/user-attachments/assets/a4ac6f2d-1419-4629-8896-de202c76000e"> | <img width="550" alt="image" src="https://github.com/user-attachments/assets/a9e41cd7-9c3f-4da5-8526-5c7f06107a84"> | 

  ```python
  import azure.functions as func
  import logging
  import json
  import os
  import uuid
  import io
  from pdfminer.high_level import extract_text
  from azure.cosmos import CosmosClient, PartitionKey
  
  app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
  
  def read_pdf_content(myblob):
      # Read the blob content into a BytesIO stream
      blob_bytes = myblob.read()
      pdf_stream = io.BytesIO(blob_bytes)
      
      # Extract text from the PDF stream
      text = extract_text(pdf_stream)
      return text
  
  def extract_invoice_data(text):
      lines = text.split('\n')
      invoice_data = {
          "id": generate_id(),
          "customer_name": "",
          "customer_email": "",
          "customer_address": "",
          "company_name": "",
          "company_phone": "",
          "company_address": "",
          "rentals": []
      }
  
      for i, line in enumerate(lines):
          if "BILL TO:" in line:
              invoice_data["customer_name"] = lines[i + 1].strip()
              invoice_data["customer_email"] = lines[i + 2].strip()
              invoice_data["customer_address"] = lines[i + 3].strip()
          elif "Company Information:" in line:
              invoice_data["company_name"] = lines[i + 1].strip()
              invoice_data["company_phone"] = lines[i + 2].strip()
              invoice_data["company_address"] = lines[i + 3].strip()
          elif "Rental Date" in line:
              for j in range(i + 1, len(lines)):
                  if lines[j].strip() == "":
                      break
                  rental_details = lines[j].split()
                  rental_date = rental_details[0]
                  title = " ".join(rental_details[1:-3])
                  description = rental_details[-3]
                  quantity = rental_details[-2]
                  total_price = rental_details[-1]
                  invoice_data["rentals"].append({
                      "rental_date": rental_date,
                      "title": title,
                      "description": description,
                      "quantity": quantity,
                      "total_price": total_price
                  })
  
      logging.info("Successfully extracted invoice data.")
      return invoice_data
  
  def save_invoice_data_to_cosmos(invoice_data, blob_name):
      try:
          endpoint = os.getenv("COSMOS_DB_ENDPOINT")
          key = os.getenv("COSMOS_DB_KEY")
          client = CosmosClient(endpoint, key)
          logging.info("Successfully connected to Cosmos DB.")
      except Exception as e:
          logging.error(f"Error connecting to Cosmos DB: {e}")
          return
      
      database_name = 'ContosoDBAIDemo'
      container_name = 'Invoices'
      
      try:
          database = client.create_database_if_not_exists(id=database_name)
          container = database.create_container_if_not_exists(
              id=container_name,
              partition_key=PartitionKey(path="/invoice_number"),
              offer_throughput=400
          )
          logging.info("Successfully ensured database and container exist.")
      except Exception as e:
          logging.error(f"Error creating database or container: {e}")
          return
      
      try:
          response = container.upsert_item(invoice_data)
          logging.info(f"Saved processed invoice data to Cosmos DB: {response}")
      except Exception as e:
          logging.error(f"Error inserting item into Cosmos DB: {e}")
  
  def generate_id():
      return str(uuid.uuid4())
  
  @app.blob_trigger(arg_name="myblob", path="pdfinvoices/{name}",
                    connection="contosostorageaidemo_STORAGE")
  def BlobTriggerContosoPDFInvoicesRaw(myblob: func.InputStream):
      logging.info(f"Python blob trigger function processed blob\n"
                   f"Name: {myblob.name}\n"
                   f"Blob Size: {myblob.length} bytes")
  
      try:
          text = read_pdf_content(myblob)
          logging.info("Successfully read and extracted text from PDF.")
      except Exception as e:
          logging.error(f"Error reading PDF: {e}")
          return
  
      logging.info(f"Extracted text from PDF: {text}")
  
      try:
          invoice_data = extract_invoice_data(text)
          logging.info(f"Extracted invoice data: {invoice_data}")
      except Exception as e:
          logging.error(f"Error extracting invoice data: {e}")
          return
  
      try:
          save_invoice_data_to_cosmos(invoice_data, myblob.name)
          logging.info("Successfully saved invoice data to Cosmos DB.")
      except Exception as e:
          logging.error(f"Error saving invoice data to Cosmos DB: {e}")
  ```

- Now, let's update the `requirements.txt`:

| Template `requirements.txt` | Updated `requirements.txt` |
| --- | --- |
| <img width="550" alt="image" src="https://github.com/user-attachments/assets/d7dec16e-4f78-446d-a7e0-4d3b1d43bec4"> | <img width="550" alt="image" src="https://github.com/user-attachments/assets/b30e6450-515b-4070-b91b-8040ecbde738"> 

```text
azure-functions
pdfminer.six
azure-cosmos==4.3.0
```
- Since this function has already been tested, you can deploy your code to the function app in your subscription. If you want to test, you can use run your function locally for testing.
  - Click on the `Azure` icon.
  - Under `workspace`, click on the `Function App` icon.
  - Click on `Deploy to Azure`.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/a9f90f93-a8ce-467f-a675-f9b8737f5a3e">

  - Select your `subscription`, your `function app`, and accept the prompt to overwrite:

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/a6492b14-491c-44d6-8d5a-f9ea670f174b">

  - After completing, you see the status in your terminal:

     <img width="959" alt="image" src="https://github.com/user-attachments/assets/f742fb8e-4974-4222-b67e-c3dc6939740f">

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/94052759-4c0f-483d-8a78-5803fab5c961">

> [!IMPORTANT]
If you need further assistance with the code, please click [here to view all the function code](./src/).

## Step 5: Test the solution

> Upload sample PDF invoices to the Blob container and verify that data is correctly ingested and stored in Cosmos DB.

- Click on `Upload`, then select `Browse for files` and choose your PDF invoices to be stored in the blob container, which will trigger the function app to parse them.

   <img width="950" alt="image" src="https://github.com/user-attachments/assets/b45d203c-0392-4488-bf21-f9b6129c9709">

- Check the logs, and traces from your function with `Application Insights`:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/b4ce7b7c-abab-4209-8af3-6c30dc5f667b">

- Under `Investigate`, click on `Performance`. Filter by time range, and `drill into the samples`. Sort the results by date (if you have many, like in my case) and click on the last one.

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/01bdebef-85af-4906-b9c0-3761e3a67c1f">

- Click on `View all`:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/355ed2ec-ff2f-4571-99c2-6c4afc6c9aff">

- Check all the logs, and traces generated. Also review the information parsed:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/4cc6ec56-5419-4668-aad1-7e59d8182ea5">

- Validate that the information was uploaded to the Cosmos DB. Under `Data Explorer`, check your `Database`:

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/28bba46b-eaf0-4bbc-a565-f7c1ad8a0ac6">

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
