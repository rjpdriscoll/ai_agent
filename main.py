import argparse
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

response = client.models.generate_content(
    model=model,
    contents=args.user_prompt,
)


def get_token_count(token_type):
    if response.usage_metadata == None:
        raise RuntimeError(
            "The metadata is empty. Be sure that the API request was successful."
        )
    if token_type == "prompt_tokens":
        prompt_tokens = response.usage_metadata.prompt_token_count
        return prompt_tokens
    if token_type == "response_tokens":
        response_tokens = response.usage_metadata.candidates_token_count
        return response_tokens
    return "Invalid token type. Please provide either 'prompt_tokens' or 'response_tokens'."


def main():
    if api_key == None:
        raise RuntimeError("No Gemini API key was found")
    print(f"Prompt tokens: {get_token_count('prompt_tokens')}")
    print(f"Response tokens: {get_token_count('response_tokens')}")
    print(response.text)


if __name__ == "__main__":
    main()
