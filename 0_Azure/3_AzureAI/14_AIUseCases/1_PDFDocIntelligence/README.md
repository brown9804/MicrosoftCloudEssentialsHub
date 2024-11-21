<img width="709" alt="image" src="https://github.com/user-attachments/assets/e6fb0e9e-5ead-4bff-8643-27a8110ca63a"># Automated PDF Invoice Processing using <br/> Azure Storage + Document Intelligence + Cosmos DB

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-21

----------

> How to parse PDFs from an Azure Storage Account, process them using Azure Document Intelligence, and store the results in Cosmos DB. <br/> <br/>
> 1. Upload your PDFs to an Azure Blob Storage container. <br/>
> 2. An Azure Function is triggered by the upload, which calls the Azure Document Intelligence API to analyze the PDFs.  <br/>
> 3. The extracted data is parsed and subsequently stored in a Cosmos DB database, ensuring a seamless and automated workflow from document upload to data storage. 

> [!NOTE]
> Advantages of Document Intelligence for organizations handling with large volumes of documents: <br/>
> - Utilizes natural language processing, computer vision, deep learning, and machine learning. <br/>
> - Handles structured, semi-structured, and unstructured documents. <br/>
> - Automates the extraction and transformation of data into usable formats like JSON or CSV

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Azure Cosmos DB - Database for the AI Era](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)

</details>

## Content 



## Overview 

> `Azure Document Intelligence`, formerly known as **Form Recognizer**, is a powerful AI service that extracts structured data from documents. It `uses machine learning models to analyze and process various types of documents, such as invoices, receipts, business cards`, and more.

