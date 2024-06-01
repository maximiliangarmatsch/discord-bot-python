"""
openAPi response module
"""
import os
from openai import OpenAI
from random import choice, randint
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_KEY")
client = OpenAI(api_key = OPENAI_API_KEY)

def get_response(user_input: str, model = "gpt-3.5-turbo") -> str:
    """
    doc string
    """
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": user_input},
                    ]
                    )
    return response.choices[0].message.content
