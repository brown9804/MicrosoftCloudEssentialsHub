# Building a Custom AI Copilot with Azure AI Studio

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-01

----------

## Wiki 

- [Tutorial: Deploy an Enterprise Chat web app](https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/deploy-chat-web-app)
- [Tutorial: Part 1 - Create resources for building a custom chat application with the prompt flow SDK](https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/copilot-sdk-create-resources)

Some of the trending AI models in Azure AI Studio. Keep in mind to `assess model performance with evaluated metrics`. You can use `model benchmarks` for guidance.

| **Model Name**       | **Provider** | **Strengths**                                                                 |
|----------------------|--------------|-----------------------------------------------------------------------------|
| **o1-preview**       | OpenAI       | Excels in complex coding, math reasoning, brainstorming, and comparative analysis|
| **o1-mini**          | OpenAI       | Optimized for shorter context tasks, efficient in instruction following and workflow management|
| **gtp4o-mini**       | OpenAI       | Compact version of GPT-4, ideal for lightweight applications and faster response times|
| **GPT-4**            | OpenAI       | Large multimodal model, excels in text and image inputs, human-level performance on various benchmarks|
| **GPT-4o**           | OpenAI       | Multimodal model with real-time reasoning across audio, vision, and text, faster and more cost-effective|
| **Phi-2**            | Microsoft    | Efficient for general-purpose language tasks with better latency and lower costs|
| **Phi-3**            | Microsoft    | Most capable and cost-effective small language models, outperforming models of the same size and next size up across various benchmarks|
| **Phi-3-mini**       | Microsoft    | Small language model with a context window of up to 128K tokens, optimized for instruction following|
| **Phi-3-small**      | Microsoft    | 7B parameter model, excels in language, reasoning, coding, and math tasks|
| **Phi-3-medium**     | Microsoft    | 14B parameter model, offering high performance across a variety of tasks|
| **Orca 2**           | Microsoft    | Advanced language understanding and generation, suitable for nuanced text tasks|
| **Meta Llama 3**     | Meta         | Large-scale NLP tasks, pre-trained with billions of parameters for diverse applications|
| **Command R+**       | Cohere       | Retrieval-augmented generation, enhancing information retrieval and text generation|
| **Stable Diffusion 2.1** | Stability AI | High-quality image generation, robust for creative and design tasks|
| **JAIS**             | Core42       | Leading Arabic language model, optimized for Arabic NLP tasks|
| **Nixtla**           | Nixtla       | Specialized in time-series forecasting and anomaly detection|

## How to 

- Step 1: Creating an Azure AI Studio Resource with Azure Open Studio
  - Sign in to Azure Portal
    1. Go to the Azure Portal.
    2. Sign in with your Azure subscription credentials.
  - Create a New Resource
    1. In the Azure Portal, select `Create a resource`.
    2. Search for `Azure AI Studio` in the search bar.
    3. Select `Azure AI Studio` from the search results and click `Create`.
  - Configure the Resource
    1. `Subscription:` Choose your Azure subscription.
    2. `Resource Group:` Select an existing resource group or create a new one.
    3. `Region:` Choose a region where the desired model is available.
    4. `Name:` Provide a unique name for your Azure AI Studio resource.
    5. `Pricing Tier:` Select the appropriate pricing tier (Standard is typically available).
  - Configure how data will be stored: Is used as the default datastore for the AI hub. You may create a new Azure Storage resource or select an existing one in your subscription.
  - Network Configuration: Choose the appropriate network security option:
     - `All networks:` Allows access from any network.
     - `Selected networks:` Restricts access to specific virtual networks.
     - `Disabled:` No network access (private endpoint connections only).
  - Review and Create
    1. Review your configurations.
    2. Click `Create` to deploy the resource.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/b9e5b4c2-2d74-4d50-9be9-31b31d4f4694">

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/de646a19-be04-4fe8-8350-92d613043d79">

- Step 2: Create a New Project in Azure AI Studio
  - **Navigate to AI Studio**: Go to the Azure AI Hub created, anc launch the Azure AI Studio from the Azure portal.
      
      <img width="300" alt="image" src="https://github.com/user-attachments/assets/f491d6d5-a332-4518-ba14-7f931f4c9be9">

  - **Create Project**: Click on `Create new project` and provide the necessary details like project name and description.
  
      <img width="550" alt="image" src="https://github.com/user-attachments/assets/b4e5c8f3-298d-4ab9-bb8e-7087d974e77a">

- Step 3: Choose a Model
  - **Model Catalog**: Browse the model catalog in Azure AI Studio.
  - **Select Model**: Choose a model that fits your use case, for example gpt-4o-mini.
    
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/d7e96dd0-7e18-4bb4-9226-63a345632b1b">

- Step 4: Add Your Data
  - **Data Integration**: Integrate your own data into the model. This can include:
      - **Product Information**: Upload product catalogs or databases.
      - **Customer Data**: Include customer interaction logs or CRM data.
  
      | **Step**               | **Description**                                                                 |
      |------------------------|---------------------------------------------------------------------------------|
      | **Identify Data Sources** | - Product Information: Gather product catalogs, databases, or any relevant product data. <br/> - Customer Data: Collect customer interaction logs, CRM data, or any other customer-related information. |
      | **Prepare Data**       | - Format Data: Ensure your data is in a compatible format (e.g., CSV, JSON, SQL databases). <br/> - Clean Data: Remove any inconsistencies or irrelevant information to improve data quality. |
      | **Upload Data**        | - Azure Blob Storage: Upload your data to Azure Blob Storage for easy access and integration. <br/> - Azure Data Lake: Alternatively, use Azure Data Lake for large-scale data storage and analytics. |
  
  - **Data Sources**: Use Azure Data Factory or other data integration tools to connect your data sources.
  
    | **Method**               | **Description**                                                                 |
    |------------------------|---------------------------------------------------------------------------------|
    | **Use Azure Data Factory**       | - Create Data Pipelines: Set up data pipelines in Azure Data Factory to automate the data integration process. <br/>   - Connect Data Sources: Use built-in connectors to link various data sources (e.g., SQL databases, Blob Storage, REST APIs). <br/>   - Transform Data: Apply data transformation steps as needed to prepare the data for integration. |
    | **Direct Integration** | - APIs: Use APIs to directly integrate data from external sources into your Azure AI Studio project. <br/>   - Custom Scripts: Write custom scripts (e.g., in Python) to fetch and process data before integrating it into the model. |
    | `Data Validation`   | - Check Data Quality: Validate the integrated data to ensure it meets the required standards. <br/>   - Test Integration: Run tests to confirm that the data is correctly integrated and accessible by the model. |

  - Add your data: Create the connection if required, if you already have it, you can you can select your data.

    <img width="764" alt="image" src="https://github.com/user-attachments/assets/b0c50db6-c16c-48fd-98ff-c68354de030d">

  - Validate your data was uploaded:

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/6b350e0c-6c0b-41d7-aa10-e948c20f06db">


### 6. Create a Prompt Flow
- **Design Interaction**: Use the prompt flow feature to design how your copilot will interact with users.
  - **Set Up Prompts**: Define the initial prompts and expected responses.
  - **Branching Logic**: Create branches for different user inputs and scenarios.

### 7. Customize with Multiple Data Sources
- **Enhance Responses**: Integrate multiple data sources to provide more accurate and comprehensive responses.
  - **Azure Cognitive Search**: Use Azure Cognitive Search to index and search your data.
  - **Hybrid Search**: Combine semantic search with traditional keyword search for better results.

### 8. Evaluate and Test
- **Evaluation Dataset**: Use a question and answer evaluation dataset to test your copilot's performance.
  - **Manual Testing**: Manually test the copilot with various queries.
  - **Automated Testing**: Set up automated tests to continuously evaluate performance.
- **Adjustments**: Make necessary adjustments based on test results to improve accuracy and relevance.

### 9. Deploy Your Copilot
- **Deployment Endpoint**: Deploy your copilot to an endpoint for consumption.
  - **Azure Functions**: Use Azure Functions to create a serverless endpoint.
  - **API Management**: Manage and secure your API with Azure API Management.

### 10. Monitor and Update
- **Performance Monitoring**: Continuously monitor your copilot's performance using Azure Monitor.
  - **Metrics and Logs**: Track key metrics and logs to identify issues.
  - **Alerts**: Set up alerts for critical issues.
- **Regular Updates**: Update your copilot with new data or improved prompt flows as needed.
  - **Feedback Loop**: Incorporate user feedback to refine and enhance the copilot.

