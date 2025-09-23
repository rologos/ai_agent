import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    joined_path = os.path.abspath(os.path.join(working_directory,file_path))
    working_path = os.path.abspath(working_directory)

    if not joined_path.startswith(working_path):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
    
    cmd = [sys.executable, joined_path, *args]

    try:
        if not os.path.exists(joined_path):
           return f'Error: File "{file_path}" not found.'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file.'

        result = subprocess.run(cmd,capture_output=True,text=True,timeout=30,cwd=os.path.dirname(joined_path))

        parts = []
        if result.stdout:
            parts.append(f"STDOUT:{result.stdout.rstrip()}")
        if result.stderr:
            parts.append(f"STDERR:{result.stderr.rstrip()}")
        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")

        if not parts:
            return "No output produced."
        return "\n".join(parts)

    except Exception as e:
        return f"Error running file: {e}"


