# How to build Custom Copilots with Copilot Studio

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-31

----------

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Use entities and slot filling in copilots](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-entities-slot-filling)
- 

</details>

## Overview 

> Copilot Studio on the Microsoft Power Platform introduces a user-friendly way to build and customize AI copilots using low-code/no-code tools, making AI solution development accessible for everyone. It simplifies task automation, enhances customer interactions, and improves workflow efficiency. 

| Feature                        | Description                                                                 | Example Use Case                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Build Custom AI Solutions**  | Easily create AI copilots that can assist with a variety of tasks.           | - Creating a chatbot to handle customer inquiries on your website. <br> - Developing an AI assistant to manage inventory and restocking. |
| **Enhance Productivity**       | Automate repetitive tasks and free up time for more strategic activities.    | - Setting up an AI to automatically sort and respond to emails. <br> - Using an AI copilot to generate regular reports and analytics. |
| **Improve Customer Engagement**| Develop AI-driven interactions that enhance customer service and satisfaction.| - Implementing an AI assistant to provide personalized product recommendations. <br> - Creating an AI-driven feedback system to gather and analyze customer opinions. |
| **Integrate Seamlessly**       | Connect your AI copilots with other Microsoft tools and services for a cohesive experience.| - Integrating an AI copilot with Microsoft Teams to assist with scheduling and reminders. <br> - Connecting AI solutions with Power BI for advanced data visualization. |

## Examples of types of copilots using Microsoft tools

### 1. Copilot Agents

> **Tool**: Power Virtual Agents

**Steps**:
1. **Sign in to Power Virtual Agents**: Go to the Power Virtual Agents website and sign in with your Microsoft account.
2. **Create a New Bot**: Click on "Create a bot" and follow the prompts to set up your bot.
3. **Define Topics**: Add topics that your bot will handle. Topics are the different areas of conversation your bot can engage in.
4. **Build Conversations**: Use the graphical interface to design the conversation flow for each topic.
5. **Test and Publish**: Test your bot to ensure it works as expected, then publish it to make it available to users.

### 2. Autonomous Copilots

> **Tool**: Power Automate

**Steps**:
1. **Sign in to Power Automate**: Go to the Power Automate website and sign in with your Microsoft account.
2. **Create a Flow**: Click on "Create" and choose the type of flow you want to build (e.g., automated, instant, scheduled).
3. **Add Triggers and Actions**: Define the trigger that starts the flow and add the actions that the flow will perform.
4. **Configure Details**: Set up the details for each action, such as specifying conditions and data inputs.
5. **Test and Activate**: Test your flow to ensure it works correctly, then activate it to start running.

### 3. Declarative Copilots

> **Tool**: Power Automate

**Steps**:
1. **Sign in to Power Automate**: Go to the Power Automate website and sign in with your Microsoft account.
2. **Create a Flow**: Click on "Create" and choose the type of flow you want to build.
3. **Define Rules**: Use the graphical interface to set up rules and conditions that dictate how the flow operates.
4. **Add Actions**: Specify the actions that the flow will take based on the defined rules.
5. **Test and Deploy**: Test your flow to ensure it follows the rules correctly, then deploy it.

### 4. Analytical Copilots

> **Tool**: Power BI

**Steps**:
1. **Sign in to Power BI**: Go to the Power BI website and sign in with your Microsoft account.
2. **Import Data**: Connect to your data sources and import the data you want to analyze.
3. **Create Reports**: Use the Power BI interface to create reports and dashboards that visualize your data.
4. **Add Insights**: Use Power BI's AI features to add insights and predictive analytics to your reports.
5. **Share and Collaborate**: Share your reports with others and collaborate on data analysis.

### 5. Creative Copilots

> **Tools**: Microsoft Designer, Microsoft 365 Apps

**Steps**:
1. **Sign in to Microsoft Designer**: Go to the Microsoft Designer website and sign in with your Microsoft account.
2. **Create a New Project**: Start a new design project and choose a template or create from scratch.
3. **Add Content**: Use the design tools to add text, images, and other content to your project.
4. **Use AI Features**: Leverage AI-driven suggestions and tools to enhance your design.
5. **Save and Share**: Save your design and share it with others.

### 6. Integrative Copilots

> **Tools**: Power Platform, Microsoft Teams, Power BI

