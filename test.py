import google.generativeai as genai
import os

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API key not set. Please set the API_KEY environment variable.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Test the model independently
response = model.generate_content("Hello, how are you?")
print("Model response:", response.text)

