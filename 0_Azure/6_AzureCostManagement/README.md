# Azure Cost Management 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-03

----------

> `Azure Cost Management` is a suite of tools designed to help organizations monitor, allocate, and optimize their cloud spending. It provides comprehensive insights into your Azure usage and costs, enabling you to manage your budget effectively and ensure that your spending aligns with your financial goals.

## Overview 

| Feature          | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **Cost Analysis**| - **Visualization**: View and analyze your costs through various charts and graphs.<br/>- **Filtering and Grouping**: Break down costs by resource, resource group, subscription, or tags to understand spending patterns. |
| **Budgeting**    | - **Create Budgets**: Set budgets for different scopes like subscriptions or resource groups.<br/>- **Alerts**: Configure alerts to notify you when spending exceeds predefined thresholds. |
| **Cost Allocation**| - **Tag Inheritance**: Enable tag inheritance to ensure costs are allocated correctly.<br/>- **Shared Costs**: Split shared costs across multiple departments or projects. |
| **Optimization** | - **Recommendations**: Receive recommendations for cost-saving opportunities.<br/>- **Anomaly Detection**: Identify and address spending anomalies proactively. |
| **Reporting**    | - **Custom Reports**: Generate custom reports to share with stakeholders.<br/>- **Power BI Integration**: Use Power BI for advanced reporting and dashboard creation. |
| **Automation**   | - **Data Export**: Automate the export of cost data to storage accounts for further analysis.<br/>- **Integration**: Integrate cost data with external tools and processes. |

## Capabilities

> Tips: 
> - **Use Tags**: Ensure your resources are properly tagged to make filtering and grouping easier.
> - **Save Views**: You can save custom views in Cost Analysis for quick access in the future.
> - **Set Up Alerts**: Consider setting up cost alerts to monitor spending and avoid unexpected charges.

**Accessing Cost Management**:
   - `Sign in` to the Azure portal.
   - `Navigate` to `Cost Management + Billing` from the left-hand menu.

      <img width="326" alt="image" src="https://github.com/user-attachments/assets/39f453f1-31a5-49fb-a2db-031e7a89ba98">

- **Set up Budgets**:
   - Go to `Cost Management` > `Budgets`.

      <img width="324" alt="image" src="https://github.com/user-attachments/assets/b7f7eb28-e8a7-4029-ab34-16dbde88fb55">
      
   - `Click on` `+ Add` to create a new budget.

      <img width="434" alt="image" src="https://github.com/user-attachments/assets/61e7e1fa-4d2c-423a-84b7-ee82c66b9a19">

   - `Define the scope` (e.g., subscription or resource group), set the budget amount, and configure the reset period (monthly, quarterly, or annually).
   - `Set up alerts` for actual and forecasted costs, and specify email recipients for notifications.

      <img width="434" alt="image" src="https://github.com/user-attachments/assets/14fb5d90-36fd-498a-8e4d-e5d8bc4f8a9c">

- **Analyzing Costs**:
   - Select `Cost Analysis` from the Cost Management menu.
   - `Use filters and groupings` to drill down into cost details by resource, resource group, or tags.
   - `Save and share custom views` to keep stakeholders informed.
     
      <img width="611" alt="image" src="https://github.com/user-attachments/assets/9b7ad624-99c8-4bd6-bbd0-f3ac1e717b78">

   - Pulling the `Billing Report`: Generate and download billing reports for specific resources.
     - **Navigate to Subscription**:
       - `Sign in` to the Azure portal.
       - `Select` the subscription where the factory is located from the `Subscriptions` menu.
     - **Access Cost Analysis**:
       - In the left-hand menu, click on `Cost Management + Billing`.
       - Under `Cost Management`, click on `Cost analysis`.

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/601db977-1fc1-4cab-8e2d-f93f5857909f">

     - **Select Time Range**:
       - In the Cost Analysis window, `click on the date range selector` at the top of the page.
       - `Choose the start and end dates` for the period during which the issue occurred.
       - `Apply` the selected date range.

          <img width="395" alt="image" src="https://github.com/user-attachments/assets/4b0a9485-5b87-4c73-9179-d22eed3bdb8e">

     - **Group by** :
       - In the Cost Analysis window, find the `Group by` dropdown menu.
       - Select the desired option, e.g `Meter` from the dropdown options to group the costs by meter.
 
          <img width="550" alt="image" src="https://github.com/user-attachments/assets/4f015458-d068-4375-90e5-1c78c9ec412e">

     - **Add Filter**:
       - Click on `Add filter` located above the cost breakdown chart.
       - From the first dropdown menu, select `Resource`.
       - From the second dropdown menu, `select the resource ID` of the factory in question.
       - `Apply` the filter to narrow down the costs to the specific resource.

          <img width="503" alt="image" src="https://github.com/user-attachments/assets/9f6461f2-e6f1-4ceb-a5ae-d730d57a11ed">

     - **Download Report**:
       - At the top of the Cost Analysis window, click on the `Download` button.
       - `Choose the format` (e.g., CSV, Excel) for the report.
       - `Save the report` to your local machine.
       - `Share the report` with the relevant stakeholders or team members.

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/f677d4b9-882e-4893-9624-a0cad7624d73">

- **Setting Up Alerts**:
   - Go to `Cost Management` > `Alerts`.
   - Click on `+ Add` to create a new alert.
   - `Choose the alert type` (e.g., anomaly detection) and configure the thresholds and notification settings.

      <img width="550" alt="image" src="https://github.com/user-attachments/assets/763e70ab-38fa-43b3-bd15-037ce17d427c">

- **Optimizing Costs**:
   - `Review cost-saving recommendations` provided by Azure.
   - `Implement suggested optimizations` to reduce unnecessary spending.
