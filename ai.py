from openai import OpenAI
from os import getenv

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


def ask(question):
    completion = client.chat.completions.create(
    extra_headers={
    },
    model="google/gemini-flash-1.5",
    messages=[
        {
        "role": "user",
        "content": question
        }
    ]
    )
    return(completion.choices[0].message.content)

def ask_sys(input, instructions):    
    return ask(f"{instructions}: {input}")