import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a model that YOU HAVE — from your list_models output
model = genai.GenerativeModel("models/gemini-2.0-flash")

response = model.generate_content("Say hello!")

print(response.text)
