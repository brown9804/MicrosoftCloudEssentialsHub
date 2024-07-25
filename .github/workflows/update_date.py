import subprocess
import re

def get_last_commit_date(file_path):
    result = subprocess.run(['git', 'log', '-1', '--format=%cd', '--date=short', file_path], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

def update_markdown_file(file_path, last_updated):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = re.sub(r'^Last updated: .*', f'Last updated: {last_updated}', content, flags=re.MULTILINE)

    with open(file_path, 'w') as file:
        file.write(updated_content)

def main():
    result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], stdout=subprocess.PIPE)
    changed_files = result.stdout.decode('utf-8').splitlines()

    for file_path in changed_files:
        if file_path.endswith('.md'):
            last_updated = get_last_commit_date(file_path)
            update_markdown_file(file_path, last_updated)
            print(f'Updated {file_path} with last updated date {last_updated}')

if __name__ == "__main__":
    main()
