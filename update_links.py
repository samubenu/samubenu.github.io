import os
import re

# Process all dinosaur pages to update links
dinosaur_pages_dir = '_pages/dinosaur_pages'
for filename in os.listdir(dinosaur_pages_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(dinosaur_pages_dir, filename)
        
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Update internal links
        content = re.sub(r'\(page_(\d+).md\)', r'(/page_\1)', content)
        content = re.sub(r'\(../dinosaurs.md\)', r'(/dinosaur_pages)', content)
        
        with open(filepath, 'w') as file:
            file.write(content)

print("Links updated in all Markdown files")