import os
import shutil
from textnode import TextNode, TextType
from markdown_blocks import markdown_to_html_node, extract_title

def copy_directory_recursive(src, dest):

    # Check if the source directory exists
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory '{src}' does not exist.")
    
    # If the destination directory exists, clear its contents
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    # Create the destination directory
    os.mkdir(dest)
    
    # Iterate through all items in the source directory
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dest_item = os.path.join(dest, item)
        
        # Check if the item is a file or directory
        if os.path.isfile(src_item):
            shutil.copy(src_item, dest_item)
            print(f"Copied file: {src_item} -> {dest_item}")
        elif os.path.isdir(src_item):
            # Recursively copy directories
            copy_directory_recursive(src_item, dest_item)


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




def main():
    source_directory = "static"
    destination_directory = "public"
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"

    copy_directory_recursive(source_directory, destination_directory)
    generate_page(from_path, template_path, dest_path)

main()