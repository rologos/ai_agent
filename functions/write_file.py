import os
from google.genai import types

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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file specified in file_path, with what is passed to this function via the content argument",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to get write a file to, relative to the working directory.",
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents that are going to be written to the file",
            ),
        },
    ),
)
