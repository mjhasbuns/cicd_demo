import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = (
    "Write a Python function loan_payment(principal, annual_rate, years) "
    "that returns the monthly payment. Return only the code, no explanation."
)

response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
code = response.text.replace("```python", "").replace("```", "").strip()

with open("loan_payment.py", "w") as f:
    f.write(code + "\n")

print("Wrote loan_payment.py")
