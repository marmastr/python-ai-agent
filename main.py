import os
import sys
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import AI_MODEL, MAX_ITERATIONS, SYSTEM_PROMPT
from functions.call_function import call_function, available_functions

if not load_dotenv():
    print("failed to load .env")
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

parser = argparse.ArgumentParser(
    prog="BOOT.DEV Python AI Agent",
    description="AI agent created using Pyhton during Boot.dev course",
)
parser.add_argument("user_prompt")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

if len(args.user_prompt) <= 0:
    print("no prompt given")
    sys.exit(1)


def main():
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)]),
    ]
    # i = 0
    # try:
    #     while i < 20:
    #         response = generate_content(client, messages, args.verbose)
    #         if response:
    #             print(response)
    #             break
    #         i += 1
    # except Exception as e:
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERATIONS:
            print(f"Maximum iterations ({MAX_ITERATIONS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(
                f"Error in generate_content: {e}"
            )  #     return f"Error: While in loop: {e}"


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model=AI_MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ),
    )
    if not response.candidates:
        return "Error: no response candidates found"
    for x in response.candidates:
        # messages.append(types.Content(role="tool",parts=[types.Part(text=x.content)]))
        messages.append(x.content)

    if verbose:
        print(f"User prompt:\n{args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if not response.function_calls:
        return response.text
    function_responses = []
    for call in response.function_calls:
        function_call_result = call_function(call, verbose)
        if not function_call_result.parts[0].function_response.response:
            raise Exception("Error: No response returned from function call")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))


if __name__ == "__main__":
    main()
