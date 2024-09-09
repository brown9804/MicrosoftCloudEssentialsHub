# Integrating Azure Language Services with Power Automate - Demo

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-09-09

----------

## Wiki 

## How to 

-  Step 1: Create a Language Resource in Azure
    1. **Sign in to Azure Portal**:
       - Go to Azure portal.
       - Use your credentials to sign in.
    2. **Create a New Resource**:
       - Click on **Create a resource** in the left-hand menu.
       - In the search bar, type **Language** and select **Language** from the list.
       - Click **Create**.
    3. **Configure the Resource**:
       - Fill in the necessary details like **Subscription**, **Resource Group**, **Region**, and **Name**.
       - Choose the **Pricing tier** that suits your needs.
       - Click **Review + create** and then **Create**.
    4. **Retrieve Endpoint and Key**:
       - Once the resource is created, navigate to it.
       - In the left-hand menu, select **Keys and Endpoint**.
       - Note down the **Key1** and **Endpoint**. You will need these for Power Automate.
-  Step 2: Set Up Power Automate Flow
    1. **Sign in to Power Automate**:
       - Go to Power Automate.
       - Use your credentials to sign in.
    2. **Create a New Flow**:
       - Click on **My flows** in the left-hand menu.
       - Select **New flow** and then **Automated cloud flow**.
       - Name your flow and click **Skip** to continue without choosing a trigger.
    3. **Add a Trigger**:
       - Under **Triggers**, select **Manually trigger a flow**.
       - Click **Create**.
-  Step 3: Add Language Service Connector
    1. **Add a New Step**:
       - Click on **+ New step**.
       - In the search bar, type **Azure AI Language**.
    2. **Select an Action**: Choose the action you need, such as **Named Entity Recognition** or any other relevant action.
    3. **Authenticate the Connector**:
       - You will be prompted to enter the **Endpoint** and **Key** from the Language resource you created in Azure.
       - Enter these details to authenticate.
-  Step 4: Integrate with OCR Engine
    1. **Add Another Step**:
       - Click on **+ New step**.
       - In the search bar, type **Computer Vision**.
    2. **Select an OCR Action**: Choose the action you need, such as **Read** or **Recognize Text**.
    3. **Authenticate the Connector**: Enter the **Endpoint** and **Key** from your Computer Vision resource in Azure.
-  Step 5: Test Your Flow
    1. **Save Your Flow**: Click **Save** at the top right corner.
    2. **Test the Flow**:
       - Click **Test** from the top navigation menu.
       - Follow the prompts to test your flow and ensure it works as expected.

