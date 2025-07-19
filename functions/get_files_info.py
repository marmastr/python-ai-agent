import os

import google.genai.types as types


def get_files_info(working_directory, directory=None):
    dir_path = os.path.abspath(os.path.join(str(working_directory), str(directory)))
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    if not dir_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        dir_list = list(
            map(
                lambda item: f"- {item}: {os.path.getsize(os.path.join(dir_path, item))},is_dir={os.path.isdir(os.path.join(dir_path, item))}",
                os.listdir(dir_path),
            )
        )
    except Exception as e:
        return f"Error: Listing files: {e}"
    result = "\n".join(dir_list)
    return result


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
