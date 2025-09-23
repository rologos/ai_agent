import os
import config

def write_file(working_directory, file_path, content):

    joined_path = os.path.abspath(os.path.join(working_directory,file_path))
    working_path = os.path.abspath(working_directory)

    if not joined_path.startswith(working_path):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    
    try:
        dir_path = os.path.dirname(joined_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(joined_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to \"{file_path}\" ({len(content)} characters written)'

    except Exception as e:
        return f"Error writing files: {e}"


