# Serverless SQL Pool: Dynamically Remove Space

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-25

----------

## Wiki 

<details>
<summary><b>List of References </b> (Click to expand)</summary>


</details>

## Content

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>


</details>

## Overview 

> [!IMPORTANT]
> The serverless SQL pool in Azure Synapse Analytics `does not support internal tables. It primarily supports external tables and temporary tables`.
> For `internal tables,` you would need to use a `dedicated SQL pool` in Synapse Analytics, which allows you to `create and manage internal tables with local storage`.

| **Table Type**      | **Description**                                                                                                                                                                                                 | **Use Cases**                                                                                                      |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **External Tables** | - Reference data stored in external sources like Azure Data Lake Storage, Azure Blob Storage, Azure Cosmos DB, etc. <br> - Data is not physically stored in the SQL pool. <br> - Useful for querying large datasets without loading them into the SQL pool. | - Querying large datasets stored externally. <br> - Performing data analysis on data stored in various formats.    |
| **Temporary Tables**| - Created and used within the scope of a session. <br> - Data is stored temporarily and is dropped when the session ends. <br> - Useful for intermediate data processing and transformations.                      | - Storing intermediate results during complex queries. <br> - Performing temporary data transformations and aggregations. |


## Demo

### Set Up a Synapse Workspace

1. **Sign in to the Azure Portal**: Go to the Azure Portal and sign in with your Azure account.
2. **Navigate to Your Synapse Workspace**: In the Azure Portal, search for your Synapse workspace or create a new one if you don't have one.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/92a5e451-1868-47e2-b32b-858591c306ee" />
  
     <img width="550" alt="image" src="https://github.com/user-attachments/assets/51e3b091-855d-4481-89e0-623705e3cf2a" />

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/7d03bfa8-e1e3-4706-970f-a89c7b8cd904" />

3. **Launch Synapse Studio**: From the Synapse workspace overview, click on the `Open Synapse Studio` button.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/302b1fd8-49a6-427e-93dc-8e952f1667e6" />

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/a368036b-c859-47fc-a1c5-d045b6910790" />

### Upload Sample Data to Storage Account 

> [!IMPORTANT]
> For this demo, `we'll be using the same storage account created with the synpase workspace`.
> `CREATE EXTERNAL DATA SOURCE is not supported in the master database of the serverless` SQL pool. Instead, you `need to create a user database and perform the operations there`.

1. Create a Container in the Storage Account:
   - Go to the Azure portal and navigate to your storage account.
   - In the left-hand menu, select `Containers`.
   - Click on `+ Container` to create a new container.
   - Enter a name for the container, such as `sample-tables-container`.
   - Set the `Public access level` to your preference (e.g., Private).
   - Click `Create`.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/3060045f-a515-4a27-a4c6-80bd2ba3d9ab" />

2. Navigate to the Container:
   - In the Azure portal, go to your storage account.
   - Select `Containers` from the left-hand menu.
   - Click on the container you created (e.g., `sample-tables-container`).
3. Upload the Sample CSV File:
   - Click on the `Upload` button.
   - In the upload blade, click on `Browse` to select the sample CSV file from your local machine.
   - Choose the file, click `Upload` to upload the file to the container.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/4fa8d1c8-e5a0-4d65-a3b5-83bf7c7118c1" />

### Create User Database

1. First, create a new database in your Synapse workspace.

     ```sql
     CREATE DATABASE {User Database Name};
     ```

     <img width="884" alt="image" src="https://github.com/user-attachments/assets/f24a4d45-6bee-46ea-bccc-b5f893044c01" />

2. Switch to the User Database: Use the newly created database.
3. Create an External Data Source: Integrate this task with the previous step by establishing the external data source within the user database.

     ```sql
     USE {User Database Name};

     CREATE EXTERNAL DATA SOURCE {Data Source Name}
     WITH (
         LOCATION = 'https://<your-storage-account>.dfs.core.windows.net/<your-container>'
     );
     ```

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/13f22e3b-7c68-4ed2-8a56-2752a5033869" />


4. **Create an External File Format**: As part of the same flow, define the format of the CSV file.

     ```sql
     CREATE EXTERNAL FILE FORMAT {File Format Name}
     WITH (
         FORMAT_TYPE = DELIMITEDTEXT,
         FORMAT_OPTIONS (
             FIELD_TERMINATOR = ',',
             STRING_DELIMITER = '"',
             FIRST_ROW = 2
         )
     );
     ```

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/40a4c6a2-bc51-49ba-9361-bec6eb0edb9e" />


5. **Create an External Table**:  Create an external table that references the sample data.

     ```sql
     CREATE EXTERNAL TABLE [Table With Spaces] (
         [ID] INT,
         [Name With Spaces] NVARCHAR(50),
         [Date With Spaces] DATE
     )
     WITH (
         LOCATION = '<file-name>.csv',
         DATA_SOURCE = {Data Source Name},
         FILE_FORMAT = {File Format Name}
     );
     ```



6. **Query the External Table**:  You can now query the external table to see the sample data.
     ```sql
     SELECT * FROM [Table With Spaces];
     ```





1. **Open the SQL Script Editor**:
   - In Synapse Studio, go to the `Develop hub` by clicking on the `Develop` icon in the left navigation pane.
   - Click on `+ New SQL script` to open the SQL script editor.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/3382ea4a-06eb-4e32-93d9-569cef7fc2f5" />


2. Create an External Data Source: Define an external data source that points to your SQL database.

     ```sql
     CREATE EXTERNAL DATA SOURCE MySQLDataSource
     WITH (
         TYPE = RDBMS,
         LOCATION = '<your-sql-server-name>.database.windows.net',
         DATABASE_NAME = '<your-database-name>',
         CREDENTIAL = MyCredential
     );
     ```

   
<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
