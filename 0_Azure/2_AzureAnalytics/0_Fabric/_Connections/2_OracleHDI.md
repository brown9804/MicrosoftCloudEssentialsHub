# Connecting Microsoft Fabric to Oracle HDI 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-09-12

----------

> Oracle Health Data Intelligence (HDI), formerly known as HealtheIntent, is a modular suite of cloud applications, services, and analytics. It enables healthcare and government stakeholders to use data from across the healthcare ecosystem to advance patient health, improve care delivery, and drive operational efficiency.

## Wiki
- [API Access and Fees and Registering an App](https://www.oracle.com/health/developer/api/)
- [Healthcare Analytics Data Integration Documentation](https://docs.oracle.com/en/industries/health-sciences/analytics-data-integration/index.html)
- [Hospital Use of APIs to Enable Data Sharing Between EHRs and Apps](https://www.healthit.gov/data/data-briefs/hospital-use-apis-enable-data-sharing-between-ehrs-and-apps)
- [Set up your Oracle database connection - Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/connector-oracle-database)
- [Oracle database connector overview - Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/data-factory/connector-oracle-database-overview)
- [Step-by-Step Guide: Interconnecting Oracle Cloud](https://blogs.oracle.com/cloudmarketplace/post/step-by-step-guide-interconnecting-oracle-cloud-infrastructure-and-microsoft-azure)
- [Connecting Oracle to Microsoft fabrics - Microsoft Fabric Community](https://community.fabric.microsoft.com/t5/General-Discussion/Connecting-Oracle-to-Microsoft-fabrics/m-p/3260454)

> Prerequisites:
>  1. **Register and Set Up API Access**
>     - **Register Your Application**: Go to the Oracle Health Developer Program console and register your application. Review and accept the API Access Terms and Conditions.
>     - **Review API Documentation**: Familiarize yourself with the Oracle Health API documentation, including available FHIR API resources.
>  2. **Install Necessary Tools**
>     - **Oracle Client**: Ensure the Oracle Client is installed on the machine running the on-premises data gateway.
>     - **Microsoft Fabric**: Set up Microsoft Fabric and ensure you have the necessary permissions to create and manage data pipelines.

## How to 

1. **Setup the Connection in Microsoft Fabric**
    - **Open Data Factory**: Navigate to Microsoft Fabric's Data Factory.

      <img width="219" alt="image" src="https://github.com/user-attachments/assets/be07d64c-5adc-4a60-970b-76dee9020ddf">

2. **Create Linked Service**:
   - Go to the **Manage** tab.
   - Select **Linked Services** and click on **New**.
   - Choose **Oracle** from the list of data stores.


     
4. **Configure Connection**:
   - **Server Name**: Enter the Oracle server name.
   - **Database Name**: Enter the name of your Oracle HDI database.
   - **Authentication**: Choose the appropriate authentication method (e.g., Basic).
   - **Username and Password**: Enter your Oracle database credentials.
   - **Test Connection**: Click on **Test Connection** to ensure the details are correct.
  
     
   - **Set Up Data Gateway**: If your Oracle database is on-premises, configure the on-premises data gateway to facilitate the connection.

 2. **Set Up Data Pipeline**
   - **Create a Pipeline**: In Data Factory, create a new pipeline to manage the data flow from Oracle Health Data Intelligence to your desired destination.
   - **Add Copy Activity**: Add a copy activity to the pipeline. Configure the source to use the Oracle linked service and specify the query or table to extract data from.

 3. **Configure Data Compression**
   - **Select Compression Type**: In the copy activity settings, choose the desired compression type (LZ4 or GZIP) for the data transfer.
   - **Destination Configuration**: Configure the destination settings to store the compressed data in your preferred format.

### Possible Issues and Solutions

 1. **Connection Issues**
   - **Issue**: Unable to connect to the Oracle database.
   - **Solution**: Verify the connection details, ensure the Oracle Client is correctly installed, and check network connectivity. Ensure the on-premises data gateway is properly configured and running.

 2. **Authentication Problems**
   - **Issue**: Authentication failures when connecting to the Oracle API.
   - **Solution**: Double-check the credentials and authentication method used. Ensure that the API key or token is valid and has the necessary permissions.

 3. **Data Transfer Errors**
   - **Issue**: Errors during data transfer.
   - **Solution**: Check the data pipeline logs for specific error messages. Ensure that the data format and schema are compatible between the source and destination. Adjust the query or data mapping as needed.

 4. **Compression Issues**
   - **Issue**: Data not being compressed as expected.
   - **Solution**: Verify the compression settings in the copy activity. Ensure that the destination supports the specified compression format (LZ4 or GZIP).

### Step 1: Configure the Connection in Microsoft Fabric

#### Create a Linked Service
1. **Open Data Factory**: Navigate to Microsoft Fabric's Data Factory.
2. **Create Linked Service**:
   - Go to the **Manage** tab.
   - Select **Linked Services** and click on **New**.
   - Choose **Oracle** from the list of data stores.
3. **Configure Connection**:
   - **Server Name**: Enter the Oracle server name.
   - **Database Name**: Enter the name of your Oracle HDI database.
   - **Authentication**: Choose the appropriate authentication method (e.g., Basic).
   - **Username and Password**: Enter your Oracle database credentials.
   - **Test Connection**: Click on **Test Connection** to ensure the details are correct.

#### Set Up Data Gateway
1. **Install On-Premises Data Gateway**:
   - Download and install the on-premises data gateway from the Microsoft website.
   - During installation, sign in with your Microsoft account and register the gateway.
2. **Configure Gateway**:
   - In Data Factory, go to the **Manage** tab.
   - Select **Integration Runtimes** and click on **New**.
   - Choose **Self-hosted** and follow the prompts to link the gateway to your Data Factory.

### Step 2: Set Up Data Pipeline

#### Create a Pipeline
1. **Create New Pipeline**:
   - In Data Factory, go to the **Author** tab.
   - Click on **New Pipeline**.
2. **Add Activities**:
   - Drag and drop the **Copy Data** activity into the pipeline canvas.

#### Add Copy Activity
1. **Configure Source**:
   - In the **Source** tab of the Copy Data activity, select the Oracle linked service you created.
   - Specify the table or query to extract data from Oracle HDI.
2. **Configure Sink**:
   - In the **Sink** tab, choose the destination data store (e.g., Azure Blob Storage, SQL Database).

### Step 3: Configure Data Compression

1. **Compression Settings**:
   - In the **Sink** tab of the Copy Data activity, scroll down to **Compression**.
   - Choose the desired compression type (LZ4 or GZIP).
2. **Configure Destination**:
   - Specify the file format and path where the compressed data will be stored.
   - Ensure the destination supports the chosen compression format.

### Possible Issues and Solutions

#### Connection Issues
- **Issue**: Unable to connect to Oracle database.
- **Solution**: Verify connection details, ensure Oracle Client is installed, and check network connectivity. Ensure the data gateway is properly configured and running.

#### Authentication Problems
- **Issue**: Authentication failures.
- **Solution**: Double-check credentials and authentication method. Ensure API key or token is valid and has necessary permissions.

#### Data Transfer Errors
- **Issue**: Errors during data transfer.
- **Solution**: Check pipeline logs for error messages. Ensure data format and schema compatibility. Adjust query or data mapping as needed.

#### Compression Issues
- **Issue**: Data not compressed as expected.
- **Solution**: Verify compression settings in the copy activity. Ensure destination supports specified compression format.

