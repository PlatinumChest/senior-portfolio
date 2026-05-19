import os
import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace the URL
    new_content = content.replace('academic_history.html', 'academic_credentials.html')
    # Replace the link text
    new_content = new_content.replace('Academic History</', 'Academic Credentials</')
    # Replace the title tag if it's the specific file
    if file == 'academic_history.html':
        new_content = new_content.replace('<title>Academic History - ', '<title>Academic Credentials - ')
        
    if new_content != content:
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Updated {file}")
