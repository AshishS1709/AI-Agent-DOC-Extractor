'''import os

# Read the .env file directly
env_path = ".env"
print(f"Reading {env_path}:")
print("=" * 50)

try:
    with open(env_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(repr(content))  # This will show hidden characters
        print("\n" + "=" * 50)
        print("Line by line:")
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {repr(line)}")
except Exception as e:
    print(f"Error reading file: {e}")'''


import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

if not GROQ_API_KEY:
    print("❌ No API key found")
    exit(1)

print(f"Testing API key: {GROQ_API_KEY[:10]}...")

# Test API call
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": GROQ_MODEL,
    "messages": [
        {"role": "user", "content": "Hello, this is a test."}
    ],
    "max_tokens": 10
}

try:
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("✅ API key is valid!")
        result = response.json()
        print("Response:", result['choices'][0]['message']['content'])
    else:
        print(f"❌ API key test failed:")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"❌ Error testing API key: {e}")