import os
import pathlib

def get_files_info(working_directory, directory="."):
    joined_path = os.path.abspath(os.path.join(working_directory, directory))
    working_path = os.path.abspath(working_directory) 
    if not joined_path.startswith(working_path + os.sep) and joined_path != working_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(joined_path):
        return f'Error: "{directory}" is not a directory' 

    contents = os.listdir(joined_path)

    list_str = []
    for item in contents:
        p = os.path.join(joined_path,item)
        if os.path.isfile(p):
            list_str.append(f" - {item}: file_size={os.path.getsize(p)} bytes, is_dir=False")
        else:
            list_str.append(f" - {item}: file_size=12 bytes, is_dir=True")

    return "\n".join(list_str)
