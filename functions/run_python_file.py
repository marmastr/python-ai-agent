import os
import subprocess

import google.genai.types as types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_work_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(
            os.path.join(str(working_directory), str(file_path))
        )
    except Exception as e:
        return f"Error: Geting abs path: {e}"
    if not abs_file_path.startswith(abs_work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{abs_file_path}" not found.'
    if not abs_file_path.endswith("py"):
        return f'Error: "{abs_file_path}" is not a Python file.'
    try:
        command = ["python", abs_file_path]
        if args:
            command.extend(args)
        completed_process = subprocess.run(
            command,
            cwd=abs_work_dir,
            capture_output=True,
            timeout=30,
            text=True,
        )
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
    except Exception as e:
        return f"Error: executing {abs_file_path}: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute the Python file in the specified directory with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional argument to pass to the Python file.",
                ),
                description="A list of optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