| Key Features | Details |
| --- | --- |
| **Prebuilt Models** | - **Invoice Model**: Extracts fields like invoice ID, date, vendor information, line items, totals, and more.<br/>- **Receipt Model**: Extracts merchant name, transaction date, total amount, and line items.<br/>- **Business Card Model**: Extracts contact information such as name, company, phone number, and email. |
| **Custom Models** | - **Training**: You can train custom models using labeled data. This involves uploading a set of documents and manually labeling the fields you want to extract.<br/>- **Model Management**: Manage versions of your custom models, retrain them with new data, and evaluate their performance. |
| **APIs and SDKs** | - **REST API**: Provides endpoints for analyzing documents, managing models, and retrieving results.<br/>- **SDKs**: Available in multiple languages (e.g., Python, C#, JavaScript) to simplify integration into your applications. |

> [!IMPORTANT]
> Regarding `Networking`, this example will cover `Public access configuration`. However, please ensure you `review your privacy requirements and adjust network and access settings as necessary for your specific case`.

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

   - Enter the Resource Group name (e.g., `RGContosoAIDoc`) and select a region (e.g., `East US 2`). You can add tags if needed.
   - Click **Review + create** and then **Create**.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/288d05ca-e5e3-47f7-9c0d-3ddb0fffe518">

## Step 2: Set Up Azure Blob Storage for PDF Ingestion

> An `Azure Storage Account` provides a `unique namespace in Azure for your data, allowing you to store and manage various types of data such as blobs, files, queues, and tables`. It serves as the foundation for all Azure Storage services, ensuring high availability, scalability, and security for your data. <br/> <br/>
> A `Blob Container` is a `logical grouping of blobs within an Azure Storage Account, similar to a directory in a file system`. Containers help organize and manage blobs, which can be any type of unstructured data like text or binary data. Each container can store an unlimited number of blobs, and you must create a container before uploading any blobs.

1. **Create a Storage Account**:
   - In the Azure portal, navigate to your **Resource Group**.
   - Click **+ Create**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/1998660c-bb80-4ea7-9865-b6cdfa125d02">

   - Search for `Storage Account`.
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/0bde893e-a40e-4dd6-bf55-964c33109e33">

   - Select the Resource Group you created.
   - Enter a Storage Account name (e.g., `invoicecontosostorage`).
   - Choose the region and performance options, and click `Next` to continue.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/bb5aeccc-e35f-45f2-a2a5-1000d92aa73a">

   - If you need to modify anything related to `Security, Access protocols, Blob Storage Tier`, you can do that in the `Advanced` tab.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/a478525f-6028-4f12-8b99-a441ed99fe0f">

   - Regarding `Networking`, this example will cover `Public access` configuration. However, please ensure you review your privacy requirements and adjust network and access settings as necessary for your specific case.
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/0273e197-6e5b-4a1c-93cc-7597730c384b">

   - Click **Review + create** and then **Create**. Once is done, you'll be able to see it in your Resource Group.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/a168a63b-2d15-4643-8200-34bf8335a0fe">

2. **Create a Blob Container**: Within the Storage Account, create a Blob Container to store your PDFs.
   - Go to your Storage Account.
   - Under **Data storage**, select **Containers**.
   - Click **+ Container**.
   - Enter a name for the container (e.g., `pdfinvoices`) and set the public access level to **Private**.
   - Click **Create**.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/27b024f8-0390-4331-bc34-59c3831d9bd1">

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

   - Please enter an account name (e.g., `contosoinvoiceaicosmos`). As with the previously configured resources, we will use the `Public network` for this example. Ensure that you adjust the architecture to include your networking requirements.
   - Select the region and other settings.
   - Click **Review + create** and then **Create**.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/47948255-3988-42f3-8e4e-80291aefaf5b">

2. **Create a Database and Container**:
   - Go to your Cosmos DB account.
   - Under **Data Explorer**, click **New Database**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/d0130cf2-aaf8-4a63-9786-4c65bc700812">

   - Enter a database name (e.g., `ContosoDBDocIntellig`) and click **OK**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/7839be4d-8d4d-476e-9d81-203b0fd2426f">

   - Click **New Container**.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/24e08dca-3399-40d2-a91d-95a6569156ad">

   - Enter a container name (e.g., `Invoices`) and set the partition key (e.g., `/transactionId`).
   - Click **OK**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/96ffc93a-078b-49f9-ad4a-470e73540c30">

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/203f4e0d-6697-4200-83bc-65f0023addb5">

## Step 4: Set Up Azure Document Intelligence

> `Azure Document Intelligence` offers robust capabilities for `extracting structured data from various document types using advanced machine learning models`. Technically, it provides `prebuilt models` for `common documents like invoices, receipts, and business cards, which can quickly extract key information without custom training. For more specific needs`, it allows `training custom models using labeled data, enabling precise extraction tailored to unique document formats`. The service is accessible via `REST APIs and SDKs` in multiple languages, facilitating seamless integration into applications. It supports `key-value pair extraction`, `table recognition`, and `text extraction`, making it a powerful tool for automating data entry, enhancing document management systems, and streamlining business processes.

1. Create Document Intelligence Resource
   - Go to the Azure Portal.
   - **Create a New Resource**:
      - Click on `Create a resource` and search for `document intelligence`.
      - Select `Document Intelligence` and click `Create`.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/e8783321-9bf3-42e2-83af-4d1c555205e3">

   - **Configure the Resource**:
      - **Subscription**: Select your Azure subscription.
      - **Resource Group**: Choose an existing resource group or create a new one.
      - **Region**: Select the region closest to your location.
      - **Name**: Provide a unique name for your Form Recognizer resource.
      - **Pricing Tier**: Choose the pricing tier that fits your needs (e.g., Standard S0).
   - Review your settings and click `Create` to deploy the resource.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/08335330-e9f5-455b-be22-6b938b979d99">

2. Configure Models
   - Using Prebuilt Models:
      - **Access Form Recognizer Studio**:
         - Navigate to your Form Recognizer resource in the Azure Portal.
         - Check your `Resource Group` if needed:

              <img width="550" alt="image" src="https://github.com/user-attachments/assets/d3559dc5-dbcb-44e6-b56d-d097d1719576">

         - Under `Overview`, click on `Go to Document Intelligence Studio`: 

              <img width="550" alt="image" src="https://github.com/user-attachments/assets/286545a3-574d-48d4-80de-66a58e5b5405">

      - **Select Prebuilt Models**: Choose the prebuilt model that matches your document type (e.g., "Invoices" for your PDF example).

           <img width="550" alt="image" src="https://github.com/user-attachments/assets/61b8fc8c-4fe2-4b28-a8bc-8459eb6bc9c3">

      - If the service resource for usage and billing is not configured, a window will appear requesting the resource information. In this case, we will use the one we recently created.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/f88bce37-d7f3-4312-9053-e06f0743cdb3">

      - **Analyze Document**:
         - Upload your PDF document to the Form Recognizer Studio.
           
              <img width="550" alt="image" src="https://github.com/user-attachments/assets/575cb5d1-8e3b-4855-8f15-246ee1ea13b8">

         - Click on `Run analysis`, the prebuilt model will automatically extract fields such as invoice ID, date, vendor information, line items, and totals.

              <img width="550" alt="image" src="https://github.com/user-attachments/assets/483ff4a5-73d3-4dcd-b35d-766f34a648b2">

         - Validate your results:

              <img width="550" alt="image" src="https://github.com/user-attachments/assets/a945bd72-ea1c-4d33-9699-f9257a2ceffa">

   - Training Custom Models (optional/if needed):
      - **Prepare Training Data**:
         - Collect a set of sample documents similar to your PDF example.
         - Label the fields you want to extract using the [Form Recognizer Labeling Tool](https://fott-2-1.azurewebsites.net/). Click [here for more information about to use it](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/v21/try-sample-label-tool?view=doc-intel-2.1.0#prerequisites-for-training-a-custom-form-model).
      - **Upload Training Data**: Upload the labeled documents to an Azure Blob Storage container.
      - Grant the necessary role (`Storage Blob Data Contributor`) to the Document Intelligence Account for the Storage Account to access the information. Otherwise, you may encounter an error like this:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/16feb31b-2a0e-4060-8e57-c870240a5109">

         - For this example we'll be using the system assigned identity to do that. Under `Identy` within your `Document Intelligence Account`, change the status to `On`, and click on `Save`:

            > A system assigned managed identity is restricted to `one per resource and is tied to the lifecycle of this resource`. `You can grant permissions to the managed identity by using Azure role-based access control (Azure RBAC). The managed identity is authenticated with Microsoft Entra ID, so you don’t have to store any credentials in code`.

           <img width="550" alt="image" src="https://github.com/user-attachments/assets/4be26e42-b9d4-4f04-ae5e-e8e6babd9366">

         - Go to your `Storage Account`, under `Access Control (IAM)` click on `+ Add`, and then `Add role assigment`:

           <img width="550" alt="image" src="https://github.com/user-attachments/assets/59881d40-eb4c-4276-b3d3-d5e7dd877af0">

         - Search for `Storage Blob Data Contributor`, click `Next`. Then, click on `select members` and search for your `Document intelligence identity`. Finally click on `Review + assign`:

            <img width="550" alt="image" src="https://github.com/user-attachments/assets/e8bbe706-8ecc-41bd-a189-846e82ccef01">

     - In the Form Recognizer Studio, select `Custom extraction model`.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/61c190d3-f795-4ac6-ab73-73e7e83b9dcc">

     - Scroll down, and click on `Create a project` (e.g, `pdfinvoiceproject`, `Extract information from pdf invoices`):

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/4d8eb2f1-a05e-47ca-b7a0-0f850a093e5f">

      - Configure the service resource for the project, choose `subscription`, `resource group`, `Document Intelligence or Cognitive Service Resource` and the `api version`.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/6a100714-844e-4a2a-a875-c50da88bc889">

      - Connect training data source: Provide the information of the Azure Blob Storage account and the folder that contains your training data.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/f15a9908-8710-4a3e-a457-8d557c8f2f48">

      - You can also `Auto label` if it's required:
            
          <img width="550" alt="image" src="https://github.com/user-attachments/assets/8552060b-f241-4d06-9a51-98b3b2171c08">

      - **Test the Model**:
         - Upload a new document to test the custom model.
         - Verify that the model correctly extracts the desired fields.

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
