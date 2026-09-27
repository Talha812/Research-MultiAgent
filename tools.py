import os
from groq import Groq


MODEL_NAME = "openai/gpt-oss-120b"


def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not configured. "
            "Add it to Streamlit Secrets."
        )

    return Groq(api_key=api_key)


def web_search(query: str) -> str:
    """
    Search the live web using Groq's built-in browser_search tool.
    """

    client = get_groq_client()

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a web research assistant. "
                    "Search the web and return factual, useful research findings. "
                    "Prefer authoritative and recent sources. "
                    "Include source names and URLs whenever available. "
                    "Do not invent sources."
                ),
            },
            {
                "role": "user",
                "content": query,
            },
        ],
        tools=[
            {
                "type": "browser_search"
            }
        ],
        tool_choice="required",
        temperature=0.2,
        max_completion_tokens=4000,
    )

    return response.choices[0].message.content or "No research results found."
