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

# Function to ask a question with a system prompt
def ask_sys(question, system_prompt, model="google/gemini-flash-1.5"):
    messages = []
    
    # Add the system prompt
    messages.append({
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": system_prompt
            }
        ]
    })
    
    # Add the user's question
    messages.append({
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": question
            }
        ]
    })
    
    return send_request(messages, model)

# Function to analyze an image (no system prompt)
def analyze_img(image_url, question="What's in this image?", model="google/gemini-flash-1.5"):
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

# Function to analyze an image with a system prompt
def analyze_img_sys(image_url, question="What's in this image?", system_prompt=None, model="google/gemini-flash-1.5"):
    messages = []
    
    # Add the system prompt if provided
    if system_prompt:
        messages.append({
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": system_prompt
                }
            ]
        })
    
    # Add the user's image and question
    messages.append({
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
    })
    
    return send_request(messages, model)

# Example usage:

# # Asking a question without a system prompt
# response_text = ask("Can you tell me a fun fact about space?")
# print(response_text)

# # Asking a question with a system prompt
# response_text_sys = ask_sys(
#     "Can you tell me a fun fact about space?",
#     system_prompt="You are a space expert AI. Provide accurate and interesting information about space."
# )
# print(response_text_sys)

# # Analyzing an image without a system prompt
# image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
# response_image = analyze_img(image_url)
# print(response_image)

# # Analyzing an image with a system prompt
# response_image_sys = analyze_img_sys(
#     image_url=image_url,
#     question="What's in this image?",
#     system_prompt="You are a highly accurate image recognition model. Please describe the content in detail."
# )
# print(response_image_sys)
