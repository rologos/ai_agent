import os
import sys
from dotenv import load_dotenv
from google import genai
from functools import reduce

def main(*args):
    if len(args) < 1:
        print("no prompt provided")
        sys.exit(1)
    joinedargs = reduce(lambda x,y: x + " " + y,args,"")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=joinedargs
    )
    
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count + 13}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main(*sys.argv[1:])
