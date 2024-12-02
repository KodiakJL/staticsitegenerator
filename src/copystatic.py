import os
import shutil

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