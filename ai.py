import requests
import json

# Base URL and API key configuration
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"

# Helper function to send requests and return only the response string
def send_request(messages, model="google/gemini-flash-1.5"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": messages
    }
    
    response = requests.post(url=API_URL, headers=headers, data=json.dumps(data))
    
    # Check if the response is successful
    if response.status_code == 200:
        try:
            # Return just the content of the response from the AI
            return response.json()['choices'][0]['message']['content']
        except KeyError:
            return "No valid response received from the AI."
    else:
        return f"Error {response.status_code}: {response.text}"

# Function to ask a question (no system prompt)
def ask(question, model="google/gemini-flash-1.5"):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": question
                }
            ]
        }
    ]
    
    return send_request(messages, model)


def ask_sys(input, instruction):
    return ask(f"{instruction}: {input}")



