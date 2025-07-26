import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from config import model_name, system_prompt


def main():
    load_dotenv()
    
    # Check for arguments and extract user prompt
    if len(sys.argv) < 2:
        print("Error: No prompt provided.")
        sys.exit(1)
    
    user_prompt = " ".join(sys.argv[1:])
    
    # Create messages list
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    # Set up API client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    # Generate response
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    
    # Handle verbose output
    if "--verbose" in sys.argv:
        print("<-------------------------->")
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("<-------------------------->")
    
    print(response.text)


if __name__ == "__main__":
    main()
