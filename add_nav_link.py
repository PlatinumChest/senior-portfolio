import os
import glob
import re

files = glob.glob('*.html')
new_link = '                    <li><a href="academic_history.html" id="history-link"><span class="icon solid fa-history">Academic History</span></a></li>\n'

for file in files:
    if file == 'academic_history.html': continue
    with open(file, 'r') as f:
        content = f.read()
    
    # We look for the <li> containing the svatantrata link
    pattern = r'(\s*<li><a href="https://svatantrata\.net/".*?>)'
    if re.search(pattern, content, re.DOTALL):
        # We want to insert our new link just before the match, keeping indentation
        content = re.sub(r'(\n)(\s*)(<li><a href="https://svatantrata\.net/)', 
                         r'\1\2<li><a href="academic_history.html" id="history-link"><span class="icon solid fa-history">Academic History</span></a></li>\1\2\3', content)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Could not find nav in {file}")
