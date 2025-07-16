import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        abs_file_path = os.path.abspath(
            os.path.join(str(working_directory), str(file_path))
        )
    except Exception as e:
        return f"Error: Geting abs path: {e}"
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        with open(abs_file_path) as f:
            file_content_string = f.read(MAX_CHARS)
    except Exception as e:
        return f"Error: Reading from file: {e}"
    if len(file_content_string) >= MAX_CHARS:
        file_content_string += (
            f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        )
    return file_content_string
