from pathlib import Path
import os

def list_files_pathlib(directory_path='.'):
    """
    Lists all files in the specified directory (non-recursive).
    
    Args:
        directory_path (str): The path to the directory to scan. 
                              Defaults to the current directory ('.').

    Returns:
        list: A list of Path objects for all files.
    """
    p = Path(directory_path)
    # Use list comprehension with .is_file() to filter out directories
    files = [item.name for item in p.iterdir() if item.is_file()]
    return files

def list_all_files_os_walk(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full file path by joining the root path and the filename
            full_path = os.path.join(root, file)
            file_list.append(full_path)
    return file_list
