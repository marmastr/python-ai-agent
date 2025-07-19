import os

import google.genai.types as types


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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The information to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
