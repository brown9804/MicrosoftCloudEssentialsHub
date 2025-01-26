# Dedicated SQL Pool: Store Procedure Dynamically Remove Space

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) 
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-26

----------

## Content

<details>
<summary><b>Table of Content </b> (Click to expand)</summary>

- [Content](#content)
- [Demo](#demo)
   - [Set Up a Synapse Workspace](#set-up-a-synapse-workspace)
   - [Create a Dedicated SQL Pool](#create-a-dedicated-sql-pool)
   - [Create Tables with Spaces in Names and Columns](#create-tables-with-spaces-in-names-and-columns)
   - [Create Views with Modified Tables/Column Names](#create-views-with-modified-tablescolumn-names)

</details>

## Demo

### Set Up a Synapse Workspace

1. **Sign in to the Azure Portal**: Go to the Azure Portal and sign in with your Azure account.
2. **Navigate to Your Synapse Workspace**: In the Azure Portal, search for your Synapse workspace or create a new one if you don't have one.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/92a5e451-1868-47e2-b32b-858591c306ee" />
  
     <img width="550" alt="image" src="https://github.com/user-attachments/assets/51e3b091-855d-4481-89e0-623705e3cf2a" />

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/7d03bfa8-e1e3-4706-970f-a89c7b8cd904" />

### Create a Dedicated SQL Pool

1. **Launch Synapse Studio**: From the Synapse workspace overview, click on the `Open Synapse Studio` button.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/302b1fd8-49a6-427e-93dc-8e952f1667e6" />

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/a368036b-c859-47fc-a1c5-d045b6910790" />

2. **Create a Dedicated SQL Pool**:
   - In Synapse Studio, go to the `Manage` hub by clicking on the `Manage` icon in the left navigation pane.
   - Under `Analytics pools`, select `SQL pools` and click on the `+ New` button.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/6d96ac07-57f1-4efd-917b-200a43091311" />

   - Enter the following details:
     - **SQL pool name**: Enter a name for your SQL pool (e.g., `SQLPOOL1`).
     - **Performance level**: Choose a performance level (e.g., `DW1000c`).
   - Click `Review + create` and then `Create` to provision the dedicated SQL pool.
  
        <img width="550" alt="image" src="https://github.com/user-attachments/assets/89ca427b-20f1-4df5-ae20-847b76cdd9a7" />

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/b8b2c94b-76e6-4ced-8812-c386c6a55f32" />

### Create Tables with Spaces in Names and Columns

1. **Open the SQL Script Editor**:
   - In Synapse Studio, go to the `Develop hub` by clicking on the `Develop` icon in the left navigation pane.
   - Click on `+ New SQL script` to open the SQL script editor.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/3382ea4a-06eb-4e32-93d9-569cef7fc2f5" />

2. **Create Sample Tables**: Use the following script to create tables with spaces in their names and columns. Click [here to see the .sql file](https://github.com/MicrosoftCloudEssentials-LearningHub/Demos-ScenariosHub/blob/main/0_Azure/2_AzureAnalytics/1_SynapseAnalytics/demos/2_synapse_views_dynamically_remove_space/1_dedicatedSQLPoolStoreProc/src/create-sample-tables.sql).

    ```sql
    -- Create sample tables with spaces in names
    CREATE TABLE [Employee Records] (
        [Employee ID] INT,
        [Employee Name] NVARCHAR(255),
        [Employee Address] NVARCHAR(255)
    );

    CREATE TABLE [Sales Data] (
        [Sale ID] INT,
        [Sale Date] DATE,
        [Employee ID] INT,
        [Sale Amount] DECIMAL(10, 2)
    );

    CREATE TABLE [Inventory Details] (
        [Item ID] INT,
        [Item Name] NVARCHAR(255),
        [Item Category] NVARCHAR(255),
        [Item Price] DECIMAL(10, 2)
    );

    -- Insert sample data into the tables
    INSERT INTO [Employee Records] ([Employee ID], [Employee Name], [Employee Address])
    VALUES (1, 'Alice Johnson', '789 Pine St');

    INSERT INTO [Employee Records] ([Employee ID], [Employee Name], [Employee Address])
    VALUES (2, 'Bob Brown', '101 Maple St');

    INSERT INTO [Sales Data] ([Sale ID], [Sale Date], [Employee ID], [Sale Amount])
    VALUES (1, '2023-02-01', 1, 200.00);

    INSERT INTO [Sales Data] ([Sale ID], [Sale Date], [Employee ID], [Sale Amount])
    VALUES (2, '2023-02-02', 2, 250.00);

    INSERT INTO [Inventory Details] ([Item ID], [Item Name], [Item Category], [Item Price])
    VALUES (1, 'Gadget', 'Electronics', 49.99);

    INSERT INTO [Inventory Details] ([Item ID], [Item Name], [Item Category], [Item Price])
    VALUES (2, 'Tool', 'Hardware', 29.99);
    ```

   <img width="550" alt="image" src="https://github.com/user-attachments/assets/6f8a154d-2fcb-4aa5-bc9f-27f6b8334017" />

3. **Run the Script**: Execute the script in the SQL script editor to create the tables and insert sample data.

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/1d02fd74-7246-4aa6-8247-b98619d70c47" />

> [!NOTE]
> Once you refresh, the tables will be visible:

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/3e6fc8a1-ad34-4a0b-8940-ae27b303190d">

  ### Create Views with Modified Tables/Column Names

1. **Create a Stored Procedure to Remove Spaces from Column Names**: Use the following script to create a stored procedure that removes spaces from column names and creates views. Click [here to see the .sql file](https://github.com/MicrosoftCloudEssentials-LearningHub/Demos-ScenariosHub/blob/main/0_Azure/2_AzureAnalytics/1_SynapseAnalytics/demos/2_synapse_views_dynamically_remove_space/1_dedicatedSQLPoolStoreProc/src/store-procedure-clean-up.sql).

    ```sql
     CREATE PROCEDURE RemoveSpacesFromColumnNames
     AS
     BEGIN
         DECLARE @tableName NVARCHAR(255)
         DECLARE @columnName NVARCHAR(255)
         DECLARE @sql NVARCHAR(MAX)
     
         -- Temporary table to store table names
         CREATE TABLE #TableNames (TABLE_NAME NVARCHAR(255))
         INSERT INTO #TableNames
         SELECT TABLE_NAME
         FROM INFORMATION_SCHEMA.TABLES
         WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo'
     
         -- Loop through each table
         WHILE EXISTS (SELECT 1 FROM #TableNames)
         BEGIN
             SELECT TOP 1 @tableName = TABLE_NAME FROM #TableNames
     
             -- Print the table name for debugging
             PRINT 'Processing table: ' + @tableName
     
             SET @sql = 'CREATE VIEW dbo.vw' + REPLACE(@tableName, ' ', '') + ' AS SELECT '
     
             -- Drop the temporary table if it exists
             IF OBJECT_ID('tempdb..#ColumnNames') IS NOT NULL
                 DROP TABLE #ColumnNames
     
             -- Temporary table to store column names
             CREATE TABLE #ColumnNames (COLUMN_NAME NVARCHAR(255))
             INSERT INTO #ColumnNames
             SELECT COLUMN_NAME
             FROM INFORMATION_SCHEMA.COLUMNS
             WHERE TABLE_NAME = @tableName
     
             -- Loop through each column
             WHILE EXISTS (SELECT 1 FROM #ColumnNames)
             BEGIN
                 SELECT TOP 1 @columnName = COLUMN_NAME FROM #ColumnNames
     
                 -- Print the column name for debugging
                 PRINT 'Processing column: ' + @columnName
     
                 -- Remove all spaces from column names
                 IF (SELECT COUNT(*) FROM #ColumnNames) = 1
                 BEGIN
                     SET @sql = @sql + 'REPLACE([' + @columnName + '], '' '', '''') AS [' + REPLACE(@columnName, ' ', '') + '] '
                 END
                 ELSE
                 BEGIN
                     SET @sql = @sql + 'REPLACE([' + @columnName + '], '' '', '''') AS [' + REPLACE(@columnName, ' ', '') + '], '
                 END
     
                 DELETE FROM #ColumnNames WHERE COLUMN_NAME = @columnName
             END
     
             -- Remove the trailing comma and space if any
             IF RIGHT(@sql, 2) = ', '
             BEGIN
                 SET @sql = LEFT(@sql, LEN(@sql) - 2)
             END
     
             SET @sql = @sql + ' FROM [' + @tableName + '];'
     
             -- Print the dynamic SQL for debugging
             PRINT 'Generated SQL: ' + @sql
     
             -- Execute the dynamic SQL
             BEGIN TRY
                 EXEC sp_executesql @sql
             END TRY
             BEGIN CATCH
                 PRINT 'Error: ' + ERROR_MESSAGE()
             END CATCH
     
             DELETE FROM #TableNames WHERE TABLE_NAME = @tableName
         END
     
         -- Clean up temporary tables
         DROP TABLE #TableNames
         DROP TABLE #ColumnNames
     END
    ```

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/13b3b5f2-3142-448f-b03a-3eeae00a1509" />

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/575905c1-bcf7-4800-981b-6ff4ab2b3302" />

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/a7244b21-c787-4f64-8689-fe66670aa86a" />

2. **Execute the Stored Procedure**: Click on `Run`, to create the stored procedure.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/17be4e92-9816-43ff-9cc3-23d9737a9056" />
    
    | Before | After |
    | --- | --- |
    | <img width="550" alt="image" src="https://github.com/user-attachments/assets/d081329c-b5f6-452f-826b-50a2dd614a1c" /> | <img width="550" alt="image" src="https://github.com/user-attachments/assets/588aa482-ac5c-4013-b926-e01db58d1733" /> |

3. Run the stored procedure to create views with modified column names.

    ```sql
    EXEC RemoveSpacesFromColumnNames
    ```

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/015b9c07-10f6-4895-bdba-4945e3277923" />

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/1ccf430e-1dff-4968-980c-a4f3913a8369" />

| Before | After |
| --- | --- |
| <img width="360" alt="image" src="https://github.com/user-attachments/assets/b0de5118-bf67-4f75-9dd7-2ae5ba33cb28" /> | <img width="360" alt="image" src="https://github.com/user-attachments/assets/ef9c6d3a-1d45-4d37-9977-431cf8b774d0" /> |

> [!NOTE]
> Once you refresh, the views will be visible:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/e0191419-29cc-448a-a14f-a76da221b015" />


<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
