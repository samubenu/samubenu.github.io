import re

def fix_links(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Replace links with the new format
    # Matches dinosaur_pages/page_X.md and replaces with dinosaur/page_X
    fixed_content = re.sub(
        r'dinosaur/page_(\d+)',
        r'/page_\1',
        content
    )
    
    with open(filepath, 'w') as file:
        file.write(fixed_content)
    
    print(f"Updated links in {filepath}")

# Fix links in main dinosaurs.md file
fix_links('/home/pinoij/programowanie/www/lab1/strona/_pages/dinosaurs.md')

print("Link updating complete!")