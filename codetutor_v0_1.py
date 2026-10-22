
from google import genai
import os

# Connect to Gemini
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("=== CODETUTOR v0.1 ===")
print("Enter a Python error and I'll help you understand it.")
print()

# Get the error from the user
error_message = input("Enter your Python error: ")

# Ask Gemini to explain it
prompt = f"""
You are a friendly Python tutor helping a beginner.

Explain this Python error:
{error_message}

Please give:
1. What the error means in simple language.
2. Common reasons it happens.
3. How to fix it.
4. A short example of corrected code.

Keep your explanation clear and beginner-friendly.
"""

try:
    print("\nAnalysing your error...\n")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("=== EXPLANATION ===")
    print(response.text)

except Exception as error:
    print("Something went wrong while contacting Gemini.")
    print(type(error).__name__)
    print(str(error)[:500])
