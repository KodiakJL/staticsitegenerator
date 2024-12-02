import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    header = markdown.strip().split("\n", 1)
    if not header[0].startswith("#"):
        raise Exception("No header found in markdown")
    return header[0].strip("# ")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page forom {from_path} to {dest_path}, using {template_path}")
    #Make local copies of the files
    with open(from_path, 'r') as file:
        markdown_file = file.read()
    with open(template_path, 'r') as template:
        template_file = template.read()
    #Convert the markdown file contenst into HTML
    html_string = markdown_to_html_node(markdown_file).to_html()
    #Extracting the title 
    title = extract_title(markdown_file)

    #Changing the source content to the actual content
    updated_title = template_file.replace("{{ Title }}", title)
    updated_file = updated_title.replace("{{ Content }}", html_string)

    #Checking if directory exist, if it doesnt we create it
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    #Writing to destination
    with open(dest_path, 'w') as dest_file:
        dest_file.write(updated_file)
