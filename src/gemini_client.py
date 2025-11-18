import os
import google.generativeai as genai

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)

def summarize_with_gemini(text: str) -> str:
    configure_gemini()

    # ✨ This model exists in your environment
    model = genai.GenerativeModel("models/gemini-2.0-flash")

    prompt = f"Summarize the following text:\n\n{text}"

    response = model.generate_content(prompt)
    return response.text
