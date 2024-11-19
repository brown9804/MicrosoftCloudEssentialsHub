# Building a Scalable Cloud-Based Database for Automated PDF Invoice Processing and Analytics

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-19

----------

> Using Azure Functions, Blob Storage, and Cosmos DB

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Azure Cosmos DB - Database for the AI Era](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
- [What is Azure SQL Database?](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql)
 
</details>

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

### Step 1: Set Up Your Azure Environment

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

### Step 2: Set Up Azure Blob Storage for PDF Ingestion

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

   - Create another container for `processedinvoices`:
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/1e7da13b-3b8f-4f75-b9cb-79ab14797620">

### Step 3: Set Up Azure Cosmos DB

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

1. **Create a Database and Container**:
   - Go to your Cosmos DB account.
   - Under **Data Explorer**, click **New Database**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/5f816576-8160-444c-8abc-086b450d98b1">

   - Enter a database name (e.g., `ContosoDBAIdemo`) and click **OK**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/5dcb8d28-b042-4038-ac37-2663b8013a3a">

   - Click **New Container**.
   - Enter a container name (e.g., `Invoices`) and set the partition key (e.g., `/transactionId`).
   - Click **OK**.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/0232de53-ee75-4f20-a45d-49cf54e3f794">

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/50fc8358-c33d-436d-9661-4127465fc21b">

### Step 4: Set Up Azure Functions for Document Ingestion and Processing

> An `Azure Function App` is a `container for hosting individual Azure Functions`. It provides the execution context for your functions, allowing you to manage, deploy, and scale them together. `Each function app can host multiple functions, which are small pieces of code that run in response to various triggers or events, such as HTTP requests, timers, or messages from other Azure services`. <br/> <br/>
> Azure Functions are designed to be lightweight and event-driven, enabling you to build scalable and serverless applications. `You only pay for the resources your functions consume while they are running, making it a cost-effective solution for many scenarios`.

1. **Create a Function App**:
   - In the Azure portal, go to your **Resource Group**.
   - Click **+ Create**.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/efac220b-72db-447b-98a7-58196b3d39dd">

   - Search for `Function App`, click on `Create`:

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/571c2880-cff7-4ed5-9840-2f1b5f58ce46">

   - Choose a `hosting option`; for this example, we will use `Consumption`. Click [here for a quick overview of hosting options](#function-app-hosting-plans):
           
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/a8bd30c5-7b21-4aac-adf2-6e1dc5ec509a">

   - Enter a name for the Function App (e.g., `ContosoFunctionAppAI`).
   - Choose your runtime stack (e.g., `.NET` or `Python`).
   - Select the region and other settings.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/e32fb474-c954-475b-971e-599f9909d35a">

   - Select **Review + create** and then **Create**. Verify the resources created in your `Resource Group`.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/352c95c7-bf6a-4e1d-937b-98dc018b69a4">

2. **Configure/Validate** the `Environment variables`:
   - Under `Settings`, go to `Environment variables`. And `+ Add` the following variables:

     -  `COSMOS_DB_ENDPOINT`: Your Cosmos DB account endpoint.
     -  `COSMOS_DB_KEY`: Your Cosmos DB account key.

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/ab7cdaad-8939-4a82-99e3-5e7cfd24e908">
    
         <img width="550" alt="image" src="https://github.com/user-attachments/assets/905aa59c-9083-4cad-8eb8-b73e5712d2df">

     - Click on `Apply` to save your configuration.

3. **Develop the Function**:
   - Go to your Function App.
   - Click on `Create function`.
   - Choose a template (e.g., **Blob trigger**) and configure it to trigger on new PDF uploads in your Blob container.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/3f111059-5d1b-4d63-9209-ac9be286b1c8">

   - Provide a function name, like `BlobTriggerPDFInvoices`
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/42476ff7-072b-40b1-9c72-c21e18dca103">

   - Choose the right path to your blob container, in this example `pdfinvoices`. And click `Create`.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/4e8692b4-bda7-4bdc-a61b-a4c377cccbba">

   - You will see something like this:
 
      <img width="550" alt="image" src="https://github.com/user-attachments/assets/a16a571d-d3e2-444d-80ff-451d6c00de4f">

   - Update the function code to extract data from PDFs and store it in Cosmos DB, use this an example. Click on `Save`.
      
     > 1. **Blob Trigger**: The function is triggered when a new PDF file is uploaded to the `pdfinvoices` container. <br/>
     > 2. **PDF Processing**: The read_pdf_content function uses pdfminer.six to read and extract text from the PDF. <br/>
     > 3. **Data Extraction**: The extracted text is processed to extract invoice data. The `generate_id` function generates a unique ID for each invoice. <br/>
     > 4. **Data Storage**: The processed invoice data is saved to Azure Cosmos DB in the `ContosoAIDemo` database and `Invoices` container.

      ```python
      import azure.functions as func
      import logging
      import PyPDF2
      import json
      import os
      from azure.cosmos import CosmosClient, PartitionKey
      import uuid

      app = func.FunctionApp()

      # Function Definitions
      
      def extract_invoice_data(text):
          # Extract invoice data from the text
          lines = text.split('\n')
          invoice_data = {
              "id": generate_id(),  # Generate a unique ID for the invoice
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
                  # Extract rental details
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
          # Connect to Cosmos DB
          try:
              endpoint = os.getenv("COSMOS_DB_ENDPOINT")
              key = os.getenv("COSMOS_DB_KEY")
              client = CosmosClient(endpoint, key)
              logging.info("Successfully connected to Cosmos DB.")
          except Exception as e:
              logging.error(f"Error connecting to Cosmos DB: {e}")
              return
          
          # Database and container names
          database_name = 'ContosoDBAIDemo'
          container_name = 'Invoices'
          
          try:
              # Create database and container if they don't exist
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
              # Insert the invoice data into Cosmos DB
              response = container.upsert_item(invoice_data)
              logging.info(f"Saved processed invoice data to Cosmos DB: {response}")
          except Exception as e:
              logging.error(f"Error inserting item into Cosmos DB: {e}")
      
      def generate_id():
          # Generate a unique ID for the invoice
          return str(uuid.uuid4())
      
      # Main Function
      
      @app.blob_trigger(arg_name="myblob", path="pdfinvoices/{name}",
                        connection="contosostorageaidemo_STORAGE")
      def blob_trigger(myblob: func.InputStream, name: str):
          logging.info(f"Python blob trigger function processed blob\n"
                       f"Name: {myblob.name}\n"
                       f"Blob Size: {myblob.length} bytes")
      
          # Read the PDF content
          try:
              reader = PyPDF2.PdfFileReader(myblob)
              text = ""
              for page_num in range(reader.numPages):
                  page = reader.getPage(page_num)
                  text += page.extract_text()
              logging.info("Successfully read and extracted text from PDF.")
          except Exception as e:
              logging.error(f"Error reading PDF: {e}")
              return
      
          logging.info(f"Extracted text from PDF: {text}")
      
          # Process the extracted text (e.g., extract invoice data)
          try:
              invoice_data = extract_invoice_data(text)
              logging.info(f"Extracted invoice data: {invoice_data}")
          except Exception as e:
              logging.error(f"Error extracting invoice data: {e}")
              return
      
          # Save the processed data to Cosmos DB
          try:
              save_invoice_data_to_cosmos(invoice_data, name)
              logging.info("Successfully saved invoice data to Cosmos DB.")
          except Exception as e:
              logging.error(f"Error saving invoice data to Cosmos DB: {e}")
      ```
       
   - You will see something like this:
  
       <img width="550" alt="image" src="https://github.com/user-attachments/assets/75e9d0ec-2c69-451c-b283-4b486bb80839">

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
