# Purview: Bulk Upload of Glossary Terms into Unified Catalog - Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-17

----------


## Wiki 

<details>
<summary><b>Table of Wiki </b> (Click to expand)</summary>

- [Microsoft Purview setup guides](https://learn.microsoft.com/en-us/purview/purview-fast-track-setup-guides)
- [Microsoft Purview (formerly Azure Purview) deployment checklist](https://learn.microsoft.com/en-us/purview/legacy/tutorial-azure-purview-checklist)
- [Import and export glossary terms](https://learn.microsoft.com/en-us/purview/legacy/how-to-import-export-glossary)

</details>


## Content 

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>

</details>

## Prerequisites
1. **Microsoft Entra Tenant**:
   - Ensure you have a Microsoft Entra tenant associated with your subscription.
   - Required roles: Information Protection Administrator, Power BI Administrator (if scanning Power BI tenants).
2. **Azure Subscription**: You need an active Azure subscription. If you don't have one, create a free subscription.
3. **Resource Providers**: Register the following resource providers in your Azure subscription:
     - `Microsoft.Storage`
     - `Microsoft.EventHub` (optional)
     - `Microsoft.Purview`

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/89697e6d-464b-4ec9-be5e-7539807cc26b" />

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/7603bd96-6b6a-40b2-9d4f-4fdffba15681" />

## Demo 

> Bulk upload glossary terms from the classic Purview to the new Unified Catalog

### Create a Microsoft Purview Account
1. **Navigate to Azure Portal**: Go to the Azure portal and search for `Microsoft Purview`.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/9ebaf4cb-38cb-4285-8786-f286107a983b" />

2. **Create Purview Account**: Click on "Create" and fill in the required details.
    - Subscription
    - Resource Group
    - Purview Account Name
    - Region
    
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/0ab094df-3040-493e-9912-affb635371fe" />

3. **Configure Event Hub (Optional)**: If you plan to use an existing Event Hubs namespace, configure it during account creation.

### Uploading Glossary Terms - (Classic Purview)

1. **Open Microsoft Purview Data Catalog**: If you're using the `classic Microsoft Purview` portal, select `Glossary`.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/354d43ab-16be-4a02-a230-4a4efccc0dfa" />

2. **Select/Create the Glossary** where you want to import terms.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/0b013cd2-7785-497a-9f49-20977bcf1a63">

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/cdbd1296-2ab4-4bac-a1f3-029b1080ac56" />

3. Select `Import terms`, and upload your filled CSV file. 

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/df5dbe5b-b3f1-46e4-ac91-381fa39e242f" />

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/79ee1f04-5bff-4680-9b44-0c6c76457cf8">

    | **Feature**                  | **System Default Template**                                      | **Create New Template**                                      |
    |------------------------------|------------------------------------------------------------------|--------------------------------------------------------------|
    | **Customization**            | Limited to predefined fields (e.g., Term, Definition)            | Highly customizable; add fields like Synonyms, Categories, etc. |
    | **Ease of Use**              | Simple and quick to use with basic fields                        | Requires initial setup to define custom fields               |
    | **Consistency**              | Standardized format with basic fields                           | Ensures consistency with custom fields tailored to your needs |
    | **Flexibility**              | Less flexible; limited to default fields                        | Highly flexible; adapt to changing requirements              |
    | **Metadata Inclusion**       | Basic metadata (Term, Definition)                               | Include additional metadata (e.g., Synonyms, Related Terms)  |
    | **Setup Time**               | Minimal setup time                                              | Requires more time to create and define custom fields        |
    | **Use Case**                 | Suitable for simple glossaries with basic terms and definitions | Ideal for complex glossaries with detailed information       |

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/886fec2b-918b-4d52-bfa3-dca5d2442895" />


   - If you're using the `new Microsoft Purview portal`, go to **Business glossary** and select **Glossaries**.




2. **Select the Glossary** where you want to import terms.

3. **Download the CSV Template**:
   - In the classic governance portal, select **Import terms**.
   - Download the provided CSV template and fill it with the terms you want to add.

4. **Fill Out the CSV File**:
   - Enter the terms and their definitions in the CSV file.
   - Ensure the file name starts with a letter and includes only letters, numbers, spaces, underscores, or other non-ASCII Unicode characters.

5. **Upload the CSV File**:
   - Go back to the Purview portal, select **Import terms**, and upload your filled CSV file.
   - The system will add all the terms to your selected glossary[1](https://learn.microsoft.com/en-us/purview/legacy/how-to-import-export-glossary).

### Downloading Glossary Terms

1. **Open Microsoft Purview Data Catalog**:
   - Navigate to the glossary where your terms are stored.

2. **Select the Terms** you want to export.

3. **Export Terms**:
   - Once you've selected the terms, the **Export terms** button will be enabled.
   - Click on it to download the terms in a CSV file[1](https://learn.microsoft.com/en-us/purview/legacy/how-to-import-export-glossary).


<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
