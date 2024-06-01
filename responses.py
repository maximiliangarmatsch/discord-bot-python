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
    Openai response method take user query and return its response.

    Parameters
    ----------
    user_input: str
        user query or input.
    model: str
        openai model name.

    Return
    ------
    response: str
        openai response for each user query.
    """
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": user_input},
                    ]
                    )
    return response.choices[0].message.content
