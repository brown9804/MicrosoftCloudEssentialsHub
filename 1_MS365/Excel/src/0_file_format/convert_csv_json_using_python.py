# ----------
# Costa Rica
# Belinda Brown, belindabrownr04@gmail.com
# May, 2021
# ----------

# Problem: Need to convert csv to json for other uses 

##############################
#### PACKAGES
##############################
import csv
import json

##############################
#### VARIABLES 
##############################
csv_path = './file_name.csv'
json_path = './file_name.json'


##############################
#### DEFINITIONS 
##############################
def csv_to_json(csv_file_path, json_file_path):
	# WORKSPACE - CSV FILE
    with open(csv_file_path, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
	# WORKSPACE - JSON FILE
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(rows, json_file)

##############################
#### MAIN 
##############################
csv_to_json(csv_path, json_path)



