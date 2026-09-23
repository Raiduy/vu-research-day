import os
import json
import openai
from dotenv import load_dotenv

# Load environment variables (ensure they are set in your environment or .env file
load_dotenv()
BASE_URL = os.getenv("NEBULA_BASE_URL")
API_KEY = os.getenv("NEBULA_API_KEY")

if not BASE_URL or not API_KEY:
    raise ValueError("NEBULA_BASE_URL and NEBULA_API_KEY must be set in the environment.")

# Configure OpenAI client for a compatible endpoint
client = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)

def send_prompt(prompt: str, model: str = "FAST.gpt-oss:120b", temperature: float = 0.7):
    """Send a prompt to an OpenAI‑compatible endpoint using the openai package.

    Args:
        prompt: The user prompt to send.
        model: The model name expected by the server.
        temperature: Sampling temperature.
    Returns:
        The generated text response.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    # Extract the assistant's reply
    return response.choices[0].message.content

if __name__ == "__main__":
    user_prompt = "Explain the theory of relativity in simple terms."
    print(send_prompt(user_prompt))
