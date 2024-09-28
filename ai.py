import requests
import json
import time

# Base URL and API key configuration
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"

# Helper function to send requests and return only the response string
def send_request(messages, model="google/gemini-flash-1.5", max_retries=3, retry_delay=2):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": messages
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url=API_URL, headers=headers, data=json.dumps(data), timeout=10)
            
            # Check if the response is successful
            if response.status_code == 200:
                try:
                    return response.json()['choices'][0]['message']['content']
                except KeyError:
                    return "No valid response received from the AI."
            else:
                print(f"Error {response.status_code}: {response.text}")
                return f"Error {response.status_code}: {response.text}"
        
        except requests.exceptions.RequestException as e:
            # Print the exception message and retry
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(retry_delay)  # Wait before retrying

    # If all attempts fail
    return "Failed to get a valid response after multiple attempts."

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
