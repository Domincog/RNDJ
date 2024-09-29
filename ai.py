from openai import OpenAI
from os import getenv

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="", #Add API key here
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
