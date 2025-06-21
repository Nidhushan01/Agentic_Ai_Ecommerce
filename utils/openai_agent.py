import openai
import os
from dotenv import load_dotenv
from openai import OpenAI



api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
def parse_user_input(user_input):
    prompt = f"""
You are an intelligent agent that converts shopping commands into strict JSON rules.

Input Command: "{user_input}"

Output only in **strict JSON** format with these fields:
- "product": (string) name of product
- "platform": (string) e-commerce platform, e.g., "Amazon"
- "target_price": (float) max price willing to pay
- "min_seller_rating": (float) default to 0.0 if not specified

Example:
{{
  "product": "iPhone",
  "platform": "Amazon",
  "target_price": 800.0,
  "min_seller_rating": 4.0
}}

Respond ONLY with valid JSON. No explanation, no formatting, no markdown.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return eval(response.choices[0].message.content)
