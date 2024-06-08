import os

def list_files_in_current_directory():
    try:
        # Get the current working directory
        current_directory = os.getcwd()
        
        # Get the name of the script file
        script_file = os.path.basename(__file__)
        
        # Get a list of all entries in the current directory
        with os.scandir(current_directory) as entries:
            # Filter out the entries that are files, excluding the script file, and get their names
            files = [entry.name for entry in entries if entry.is_file() and entry.name != script_file]
        
        return files
    except PermissionError:
        print(f"Permission denied to access the directory {current_directory}.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Get the list of files in the current directory
files = list_files_in_current_directory()

# Print the list of files in the desired format
if files:
    print("Files in the current directory:")
    formatted_files = [f"'{file}'" for file in files]
    print(", ".join(formatted_files))
else:
    print("No files found or an error occurred.")

input("Type to terminate")