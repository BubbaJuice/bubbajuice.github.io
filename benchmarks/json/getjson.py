import os
import json

def list_files_in_current_directory():
    try:
        # Get the current working directory
        current_directory = os.getcwd()
        
        # Get the name of the script file
        script_file = os.path.basename(__file__)
        
        # Get a list of all entries in the current directory
        with os.scandir(current_directory) as entries:
            # Filter out the entries that are files, excluding the script file, and get their names
            files = [entry.name for entry in entries if entry.is_file() and entry.name != script_file and entry.name.endswith('.json')]
        
        return files
    except PermissionError:
        print(f"Permission denied to access the directory {current_directory}.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def combine_json_files(files):
    combined_data = []
    for file in files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                combined_data.append(data)
        except Exception as e:
            print(f"An error occurred while reading {file}: {e}")
    return combined_data

def save_combined_json(data, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        print(f"Combined JSON saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while saving the combined JSON: {e}")

# Get the list of files in the current directory
files = list_files_in_current_directory()

# Combine the JSON files
combined_data = combine_json_files(files)

# Save the combined JSON to a regular file
save_combined_json(combined_data, 'all_data.json')

input("Type to terminate")