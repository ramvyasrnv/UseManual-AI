# qa_model.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY") # Replace with your real OpenAI key

def get_answer(manual_text, user_question):
    """Get answer using OpenAI GPT-3.5/4 Chat Completion API."""
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that answers user questions based only on the given product manual."
        },
        {
            "role": "user",
            "content": f"Manual:\n{manual_text}\n\nQuestion: {user_question}"
        }
    ]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # You can change to "gpt-4" if available
        messages=messages,
        temperature=0.3,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()
