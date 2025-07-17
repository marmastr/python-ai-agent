import google.genai.types as types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to read content from, relative to the working directory.",
            ),
        },
    ),
)
