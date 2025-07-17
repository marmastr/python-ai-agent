import google.genai.types as types

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
                type=types.Type.STRING,
                description="A list of optional arguments to execute the Python file with.",
            ),
        },
    ),
)
