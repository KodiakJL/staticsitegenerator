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

    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # If the path is a file
    if os.path.isfile(dir_path_content):
        if dir_path_content.endswith(".md"):
            generate_page(dir_path_content, template_path, dest_dir_path.replace(".md", ".html"))
        return
    dir_list = os.listdir(dir_path_content)
    #If the path is not a file
    for dir in dir_list:
        current_path = os.path.join(dir_path_content, dir)
        # Create new destination directory path that mirrors content structure
        new_dest = os.path.join(dest_dir_path, dir)
        os.makedirs(new_dest, exist_ok=True)
        # Recurse with new destination path
        generate_pages_recursive(current_path, template_path, new_dest)

