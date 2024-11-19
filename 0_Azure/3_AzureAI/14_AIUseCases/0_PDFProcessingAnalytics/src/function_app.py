import azure.functions as func
import logging
import json
import os
import uuid
import io
from pdfminer.high_level import extract_text
from azure.cosmos import CosmosClient, PartitionKey

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

def read_pdf_content(myblob):
    # Read the blob content into a BytesIO stream
    blob_bytes = myblob.read()
    pdf_stream = io.BytesIO(blob_bytes)
    
    # Extract text from the PDF stream
    text = extract_text(pdf_stream)
    return text

def extract_invoice_data(text):
    lines = text.split('\n')
    invoice_data = {
        "id": generate_id(),
        "customer_name": "",
        "customer_email": "",
        "customer_address": "",
        "company_name": "",
        "company_phone": "",
        "company_address": "",
        "rentals": []
    }

    for i, line in enumerate(lines):
        if "BILL TO:" in line:
            invoice_data["customer_name"] = lines[i + 1].strip()
            invoice_data["customer_email"] = lines[i + 2].strip()
            invoice_data["customer_address"] = lines[i + 3].strip()
        elif "Company Information:" in line:
            invoice_data["company_name"] = lines[i + 1].strip()
            invoice_data["company_phone"] = lines[i + 2].strip()
            invoice_data["company_address"] = lines[i + 3].strip()
        elif "Rental Date" in line:
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == "":
                    break
                rental_details = lines[j].split()
                rental_date = rental_details[0]
                title = " ".join(rental_details[1:-3])
                description = rental_details[-3]
                quantity = rental_details[-2]
                total_price = rental_details[-1]
                invoice_data["rentals"].append({
                    "rental_date": rental_date,
                    "title": title,
                    "description": description,
                    "quantity": quantity,
                    "total_price": total_price
                })

    logging.info("Successfully extracted invoice data.")
    return invoice_data

def save_invoice_data_to_cosmos(invoice_data, blob_name):
    try:
        endpoint = os.getenv("COSMOS_DB_ENDPOINT")
        key = os.getenv("COSMOS_DB_KEY")
        client = CosmosClient(endpoint, key)
        logging.info("Successfully connected to Cosmos DB.")
    except Exception as e:
        logging.error(f"Error connecting to Cosmos DB: {e}")
        return
    
    database_name = 'ContosoDBAIDemo'
    container_name = 'Invoices'
    
    try:
        database = client.create_database_if_not_exists(id=database_name)
        container = database.create_container_if_not_exists(
            id=container_name,
            partition_key=PartitionKey(path="/invoice_number"),
            offer_throughput=400
        )
        logging.info("Successfully ensured database and container exist.")
    except Exception as e:
        logging.error(f"Error creating database or container: {e}")
        return
    
    try:
        response = container.upsert_item(invoice_data)
        logging.info(f"Saved processed invoice data to Cosmos DB: {response}")
    except Exception as e:
        logging.error(f"Error inserting item into Cosmos DB: {e}")

def generate_id():
    return str(uuid.uuid4())

@app.blob_trigger(arg_name="myblob", path="pdfinvoices/{name}",
                  connection="contosostorageaidemo_STORAGE")
def BlobTriggerContosoPDFInvoicesRaw(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob\n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    try:
        text = read_pdf_content(myblob)
        logging.info("Successfully read and extracted text from PDF.")
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        return

    logging.info(f"Extracted text from PDF: {text}")

    try:
        invoice_data = extract_invoice_data(text)
        logging.info(f"Extracted invoice data: {invoice_data}")
    except Exception as e:
        logging.error(f"Error extracting invoice data: {e}")
        return

    try:
        save_invoice_data_to_cosmos(invoice_data, myblob.name)
        logging.info("Successfully saved invoice data to Cosmos DB.")
    except Exception as e:
        logging.error(f"Error saving invoice data to Cosmos DB: {e}")