# Automated PDF Invoice Processing using <br/> Azure Storage + Document Intelligence + Cosmos DB

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-20

----------

> How to parse PDFs from an Azure Storage Account, process them using Azure Document Intelligence, and store the results in Cosmos DB. <br/> <br/>
> 1. Upload your PDFs to an Azure Blob Storage container. <br/>
> 2. An Azure Function is triggered by the upload, which calls the Azure Document Intelligence API to analyze the PDFs.  <br/>
> 3. The extracted data is parsed and subsequently stored in a Cosmos DB database, ensuring a seamless and automated workflow from document upload to data storage. 

## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Azure Cosmos DB - Database for the AI Era](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)

</details>

## Content 



## Overview 

> `Azure Document Intelligence`, formerly known as **Form Recognizer**, is a powerful AI service that extracts structured data from documents. It `uses machine learning models to analyze and process various types of documents, such as invoices, receipts, business cards`, and more.

| Key Features | Details |
| --- | --- |
| **Prebuilt Models** | - **Invoice Model**: Extracts fields like invoice ID, date, vendor information, line items, totals, and more.<br/>- **Receipt Model**: Extracts merchant name, transaction date, total amount, and line items.<br/>- **Business Card Model**: Extracts contact information such as name, company, phone number, and email. |
| **Custom Models** | - **Training**: You can train custom models using labeled data. This involves uploading a set of documents and manually labeling the fields you want to extract.<br/>- **Model Management**: Manage versions of your custom models, retrain them with new data, and evaluate their performance. |
| **APIs and SDKs** | - **REST API**: Provides endpoints for analyzing documents, managing models, and retrieving results.<br/>- **SDKs**: Available in multiple languages (e.g., Python, C#, JavaScript) to simplify integration into your applications. |



<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
