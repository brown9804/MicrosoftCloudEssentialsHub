import os
import subprocess
from datetime import datetime

# Get the list of modified files
result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1'], stdout=subprocess.PIPE)
modified_files = result.stdout.decode('utf-8').split()

# Filter for Markdown files
modified_md_files = [f for f in modified_files if f.endswith('.md')]

# Current date
current_date = datetime.utcnow().strftime('%Y-%m-%d')

# Function to update the last modified date in a file
def update_date_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith('Last updated:'):
                file.write(f'Last updated: {current_date}\n')
            else:
                file.write(line)

# Check if there are any modified Markdown files
if not modified_md_files:
    print("No modified Markdown files found.")
    exit(0)

# Update the date in each modified Markdown file
for file_path in modified_md_files:
    update_date_in_file(file_path)
