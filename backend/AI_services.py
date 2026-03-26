import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_question(role="python"):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Generate one interview question for a {role} developer."
    response = model.generate_content(prompt)
    return response.text
