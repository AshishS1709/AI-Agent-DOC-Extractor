import os
from dotenv import load_dotenv

print("Current working directory:", os.getcwd())
print(".env file exists:", os.path.exists(".env"))

# Try loading from current directory
load_dotenv()

# Also try loading with explicit path
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
print("Trying to load .env from:", env_path)
load_dotenv(dotenv_path=env_path)

# Get the values
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

print("GROQ_API_KEY loaded:", GROQ_API_KEY is not None)
print("GROQ_MODEL loaded:", GROQ_MODEL is not None)

if GROQ_API_KEY:
    print("API Key (first 10 chars):", GROQ_API_KEY[:10] + "...")
else:
    print("❌ GROQ_API_KEY is None or empty")
    
if GROQ_MODEL:
    print("Model:", GROQ_MODEL)
else:
    print("❌ GROQ_MODEL is None or empty")

# Raise error if not found
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")
if not GROQ_MODEL:
    raise ValueError("GROQ_MODEL not found in environment variables")