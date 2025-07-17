import os
import sys
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import AI_MODEL, SYSTEM_PROMPT
from functions.available_functions import available_functions

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
    response = client.models.generate_content(
        model=AI_MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ),
    )
    if args.verbose:
        print(f"User prompt:\n{args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
