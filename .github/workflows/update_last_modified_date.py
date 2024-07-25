# Add last update date into each markdown 
import os
import datetime

def update_last_modified_date(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith('last-modified-date:'):
            lines[i] = f'last-modified-date: {datetime.datetime.utcnow().strftime("%Y-%m-%d")}\n'
            break

    with open(file_path, 'w') as file:
        file.writelines(lines)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            update_last_modified_date(os.path.join(root, file))
