import os
import config
from google.genai import types

def get_file_content(working_directory, file_path):
    joined_path = os.path.abspath(os.path.join(working_directory,file_path))
    working_path = os.path.abspath(working_directory)

    if not joined_path.startswith(working_path):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.isfile(joined_path):
        return f"Error: File not found or is not regular file:\"{file_path}\""

    try:
        with open(joined_path, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
        if len(file_content_string) ==10000:
            file_content_string = file_content_string + f"[...File \"{file_path}\" truncated at 10000 characters]"
        return file_content_string
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Fetches the contents of a file up to a 10000 character limit",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to get contents fromfrom, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
