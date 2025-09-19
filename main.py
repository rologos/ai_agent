import os
import sys
from dotenv import load_dotenv
from google import genai
from functools import reduce
from google.genai import types

def main(*args):
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    usernameswitch = False
    if args[-1] == "--verbose":
        user_prompt = " ".join(args[:-1])
        usernameswitch = True
    else:
        user_prompt = " ".join(args)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=messages,
    )
    
    print(response.text)
    if usernameswitch:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count + 13}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
