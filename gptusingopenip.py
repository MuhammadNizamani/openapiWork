import openai
import os

# import json
# import sseclient
# # Load the environment variables from .env
 

# Access the environment variables
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# # Access API key from environment variable
api_key = os.getenv('KEY')

openai.api_key = api_key
# res=openai.ChatCompletion.create({"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": "what is pakistan and what is sindh?"}]})

# print(res)


# openai.api_key = 'YOUR_API_KEY'

def call_openai_api(prompt):
    response = openai.ChatCompletion.create(
        # engine='davinci-codex', # Specify the desired language model
        model ="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}
        ]
    )

    if 'choices' in response:
        return response['choices'][0]['message']['content']
    else:
        return None

# Example usage
prompt_text = "What is the capital of France?"
response = call_openai_api(prompt_text)
print(response)

