from config import WORK_DIR
import google.genai.types as types
from functions.available_functions import available_functions
from functions.run_python_file import run_python_file


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    functions_enabled = []
    for f in available_functions.function_declarations:
        functions_enabled.append(f.name)
    if function_call_part.name not in functions_enabled:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={
                        "error": f"Unknown function: {function_call_part.name}{functions_enabled}"
                    },
                )
            ],
        )
    command = {"working_directory": WORK_DIR}
    if function_call_part.name:
        command.update({"file_path": f"{function_call_part.name}.py"})
    if function_call_part.args:
        command.update({"args": function_call_part.args})

    result = run_python_file(**command)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )
