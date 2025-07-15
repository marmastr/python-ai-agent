import os


def in_context(working_directory, directory):
    dir_path = os.path.abspath(os.path.join(str(working_directory), str(directory)))
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    if not dir_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
