from dotenv import dotenv_values
import google.generativeai as genai
key = dotenv_values(".env").get("GOOGLE_API_KEY")

genai.configure(api_key = key)
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
    text = text.replace('•', '  *')
    return text

def genAI(prompt : str):
    response = model.generate_content(prompt)
    result = response.text
    markdown = to_markdown(result)
    return {"text": [markdown], "sticker": "", "audio": ""}

