# Parsing XML files in Power Query - Overview 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-17

----------

> Parsing an XML file and converting it into columns and rows using Microsoft Fabric's Data Factory

## Wiki 

<details>
<summary><b>Table of Wiki </b> (Click to expand)</summary>

- [XML format in Data Factory in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/format-xml)
- [Best practices when working with Power Query](https://github.com/MicrosoftDocs/powerquery-docs/blob/main/powerquery-docs/best-practices.md#best-practices-when-working-with-power-query)

</details>


## Content 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>


</details>

## Overview 

| **Technical Overview**       | **Details**                                                                                                                                                       |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data Pipeline Setup**   | - **Data Pipeline**: A data pipeline in Microsoft Fabric's Data Factory orchestrates the data flow from the source (XML file) to the destination (e.g., SQL Database, Data Lake). This involves defining the source, transformations, and destination.<br/>- **Copy Activity**: The core activity used to copy data from the XML source to the destination. It supports various transformations and data mappings, ensuring data integrity and consistency during the transfer. |
| **Source Dataset Configuration** | - **Dataset Type**: The source dataset type must be set to Xml to correctly interpret the structure and content of the XML file.<br/>- **Location**: Specifies the location of the XML file. This can be in Azure Blob Storage, Amazon S3, Azure Data Lake, etc., allowing flexibility in data storage options.<br/>- **Encoding**: Defines the encoding type used to read the XML file (e.g., UTF-8, UTF-16), ensuring the correct interpretation of character sets.<br/>- **Compression**: If the XML file is compressed, specify the compression type (e.g., gzip, bzip2) to enable proper decompression during data extraction. |
| **Sink Dataset Configuration** | - **Dataset Type**: The sink dataset type depends on the destination (e.g., SQL Database, Data Lake), which determines how the data will be stored and accessed.<br/>- **Connection**: Configure the connection settings to the destination, including authentication and network settings to ensure secure and reliable data transfer.<br/>- **Schema Mapping**: Map the XML elements to the corresponding columns in the destination, ensuring that the data structure is preserved and correctly interpreted in the target system. |
| **Copy Activity Configuration** | `Source Settings`:<br/>  - **XmlSource**: Specifies the XML source settings, including the root node path, which defines the starting point for data extraction.<br/>  - **Compression**: Configure compression settings if the XML file is compressed, ensuring that the data is properly decompressed before processing.<br/>`Sink Settings`:<br/>  - **SqlSink**: Specifies the SQL sink settings or other destination settings, including table names and data types.<br/>  - **Column Mapping**: Map the XML elements to the destination columns, ensuring that each piece of data is correctly placed in the target schema. |
| **Running the Pipeline**  | - **Validation**: Validate the pipeline to ensure there are no configuration errors, checking for issues such as missing fields or incorrect data types.<br/>- **Debugging**: Debug the pipeline to test the data flow and ensure it works as expected, identifying and resolving any issues that arise during the process.<br/>- **Execution**: Run the pipeline to parse the XML file and load the data into the destination, monitoring the process to ensure successful completion and data accuracy. |

## Demo 

> [!IMPORTANT]
> Tips
> 1. **Filter Early**: Apply filters as early as possible in your query to reduce the amount of data being processed. This can significantly speed up the parsing process. <br/>
> 2. **Use `Xml.Document` Instead of `Xml.Tables`**: When loading XML data, use `Xml.Document` to get a more flexible structure that you can manipulate more efficiently. This approach can help expose all data elements for easier access. <br/>
> 3. **Avoid Nested Expansions**: Minimize the number of nested table expansions. Each expansion can add significant overhead, so try to flatten the structure as much as possible. <br/>
> 4. **Work with a Subset of Data**: If the XML file is large, consider working with a smaller subset of the data during the development phase. This can make the process faster and easier to manage. <br/>
> 5. **Optimize Data Types**: Ensure that you are using the correct data types for your columns. Incorrect data types can slow down the processing. <br/>
> 6. **Modular Approach**: Break down your query into smaller, manageable steps. This modular approach can help isolate performance issues and make the query easier to debug.


### Step 1: Set Up Your Data Pipeline

1. **Create a Data Pipeline**:
   - Go to your [Microsoft Fabric workspace](https://app.fabric.microsoft.com/home).

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/b16c5a86-630a-4e73-8ffc-4445bb863a4e" />

   - Navigate to Data Factory and create a new data pipeline in your existing workspace or create new.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/73632982-e4d5-4f76-8ce5-dbcca39c268c" />

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/266a7820-bc81-4048-b532-3efc1ac5b519" />

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/86d7caed-893e-428e-abb4-9939d9c07a8f" />

2. **Add a Copy Activity**:
   - In the pipeline, add a Copy activity.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/cc116355-a4cc-4f4d-8ffd-1f60bda65ed7" />

### Step 2: Configure the Source Dataset

> [!NOTE]
> For this purpose, I already have a lakehouse with some XML files in place. Here is the input source used, few examples of [XML File: Employee Records](https://github.com/MicrosoftCloudEssentials-LearningHub/Demos-ScenariosHub/tree/main/0_Azure/2_AzureAnalytics/0_Fabric/demos/26_ParsingXMLfilesPQuery/samples) used.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/e5d6b1b4-8330-47a7-8ffb-fe990d83b12b" />

1. **Create a Source Dataset**:
   - In the Datasets section, create a new dataset.
   - Choose the XML format and configure the connection to your XML file (e.g., from Azure Blob Storage, Amazon S3, etc.).

2. **Set Dataset Properties**:
   - Set the `type` property to `Xml`.
   - Configure the `location` property to point to your XML file.
   - Optionally, set other properties like `encodingName`, `compression`, etc.

### Step 3: Configure the Sink Dataset

1. **Create a Sink Dataset**:
   - Create a new dataset for the destination (e.g., Azure SQL Database, Data Lake, etc.).
   - Configure the connection and format for the sink dataset.

### Step 4: Configure the Copy Activity

1. **Source Settings**:
   - In the Copy activity, select your XML source dataset.
   - Configure any additional settings, such as compression type and null value representation.

2. **Sink Settings**:
   - Select your sink dataset.
   - Map the columns from the XML source to the columns in the sink dataset.

### Step 5: Run the Pipeline

1. **Validate and Debug**:
   - Validate your pipeline to ensure there are no errors.
   - Debug the pipeline to test the data flow.

2. **Run the Pipeline**:
   - Once validated, run the pipeline to parse the XML file and load the data into the destination.

### Example Configuration

Here's a simplified example of how you might configure the XML parsing in the pipeline:

```json
{
    "name": "CopyXMLToSQL",
    "properties": {
        "activities": [
            {
                "name": "CopyXMLToSQL",
                "type": "Copy",
                "inputs": [
                    {
                        "referenceName": "XMLSourceDataset",
                        "type": "DatasetReference"
                    }
                ],
                "outputs": [
                    {
                        "referenceName": "SQLSinkDataset",
                        "type": "DatasetReference"
                    }
                ],
                "typeProperties": {
                    "source": {
                        "type": "XmlSource",
                        "xmlSettings": {
                            "rootNodePath": "/Company/Employees/Employee"
                        }
                    },
                    "sink": {
                        "type": "SqlSink"
                    }
                }
            }
        ]
    }
}
```

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
