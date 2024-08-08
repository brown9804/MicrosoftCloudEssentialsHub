# Open-Source Models for OCR and Document Processing in Azure

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-08

----------

> **Optical Character Recognition `(OCR)`** is a technology that converts different types of documents, such as scanned paper documents, PDFs, or images captured by a digital camera, into editable and searchable data. OCR is widely used to digitize printed texts so that they can be electronically edited, searched, and stored more compactly.


## Wiki 

- [How to use Open Source foundation models curated by Azure Machine](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-foundation-models?view=azureml-api-2)
- [Model Catalog and Collections](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-catalog?view=azureml-api-2)
- [Open Source on Azure](https://azure.microsoft.com/en-us/solutions/open-source/)
- [Introducing the Azure AI Model Inference API](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/introducing-the-azure-ai-model-inference-api/ba-p/4144292)
- [Journey Series for Generative AI Application Architecture](https://techcommunity.microsoft.com/t5/educator-developer-blog/journey-series-for-generative-ai-application-architecture/ba-p/4065564)
- [Automate document processing with AI Document Intelligence](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/automate-document-processing-azure-form-recognizer)

## OSS Models 

| **Model** | **Provider** | **Capabilities** |
|-----------|--------------|------------------|
| **LayoutLMv3** | Hugging Face | Document layout analysis, OCR, information extraction from documents |
| **DiT (Document Image Transformer)** | Hugging Face | Document image analysis, OCR, object detection in documents |
| **BERT** | Hugging Face | Natural language understanding, text classification, sentiment analysis |
| **GPT-3** | OpenAI | Text generation, summarization, translation, question answering |
| **Tesseract** | Open Source | OCR, text extraction from images and PDFs |
| **EasyOCR** | Open Source | OCR, text extraction from images and PDFs |
| **DocTR** | Hugging Face | OCR, text extraction from images and PDFs |

## Models for Image and PDF Ingestion

Models like **LayoutLMv3** and **DiT** from Hugging Face, which are designed for document layout analysis and OCR. These models can ingest images or PDFs, perform OCR to extract text, and then process that text for various tasks.

## Building an OCR Solution in Azure

To build an OCR solution in Azure, you can use the following steps:

```mermaid 
graph TD
    A[Upload Documents to Azure Blob Storage] --> B[OCR Processing with Tesseract or EasyOCR]
    B --> C[Extract Text from Documents]
    C --> D[Text Processing with NLP Models]
    D --> E[Search Implementation with Azure AI Search]
```

1. **Data Ingestion**: Use Azure Blob Storage to store your images or PDFs.
2. **OCR Processing**: Use Azure AI Document Intelligence or deploy open-source OCR models like Tesseract or EasyOCR on Azure Machine Learning.
3. **Data Extraction**: Extract text from the documents using the OCR models.
4. **Data Processing**: Use natural language processing (NLP) models to analyze and process the extracted text.
5. **Search and Query**: Implement search functionality using Azure AI Search or other search frameworks to perform searches like a leucine search.

## Recommended Trainings 

- **[OCR - Optical Character Recognition](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-ocr)**:
   - Learn how to use OCR services to extract printed and handwritten text from images and documents.
   - Understand the different OCR engines and how to implement them in your applications.
-  **[Quickstart: Optical character recognition (OCR)](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library)**:
   - A step-by-step guide to getting started with OCR using Azure AI Vision.
   - Includes code examples and instructions for setting up your environment.
- **[Implement open-source software - Training](https://learn.microsoft.com/en-us/training/modules/implement-open-source-software-azure/)**:
   - Explore how to implement open-source software in Azure.
   - Understand common open-source licenses and their implications.


