# Fabric: Medallion Architecture Overview 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-24

------------------------------------------

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Fabric Draw.io icons](https://github.com/marclelijveld/Fabric-Icons/tree/main)

</details>


## Overview 

> The medallion architecture is a data design pattern used in data lakes and lakehouses to organize data at different levels of refinement. It's a best practice for managing the data lifecycle and ensuring data quality

| Layer       | Description |
|-------------|-------------|
| **Bronze Layer** | This layer contains the raw data ingested from various sources. The data is typically stored in its original format and is append-only. The Bronze layer acts as the landing zone for all incoming data. |
| **Silver Layer** | This layer contains cleaned and transformed data. The data in the Silver layer is often enriched with additional information and is structured in a way that makes it easier to query and analyze. This layer is also where data quality checks and transformations are applied. |
| **Gold Layer** | This layer contains curated and aggregated data that is ready for consumption by business intelligence and reporting tools. The data in the Gold layer is highly structured and optimized for performance. |

> [!NOTE]
> This demo will be created step by step. Please note that Microsoft Fabric already assists by setting up the medallion flow for you.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/7eec0098-7b7b-453c-9dbb-ee1a6390577b">

<img width="550" alt="image" src="https://github.com/user-attachments/assets/4bbb5f10-415b-44b2-8fd0-a5a12482ce2c">

## Demo 

Implementing a medallion architecture provides several benefits:
- **Data Quality**: By organizing data into layers, you can apply quality checks and transformations in a structured manner, ensuring that the data in the Gold layer is reliable and ready for analysis.
- **Scalability**: The architecture allows you to scale your data processing pipelines independently for each layer, providing flexibility and efficiency.
- **Performance**: The Gold layer is optimized for performance, which means that your reporting and analytics queries will run faster.
- **Simplicity**: It simplifies the data pipeline by breaking it down into smaller, manageable steps, each with a clear purpose.
- **Auditability**: It provides a clear data lineage, making it easier to trace the origin of data and understand the transformations applied at each stage.


<img width="650" alt="image" src="https://github.com/user-attachments/assets/2a6a887f-f560-4e74-ac2e-68f8c34d245f">

- Step 1: Set Up Your Environment
    1. **Create a Fabric Workspace**: This will be your central hub for all activities.
       - Navigate to the Fabric portal.
       - Click on `Create a resource` and select `Fabric Workspace`.
       - Provide a name and other required details, then create the workspace.
         
          <img width="550" alt="image" src="https://github.com/user-attachments/assets/8f259cac-1dcb-4129-9070-0b31899c4ab4">

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/2f3225fc-6aa6-4eeb-8207-75038b36f18f">

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/1831c97d-6b9a-4470-968d-e7803bc58b80">

    2. **Create Lakehouses**: Set up three lakehouses for the Bronze, Silver, and Gold layers.
       - In your Fabric workspace, create three lakehouses named `raw_Bronze`, `cleansed_Silver`, and `curated_Gold`.

          <p float="left">
            <img src="https://github.com/user-attachments/assets/f0f5baf2-9ad2-4422-9089-14aa28ae5181" width="250" />
            <img src="https://github.com/user-attachments/assets/5827c73a-1291-4fb6-a2c6-0c61f4808164" width="550" /> 
          </p>

### Step 2: Ingest Data into the Bronze Layer
1. **Identify Data Sources**: Determine the sources from which you'll ingest data.
   - List all the data sources such as databases, APIs, file systems, etc.

2. **Create Dataflows or Pipelines**: Use Data Factory to create dataflows or pipelines that ingest data into the Bronze lakehouse.
   - In Data Factory, create a new pipeline.
   - Add activities to the pipeline to ingest data from the identified sources.

3. **Configure Data Ingestion**: Set up the data ingestion process to load data into the Bronze layer in its raw format.
   - Configure the source and destination settings in the pipeline activities.
   - Ensure the data is being ingested into the `raw_Bronze` lakehouse.

### Step 3: Transform Data in the Silver Layer
1. **Create Notebooks or Dataflows**: Use Fabric's notebooks or dataflows to read data from the Bronze layer.
   - In the Fabric workspace, create a new notebook.
   - Connect the notebook to the `raw_Bronze` lakehouse.

2. **Data Cleaning**: Apply data cleaning steps to handle missing values, remove duplicates, and correct data types.
   - Write code in the notebook to clean the data.
   - Use functions like `dropna()`, `dropDuplicates()`, and `withColumn()` to clean the data.

3. **Data Enrichment**: Enrich the data with additional information if needed.
   - Join the data with reference tables or lookup values.
   - Add new columns with enriched information.

4. **Write to Silver Layer**: Write the cleaned and transformed data to the Silver lakehouse.
   - Use the `write.format("delta").save()` method to save the data to the `cleansed_Silver` lakehouse.

### Step 4: Curate Data in the Gold Layer
1. **Read Data from Silver Layer**: Use notebooks or dataflows to read data from the Silver lakehouse.
   - In a new notebook, connect to the `cleansed_Silver` lakehouse.

2. **Apply Business Logic**: Apply any additional business logic or aggregations.
   - Write code to perform aggregations and calculations.
   - Use functions like `groupBy()`, `agg()`, and `sum()` to aggregate the data.

3. **Write to Gold Layer**: Write the curated data to the Gold lakehouse.
   - Use the `write.format("delta").save()` method to save the data to the `curated_Gold` lakehouse.

### Step 5: Set Up Pipelines for Orchestration
1. **Create Pipelines**: Create pipelines to automate the movement of data from the Bronze layer to the Silver layer, and from the Silver layer to the Gold layer.
   - In Data Factory, create a new pipeline.
   - Add a copy activity to move data from the `raw_Bronze` lakehouse to the `cleansed_Silver` lakehouse.
   - Add another copy activity to move data from the `cleansed_Silver` lakehouse to the `curated_Gold` lakehouse.

2. **Schedule Pipelines**: Schedule these pipelines to run at appropriate intervals.
   - Set up triggers in Data Factory to run the pipelines on a schedule that aligns with your data freshness requirements.
   - Consider the frequency of data updates and the latency that is acceptable for your use case.

### Step 6: Enable Data Access for Reporting
1. **Configure SQL Analytics Endpoint**: Ensure that the data in the Gold layer is accessible to your reporting tools.
   - In the Fabric workspace, navigate to the `curated_Gold` lakehouse.
   - Enable the SQL analytics endpoint to allow direct querying of the data.

2. **Create Power BI Reports**: Use Power BI in Direct Lake Mode to create reports and dashboards from the data in the Gold layer.
   - Open Power BI Desktop.
   - Connect to the `curated_Gold` lakehouse using the SQL analytics endpoint.
   - Build reports and dashboards that provide insights into the data.

### Example Code Snippets for Orchestration
Here are some example code snippets that demonstrate the orchestration of data movement between the layers:

**PySpark Code to Move Data from Bronze to Silver**:
```python
# Read data from the Bronze layer
bronze_df = spark.read.format("delta").load("abfss://<your-container-name>@<your-storage-account-name>.dfs.core.windows.net/<your-bronze-path>/Tables/data")

# Perform transformations (if any)
silver_df = bronze_df  # Assuming no transformations for simplicity

# Write data to the Silver layer
silver_df.write.mode("overwrite").option("mergeSchema", "true").format("delta").save("abfss://<your-container-name>@<your-storage-account-name>.dfs.core.windows.net/<your-silver-path>/Tables/data")
```

**PySpark Code to Move Data from Silver to Gold**:
```python
# Read data from the Silver layer
silver_df = spark.read.format("delta").load("abfss://<your-container-name>@<your-storage-account-name>.dfs.core.windows.net/<your-silver-path>/Tables/data")

# Perform aggregations
gold_df = silver_df.groupBy("Name").agg(
    sum("Count").alias("TotalCount"),
    avg("price").alias("AveragePrice"),
    avg("tax").alias("AverageTax")
)

# Write data to the Gold layer
gold_df.write.mode("overwrite").option("mergeSchema", "true").format("delta").save("abfss://<your-container-name>@<your-storage-account-name>.dfs.core.windows.net/<your-gold-path>/Tables/curated_data")
```

