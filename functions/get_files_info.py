import os
import pathlib

def get_files_info(working_directory, directory="."):
    joined_path = os.path.abspath(os.path.join(working_directory, directory))
    working_path = os.path.abspath(working_directory)
    if not joined_path.startswith(working_path + os.sep):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
'''
    if not os.path.isdirectory(director):
        return f'Error: "{directory}" is not a directory' 
    '''
