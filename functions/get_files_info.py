import os
from config import MAX_CHARS
import subprocess

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{str(directory)}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{str(directory)}" is not a directory'
    
    try:
        file_info_list = []

        for file_name in os.listdir(full_path):
                file_path = os.path.join(full_path, file_name)
                is_dir_value = os.path.isdir(file_path)

                file_size = os.path.getsize(file_path)    
                

                std_line = f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir_value}"
                file_info_list.append(std_line)

        return "\n".join(file_info_list)
    
    except Exception as e:
        return f"Error: {e}"
    
def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{str(file_path)}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string

    except Exception as e:
        return f"Error: {e}"

def write_file(working_directory, file_path, content):

    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write "{str(file_path)}" as it is outside the permitted working directory'
    
    try:
        dir_path = os.path.dirname(full_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
                      
        with open(full_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"
    
def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{str(file_path)}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{str(file_path)}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{str(file_path)}" is not a Python file.'
    
    try:
        cmd = ["python", file_path] + args

        result = subprocess.run(cmd, timeout=30, capture_output=True, text=True, cwd=working_directory)
        return_code = result.returncode
        
        if return_code != 0:
            return f"Process exited with code {return_code}\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        if not result.stdout and not result.stderr:
            return "No output produced."
        
        return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
