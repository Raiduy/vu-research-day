# Programmatic Prompts Example

This directory contains a minimal example showing how to call an **OpenAI‑compatible** endpoint (e.g., a self‑hosted model or Azure OpenAI) from Python using the modern `openai` SDK (v1).

---

## Files

| File | Description |
|------|-------------|
| `openai_example.py` | Python script that loads configuration from a `.env` file, creates an `openai.OpenAI` client, and provides a `send_prompt` function to get a chat completion. |
| `requirements.txt`   | Lists the Python dependencies (`openai` and `python-dotenv`). |
| `example.env`       | Template showing the required environment variables (not committed to source control). |
| `README.md`         | This documentation. |

---

## Prerequisites

1. **Python 3.8+**
2. A **virtual environment** (recommended) to keep dependencies isolated.
3. An OpenAI‑compatible endpoint that accepts the standard `/v1/chat/completions` API.
4. The environment variables `NEBULA_BASE_URL` and `NEBULA_API_KEY` set either in your shell or in a `.env` file placed in this directory.

---

## Setup

Open your Terminal (macOS/Linux) or Command Prompt / PowerShell (Windows) and navigate to this folder. Then run the following commands:

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install the required packages
pip install -r requirements.txt
```

Create a new file named exactly `.env` (with a dot at the beginning and no other name) in this directory. You can copy the contents from `example.env` and update it with your endpoint information:

```dotenv
NEBULA_BASE_URL=https://your-endpoint.com   # Base URL without trailing slash
NEBULA_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx     # Your API key
```

---

## How the code works

```python
import os
import json
import openai
from dotenv import load_dotenv

# Load variables from .env (if present)
load_dotenv()
BASE_URL = os.getenv("NEBULA_BASE_URL")
API_KEY  = os.getenv("NEBULA_API_KEY")

# Initialise the OpenAI client for a custom endpoint
client = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)
```

* `load_dotenv()` pulls the values from a `.env` file into the process environment.
* The `openai.OpenAI` client is instantiated with the custom `base_url` and `api_key`.
* `send_prompt()` builds the chat request using the modern SDK call:

```python
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature,
)
return response.choices[0].message.content.strip()
```

The function returns the assistant’s reply as a plain string.

---

## Running the example

```bash
python programatic-prompts/openai_example.py
```

You should see the model’s response printed to the console.

---

## Customisation

* **Model name** – Change the default `model` argument when calling `send_prompt` to match the model deployed at your endpoint.
* **Parameters** – Add extra parameters (e.g., `max_tokens`, `top_p`) to the `client.chat.completions.create` call as needed.
* **Error handling** – The example raises a `ValueError` if the required environment variables are missing; you can extend this to more sophisticated handling.

