import os

def add_front_matter(filepath, layout, title):
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Extract title from markdown if exists
    if not title and content.startswith('# '):
        title = content.split('\n')[0][2:]
    
    front_matter = f"""---
layout: {layout}
title: "{title}"
permalink: /{os.path.basename(filepath).replace('.md', '')}
---

{content}"""
    
    with open(filepath, 'w') as file:
        file.write(front_matter)

# Process main dinosaur index
add_front_matter('_pages/dinosaurs.md', 'page', 'Dinosaur Encyclopedia')

# Process all dinosaur pages
dinosaur_pages_dir = r'_pages/dinosaur_pages'
for filename in os.listdir(dinosaur_pages_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(dinosaur_pages_dir, filename)
        add_front_matter(filepath, 'page', '')

print("Front matter added to all Markdown files")