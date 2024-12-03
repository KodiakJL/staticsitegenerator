import os
import shutil
from copystatic import copy_directory_recursive
from generate_content import generate_pages_recursive



def main():
    source_directory = "static"
    destination_directory = "public"
    from_path = "content"
    template_path = "template.html"
    dest_path = "public"

    copy_directory_recursive(source_directory, destination_directory)
    generate_pages_recursive(from_path, template_path, dest_path)

main()