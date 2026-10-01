import os
from dotenv import load_dotenv
from google import genai

# .env file se API key load karo
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key nahi mili! .env file check karo.")

# Gemini client banao
client = genai.Client(api_key=api_key)

# User se question lo
question = input("Ask Gemini: ")

try:
    # Gemini API se response lo
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=question
    )

    # Answer print karo
    print("\nGemini ka jawab:")
    print(response.text)

except Exception as e:
    print("\nError aaya:")
    print(e)