import logging
import azure.functions as func
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.cosmos import CosmosClient, PartitionKey, exceptions
from azure.identity import DefaultAzureCredential
import os
import uuid

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

## DEFINITIONS 
def initialize_form_recognizer_client():
    endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")
    key = os.getenv("FORM_RECOGNIZER_KEY")
    if not isinstance(key, str):
        raise ValueError("FORM_RECOGNIZER_KEY must be a string")
    logging.info(f"Form Recognizer endpoint: {endpoint}")
    return DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def read_pdf_content(myblob):
    logging.info(f"Reading PDF content from blob: {myblob.name}")
    return myblob.read()

def analyze_pdf(form_recognizer_client, pdf_bytes):
    logging.info("Starting PDF analysis.")
    poller = form_recognizer_client.begin_analyze_document(
        model_id="prebuilt-invoice",
        document=pdf_bytes
    )
    logging.info("PDF analysis in progress.")
    return poller.result()

def extract_invoice_data(result):
    logging.info("Extracting invoice data from analysis result.")
    invoice_data = {
        "id": str(uuid.uuid4()),
        "customer_name": "",
        "customer_email": "",
        "customer_address": "",
        "company_name": "",
        "company_phone": "",
        "company_address": "",
        "rentals": []
    }

    def serialize_field(field):
        if field:
            return str(field.value)  # Convert to string
        return ""
    
    for document in result.documents:
        fields = document.fields
        invoice_data["customer_name"] = serialize_field(fields.get("CustomerName"))
        invoice_data["customer_email"] = serialize_field(fields.get("CustomerEmail"))
        invoice_data["customer_address"] = serialize_field(fields.get("CustomerAddress"))
        invoice_data["company_name"] = serialize_field(fields.get("VendorName"))
        invoice_data["company_phone"] = serialize_field(fields.get("VendorPhoneNumber"))
        invoice_data["company_address"] = serialize_field(fields.get("VendorAddress"))

        items = fields.get("Items").value if fields.get("Items") else []
        for item in items:
            item_value = item.value if item.value else {}
            rental = {
                "rental_date": serialize_field(item_value.get("Date")),
                "title": serialize_field(item_value.get("Description")),
                "description": serialize_field(item_value.get("Description")),
                "quantity": serialize_field(item_value.get("Quantity")),
                "total_price": serialize_field(item_value.get("TotalPrice"))
            }
            invoice_data["rentals"].append(rental)

    logging.info(f"Successfully extracted invoice data: {invoice_data}")
    return invoice_data

def save_invoice_data_to_cosmos(invoice_data):
    try:
        endpoint = os.getenv("COSMOS_DB_ENDPOINT")
        key = os.getenv("COSMOS_DB_KEY")
        aad_credentials = DefaultAzureCredential()
        client = CosmosClient(endpoint, credential=aad_credentials, consistency_level='Session')
        logging.info("Successfully connected to Cosmos DB using AAD default credential")
    except Exception as e:
        logging.error(f"Error connecting to Cosmos DB: {e}")
        return
    
    database_name = "ContosoDBDocIntellig"
    container_name = "Invoices"

    
    try: # Check if the database exists
        # If the database does not exist, create it
        database = client.create_database_if_not_exists(database_name)
        logging.info(f"Database '{database_name}' does not exist. Creating it.")
    except exceptions.CosmosResourceExistsError: # If error get name, keep going 
        database = client.get_database_client(database_name)
        logging.info(f"Database '{database_name}' already exists.")

    database.read()
    logging.info(f"Reading into '{database_name}' DB")

    try: # Check if the container exists
        # If the container does not exist, create it
        container = database.create_container(
            id=container_name,
            partition_key=PartitionKey(path="/transactionId"),
            offer_throughput=400
        )
        logging.info(f"Container '{container_name}' does not exist. Creating it.")
    except exceptions.CosmosResourceExistsError:
        container = database.get_container_client(container_name)
        logging.info(f"Container '{container_name}' already exists.")
    except exceptions.CosmosHttpResponseError:
        raise

    container.read()
    logging.info(f"Reading into '{container}' container")

    try:
        response = container.upsert_item(invoice_data)
        logging.info(f"Saved processed invoice data to Cosmos DB: {response}")
    except Exception as e:
        logging.error(f"Error inserting item into Cosmos DB: {e}")

## MAIN 
@app.blob_trigger(arg_name="myblob", path="pdfinvoices/{name}",
                  connection="invoicecontosostorage_STORAGE")
def BlobTriggerContosoPDFInvoicesDocIntelligence(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob\n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    try:
        form_recognizer_client = initialize_form_recognizer_client()
        pdf_bytes = read_pdf_content(myblob)
        logging.info("Successfully read PDF content from blob.")
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        return

    try:
        result = analyze_pdf(form_recognizer_client, pdf_bytes)
        logging.info("Successfully analyzed PDF using Document Intelligence.")
    except Exception as e:
        logging.error(f"Error analyzing PDF: {e}")
        return

    try:
        invoice_data = extract_invoice_data(result)
        logging.info(f"Extracted invoice data: {invoice_data}")
    except Exception as e:
        logging.error(f"Error extracting invoice data: {e}")
        return

    try:
        save_invoice_data_to_cosmos(invoice_data)
        logging.info("Successfully saved invoice data to Cosmos DB.")
    except Exception as e:
        logging.error(f"Error saving invoice data to Cosmos DB: {e}")