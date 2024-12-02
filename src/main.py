import os
import shutil
from copystatic import copy_directory_recursive
from generate_content import generate_page



def main():
    source_directory = "static"
    destination_directory = "public"
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"

    copy_directory_recursive(source_directory, destination_directory)
    generate_page(from_path, template_path, dest_path)

main()