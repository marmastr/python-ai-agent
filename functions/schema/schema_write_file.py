import google.genai.types as types

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
    ),
)
