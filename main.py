import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"

response = client.models.generate_content(
    model=model,
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
)

prompt_tokens = str
response_tokens = str


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
    return "Invalid token type"


def main():
    if api_key == None:
        raise RuntimeError("No Gemini API key was found")
    print(f"Prompt tokens: {get_token_count('prompt_tokens')}")
    print(f"Response tokens: {get_token_count('response_tokens')}")
    print(response.text)


if __name__ == "__main__":
    main()
