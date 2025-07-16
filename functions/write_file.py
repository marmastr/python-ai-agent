import os


def write_file(working_directory: str, file_path: str, content: str):
    try:
        abs_file_path = os.path.abspath(
            os.path.join(str(working_directory), str(file_path))
        )
    except Exception as e:
        return f"Error: Geting abs path: {e}"
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(abs_file_path)):
        try:
            os.makedirs(os.path.dirname(abs_file_path))
        except Exception as e:
            return f"Error: Creating path {e}"
    try:
        with open(abs_file_path, "w") as f:
            num = f.write(content)
    except Exception as e:
        return f"Error: Writing file: {e}"
    else:
        return f'Successfully wrote to "{file_path}" ({num} characters written)'