**Steps**:
1. **Identify Integration Points**: Determine which Microsoft tools and services you want to integrate.
2. **Create Flows**: Use Power Automate to create flows that connect different tools and automate tasks.
3. **Set Up Connectors**: Use connectors to link your AI copilots with other Microsoft services like Teams and Power BI.
4. **Configure Actions**: Define the actions that your copilot will take within the integrated environment.
5. **Test and Implement**: Test the integrations to ensure they work seamlessly, then implement them.

## Demo 

### Topic 1: Configure your your environment and Create a Copilot

- Go to [Microsoft Copilot Studio Home Page](https://copilotstudio.microsoft.com/)
- Prompt your case, for example:

  ```text
  I'm planning to develop a support copilot for our Contoso customers. This tool will assist by providing answers to frequently asked questions and performing routine tasks, such as order status updates.
  ```

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/db23a02f-6000-43b7-8617-af4504faa040">

- Setup your Copilot Name, Icon, description and instructions:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/2197193b-d91e-4a2a-8078-251441c06e3a">

  ```
  - Information should come from https://learn.microsoft.com/en-us/microsoft-copilot-studio/ and from https://www.microsoft.com/en-us/microsoft-copilot/
  - Maintain a professional, cheerful tone focused on our clients, avoiding any mention of competitors or comparisons with their products.
  ```

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/3de35622-6af0-4dc8-b383-2c39e347bee7">

  > You will see a screen like this while you wait to Copilot to create your bot:
  
  <img width="550" alt="image" src="https://github.com/user-attachments/assets/028904ba-88c5-418b-9203-bc879b640b97">

  > You can see it by the `Copilots` section:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/d828671c-eb5b-4049-95f0-32ee8b46ccd5">

- You can keep configuring different settings available:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/e7bd4c43-7e2d-46e9-a37b-3cc4f6f41a51">

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/b680d628-6462-4728-bec2-6957ee2fa065">

- Create topics if needed:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/ee2f4108-7698-4ede-8b99-ff0418dbb7d2">

  > It will look like this:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/94dd43e1-02b5-4468-8b82-38745492356a">

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/4b9b6ec4-69bd-45c6-bea3-554e3d7d064d">

- Before you publish your copilot, please navigate to the `Security` section and adjust the `Authentication` settings according to your requirements:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/047ac431-27c4-4ab0-913e-bc80004dd962">

- Once you are ready, `Publish` your own Copilot:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/c1f5deb9-8541-4fbf-9208-c354fc72e4f8">

### Topic 2: Understanding Entities & Slot Filling

| Concept       | Description                                                                 | Example                                                                                   |
|---------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Entities**  | Key pieces of information that the AI copilot needs to understand and extract from user inputs. | - **Examples**: Names, dates, locations, product names, quantities. <br> - **Usage**: "Book a flight to New York for tomorrow" (Entities: "New York" - location, "tomorrow" - date). |
| **Slot Filling** | The process of collecting all necessary entities (or slots) required to complete a task. The AI copilot asks follow-up questions to gather any missing information. | - **Example**: For booking a flight, the copilot might need the departure city, destination city, date, and time. If the user only provides the destination, the copilot will ask for the remaining details. <br> - **Scenario**: Booking a meeting room. <br> **Entities**: Date, time, room number, duration. <br> **User Input**: "I need a room for a meeting tomorrow." <br> **Slot Filling**: <br> - Copilot: "What time is the meeting?" <br> - User: "At 3 PM." <br> - Copilot: "How long will the meeting last?" <br> - User: "2 hours." <br> - Copilot: "Which room would you like to book?" <br> - User: "Room 101." |

- Go to `Settings` in top-right corner, and select `Entities`. Then select `Add` an entity and `New entity`.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/b543c6ff-ac7c-4b6b-9268-d9bacd301a02">

- You can choose between `Closed list` or `Regular expression (Regex)`:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/9171775c-140b-4a2c-b344-a1bbda1f46c1">

  > If you choose `Closed list` you will se a window like this:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/562c8b59-6f42-46ab-b634-9209f695ea71">

- You can add that `Entity` to the `Topic`:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/bfd4ce79-59c4-4bbf-86e5-62a776dcaa5c">


  <img width="550" alt="image" src="https://github.com/user-attachments/assets/53155f54-de30-462a-a0c8-3cae98d05758">

- You can test the `Slot Filling`, by having the `Variables` window open:

  <video src='https://github.com/user-attachments/assets/625d865d-6259-4b07-8d6c-565c0d3675d1' width=180/>

- You can access the code editor:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/3918e5a0-6ef7-4898-a84d-a0e6630f37c3">

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/011e6cb9-e779-4852-9277-1038600eecab">


### Topic 3: 

