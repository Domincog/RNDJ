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


# Function to ask a text-based question
def ask_question(question, model="google/gemini-flash-1.5"):
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


# Function to ask about an image
def analyze_image(image_url, question="What's in this image?", model="google/gemini-flash-1.5"):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": question
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ]
        }
    ]
    
    return send_request(messages, model)


# Example usage:

# Asking a text-based question
response_text = ask_question("Can you tell me a fun fact about space?")
print(response_text)

# Analyzing an image
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
response_image = analyze_image(image_url)
print(response_image)
