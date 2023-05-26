# from datetime import time
# import requests
import os

# import json
# import sseclient
# # Load the environment variables from .env
 

# Access the environment variables
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API key from environment variable
api_key = os.getenv('KEY')

# Use the API key in your code
print(api_key)


import requests
import time

def call_openai_api(prompt):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        # Retry after a default duration
        retry_after = 5  # Set your desired default retry interval in seconds
        print(f"Received 429 error. Retrying after {retry_after} seconds...")
        time.sleep(retry_after)
        return call_openai_api(prompt)  # Retry the API call
    else:
        print(response.status_code)
        return None

# Example usage
prompt_text = "Once upon a time"
response = call_openai_api(prompt_text)
if response:
    print(response["choices"][0]["text"])
