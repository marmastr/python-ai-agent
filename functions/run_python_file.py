import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        cwd = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(str(cwd), str(file_path)))
    except Exception as e:
        return f"Error: Geting abs path: {e}"
    if not abs_file_path.startswith(cwd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith("py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        command = ["python", abs_file_path]
        if args:
            command.extend(args)
        completed_process = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            timeout=30,
            text=True,
        )
    except Exception as e:
        return f"Error: {e}"
    else:
        result = []
        if completed_process.stdout:
            result.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            result.append(f"STDERR:\n{completed_process.stderr}")
        if completed_process.returncode != 0:
            result.append(f"Process exited with code {completed_process.returncode}")
        if result:
            return "\n".join(result)
        else:
            return "No output produced"
