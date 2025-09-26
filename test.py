import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load your API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("⚠️ GEMINI_API_KEY not found in .env")

genai.configure(api_key=api_key)

# Pick a model to test (start with flash)
model = genai.GenerativeModel("gemini-1.5-flash")

# Simple test prompt
prompt = "Hello Gemini! Reply with just one word: Hi"
response = model.generate_content(prompt)

print("✅ Gemini response:", response.text)
